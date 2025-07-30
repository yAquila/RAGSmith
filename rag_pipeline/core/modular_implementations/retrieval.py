import time, os, sys
import logging, requests, json
from typing import List, Dict, Any, Optional, TypedDict
from abc import ABC, abstractmethod
from neo4j import GraphDatabase

from rag_pipeline.core.modular_framework import (
    RetrievalComponent, Document, Query
)

logger = logging.getLogger(__name__)

class RetrievalResult(TypedDict):
    documents: List[Document]
    embedding_token_count: float
    llm_input_token_count: float
    llm_output_token_count: float

class SimpleVectorRAG(RetrievalComponent):
    """✅ CURRENTLY IMPLEMENTED - Simple vector-based retrieval with semantic scoring"""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.vectorstore = None
        self._setup_vectorstore()
    
    def _setup_vectorstore(self):
        """Setup the vector store"""
        try:
            from rag_pipeline.util.vectorstore.qdrant_store import QdrantVectorStore
            from rag_pipeline.util.vectorstore.dataset_utils import generate_dataset_hash_from_folder
            import os
            
            # Use embedding model from config
            embedding_model = self.config.get("embedding_model", "mxbai-embed-large")
            
            # Use dataset path from config or default
            dataset_path = self.config.get("dataset_path")
            if not dataset_path:
                dataset_path = os.path.join(
                    "rag_pipeline",
                    "default_datasets",
                    "cleaned_gen_programming_5"
                )
            
            # Generate hash from the folder
            dataset_hash = generate_dataset_hash_from_folder(dataset_path)
            self.vectorstore = QdrantVectorStore(embedding_model, dataset_hash)
            
        except Exception as e:
            logger.error(f"Failed to setup vectorstore: {e}")
            raise
    
    async def retrieve(self, query: Query, k: Optional[int] = None) -> RetrievalResult:
        """Retrieve documents using vector similarity search"""
        k = k or self.config.get("top_k", 10)
        
        try:
            # Use the processed query text
            query_text = query.processed_text
            
            # Perform similarity search
            results = self.vectorstore.similarity_search(query_text, k)
            
            # Convert to Document objects
            documents = []
            for result in results:
                doc = Document(
                    doc_id=result.get("doc_id", ""),
                    content=result.get("page_content", ""),
                    score=result.get("score", 0.0),
                    metadata=result.get("metadata", {})
                )
                documents.append(doc)
            
            # Embedding token count: sum of tokens in all retrieved documents
            embedding_token_count = len(query_text.split())
            result = RetrievalResult(
                documents=documents,
                embedding_token_count=float(embedding_token_count),
                llm_input_token_count=0.0,
                llm_output_token_count=0.0
            )
            return result
            
        except Exception as e:
            logger.error(f"Retrieval failed: {e}")
            result = RetrievalResult(
                documents=[],
                embedding_token_count=0.0,
                llm_input_token_count=0.0,
                llm_output_token_count=0.0
            )
            return result
    
    async def index_documents(self, documents: List[Document]) -> bool:
        """Index documents in the vector store"""
        try:
            import pandas as pd
            
            # Convert to pandas DataFrame for existing indexing logic
            docs_data = []
            for doc in documents:
                docs_data.append({
                    'text': doc.content,
                    'doc_id': doc.doc_id,
                    'metadata': doc.metadata or {}
                })
            
            docs_df = pd.DataFrame(docs_data)
            return self.vectorstore.index_documents(docs_df)
            
        except Exception as e:
            logger.error(f"Failed to index documents: {e}")
            return False

