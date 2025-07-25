"""
Qdrant vector store implementation for retrieval benchmarks.

Provides comprehensive vector store operations including:
- Collection management
- Document indexing with resumption support
- Similarity search
- Status monitoring and validation
"""

import logging
import pandas as pd
import ast
import json
import hashlib
import uuid
import time
import os
import requests
from typing import List, Dict, Any, Optional, Tuple
from qdrant_client import QdrantClient
from qdrant_client.http import models
from qdrant_client.http.models import Distance, VectorParams, PointStruct, Filter, FieldCondition, MatchValue

logger = logging.getLogger(__name__)


class QdrantVectorStore:
    """Qdrant-based vector store for retrieval benchmarks"""
    
    def __init__(self, embedding_model: str, dataset_hash: str, collection_name: str = "retrieval_benchmark"):
        """
        Initialize Qdrant vector store
        
        Args:
            embedding_model: Name of embedding model (e.g., 'nomic-embed-text')
            dataset_hash: Hash of the dataset being indexed (first 8 chars)
            collection_name: Base name of the Qdrant collection
        """
        self.embedding_model = embedding_model
        self.dataset_hash = dataset_hash[:8]  # Use first 8 characters for brevity
        # Collection name includes both dataset hash and embedding model
        self.collection_name = f"{collection_name}_{self.dataset_hash}_{embedding_model.replace(':', '_').replace('-', '_')}"
        
        # Use a consistent UUID for metadata point based on collection name
        self.metadata_point_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"metadata_{self.collection_name}"))
        
        # Initialize Qdrant client
        qdrant_url = os.getenv("QDRANT_URL", "http://qdrant2:6333")
        self.client = QdrantClient(url=qdrant_url)
        
        # Initialize embedding model with direct API
        self.ollama_api_url = os.getenv("OLLAMA_API_URL", "http://ollama-gpu-3:11435/api")
        self.ollama_base_url = self.ollama_api_url.replace("/api", "")
        
        # Debug: Print the actual model name being used
        logger.info(f"Initializing direct Ollama API with model: '{embedding_model}', base_url: '{self.ollama_base_url}'")
        
        # Setup session for connection pooling with enhanced settings for large datasets
        self.session = requests.Session()
        from urllib3.util.retry import Retry
        
        # Configure retry strategy with backoff
        retry_strategy = Retry(
            total=5,                # Total number of retries
            status_forcelist=[429, 500, 502, 503, 504],  # HTTP status codes to retry on
            backoff_factor=1,       # Backoff factor for retries
            raise_on_status=False   # Don't raise on status codes
        )
        
        adapter = requests.adapters.HTTPAdapter(
            pool_connections=20,    # Increased pool connections
            pool_maxsize=40,        # Increased pool size
            max_retries=retry_strategy
        )
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)
        
        # Get embedding dimension
        self.embedding_dim = self._get_embedding_dimension()
        
        logger.info(f"Initialized QdrantVectorStore with model {embedding_model}, "
                   f"collection {self.collection_name}, embedding dimension {self.embedding_dim}")
    
    def _get_embedding_api(self, text: str, timeout: int = 60) -> List[float]:
        """Get embedding using direct Ollama API call with timeout"""
        url = f"{self.ollama_api_url}/embeddings"
        
        payload = {
            "model": self.embedding_model,
            "prompt": text
        }
        
        try:
            response = self.session.post(url, json=payload, timeout=timeout)
            response.raise_for_status()
            
            result = response.json()
            embedding = result.get("embedding", [])
            
            if not embedding:
                raise ValueError("Empty embedding returned from API")
                
            return embedding
            
        except requests.exceptions.Timeout:
            raise TimeoutError(f"Embedding API call timed out after {timeout} seconds")
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Embedding API call failed: {e}")
    
    def _get_embeddings_batch_api(self, texts: List[str], timeout: int = 120) -> List[List[float]]:
        """Get embeddings for multiple texts using direct Ollama API calls with optional parallelization"""
        embeddings = []
        
        # For now, process sequentially to avoid overwhelming the Ollama server
        # Could be optimized with ThreadPoolExecutor if needed
        for i, text in enumerate(texts):
            try:
                embedding = self._get_embedding_api(text, timeout=timeout)
                embeddings.append(embedding)
                logger.debug(f"Generated embedding {i+1}/{len(texts)}")
            except Exception as e:
                logger.error(f"Failed to generate embedding for text {i+1}: {e}")
                raise
            
        return embeddings
    
    def _get_embedding_dimension(self) -> int:
        """Get embedding dimension by testing with a sample text"""
        try:
            logger.info(f"Testing embedding dimension with model: {self.embedding_model}")
            sample_embedding = self._get_embedding_api("test", timeout=10)
            logger.info(f"Successfully got embedding of dimension: {len(sample_embedding)}")
            return len(sample_embedding)
        except Exception as e:
            logger.error(f"Failed to get embedding dimension for model '{self.embedding_model}': {e}")
            logger.error(f"Full error details: {type(e).__name__}: {str(e)}")
            # Default dimension for nomic-embed-text
            logger.warning(f"Using default dimension 768 for model: {self.embedding_model}")
            return 768
    
    def _create_collection_if_not_exists(self):
        """Create Qdrant collection if it doesn't exist"""
        try:
            collections = self.client.get_collections().collections
            collection_names = [col.name for col in collections]
            
            if self.collection_name not in collection_names:
                logger.info(f"Creating collection {self.collection_name}")
                self.client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=VectorParams(
                        size=self.embedding_dim,
                        distance=Distance.COSINE
                    )
                )
                logger.info(f"Created collection {self.collection_name}")
            else:
                logger.info(f"Collection {self.collection_name} already exists")
                
        except Exception as e:
            logger.error(f"Error creating collection: {e}")
            raise
    
    def _generate_doc_hash(self, text: str, doc_id: str) -> str:
        """Generate a unique hash for a document"""
        content = f"{doc_id}:{text}"
        return hashlib.md5(content.encode()).hexdigest()
    
    def _generate_dataset_hash(self, docs_df: pd.DataFrame) -> str:
        """Generate a hash for the entire dataset to detect changes"""
        # Create a hash based on the content of all documents
        content_hashes = []
        for idx, row in docs_df.iterrows():
            text = row['text']
            metadata_str = row['metadata']
            try:
                metadata = ast.literal_eval(metadata_str) if isinstance(metadata_str, str) else metadata_str
            except:
                try:
                    metadata = json.loads(metadata_str) if isinstance(metadata_str, str) else metadata_str
                except:
                    metadata = {"doc_id": str(idx)}
            
            doc_id = metadata.get('doc_id', str(idx))
            content_hashes.append(self._generate_doc_hash(text, doc_id))
        
        # Sort and combine all hashes to create dataset hash
        content_hashes.sort()
        combined_content = "".join(content_hashes)
        return hashlib.md5(combined_content.encode()).hexdigest()
    
    def check_indexing_status(self, docs_df: pd.DataFrame) -> Dict[str, Any]:
        """Check the indexing status and return detailed information"""
        try:
            # Check if collection exists
            collections = self.client.get_collections().collections
            collection_names = [col.name for col in collections]
            
            if self.collection_name not in collection_names:
                return {
                    "status": "not_indexed",
                    "collection_exists": False,
                    "points_count": 0,
                    "expected_count": len(docs_df),
                    "completion_percentage": 0.0,
                    "needs_indexing": True,
                    "needs_resume": False
                }
            
            # Get collection info
            collection_info = self.client.get_collection(self.collection_name)
            current_points = collection_info.points_count
            expected_count = len(docs_df)
            
            if current_points == 0:
                return {
                    "status": "empty",
                    "collection_exists": True,
                    "points_count": 0,
                    "expected_count": expected_count,
                    "completion_percentage": 0.0,
                    "needs_indexing": True,
                    "needs_resume": False
                }
            
            # Check if we have stored the dataset hash in metadata
            dataset_hash = self._generate_dataset_hash(docs_df)
            
            # Try to get metadata point
            try:
                metadata_point = self.client.retrieve(
                    collection_name=self.collection_name,
                    ids=[self.metadata_point_id]
                )
                
                if metadata_point and len(metadata_point) > 0:
                    stored_hash = metadata_point[0].payload.get("dataset_hash")
                    stored_doc_count = metadata_point[0].payload.get("document_count", 0)
                    
                    if stored_hash == dataset_hash:
                        # Same dataset, check completion
                        if current_points >= expected_count:
                            return {
                                "status": "complete",
                                "collection_exists": True,
                                "points_count": current_points,
                                "expected_count": expected_count,
                                "completion_percentage": 100.0,
                                "needs_indexing": False,
                                "needs_resume": False
                            }
                        else:
                            # Incomplete indexing detected!
                            completion_pct = (current_points / expected_count) * 100
                            return {
                                "status": "incomplete",
                                "collection_exists": True,
                                "points_count": current_points,
                                "expected_count": expected_count,
                                "completion_percentage": completion_pct,
                                "needs_indexing": True,
                                "needs_resume": True,
                                "dataset_hash": dataset_hash,
                                "stored_doc_count": stored_doc_count
                            }
                    else:
                        # Different dataset
                        return {
                            "status": "different_dataset",
                            "collection_exists": True,
                            "points_count": current_points,
                            "expected_count": expected_count,
                            "completion_percentage": 0.0,
                            "needs_indexing": True,
                            "needs_resume": False,
                            "old_dataset_hash": stored_hash,
                            "new_dataset_hash": dataset_hash
                        }
            except Exception as e:
                logger.warning(f"Could not retrieve metadata point: {e}")
                # Fallback without metadata
                if current_points >= expected_count:
                    return {
                        "status": "complete_no_metadata",
                        "collection_exists": True,
                        "points_count": current_points,
                        "expected_count": expected_count,
                        "completion_percentage": 100.0,
                        "needs_indexing": False,
                        "needs_resume": False
                    }
                else:
                    completion_pct = (current_points / expected_count) * 100
                    return {
                        "status": "incomplete_no_metadata",
                        "collection_exists": True,
                        "points_count": current_points,
                        "expected_count": expected_count,
                        "completion_percentage": completion_pct,
                        "needs_indexing": True,
                        "needs_resume": True
                    }
            
        except Exception as e:
            logger.error(f"Error checking indexing status: {e}")
            return {
                "status": "error",
                "collection_exists": False,
                "points_count": 0,
                "expected_count": len(docs_df),
                "completion_percentage": 0.0,
                "needs_indexing": True,
                "needs_resume": False,
                "error": str(e)
            }

    def is_dataset_indexed(self, docs_df: pd.DataFrame) -> bool:
        """Check if the dataset is already indexed (backward compatibility)"""
        status = self.check_indexing_status(docs_df)
        return not status["needs_indexing"]
    
    def get_indexed_document_ids(self) -> set:
        """Get set of document IDs that are already indexed in the collection"""
        try:
            indexed_doc_ids = set()
            
            # Scroll through all points in the collection
            next_page_offset = None
            while True:
                result = self.client.scroll(
                    collection_name=self.collection_name,
                    scroll_filter=models.Filter(
                        must=[
                            models.FieldCondition(
                                key="is_metadata",
                                match=models.MatchValue(value=False)  # Only get actual documents, not metadata
                            )
                        ]
                    ),
                    limit=1000,
                    offset=next_page_offset,
                    with_payload=True,
                    with_vectors=False  # We don't need vectors, just payloads
                )
                
                points, next_page_offset = result
                
                if not points:
                    break
                
                for point in points:
                    doc_id = point.payload.get('doc_id')
                    if doc_id:
                        indexed_doc_ids.add(str(doc_id))
                
                if next_page_offset is None:
                    break
            
            logger.info(f"Found {len(indexed_doc_ids)} already indexed documents")
            return indexed_doc_ids
            
        except Exception as e:
            logger.error(f"Error getting indexed document IDs: {e}")
            return set()
    
    def find_missing_documents(self, docs_df: pd.DataFrame) -> pd.DataFrame:
        """Find documents that are not yet indexed"""
        try:
            indexed_doc_ids = self.get_indexed_document_ids()
            
            missing_docs = []
            for idx, row in docs_df.iterrows():
                # Parse metadata to get doc_id
                metadata_str = row.get('metadata', str(idx))
                try:
                    metadata = ast.literal_eval(metadata_str) if isinstance(metadata_str, str) else metadata_str
                except:
                    try:
                        metadata = json.loads(metadata_str) if isinstance(metadata_str, str) else metadata_str
                    except:
                        metadata = {"doc_id": str(idx)}
                
                # Ensure doc_id is present
                if 'doc_id' not in metadata:
                    metadata['doc_id'] = str(idx)
                
                doc_id = str(metadata['doc_id'])
                
                # If this document is not already indexed, add it to missing list
                if doc_id not in indexed_doc_ids:
                    missing_docs.append(row)
            
            missing_df = pd.DataFrame(missing_docs) if missing_docs else pd.DataFrame()
            logger.info(f"Found {len(missing_df)} documents that need to be indexed out of {len(docs_df)} total")
            
            return missing_df
            
        except Exception as e:
            logger.error(f"Error finding missing documents: {e}")
            # If we can't determine missing docs, return all docs to be safe
            return docs_df
    
    def index_documents(self, docs_df: pd.DataFrame, batch_size: int = 100, force_reindex: bool = False) -> bool:
        """
        Index documents from retrieval_docs.csv into Qdrant
        
        Args:
            docs_df: DataFrame with 'text' and 'metadata' columns
            batch_size: Number of documents to process in each batch
            force_reindex: Force re-indexing even if documents already exist
            
        Returns:
            True if successful, False otherwise
        """
        try:
            logger.info(f"Starting to index {len(docs_df)} documents")
            
            # Check indexing status
            status = self.check_indexing_status(docs_df)
            logger.info(f"Indexing status: {status['status']} - {status['points_count']}/{status['expected_count']} documents ({status['completion_percentage']:.1f}%)")
            
            # If already fully indexed and not forcing reindex, skip
            if not force_reindex and not status["needs_indexing"]:
                logger.info("Dataset already fully indexed, skipping indexing")
                return True
            
            # Create collection if it doesn't exist
            self._create_collection_if_not_exists()
            
            # Determine what documents to index
            docs_to_index = docs_df
            resume_indexing = False
            
            if force_reindex:
                # Force reindex: clear everything and start fresh
                logger.info("Force reindex requested - clearing existing documents in collection")
                self.clear_collection()
                self._create_collection_if_not_exists()
                docs_to_index = docs_df
            elif status["needs_resume"] and status["status"] in ["incomplete", "incomplete_no_metadata"]:
                # Resume incomplete indexing: only index missing documents
                logger.info(f"Resuming incomplete indexing from {status['points_count']}/{status['expected_count']} documents")
                missing_docs = self.find_missing_documents(docs_df)
                if len(missing_docs) == 0:
                    logger.info("No missing documents found, indexing appears complete")
                    return True
                docs_to_index = missing_docs
                resume_indexing = True
                logger.info(f"Found {len(docs_to_index)} documents to index (resuming from {status['points_count']} already indexed)")
            else:
                # Different dataset or empty collection: clear and start fresh
                if status["points_count"] > 0:
                    logger.info("Different dataset detected or empty collection - clearing existing documents")
                    self.clear_collection()
                    self._create_collection_if_not_exists()
                docs_to_index = docs_df
            
            # Generate dataset hash for tracking
            dataset_hash = self._generate_dataset_hash(docs_df)
            
            points = []
            
            # Add/update dataset metadata point (only if not resuming or if this is the first time)
            if not resume_indexing or status["status"] not in ["incomplete", "incomplete_no_metadata"]:
                metadata_point = PointStruct(
                    id=self.metadata_point_id,
                    vector=[0.0] * self.embedding_dim,  # Dummy vector
                    payload={
                        "dataset_hash": dataset_hash,
                        "document_count": len(docs_df),  # Total expected documents
                        "indexed_at": time.time(),
                        "embedding_model": self.embedding_model,
                        "is_metadata": True
                    }
                )
                points.append(metadata_point)
                logger.info("Added/updated dataset metadata point")
            
            # Process documents in batches for embedding
            # Adaptive batch size based on dataset size
            total_original_docs = len(docs_df)
            total_docs_to_index = len(docs_to_index)
            already_indexed = status.get("points_count", 0) if resume_indexing else 0
            
            if total_original_docs > 10000:
                embedding_batch_size = 50  # Larger batches for big datasets
            elif total_original_docs > 1000:
                embedding_batch_size = 30  # Medium batches
            else:
                embedding_batch_size = 20  # Small batches for small datasets
            
            if resume_indexing:
                logger.info(f"Resuming indexing: {already_indexed} already indexed, {total_docs_to_index} remaining to index")
            else:
                logger.info(f"Starting fresh indexing: {total_docs_to_index} documents to index")
            
            for batch_start in range(0, total_docs_to_index, embedding_batch_size):
                batch_end = min(batch_start + embedding_batch_size, total_docs_to_index)
                batch_df = docs_to_index.iloc[batch_start:batch_end]
                
                # Prepare batch data
                batch_texts = []
                batch_metadata = []
                batch_doc_ids = []
                
                for idx, row in batch_df.iterrows():
                    try:
                        text = row['text']
                        metadata_str = row['metadata']
                        if isinstance(metadata_str, str):
                            
                        # Parse metadata (it's stored as a string representation of a dict)
                            try:
                                metadata = ast.literal_eval(metadata_str)
                            except:
                                # If parsing fails, try json.loads
                                try:
                                    metadata = json.loads(metadata_str)
                                except:
                                    logger.warning(f"Failed to parse metadata for doc {idx}: {metadata_str}")
                                    metadata = {"doc_id": str(idx)}
                        elif isinstance(metadata_str, dict):
                            metadata = metadata_str
                        else:
                            logger.warning(f"Invalid metadata type for doc {idx}: {type(metadata_str)}")
                            metadata = {"doc_id": str(idx)}
                        
                        # Ensure doc_id is present
                        if 'doc_id' not in metadata:
                            metadata['doc_id'] = str(idx)
                        
                        doc_id = metadata['doc_id']
                        batch_texts.append(text)
                        batch_metadata.append(metadata)
                        batch_doc_ids.append(doc_id)
                        
                    except Exception as e:
                        logger.error(f"Error processing document {idx}: {e}")
                        continue
                
                # Generate embeddings for the batch
                try:
                    # Use longer timeout for large datasets
                    batch_timeout = 180 if total_original_docs > 10000 else 120
                    batch_embeddings = self._get_embeddings_batch_api(batch_texts, timeout=batch_timeout)
                    
                    # Create points for the batch
                    for i, (text, metadata, doc_id, embedding) in enumerate(zip(batch_texts, batch_metadata, batch_doc_ids, batch_embeddings)):
                        point_id = self._generate_doc_hash(text, doc_id)
                        point = PointStruct(
                            id=point_id,
                            vector=embedding,
                            payload={
                                "text": text,
                                "doc_id": doc_id,
                                "metadata": metadata,
                                "is_metadata": False
                            }
                        )
                        points.append(point)
                        
                        # Process in batches for Qdrant
                        if len(points) >= batch_size:
                            self._upsert_points(points)
                            points = []
                    
                    # Enhanced progress reporting with resumption context
                    current_indexed = already_indexed + batch_end
                    total_progress_pct = (current_indexed / total_original_docs) * 100
                    batch_progress_pct = (batch_end / total_docs_to_index) * 100
                    
                    if resume_indexing:
                        logger.info(f"Resumption progress: {batch_end}/{total_docs_to_index} new documents ({batch_progress_pct:.1f}%) | Total: {current_indexed}/{total_original_docs} ({total_progress_pct:.1f}%)")
                    else:
                        logger.info(f"Indexed {batch_end}/{total_docs_to_index} documents ({batch_progress_pct:.1f}%)")
                    
                    # Add small delay between batches for large datasets to avoid overwhelming server
                    if total_original_docs > 5000 and batch_end < total_docs_to_index:
                        time.sleep(0.5)  # 500ms delay between batches
                    
                except (TimeoutError, requests.exceptions.Timeout) as e:
                    logger.warning(f"Batch embedding generation timed out for batch {batch_start}-{batch_end}, falling back to individual processing: {e}")
                    # Fall back to individual processing for this batch
                except Exception as e:
                    logger.error(f"Error generating embeddings for batch {batch_start}-{batch_end}: {e}")
                    # Fall back to individual processing for this batch
                    for text, metadata, doc_id in zip(batch_texts, batch_metadata, batch_doc_ids):
                        try:
                            # Use longer timeout for individual fallback processing
                            individual_timeout = 90 if total_original_docs > 10000 else 60
                            embedding = self._get_embedding_api(text, timeout=individual_timeout)
                            point_id = self._generate_doc_hash(text, doc_id)
                            point = PointStruct(
                                id=point_id,
                                vector=embedding,
                                payload={
                                    "text": text,
                                    "doc_id": doc_id,
                                    "metadata": metadata,
                                    "is_metadata": False
                                }
                            )
                            points.append(point)
                            
                            if len(points) >= batch_size:
                                self._upsert_points(points)
                                points = []
                                
                        except (TimeoutError, requests.exceptions.Timeout) as e:
                            logger.warning(f"Individual embedding generation timed out, skipping document: {e}")
                            continue
                        except Exception as e:
                            logger.error(f"Error processing individual document: {e}")
                            continue
            
            # Process remaining points
            if points:
                self._upsert_points(points)
            
            # Final success logging with proper context
            if resume_indexing:
                final_count = already_indexed + total_docs_to_index
                logger.info(f"Successfully resumed and completed indexing: {total_docs_to_index} new documents indexed, {final_count}/{total_original_docs} total documents now indexed")
            else:
                logger.info(f"Successfully indexed {total_docs_to_index} documents")
            
            return True
            
        except Exception as e:
            logger.error(f"Error indexing documents: {e}")
            return False
    
    def _upsert_points(self, points: List[PointStruct]):
        """Upsert points to Qdrant with retry logic"""
        max_retries = 3
        for attempt in range(max_retries):
            try:
                self.client.upsert(
                    collection_name=self.collection_name,
                    points=points
                )
                return
            except Exception as e:
                if attempt == max_retries - 1:
                    raise e
                logger.warning(f"Upsert attempt {attempt + 1} failed: {e}, retrying...")
                time.sleep(1)
    
    def similarity_search(self, query: str, k: int = 5) -> List[Dict[str, Any]]:
        """
        Perform similarity search
        
        Args:
            query: Search query
            k: Number of results to return
            
        Returns:
            List of search results with metadata
        """
        try:
            # Debug: Log the search operation
            logger.info(f"Similarity search in collection {self.collection_name} for query: '{query[:50]}...', k={k}")
            
            # Generate query embedding
            query_embedding = self._get_embedding_api(query, timeout=10)
            
            # Search in Qdrant - request more results to account for metadata filtering
            search_results = self.client.search(
                collection_name=self.collection_name,
                query_vector=query_embedding,
                limit=k + 10,  # Request extra to account for metadata filtering
                with_payload=True,
                query_filter=models.Filter(
                    must=[
                        models.FieldCondition(
                            key="is_metadata",
                            match=models.MatchValue(value=False)
                        )
                    ]
                )
            )
            
            # Format results and limit to k
            results = []
            for result in search_results[:k]:
                # Extract metadata and ensure doc_id is accessible
                metadata = result.payload.get('metadata', {})
                doc_id = result.payload.get('doc_id')
                if doc_id and 'doc_id' not in metadata:
                    metadata['doc_id'] = doc_id
                
                results.append({
                    'page_content': result.payload['text'],
                    'metadata': metadata,
                    'doc_id': doc_id,  # Make doc_id directly accessible
                    'score': result.score
                })
            
            # Debug: Log sample results
            if results:
                first_result = results[0]
                logger.info(f"Search in {self.collection_name} returned {len(results)} results. First result: doc_id={first_result.get('doc_id')}, score={first_result.get('score'):.4f}, content='{first_result.get('page_content', '')[:100]}...'")
            else:
                logger.warning(f"Search in {self.collection_name} returned no results for query: '{query[:50]}...'")
            
            return results
            
        except (TimeoutError, requests.exceptions.Timeout) as e:
            logger.error(f"Similarity search timed out: {e}")
            return []
        except Exception as e:
            logger.error(f"Error in similarity search: {e}")
            return []
    
    def get_collection_info(self) -> Dict[str, Any]:
        """Get information about the collection"""
        try:
            info = self.client.get_collection(self.collection_name)
            
            # Get metadata about the dataset
            try:
                metadata_point = self.client.retrieve(
                    collection_name=self.collection_name,
                    ids=[self.metadata_point_id]
                )
                
                dataset_info = {}
                if metadata_point and len(metadata_point) > 0:
                    payload = metadata_point[0].payload
                    dataset_info = {
                        "document_count": payload.get("document_count", 0),
                        "indexed_at": payload.get("indexed_at", 0),
                        "embedding_model": payload.get("embedding_model", "unknown"),
                        "dataset_hash": payload.get("dataset_hash", "unknown")
                    }
            except:
                dataset_info = {}
            
            return {
                "name": self.collection_name,
                "vectors_count": info.vectors_count,
                "indexed_vectors_count": info.indexed_vectors_count,
                "points_count": info.points_count,
                "status": info.status,
                "dataset_info": dataset_info
            }
        except Exception as e:
            logger.error(f"Error getting collection info: {e}")
            return {}
    
    def clear_collection(self):
        """Clear all documents from the collection (but keep the collection structure)"""
        try:
            self.client.delete_collection(self.collection_name)
            self._create_collection_if_not_exists()
            logger.info(f"Cleared collection {self.collection_name}")
        except Exception as e:
            logger.error(f"Error clearing collection: {e}")
    
    def delete_collection_completely(self):
        """Completely delete the collection without recreating it (for factory reset)"""
        try:
            self.client.delete_collection(self.collection_name)
            logger.info(f"Completely deleted collection {self.collection_name}")
        except Exception as e:
            logger.error(f"Error completely deleting collection: {e}")
            # Don't raise - collection might not exist, which is fine for factory reset
    
    def force_reindex(self, docs_df: pd.DataFrame, batch_size: int = 100) -> bool:
        """Force re-indexing of documents, clearing existing data"""
        return self.index_documents(docs_df, batch_size=batch_size, force_reindex=True) 