class KeywordSearchBM25(RetrievalComponent):
    """BM25-based keyword search retrieval"""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        from rag_pipeline.util.retrieval_utils.bm25_utils import BM25IndexManager
        self.index_manager = BM25IndexManager(config)
        self._setup_bm25_index()
    
    def _setup_bm25_index(self):
        """Setup the BM25 index"""
        try:
            from rag_pipeline.util.vectorstore.dataset_utils import generate_dataset_hash_from_folder
            
            # Use dataset path from config or default
            dataset_path = self.config.get("dataset_path")
            if not dataset_path:
                dataset_path = os.path.join(
                    "rag_pipeline",
                    "default_datasets",
                    "cleaned_gen_programming_5"
                )
            
            # Generate hash from the folder
            dataset_hash = generate_dataset_hash_from_folder(dataset_path)
            
            # Load documents for indexing
            from rag_pipeline.core.dataset import RAGDataset
            dataset = RAGDataset(dataset_path)
            documents = dataset.get_documents()
            
            # Create a temporary CSV file for the BM25 index manager
            import tempfile
            import pandas as pd
            docs_data = []
            for doc in documents:
                docs_data.append({
                    'text': doc.content,
                    'doc_id': doc.doc_id,
                    'metadata': doc.metadata or {}
                })
            
            docs_df = pd.DataFrame(docs_data)
            temp_csv_path = tempfile.mktemp(suffix='.csv')
            docs_df.to_csv(temp_csv_path, index=False)
            
            self.index_manager.setup_index_paths(dataset_hash, temp_csv_path)
            
            # Load existing index or create new one
            if self.index_manager.load_existing_index():
                logger.info("Loaded existing BM25 index")
            else:
                logger.info("Creating new BM25 index")
                self._create_index_from_documents(documents)
                
        except Exception as e:
            logger.error(f"Failed to setup BM25 index: {e}")
            raise
    
    def _create_index_from_documents(self, documents: List[Document]) -> bool:
        """Create BM25 index from a list of Document objects"""
        try:
            return self.index_manager.index_documents(documents)
            
        except Exception as e:
            logger.error(f"Failed to create index from documents: {e}")
            return False
    

    async def retrieve(self, query: Query, k: Optional[int] = None) -> RetrievalResult:
        """Retrieve documents using BM25 keyword search"""
        k = k or self.config.get("top_k", 10)
        
        try:
            # Perform search using index manager
            query_text = query.processed_text
            results = self.index_manager.search(query_text, k)
            
            # Convert to Document objects
            documents = []
            for result in results:
                doc = Document(
                    doc_id=result.get("doc_id", ""),
                    content=result.get("content", ""),
                    score=result.get("score", 0.0),
                    metadata=result.get("metadata", {})
                )
                documents.append(doc)
            
            # Calculate token count for the query (simple split for consistency)
            
            result = RetrievalResult(
                documents=documents,
                embedding_token_count=0.0,
                llm_input_token_count=0.0,
                llm_output_token_count=0.0
            )
            return result
            
        except Exception as e:
            logger.error(f"BM25 retrieval failed: {e}")
            return RetrievalResult(
                documents=[],
                embedding_token_count=0.0,
                llm_input_token_count=0.0,
                llm_output_token_count=0.0
            )
    
    async def index_documents(self, documents: List[Document]) -> bool:
        """Index documents for BM25 search"""
        try:
            return self.index_manager.index_documents(documents)
        except Exception as e:
            logger.error(f"Failed to index documents: {e}")
            return False
    
    def get_index_stats(self) -> Dict[str, Any]:
        """Get statistics about the BM25 index"""
        return self.index_manager.get_stats()

from rag_pipeline.util.retrieval_utils.combination_utils import ScoreCombiner, RankFusionCombiner, HybridUtils

class HybridSearch(RetrievalComponent):
    """
    Unified hybrid retrieval class supporting both Convex Combination (CC) and 
    Reciprocal Rank Fusion (RRF) methods for combining vector and keyword search results.
    """
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.vector_retriever = None
        self.keyword_retriever = None
        self.combination_method = self.config.get("combination_method", "convex_combination")
        self._setup_retrievers()
    
    def _setup_retrievers(self):
        """Setup vector and keyword retrievers"""
        try:
            # Create vector retriever
            self.vector_retriever = SimpleVectorRAG(self.config)
            
            self.keyword_retriever = KeywordSearchBM25(self.config)
            
            logger.info(f"Hybrid search initialized with combination method: {self.combination_method}")
            
        except Exception as e:
            logger.error(f"Failed to setup hybrid retrievers: {e}")
            raise
    
    async def retrieve(self, query: Query, k: Optional[int] = None) -> RetrievalResult:
        """Retrieve documents using the configured hybrid approach"""
        k = k or self.config.get("top_k", 10)
        
        try:
            excessive_k = self.config.get("excessive_k", k * 3)

            # Perform vector search
            vector_result = await self.vector_retriever.retrieve(query, excessive_k)
            vector_results = []
            for doc in vector_result.get('documents', []):
                vector_results.append({
                    'doc_id': doc.doc_id,
                    'content': doc.content,
                    'score': doc.score,
                    'metadata': doc.metadata
                })
            
            # Perform keyword search
            keyword_result = await self.keyword_retriever.retrieve(query, excessive_k)
            keyword_results = []
            for doc in keyword_result.get('documents', []):
                keyword_results.append({
                    'doc_id': doc.doc_id,
                    'content': doc.content,
                    'score': doc.score,
                    'metadata': doc.metadata
                })
            
            # Combine results based on the configured method
            if self.combination_method == "convex_combination":
                combined_results = self._combine_with_convex_combination(vector_results, keyword_results)
            elif self.combination_method == "reciprocal_rank_fusion":
                combined_results = self._combine_with_rrf(vector_results, keyword_results)
            elif self.combination_method == "borda_count":
                combined_results = self._combine_with_borda_count(vector_results, keyword_results)
            else:
                raise ValueError(f"Invalid combination method: {self.combination_method}")
            
            # Filter to top k
            top_results = HybridUtils.filter_top_k(combined_results, k)
            
            # Convert back to Document objects
            documents = []
            for result in top_results:
                doc = Document(
                    doc_id=result['doc_id'],
                    content=result['content'],
                    score=result['score'],
                    metadata=result['metadata']
                )
                documents.append(doc)
            
            # Calculate token counts (sum from both retrievers)
            total_embedding_tokens = (
                vector_result.get('embedding_token_count', 0.0) + 
                keyword_result.get('embedding_token_count', 0.0)
            )
            
            # Create final result
            result = RetrievalResult(
                documents=documents,
                embedding_token_count=total_embedding_tokens,
                llm_input_token_count=0.0,
                llm_output_token_count=0.0
            )
            
            # Log combination statistics if debug mode is enabled
            if self.config.get("debug_mode", False):
                overlap_stats = HybridUtils.calculate_result_overlap(vector_results, keyword_results)
                logger.info(f"Hybrid search ({self.combination_method}) stats: {overlap_stats}")
            
            return result
            
        except Exception as e:
            logger.error(f"Hybrid search retrieval failed: {e}")
            return RetrievalResult(
                documents=[],
                embedding_token_count=0.0,
                llm_input_token_count=0.0,
                llm_output_token_count=0.0
            )
    
    def _combine_with_convex_combination(
        self, 
        vector_results: List[Dict[str, Any]], 
        keyword_results: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Combine results using convex combination"""
        try:
            return HybridUtils.combine_with_convex_combination(
                results_list=[vector_results, keyword_results],
                method_names=["vector","keyword"],
                weights=[self.config.get("alpha", 0.5),1-self.config.get("alpha", 0.5)],
                normalization_method=self.config.get("normalization_method", "minmax"),
                excessive_k=self.config.get("excessive_k", 60)
                )
        except Exception as e:
            logger.error(f"Convex combination failed: {e}")
            return []
    
    def _combine_with_rrf(
        self, 
        vector_results: List[Dict[str, Any]], 
        keyword_results: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Combine results using Reciprocal Rank Fusion"""
        try:
            return HybridUtils.combine_with_rrf(
                results_list=[vector_results, keyword_results],
                method_names=["vector","keyword"],
                excessive_k=self.config.get("excessive_k", 60)
            )
            
        except Exception as e:
            logger.error(f"RRF combination failed: {e}")
            return []
    
    def _combine_with_borda_count(
        self, 
        vector_results: List[Dict[str, Any]], 
        keyword_results: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Combine results using Borda count"""
        try:
            return HybridUtils.combine_with_borda_count(
                results_list=[vector_results, keyword_results],
                method_names=["vector","keyword"],
                excessive_k=self.config.get("excessive_k", 60)
            )
        except Exception as e:
            logger.error(f"Borda count combination failed: {e}")
            return []

    async def index_documents(self, documents: List[Document]) -> bool:
        """Index documents in both vector and keyword retrievers"""
        try:
            # Index in both retrievers
            vector_success = await self.vector_retriever.index_documents(documents)
            keyword_success = await self.keyword_retriever.index_documents(documents)
            
            # Return True only if both succeed
            success = vector_success and keyword_success
            
            if success:
                logger.info(f"Successfully indexed {len(documents)} documents in hybrid search system")
            else:
                logger.warning("Partial indexing failure in hybrid search system")
            
            return success
            
        except Exception as e:
            logger.error(f"Failed to index documents in hybrid search: {e}")
            return False
    
    def get_retriever_stats(self) -> Dict[str, Any]:
        """Get statistics from both retrievers and hybrid configuration"""
        try:
            stats = {
                'vector_stats': {},
                'keyword_stats': {},
                'hybrid_config': {
                    'combination_method': self.combination_method,
                    'excessive_k': self.config.get("excessive_k", 60)
                }
            }
            
            # Add method-specific parameters
            if self.combination_method == "convex_combination":
                stats['hybrid_config'].update({
                    'alpha': self.config.get("alpha", 0.5),
                    'normalization_method': self.config.get("normalization_method", "minmax")
                })
            else:  # reciprocal_rank_fusion
                stats['hybrid_config'].update({
                    'excessive_k': self.config.get("excessive_k", 60)
                })
            
            # Get vector stats if available
            if hasattr(self.vector_retriever, 'get_index_stats'):
                stats['vector_stats'] = self.vector_retriever.get_index_stats()
            
            # Get keyword stats if available
            if hasattr(self.keyword_retriever, 'get_index_stats'):
                stats['keyword_stats'] = self.keyword_retriever.get_index_stats()
            
            return stats
            
        except Exception as e:
            logger.error(f"Failed to get retriever stats: {e}")
            return {}
    
    async def get_combination_analysis(self, query: Query, k: Optional[int] = None) -> Dict[str, Any]:
        """
        Analyze the combination process for debugging purposes.
        Returns detailed information about how results were combined.
        """
        try:
            k = k or self.config.get("top_k", 10)
            excessive_k = self.config.get("excessive_k", k * 3)
            
            # Get individual results
            vector_result = await self.vector_retriever.retrieve(query, excessive_k)
            keyword_result = await self.keyword_retriever.retrieve(query, excessive_k)
            
            vector_results = [
                {'doc_id': doc.doc_id, 'content': doc.content, 'score': doc.score, 'metadata': doc.metadata}
                for doc in vector_result.get('documents', [])
            ]
            keyword_results = [
                {'doc_id': doc.doc_id, 'content': doc.content, 'score': doc.score, 'metadata': doc.metadata}
                for doc in keyword_result.get('documents', [])
            ]
            
            # Calculate overlap
            overlap_stats = HybridUtils.calculate_result_overlap(vector_results, keyword_results)
            
            # Get combined results
            if self.combination_method == "convex_combination":
                combined_results = self._combine_with_convex_combination(vector_results, keyword_results)
                method_params = {
                    'alpha': self.config.get("alpha", 0.5),
                    'normalization_method': self.config.get("normalization_method", "minmax"),
                    'excessive_k': excessive_k
                }
            elif self.combination_method == "reciprocal_rank_fusion":
                combined_results = self._combine_with_rrf(vector_results, keyword_results)
                method_params = {
                    'excessive_k': excessive_k
                }
            elif self.combination_method == "borda_count":
                combined_results = self._combine_with_borda_count(vector_results, keyword_results)
                method_params = {
                    'excessive_k': excessive_k
                }
            else:
                raise ValueError(f"Invalid combination method: {self.combination_method}")
            
            analysis = {
                'query_text': query.processed_text,
                'combination_method': self.combination_method,
                'parameters': {
                    'excessive_k': excessive_k,
                    'final_k': k,
                    **method_params
                },
                'overlap_stats': overlap_stats,
                'vector_top_5': [r['doc_id'] for r in vector_results[:5]],
                'keyword_top_5': [r['doc_id'] for r in keyword_results[:5]],
                'combined_top_5': [r['doc_id'] for r in combined_results[:5]],
                'total_unique_docs': len(combined_results)
            }
            
            return analysis
            
        except Exception as e:
            logger.error(f"Failed to generate combination analysis: {e}")
            return {}


class GraphRAG(RetrievalComponent):
    """Graph-based RAG retrieval using Neo4j knowledge graph"""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        
        # Neo4j configuration
        self.neo4j_uri = config.get("graph_rag_neo4j_uri", "bolt://neo4j:7687")
        self.neo4j_user = config.get("graph_rag_neo4j_user", "neo4j")
        self.neo4j_password = config.get("graph_rag_neo4j_password", "admin123")
        
        # Ollama configuration for embeddings
        self.ollama_url = config.get("graph_rag_ollama_embedding_url", "http://ollama_gpu-3:11434/api/embeddings")
        self.embedding_model = config.get("graph_rag_embedding_model", "mxbai-embed-large")
        
        # Graph retrieval parameters
        self.retrieval_method = config.get("graph_rag_retrieval_method", "basic")  # "basic" or "traversal"
        self.similarity_threshold = config.get("graph_rag_similarity_threshold", 0.7)
        self.max_depth = config.get("graph_rag_max_depth", 2)  # for traversal method
        
        # Vector index configuration
        self.vector_index_name = config.get("graph_rag_vector_index_name", "entity_embeddings")
        self.embedding_dimension = config.get("graph_rag_embedding_dimension", 1024)
        
        # Initialize Neo4j driver
        self.driver = None
        self._setup_neo4j_connection()
        self._initialize_vector_index()
    
    def _setup_neo4j_connection(self):
        """Setup Neo4j database connection"""
        try:
            self.driver = GraphDatabase.driver(
                self.neo4j_uri, 
                auth=(self.neo4j_user, self.neo4j_password)
            )
            # Test connection
            with self.driver.session() as session:
                session.run("RETURN 1")
            logger.info("Neo4j connection established successfully")
        except Exception as e:
            logger.error(f"Failed to connect to Neo4j: {e}")
            raise
    
    def _initialize_vector_index(self):
        """Initialize vector index for entity embeddings"""
        try:
            with self.driver.session() as session:
                # Check if index already exists
                result = session.run("SHOW INDEXES")
                existing_indexes = [record.get("name") for record in result]
                
                if self.vector_index_name not in existing_indexes:
                    # Create vector index
                    session.run(f"""
                    CREATE VECTOR INDEX {self.vector_index_name} 
                    FOR (n:Entity) 
                    ON (n.embedding) 
                    OPTIONS {{
                        indexConfig: {{
                            `vector.dimensions`: {self.embedding_dimension},
                            `vector.similarity_function`: 'cosine'
                        }}
                    }}
                    """)
                    logger.info(f"Created vector index: {self.vector_index_name}")
                else:
                    logger.info(f"Vector index {self.vector_index_name} already exists")
        except Exception as e:
            logger.warning(f"Could not initialize vector index: {e}")

    def _embed_text_with_ollama(self, text: str) -> List[float]:
        """Generate embeddings using OllamaEmbeddings (langchain_community)"""
        try:
            from langchain_community.embeddings import OllamaEmbeddings
            import os

            # Get the Ollama API URL from environment variable or config
            ollama_api_url = os.getenv("OLLAMA_API_URL", "http://ollama-gpu-3:11435/api")
            # Remove '/api' suffix for OllamaEmbeddings base_url
            base_url = ollama_api_url.replace("/api", "")

            embedding_model = getattr(self, "embedding_model", "mxbai-embed-large")
            embedding = OllamaEmbeddings(
                model=embedding_model,
                base_url=base_url
            )
            result = embedding.embed_query(text)
            if not result or not isinstance(result, list):
                raise ValueError("No embedding returned")
            return result
        except Exception as e:
            logger.error(f"Failed to generate embedding with OllamaEmbeddings: {e}")
            # Return zero vector as fallback
            return [0.0] * self.embedding_dimension

    def _retrieve_context_basic(self, query_embedding: List[float], top_k: int) -> List[Dict[str, Any]]:
        """Basic retrieval using vector similarity"""
        cypher_query = """
        // Find similar entities using cosine similarity
        MATCH (e:Entity)
        WHERE e.embedding IS NOT NULL
        WITH e, 
             reduce(acc = 0.0, i IN range(0, size(e.embedding)-1) | 
                    acc + e.embedding[i] * $query_embedding[i]) / 
             (sqrt(reduce(acc = 0.0, i IN range(0, size(e.embedding)-1) | 
                   acc + e.embedding[i] * e.embedding[i])) * 
              sqrt(reduce(acc = 0.0, i IN range(0, size($query_embedding)-1) | 
                   acc + $query_embedding[i] * $query_embedding[i]))) AS similarity
        WHERE similarity >= $similarity_threshold
        
        // Get direct relations from similar entities with all metadata
        MATCH (e)-[r:RELATION]->(target:Entity)
        RETURN DISTINCT 
            e.name AS subject, 
            r.type AS relation, 
            target.name AS object, 
            r.source_doc AS source_doc,
            r.doc_id AS doc_id,
            r.sentence AS sentence,
            r.created_at AS created_at,
            r.chunk_id AS chunk_id,
            similarity
        ORDER BY similarity DESC
        LIMIT $top_k
        """
        
        with self.driver.session() as session:
            result = session.run(
                cypher_query,
                query_embedding=query_embedding,
                similarity_threshold=self.similarity_threshold,
                top_k=top_k
            )
            
            relations = []
            for record in result:
                relations.append({
                    'subject': record['subject'],
                    'relation': record['relation'],
                    'object': record['object'],
                    'source_doc': record.get('source_doc'),
                    'doc_id': record.get('doc_id'),
                    'sentence': record.get('sentence'),
                    'created_at': record.get('created_at'),
                    'chunk_id': record.get('chunk_id'),
                    'similarity': record['similarity']
                })
            
            return relations
    
    def _retrieve_context_traversal(self, query_embedding: List[float], top_k: int) -> List[Dict[str, Any]]:
        """Enhanced retrieval with graph traversal"""
        cypher_query = """
        // Step 1: Find similar entities
        MATCH (e:Entity)
        WHERE e.embedding IS NOT NULL
        WITH e, 
             reduce(acc = 0.0, i IN range(0, size(e.embedding)-1) | 
                    acc + e.embedding[i] * $query_embedding[i]) / 
             (sqrt(reduce(acc = 0.0, i IN range(0, size(e.embedding)-1) | 
                   acc + e.embedding[i] * e.embedding[i])) * 
              sqrt(reduce(acc = 0.0, i IN range(0, size($query_embedding)-1) | 
                   acc + $query_embedding[i] * $query_embedding[i]))) AS similarity
        WHERE similarity >= $similarity_threshold
        ORDER BY similarity DESC
        LIMIT 10
        
        // Step 2: Traverse graph to find connected entities
        MATCH path = (e)-[*1..$max_depth]-(connected:Entity)
        WITH e, connected, similarity, length(path) AS distance
        
        // Step 3: Get all relations involving these connected entities with metadata
        MATCH (a:Entity)-[r:RELATION]->(b:Entity)
        WHERE a.name IN [e.name, connected.name] OR b.name IN [e.name, connected.name]
        
        RETURN DISTINCT
            a.name AS subject,
            r.type AS relation,
            b.name AS object,
            r.source_doc AS source_doc,
            r.doc_id AS doc_id,
            r.sentence AS sentence,
            r.created_at AS created_at,
            r.chunk_id AS chunk_id,
            similarity,
            distance
        ORDER BY similarity DESC, distance ASC
        LIMIT $top_k
        """
        
        with self.driver.session() as session:
            result = session.run(
                cypher_query,
                query_embedding=query_embedding,
                similarity_threshold=self.similarity_threshold,
                max_depth=self.max_depth,
                top_k=top_k
            )
            
            relations = []
            for record in result:
                relations.append({
                    'subject': record['subject'],
                    'relation': record['relation'],
                    'object': record['object'],
                    'source_doc': record.get('source_doc'),
                    'doc_id': record.get('doc_id'),
                    'sentence': record.get('sentence'),
                    'created_at': record.get('created_at'),
                    'chunk_id': record.get('chunk_id'),
                    'similarity': record['similarity'],
                    'distance': record.get('distance', 0)
                })
            
            return relations
    
    def _relations_to_documents(self, relations: List[Dict[str, Any]]) -> List[Document]:
        """Convert graph relations to Document objects with rich metadata"""
        documents = []
        
        for i, rel in enumerate(relations):
            # Create content from relation and include context sentence if available
            base_content = f"{rel['subject']} {rel['relation']} {rel['object']}"
            
            # Add sentence context if available
            if rel.get('sentence') and rel['sentence'].strip():
                content = f"{base_content}\nContext: {rel['sentence']}"
            else:
                content = base_content
            
            # Generate unique doc_id that includes relation info
            relation_doc_id = f"graph_rel_{rel.get('doc_id', 'unknown')}_{i}"
            
            # Create comprehensive metadata
            metadata = {
                # Source tracking
                'source_doc': rel.get('source_doc', 'unknown'),
                'original_doc_id': rel.get('doc_id'),
                'chunk_id': rel.get('chunk_id'),
                
                # Relation information
                'relation_type': rel['relation'],
                'subject': rel['subject'],
                'object': rel['object'],
                'sentence': rel.get('sentence', ''),
                
                # Retrieval information
                'similarity_score': rel.get('similarity', 0.0),
                'graph_distance': rel.get('distance', 0),
                'retrieval_method': self.retrieval_method,
                
                # Timestamps
                'created_at': rel.get('created_at'),
                'retrieved_at': time.time(),
                
                # Graph-specific
                'is_graph_relation': True,
                'relation_index': i
            }
            
            # Create document
            doc = Document(
                doc_id=relation_doc_id,
                content=content,
                score=rel.get('similarity', 0.0),
                metadata=metadata
            )
            documents.append(doc)
        
        return documents
    
    async def retrieve(self, query: Query, k: Optional[int] = None) -> Dict[str, Any]:
        """Retrieve documents using graph-based search"""
        k = k or self.config.get("top_k", 10)
        
        try:
            # Generate query embedding
            query_text = query.processed_text
            query_embedding = self._embed_text_with_ollama(query_text)
            
            if not query_embedding or all(x == 0.0 for x in query_embedding):
                logger.warning("Failed to generate valid query embedding")
                return {
                    'documents': [],
                    'embedding_token_count': 0.0,
                    'llm_input_token_count': 0.0,
                    'llm_output_token_count': 0.0
                }
            
            # Retrieve relations based on method
            if self.retrieval_method == "basic":
                relations = self._retrieve_context_basic(query_embedding, k)
            elif self.retrieval_method == "traversal":
                relations = self._retrieve_context_traversal(query_embedding, k)
            else:
                raise ValueError(f"Unknown retrieval method: {self.retrieval_method}")
            
            if not relations:
                logger.info("No relevant relations found in knowledge graph")
                return {
                    'documents': [],
                    'embedding_token_count': float(len(query_text.split())),
                    'llm_input_token_count': 0.0,
                    'llm_output_token_count': 0.0
                }
            
            # Convert relations to documents
            documents = self._relations_to_documents(relations)
            
            # Calculate token counts
            embedding_token_count = float(len(query_text.split()))
            
            logger.info(f"Retrieved {len(documents)} documents using {self.retrieval_method} method")
            
            return {
                'documents': documents,
                'embedding_token_count': embedding_token_count,
                'llm_input_token_count': 0.0,
                'llm_output_token_count': 0.0
            }
            
        except Exception as e:
            logger.error(f"Graph retrieval failed: {e}")
            return {
                'documents': [],
                'embedding_token_count': 0.0,
                'llm_input_token_count': 0.0,
                'llm_output_token_count': 0.0
            }
    
    async def index_documents(self, documents: List[Document]) -> bool:
        """
        Index documents in the knowledge graph by extracting relations.
        Tracks document provenance with doc_id and other metadata.
        """
        try:
            logger.info(f"Starting to index {len(documents)} documents in knowledge graph")
            
            for doc in documents:
                doc_id = doc.doc_id
                source_doc = doc.metadata.get('source', doc_id) if doc.metadata else doc_id
                
                logger.info(f"Processing document: {doc_id}")
                
                # Check if document already processed (optional optimization)
                if self._is_document_already_processed(doc_id):
                    logger.info(f"Document {doc_id} already processed, skipping")
                    continue
                
                # Extract relations from document content using LLM with chunking
                all_relations = []
                chunks = self._chunk_text(doc.content, self.config.get("max_chunk_chars", 4000))
                
                for chunk_idx, chunk in enumerate(chunks):
                    logger.debug(f"Processing chunk {chunk_idx + 1}/{len(chunks)} for doc {doc_id}")
                    relations = self._extract_relations_llm_ollama(chunk)
                    
                    if relations:
                        # Add relations to Neo4j with chunk tracking
                        self._add_relations_to_neo4j(
                            relations, 
                            source_doc=source_doc,
                            doc_id=doc_id, 
                            chunk_id=chunk_idx
                        )
                        all_relations.extend(relations)
                        logger.debug(f"Added {len(relations)} relations from chunk {chunk_idx}")
                
                if all_relations:
                    logger.info(f"Successfully indexed {len(all_relations)} relations from document {doc_id}")
                    
                    # Generate embeddings for new entities
                    self._embed_new_entities()
                else:
                    logger.warning(f"No relations extracted from document {doc_id}")
            
            logger.info(f"Successfully completed indexing {len(documents)} documents")
            return True
            
        except Exception as e:
            logger.error(f"Failed to index documents: {e}")
            return False
    
    def _is_document_already_processed(self, doc_id: str) -> bool:
        """Check if a document has already been processed"""
        try:
            with self.driver.session() as session:
                result = session.run(
                    "MATCH ()-[r:RELATION {doc_id: $doc_id}]-() RETURN COUNT(r) AS count",
                    doc_id=doc_id
                )
                count = result.single()["count"]
                return count > 0
        except Exception as e:
            logger.warning(f"Could not check if document {doc_id} was processed: {e}")
            return False
    
    def _extract_relations_with_ollama(self, text: str, doc_id: str) -> List[Dict[str, Any]]:
        """
        Extract relations using Ollama LLM (adapted from graph_utils.py)
        """
        # Chunk text if it's too long
        max_chars = self.config.get("max_chunk_chars", 4000)
        chunks = self._chunk_text(text, max_chars)
        
        all_relations = []
        for chunk in chunks:
            relations = self._extract_relations_llm_ollama(chunk)
            all_relations.extend(relations)
        
        return all_relations
    
    def _chunk_text(self, text: str, max_chars: int = 4000) -> List[str]:
        """Split text into chunks"""
        chunks = []
        start = 0
        while start < len(text):
            end = min(start + max_chars, len(text))
            chunks.append(text[start:end])
            start = end
        return chunks
    
    def _extract_relations_llm_ollama(self, text: str) -> List[Dict[str, Any]]:
        """Extract relations using Ollama LLM (via OllamaUtil)"""
        from rag_pipeline.util.api.ollama_client import OllamaUtil

        ollama_model = self.config.get("graph_rag_ollama_model", "gemma3:4b")
        
        prompt = f"""
You are an expert relation extraction system.

Extract all meaningful factual relations as triples from the text below.
Return ONLY a valid JSON array (NO explanation, NO code fences, NO extra text).
Each item MUST have exactly these keys:
- "subject"
- "relation"
- "object"
- "sentence"

If something is not a relation triple, DO NOT include it.

Text:
\"\"\"{text}\"\"\"
"""

        try:
            ollama_result = OllamaUtil.get_ollama_response(ollama_model, prompt)
            if ollama_result is None:
                logger.error("OllamaUtil.get_ollama_response returned None")
                return []
            text_out = ollama_result.get("response", "")

            # Parse JSON response
            import json
            import re

            cleaned = re.sub(r"```[a-zA-Z]*", "", text_out).strip()
            cleaned = cleaned.strip("` \n")

            json_arrays = re.findall(r"\[.*?\]", cleaned, flags=re.S)
            parsed_relations = []

            if not json_arrays:
                try:
                    single = json.loads(cleaned)
                    if isinstance(single, list):
                        json_arrays = [cleaned]
                except Exception:
                    return []

            for arr in json_arrays:
                try:
                    parsed = json.loads(arr)
                    if isinstance(parsed, list):
                        parsed_relations.extend(parsed)
                except Exception:
                    continue

            # Normalize relations
            normalized = []
            for r in parsed_relations:
                if not isinstance(r, dict):
                    continue
                subj = (r.get("subject") or "").strip()
                rel = (r.get("relation") or r.get("verb") or "").strip()
                obj = (r.get("object") or "").strip()
                sent = (r.get("sentence") or text).strip()
                
                if subj and rel and obj:
                    normalized.append({
                        "subject": subj,
                        "relation": rel,
                        "object": obj,
                        "sentence": sent
                    })

            return normalized
            
        except Exception as e:
            logger.error(f"LLM relation extraction failed: {e}")
            return []
    
    def _add_relations_to_neo4j(self, relations: List[Dict[str, Any]], source_doc: str, doc_id: str = None, chunk_id: int = None):
        """Add relations to Neo4j database with comprehensive metadata"""
        import datetime
        
        with self.driver.session() as session:
            for i, rel in enumerate(relations):
                # Create timestamp
                created_at = datetime.datetime.now().isoformat()
                
                # Prepare relation properties with metadata
                relation_props = {
                    'type': rel["relation"],
                    'source_doc': source_doc,
                    'doc_id': doc_id or source_doc,
                    'sentence': rel.get("sentence", ""),
                    'created_at': created_at,
                    'relation_id': f"{doc_id}_{chunk_id}_{i}" if doc_id and chunk_id is not None else f"{source_doc}_{i}"
                }
                
                # Add chunk_id if provided
                if chunk_id is not None:
                    relation_props['chunk_id'] = chunk_id
                
                session.run(
                    """
                    MERGE (a:Entity {name: $subject})
                    MERGE (b:Entity {name: $object})
                    MERGE (a)-[r:RELATION {
                        type: $type,
                        source_doc: $source_doc,
                        doc_id: $doc_id,
                        relation_id: $relation_id
                    }]->(b)
                    SET r.sentence = $sentence,
                        r.created_at = $created_at,
                        r.chunk_id = $chunk_id
                    """,
                    subject=rel["subject"],
                    object=rel["object"],
                    **relation_props
                )
    
    def _embed_new_entities(self):
        """Generate embeddings for entities that don't have them"""
        with self.driver.session() as session:
            # Find entities without embeddings
            result = session.run("MATCH (n:Entity) WHERE n.embedding IS NULL RETURN n.name AS name LIMIT 100")
            entities_to_embed = [record["name"] for record in result]
            
            for entity_name in entities_to_embed:
                try:
                    embedding = self._embed_text_with_ollama(entity_name)
                    if embedding and not all(x == 0.0 for x in embedding):
                        session.run(
                            "MATCH (n:Entity {name: $name}) SET n.embedding = $embedding",
                            name=entity_name, embedding=embedding
                        )
                        logger.debug(f"Generated embedding for entity: {entity_name}")
                except Exception as e:
                    logger.warning(f"Failed to embed entity '{entity_name}': {e}")
    
    def get_graph_stats(self) -> Dict[str, Any]:
        """Get statistics about the knowledge graph with document-level breakdown"""
        try:
            with self.driver.session() as session:
                # Count entities
                entity_count = session.run("MATCH (n:Entity) RETURN COUNT(n) AS count").single()["count"]
                
                # Count relations
                relation_count = session.run("MATCH ()-[r:RELATION]->() RETURN COUNT(r) AS count").single()["count"]
                
                # Count entities with embeddings
                embedded_count = session.run("MATCH (n:Entity) WHERE n.embedding IS NOT NULL RETURN COUNT(n) AS count").single()["count"]
                
                # Count unique documents
                doc_count = session.run("MATCH ()-[r:RELATION]->() WHERE r.doc_id IS NOT NULL RETURN COUNT(DISTINCT r.doc_id) AS count").single()["count"]
                
                # Count unique source documents
                source_doc_count = session.run("MATCH ()-[r:RELATION]->() WHERE r.source_doc IS NOT NULL RETURN COUNT(DISTINCT r.source_doc) AS count").single()["count"]
                
                # Get document-level statistics
                doc_stats = session.run("""
                    MATCH ()-[r:RELATION]->()
                    WHERE r.doc_id IS NOT NULL
                    RETURN r.doc_id AS doc_id, 
                           r.source_doc AS source_doc,
                           COUNT(r) AS relation_count
                    ORDER BY relation_count DESC
                    LIMIT 10
                """)
                
                top_docs = []
                for record in doc_stats:
                    top_docs.append({
                        'doc_id': record['doc_id'],
                        'source_doc': record['source_doc'],
                        'relation_count': record['relation_count']
                    })
                
                return {
                    'total_entities': entity_count,
                    'total_relations': relation_count,
                    'entities_with_embeddings': embedded_count,
                    'embedding_coverage': embedded_count / entity_count if entity_count > 0 else 0,
                    'unique_documents': doc_count,
                    'unique_source_documents': source_doc_count,
                    'avg_relations_per_doc': relation_count / doc_count if doc_count > 0 else 0,
                    'top_documents_by_relations': top_docs,
                    'retrieval_method': self.retrieval_method,
                    'similarity_threshold': self.similarity_threshold
                }
        except Exception as e:
            logger.error(f"Failed to get graph stats: {e}")
            return {}
    
    def get_document_relations(self, doc_id: str) -> List[Dict[str, Any]]:
        """Get all relations from a specific document"""
        try:
            with self.driver.session() as session:
                result = session.run("""
                    MATCH (a:Entity)-[r:RELATION]->(b:Entity)
                    WHERE r.doc_id = $doc_id
                    RETURN a.name AS subject,
                           r.type AS relation,
                           b.name AS object,
                           r.sentence AS sentence,
                           r.chunk_id AS chunk_id,
                           r.created_at AS created_at
                    ORDER BY r.chunk_id, r.relation_id
                """, doc_id=doc_id)
                
                relations = []
                for record in result:
                    relations.append({
                        'subject': record['subject'],
                        'relation': record['relation'],
                        'object': record['object'],
                        'sentence': record['sentence'],
                        'chunk_id': record['chunk_id'],
                        'created_at': record['created_at']
                    })
                
                return relations
        except Exception as e:
            logger.error(f"Failed to get relations for document {doc_id}: {e}")
            return []
    
    def get_documents_containing_entity(self, entity_name: str) -> List[Dict[str, Any]]:
        """Get all documents that contain relations involving a specific entity"""
        try:
            with self.driver.session() as session:
                result = session.run("""
                    MATCH (e:Entity {name: $entity_name})-[r:RELATION]-(other:Entity)
                    RETURN DISTINCT r.doc_id AS doc_id,
                                   r.source_doc AS source_doc,
                                   COUNT(r) AS relation_count
                    WHERE r.doc_id IS NOT NULL
                    ORDER BY relation_count DESC
                """, entity_name=entity_name)
                
                documents = []
                for record in result:
                    documents.append({
                        'doc_id': record['doc_id'],
                        'source_doc': record['source_doc'],
                        'relation_count': record['relation_count']
                    })
                
                return documents
        except Exception as e:
            logger.error(f"Failed to get documents for entity {entity_name}: {e}")
            return []
    
    def delete_document_relations(self, doc_id: str) -> bool:
        """Delete all relations from a specific document"""
        try:
            with self.driver.session() as session:
                result = session.run("""
                    MATCH ()-[r:RELATION {doc_id: $doc_id}]->()
                    DELETE r
                    RETURN COUNT(*) AS deleted_count
                """, doc_id=doc_id)
                
                deleted_count = result.single()["deleted_count"]
                logger.info(f"Deleted {deleted_count} relations from document {doc_id}")
                return True
        except Exception as e:
            logger.error(f"Failed to delete relations for document {doc_id}: {e}")
            return False
    
    def __del__(self):
        """Close Neo4j driver connection"""
        if self.driver:
            self.driver.close()