import time, os, sys
import logging, requests, json
from typing import List, Dict, Any, Optional, TypedDict
from abc import ABC, abstractmethod
from neo4j import GraphDatabase
import pandas as pd

from rag_pipeline.core.modular_framework import (
    RetrievalComponent, Document, Query
)
from rag_pipeline.util.retrieval_utils.combination_utils import HybridUtils

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
    
    def _setup_vectorstore(self, documents: Optional[List[Document]] = None):
        """Setup the vector store"""

        from rag_pipeline.util.vectorstore.qdrant_store import QdrantVectorStore
        
        # Use embedding model from config
        embedding_model = self.config.get("embedding_model", "mxbai-embed-large")

        if documents is not None:
            try:
                docs_data = []
                for doc in documents:
                    docs_data.append({
                        'text': doc.content,
                        'doc_id': doc.doc_id,
                        'metadata': doc.metadata or {}
                    })
                
                docs_df = pd.DataFrame(docs_data)
                dataset_hash = QdrantVectorStore._generate_dataset_hash(docs_df)
                self.vectorstore = QdrantVectorStore(embedding_model, dataset_hash)
            except Exception as e:
                logger.error(f"Failed to setup vectorstore from documents: {e}")
                raise
        else:
            try:
                from rag_pipeline.util.vectorstore.dataset_utils import generate_dataset_hash_from_folder
                import os

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
            documents = HybridUtils.convert_to_documents(results)
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
            if self.vectorstore is None:
                self._setup_vectorstore(documents)
            
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
            documents = HybridUtils.convert_to_documents(results)
            
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
            vector_results = HybridUtils.convert_documents_to_results(vector_result.get('documents', []))
            
            # Perform keyword search
            keyword_result = await self.keyword_retriever.retrieve(query, excessive_k)
            keyword_results = HybridUtils.convert_documents_to_results(keyword_result.get('documents', []))
            
            # Combine results based on the configured method
            if self.combination_method == "convex_combination":
                combined_results = self._combine_with_convex_combination([vector_results, keyword_results])
            elif self.combination_method == "reciprocal_rank_fusion":
                combined_results = self._combine_with_rrf([vector_results, keyword_results])
            elif self.combination_method == "borda_count":
                combined_results = self._combine_with_borda_count([vector_results, keyword_results])
            elif self.combination_method == "simply":
                combined_results = HybridUtils.combine_simply(
                    results_list=[vector_results, keyword_results],
                    method_names=["vector","keyword"],
                    normalization_method=self.config.get("normalization_method", "minmax")
                )
            else:
                raise ValueError(f"Invalid combination method: {self.combination_method}")
            
            # Filter to top k
            top_results = HybridUtils.filter_top_k(combined_results, k)
            
            # Convert back to Document objects
            documents = HybridUtils.convert_to_documents(top_results)
            
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
        results_list: List[List[Dict[str, Any]]]
    ) -> List[Dict[str, Any]]:
        """Combine results using convex combination"""
        try:
            return HybridUtils.combine_with_convex_combination(
                results_list=results_list,
                method_names=["vector","keyword"],
                weights=[1/len(self.retrieval_methods)] * len(self.retrieval_methods) if self.config.get("weights", None) is None else self.config.get("weights"), 
                normalization_method=self.config.get("normalization_method", "minmax"),
                )
        except Exception as e:
            logger.error(f"Convex combination failed: {e}")
            return []
    
    def _combine_with_rrf(
        self, 
        results_list: List[List[Dict[str, Any]]]
    ) -> List[Dict[str, Any]]:
        """Combine results using Reciprocal Rank Fusion"""
        try:
            return HybridUtils.combine_with_rrf(
                results_list=results_list,
                method_names=["vector","keyword"],
            )
            
        except Exception as e:
            logger.error(f"RRF combination failed: {e}")
            return []
    
    def _combine_with_borda_count(
        self, 
        results_list: List[List[Dict[str, Any]]]
    ) -> List[Dict[str, Any]]:
        """Combine results using Borda count"""
        try:
            return HybridUtils.combine_with_borda_count(
                results_list=results_list,
                method_names=["vector","keyword"],
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
        self.ollama_url = config.get("graph_rag_ollama_embedding_url", "http://ollama-gpu-3:11435/api/embeddings")
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

        ollama_model = self.config.get("graph_rag_ollama_model", "gemma3:12b")
        
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


class HyperGraphRAG(RetrievalComponent):
    """HyperGraph-based RAG retrieval using Neo4j hypergraph with multi-entity relationships"""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        
        # Neo4j configuration
        self.neo4j_uri = config.get("hypergraph_neo4j_uri", "bolt://neo4j:7687")
        self.neo4j_user = config.get("hypergraph_neo4j_user", "neo4j")
        self.neo4j_password = config.get("hypergraph_neo4j_password", "admin123")
        
        # Ollama embedding configuration
        self.embedding_model = config.get("hypergraph_embedding_model", "mxbai-embed-large")
        self.embedding_dimension = config.get("hypergraph_embedding_dimension", 1024)
        
        # HyperGraph retrieval parameters
        self.retrieval_method = config.get("hypergraph_retrieval_method", "basic")  # "basic" or "expansion"
        self.similarity_threshold = config.get("hypergraph_similarity_threshold", 0.7)
        self.max_depth = config.get("hypergraph_max_depth", 2)
        self.min_hyperedge_entities = config.get("hypergraph_min_entities", 3)
        
        # Processing parameters
        self.chunk_size = config.get("hypergraph_chunk_size", 2000)
        
        # Initialize components
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
            logger.info("Neo4j connection for HyperGraphRAG established successfully")
        except Exception as e:
            logger.error(f"Failed to connect to Neo4j for HyperGraphRAG: {e}")
            raise
    
    def _embed_text(self, text: str) -> List[float]:
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
    
    def _initialize_vector_index(self):
        """Initialize vector index for hyperedge embeddings"""
        try:
            with self.driver.session() as session:
                # Create indexes for better performance
                session.run("CREATE INDEX hyperedge_type_idx IF NOT EXISTS FOR (he:HyperEdge) ON (he.type)")
                session.run("CREATE INDEX entity_name_idx IF NOT EXISTS FOR (e:HyperEntity) ON (e.name)")
                session.run("CREATE INDEX hyperedge_doc_idx IF NOT EXISTS FOR (he:HyperEdge) ON (he.source_document)")
                
                logger.info("HyperGraphRAG indexes created successfully")
        except Exception as e:
            logger.warning(f"Could not initialize indexes: {e}")
    
    def _extract_hyperedges_with_llm(self, text: str) -> List[Dict[str, Any]]:
        """Extract hyperedge relations using LLM (via OllamaUtil)"""
        from rag_pipeline.util.api.ollama_client import OllamaUtil

        ollama_model = self.config.get("hypergraph_ollama_model", "gemma3:12b")
        
        prompt = f"""
You are an advanced hypergraph relation extraction system.

Your task is to extract all meaningful hyperedges from the text below. A hyperedge represents a relationship, or group that connects {self.min_hyperedge_entities} to 10 entities in a single, coherent context.

Guidelines:
- Each hyperedge must involve between {self.min_hyperedge_entities} and 10 named entities.
- Focus on group-based relationships involving multiple entities.
- Use only information explicitly stated in the text (no inference beyond sentence level).

Output format:
Return only a valid JSON array. No explanations, no markdown/code formatting, no additional text.

Each JSON object must have exactly these fields:
- "entities": [ "Entity1", "Entity2", ... ],
- "hyperedge_type": "short_relation_type",
- "description": "brief description of the hyperedge",
- "source_sentence": "original sentence from the text"

Examples:
- "entities": ["Alice", "Bob", "Charlie"],
- "hyperedge_type": "research_team",
- "description": "Researchers collaborating on AI project",
- "source_sentence": "Alice, Bob, and Charlie collaborated on an AI project at MIT."

- "entities": ["John", "Mary", "David"],
- "hyperedge_type": "event_attendance",
- "description": "Participants in Conference 2024",
- "source_sentence": "John, Mary, and David attended the Conference 2024 in Berlin."

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
            
            # Clean up potential JSON issues
            # Remove control characters first
            cleaned = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', cleaned)
            
            # Remove invisible characters
            cleaned = re.sub(r'⁠', '', cleaned)
            
            # Properly escape backslashes in LaTeX notation for JSON
            # This preserves the LaTeX content while making it JSON-safe
            cleaned = re.sub(r'\\\\', r'\\\\\\\\', cleaned)  # Double escape existing double backslashes
            cleaned = re.sub(r'\\(?!["\\/bfnrt])', r'\\\\', cleaned)  # Escape single backslashes
            
            logger.debug(f"Cleaned text: {cleaned}")

            # Try direct JSON parsing first
            try:
                parsed_data = json.loads(cleaned)
                if isinstance(parsed_data, list):
                    logger.debug("Successfully parsed as direct JSON array")
                    parsed_hyperedges = parsed_data
                else:
                    logger.error("Parsed JSON is not a list")
                    return []
            except Exception as e:
                logger.error(f"Failed to parse as direct JSON: {e}")
                # Try with more aggressive cleaning
                try:
                    # Remove all non-printable characters and try again
                    cleaned_aggressive = re.sub(r'[^\x20-\x7e]', '', cleaned)
                    logger.info(f"Trying with aggressive cleaning: {cleaned_aggressive[:200]}...")
                    parsed_data = json.loads(cleaned_aggressive)
                    if isinstance(parsed_data, list):
                        logger.info("Successfully parsed with aggressive cleaning")
                        parsed_hyperedges = parsed_data
                    else:
                        logger.error("Parsed JSON is still not a list after aggressive cleaning")
                        return []
                except Exception as e2:
                    logger.error(f"Failed to parse even with aggressive cleaning: {e2}")
                    return []

            # Validate and filter hyperedges
            validated_hyperedges = []
            for i, hyperedge in enumerate(parsed_hyperedges):
                logger.debug(f"Validating hyperedge {i}: {hyperedge}")
                if isinstance(hyperedge, dict) and self._validate_hyperedge(hyperedge):
                    validated_hyperedges.append(hyperedge)
                    logger.debug(f"Hyperedge {i} validated successfully")
                else:
                    logger.debug(f"Hyperedge {i} failed validation")

            logger.debug(f"Parsed {len(parsed_hyperedges)} hyperedges, validated {len(validated_hyperedges)}")
            return validated_hyperedges
            
        except Exception as e:
            logger.error(f"LLM hyperedge extraction failed: {e}")
            return []
    
    def _validate_hyperedge(self, hyperedge: Dict[str, Any]) -> bool:
        """Validate extracted hyperedge"""
        required_keys = ["entities", "hyperedge_type", "description", "source_sentence"]
        if not all(key in hyperedge for key in required_keys):
            logger.info(f"Missing required keys. Found: {list(hyperedge.keys())}, Required: {required_keys}")
            return False
        
        entities = hyperedge["entities"]
        if not isinstance(entities, list):
            logger.info(f"Entities is not a list: {type(entities)}")
            return False
            
        if len(entities) < self.min_hyperedge_entities:
            logger.info(f"Not enough entities: {len(entities)} < {self.min_hyperedge_entities}")
            return False
            
        logger.info(f"Hyperedge validation passed: {len(entities)} entities")
        return True
    
    def _chunk_text(self, text: str) -> List[str]:
        """Split text into chunks"""
        chunks = []
        start = 0
        while start < len(text):
            end = min(start + self.chunk_size, len(text))
            chunks.append(text[start:end])
            start = end
        return chunks
    
    def _store_hyperedge(self, session, hyperedge_data: Dict[str, Any], source_doc: str):
        """Store hyperedge and its entities in Neo4j"""
        try:
            # Create hyperedge node
            embedding = self._embed_text(hyperedge_data["description"])
            
            session.run("""
                MERGE (he:HyperEdge {
                    type: $type,
                    description: $description,
                    source_document: $source_document
                })
                SET he.entity_count = $entity_count,
                    he.source_sentence = $source_sentence,
                    he.embedding = $embedding,
                    he.created_at = datetime()
                """,
                type=hyperedge_data["hyperedge_type"],
                description=hyperedge_data["description"],
                source_document=source_doc,
                entity_count=len(hyperedge_data["entities"]),
                source_sentence=hyperedge_data["source_sentence"],
                embedding=embedding
            )
            
            # Connect entities to hyperedge
            for entity_name in hyperedge_data["entities"]:
                session.run("""
                    MERGE (e:HyperEntity {name: $entity_name})
                    WITH e
                    MATCH (he:HyperEdge {type: $type, description: $description, source_document: $source_document})
                    MERGE (e)-[:MEMBER_OF]->(he)
                    """,
                    entity_name=entity_name,
                    type=hyperedge_data["hyperedge_type"],
                    description=hyperedge_data["description"],
                    source_document=source_doc
                )
                
        except Exception as e:
            logger.error(f"Failed to store hyperedge: {e}")
    
    def _retrieve_basic_hypergraph(self, query_embedding: List[float], top_k: int) -> List[Dict[str, Any]]:
        """Basic hypergraph retrieval using vector similarity"""
        cypher_query = """
        MATCH (he:HyperEdge)
        WHERE he.embedding IS NOT NULL
        WITH he, 
             reduce(acc = 0.0, i IN range(0, size(he.embedding)-1) | 
                    acc + he.embedding[i] * $query_embedding[i]) / 
             (sqrt(reduce(acc = 0.0, i IN range(0, size(he.embedding)-1) | 
                   acc + he.embedding[i] * he.embedding[i])) * 
              sqrt(reduce(acc = 0.0, i IN range(0, size($query_embedding)-1) | 
                   acc + $query_embedding[i] * $query_embedding[i]))) AS similarity
        WHERE similarity >= $similarity_threshold
        
        MATCH (e:HyperEntity)-[:MEMBER_OF]->(he)
        RETURN DISTINCT 
            he.type AS hyperedge_type,
            he.description AS hyperedge_description,
            collect(e.name) AS entities,
            he.source_sentence AS source_sentence,
            he.source_document AS source_document,
            similarity
        ORDER BY similarity DESC
        LIMIT $top_k
        """
        
        with self.driver.session() as session:
            try:
                result = session.run(
                    cypher_query,
                    query_embedding=query_embedding,
                    similarity_threshold=self.similarity_threshold,
                    top_k=top_k
                )
                
                hyperedges = []
                for record in result:
                    hyperedges.append({
                        'hyperedge_type': record['hyperedge_type'],
                        'description': record['hyperedge_description'],
                        'entities': record['entities'],
                        'source_sentence': record['source_sentence'],
                        'source_document': record['source_document'],
                        'similarity': record['similarity']
                    })
                
                return hyperedges
                
            except Exception as e:
                logger.error(f"Basic hypergraph retrieval failed: {e}")
                return []
    
    def _retrieve_expansion_hypergraph(self, query_embedding: List[float], top_k: int) -> List[Dict[str, Any]]:
        """Enhanced hypergraph retrieval with expansion"""
        cypher_query = """
        // Step 1: Find similar hyperedges
        MATCH (he:HyperEdge)
        WHERE he.embedding IS NOT NULL
        WITH he, 
             reduce(acc = 0.0, i IN range(0, size(he.embedding)-1) | 
                    acc + he.embedding[i] * $query_embedding[i]) / 
             (sqrt(reduce(acc = 0.0, i IN range(0, size(he.embedding)-1) | 
                   acc + he.embedding[i] * he.embedding[i])) * 
              sqrt(reduce(acc = 0.0, i IN range(0, size($query_embedding)-1) | 
                   acc + $query_embedding[i] * $query_embedding[i]))) AS similarity
        WHERE similarity >= $similarity_threshold
        ORDER BY similarity DESC
        LIMIT 5
        
        // Step 2: Find entities in these hyperedges
        MATCH (e:HyperEntity)-[:MEMBER_OF]->(he)
        WITH e, he, similarity
        
        // Step 3: Find other hyperedges these entities belong to
        MATCH (e)-[:MEMBER_OF]->(other_he:HyperEdge)
        WHERE other_he <> he
        
        MATCH (other_e:HyperEntity)-[:MEMBER_OF]->(other_he)
        
        RETURN DISTINCT
            he.type AS original_type,
            he.description AS original_description,
            other_he.type AS connected_type,
            other_he.description AS connected_description,
            collect(other_e.name) AS connected_entities,
            similarity,
            1 AS distance
        ORDER BY similarity DESC, distance ASC
        LIMIT $top_k
        """
        
        with self.driver.session() as session:
            try:
                result = session.run(
                    cypher_query,
                    query_embedding=query_embedding,
                    similarity_threshold=self.similarity_threshold,
                    top_k=top_k
                )
                
                expansions = []
                for record in result:
                    expansions.append({
                        'original_type': record['original_type'],
                        'original_description': record['original_description'],
                        'connected_type': record['connected_type'],
                        'connected_description': record['connected_description'],
                        'connected_entities': record['connected_entities'],
                        'similarity': record['similarity'],
                        'distance': record['distance']
                    })
                
                return expansions
                
            except Exception as e:
                logger.error(f"Expansion hypergraph retrieval failed: {e}")
                return []
    
    def _hyperedges_to_documents(self, hyperedges: List[Dict[str, Any]], query_text: str) -> List[Document]:
        """Convert hyperedges to Document objects"""
        documents = []
        
        for i, hyperedge in enumerate(hyperedges):
            if 'entities' in hyperedge:
                # Basic retrieval format
                entities_str = ", ".join(hyperedge['entities'])
                content = f"Hyperedge [{hyperedge['hyperedge_type']}]: {entities_str} - {hyperedge['description']}"
                
                if hyperedge.get('source_sentence'):
                    content += f"\nContext: {hyperedge['source_sentence']}"
                
                metadata = {
                    'hyperedge_type': hyperedge['hyperedge_type'],
                    'entities': hyperedge['entities'],
                    'description': hyperedge['description'],
                    'source_sentence': hyperedge.get('source_sentence', ''),
                    'source_document': hyperedge.get('source_document', ''),
                    'original_doc_id': hyperedge.get('source_document', ''),
                    'similarity_score': hyperedge.get('similarity', 0.0),
                    'retrieval_method': 'basic',
                    'is_hypergraph_relation': True,
                    'query_text': query_text,
                    'retrieved_at': time.time()
                }
                
                score = hyperedge.get('similarity', 0.0)
                
            else:
                # Expansion retrieval format
                content = f"Original: [{hyperedge['original_type']}] {hyperedge['original_description']}\n"
                content += f"Connected: [{hyperedge['connected_type']}] {hyperedge['connected_description']}"
                
                entities_str = ", ".join(hyperedge.get('connected_entities', []))
                if entities_str:
                    content += f"\nEntities: {entities_str}"
                
                metadata = {
                    'hyperedge_type': 'expansion',
                    'original_type': hyperedge['original_type'],
                    'connected_type': hyperedge['connected_type'],
                    'original_description': hyperedge['original_description'],
                    'connected_description': hyperedge['connected_description'],
                    'connected_entities': hyperedge.get('connected_entities', []),
                    'similarity_score': hyperedge.get('similarity', 0.0),
                    'distance': hyperedge.get('distance', 0),
                    'retrieval_method': 'expansion',
                    'is_hypergraph_expansion': True,
                    'query_text': query_text,
                    'original_doc_id': hyperedge.get('source_document', ''),
                    'retrieved_at': time.time()
                }
                
                # Convert distance to similarity score
                distance = hyperedge.get('distance', 1)
                score = 1.0 / (1.0 + distance)
            
            doc = Document(
                doc_id=f"hypergraph_{i}_{metadata['original_doc_id']}",
                content=content,
                score=score,
                metadata=metadata
            )
            documents.append(doc)
        
        return documents
    
    async def retrieve(self, query: Query, k: Optional[int] = None) -> RetrievalResult:
        """Retrieve documents using hypergraph-based search"""
        k = k or self.config.get("top_k", 10)
        
        try:
            query_text = query.processed_text
            query_embedding = self._embed_text(query_text)
            
            if not query_embedding or all(x == 0.0 for x in query_embedding):
                logger.warning("Failed to generate valid query embedding")
                return RetrievalResult(
                    documents=[],
                    embedding_token_count=0.0,
                    llm_input_token_count=0.0,
                    llm_output_token_count=0.0
                )
            
            # Retrieve hyperedges based on method
            if self.retrieval_method == "basic":
                hyperedges = self._retrieve_basic_hypergraph(query_embedding, k)
            elif self.retrieval_method == "expansion":
                hyperedges = self._retrieve_expansion_hypergraph(query_embedding, k)
            else:
                raise ValueError(f"Unknown retrieval method: {self.retrieval_method}")
            
            # Convert to documents
            documents = self._hyperedges_to_documents(hyperedges, query_text)
            
            # Limit to top k
            if len(documents) > k:
                documents = sorted(documents, key=lambda x: x.score, reverse=True)[:k]
            
            embedding_token_count = float(len(query_text.split()))
            
            logger.info(f"Retrieved {len(documents)} documents using HyperGraphRAG {self.retrieval_method} method")
            
            return RetrievalResult(
                documents=documents,
                embedding_token_count=embedding_token_count,
                llm_input_token_count=0.0,
                llm_output_token_count=0.0
            )
            
        except Exception as e:
            logger.error(f"HyperGraphRAG retrieval failed: {e}")
            return RetrievalResult(
                documents=[],
                embedding_token_count=0.0,
                llm_input_token_count=0.0,
                llm_output_token_count=0.0
            )
    
    async def index_documents(self, documents: List[Document]) -> bool:
        """Index documents by extracting hyperedge relations"""
        try:
            logger.info(f"Starting to index {len(documents)} documents in hypergraph")
            
            with self.driver.session() as session:
                for doc in documents:
                    doc_id = doc.doc_id
                    source_doc = doc.metadata.get('source', doc_id) if doc.metadata else doc_id
                    
                    logger.debug(f"Processing document: {doc_id}")
                    
                    # Check if already processed
                    if self._is_document_processed(session, source_doc):
                        logger.debug(f"Document {source_doc} already processed, skipping")
                        continue
                    
                    # Process chunks
                    chunks = self._chunk_text(doc.content)
                    total_hyperedges = 0
                    
                    for chunk_idx, chunk in enumerate(chunks):
                        try:
                            hyperedges = self._extract_hyperedges_with_llm(chunk)
                            logger.info(f"Extracted {len(hyperedges)} hyperedges from chunk {chunk_idx}")
                            
                            for hyperedge in hyperedges:
                                self._store_hyperedge(session, hyperedge, source_doc)
                                total_hyperedges += 1
                                
                        except Exception as e:
                            logger.error(f"Error processing chunk {chunk_idx}: {e}")
                            continue
                    
                    logger.info(f"Stored {total_hyperedges} hyperedges from document {doc_id}")
            
            logger.info(f"Successfully indexed {len(documents)} documents in hypergraph")
            return True
            
        except Exception as e:
            logger.error(f"Failed to index documents: {e}")
            return False
    
    def _is_document_processed(self, session, source_doc: str) -> bool:
        """Check if document has been processed"""
        try:
            result = session.run(
                "MATCH (he:HyperEdge {source_document: $source_doc}) RETURN COUNT(he) AS count",
                source_doc=source_doc
            )
            return result.single()["count"] > 0
        except Exception:
            return False
    
    def get_hypergraph_stats(self) -> Dict[str, Any]:
        """Get hypergraph statistics"""
        try:
            with self.driver.session() as session:
                # Count hyperedges
                result = session.run("MATCH (he:HyperEdge) RETURN COUNT(he) AS count")
                hyperedge_count = result.single()["count"]
                
                # Count entities
                result = session.run("MATCH (e:HyperEntity) RETURN COUNT(e) AS count")
                entity_count = result.single()["count"]
                
                # Average entities per hyperedge
                result = session.run("MATCH (he:HyperEdge) RETURN AVG(he.entity_count) AS avg")
                avg_entities = result.single()["avg"] or 0
                
                # Count unique documents
                result = session.run("MATCH (he:HyperEdge) RETURN COUNT(DISTINCT he.source_document) AS count")
                doc_count = result.single()["count"]
                
                return {
                    'hyperedge_count': hyperedge_count,
                    'entity_count': entity_count,
                    'avg_entities_per_hyperedge': avg_entities,
                    'unique_documents': doc_count,
                    'retrieval_method': self.retrieval_method,
                    'similarity_threshold': self.similarity_threshold,
                    'max_depth': self.max_depth,
                    'min_hyperedge_entities': self.min_hyperedge_entities
                }
        except Exception as e:
            logger.error(f"Failed to get hypergraph stats: {e}")
            return {}
    
    def get_sample_hyperedges(self, limit: int = 20) -> List[Dict[str, Any]]:
        """Get sample hyperedges"""
        try:
            with self.driver.session() as session:
                result = session.run("""
                    MATCH (e:HyperEntity)-[:MEMBER_OF]->(he:HyperEdge)
                    RETURN he.type AS type, 
                           he.description AS description,
                           collect(e.name) AS entities,
                           he.entity_count AS entity_count
                    ORDER BY he.entity_count DESC
                    LIMIT $limit
                    """, limit=limit)
                
                hyperedges = []
                for record in result:
                    hyperedges.append({
                        'type': record['type'],
                        'description': record['description'],
                        'entities': record['entities'],
                        'entity_count': record['entity_count']
                    })
                
                return hyperedges
        except Exception as e:
            logger.error(f"Failed to get sample hyperedges: {e}")
            return []
    
    def __del__(self):
        """Close Neo4j driver connection"""
        if self.driver:
            self.driver.close()


class CompleteHybrid(RetrievalComponent):

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.retrieval_methods = config.get("retrieval_methods", ["vector", "keyword"])
        self.combination_method = config.get("combination_method", "simply")
        self.normalization_method = config.get("normalization_method", "minmax")
        self.retrievers = []
        self._setup_retrievers()

    def _setup_retrievers(self):
        """Setup retrievers"""
        self.retrievers = []
        for retrieval_method in self.retrieval_methods:
            if retrieval_method == "vector":
                self.retrievers.append(SimpleVectorRAG(self.config))
            elif retrieval_method == "keyword":
                self.retrievers.append(KeywordSearchBM25(self.config))
            elif retrieval_method == "graph":
                self.retrievers.append(GraphRAG(self.config))
            elif retrieval_method == "hypergraph":
                self.retrievers.append(HyperGraphRAG(self.config))

    async def retrieve(self, query: Query, k: Optional[int] = None) -> RetrievalResult:
        """Retrieve documents using complete hybrid retrieval"""
        k = k or self.config.get("top_k", 10)
        results_with_tokens = []
        results = []
        for retriever in self.retrievers:
            r = await retriever.retrieve(query, k)
            results_with_tokens.append(r)
            results.append(HybridUtils.convert_documents_to_results(r.get("documents",[])))
        # Combine results based on the configured method
        if self.combination_method == "convex_combination":
            combined_results = self._combine_with_convex_combination(results)
        elif self.combination_method == "reciprocal_rank_fusion":
            combined_results = self._combine_with_rrf(results)
        elif self.combination_method == "borda_count":
            combined_results = self._combine_with_borda_count(results)
        elif self.combination_method == "simply":
            combined_results = HybridUtils.combine_simply(
                results_list=results,
                method_names=self.retrieval_methods,
                normalization_method=self.normalization_method
            )
        else:
            raise ValueError(f"Invalid combination method: {self.combination_method}")
        final_results = HybridUtils.convert_to_documents(combined_results)
        logger.debug(f"Final results: {final_results}")
        return RetrievalResult(
            documents=final_results,
            embedding_token_count=sum(result.get("embedding_token_count") for result in results_with_tokens),
            llm_input_token_count=sum(result.get("llm_input_token_count") for result in results_with_tokens),
            llm_output_token_count=sum(result.get("llm_output_token_count") for result in results_with_tokens)
        )
    
    async def index_documents(self, documents: List[Document]) -> bool:
        """Index documents using complete hybrid retrieval"""
        success = True
        for retriever in self.retrievers:
            success = success and await retriever.index_documents(documents)
        return success
    

    def _combine_with_convex_combination(
        self, 
        results_list: List[List[Dict[str, Any]]]
    ) -> List[Dict[str, Any]]:
        """Combine results using convex combination"""
        try:
            return HybridUtils.combine_with_convex_combination(
                results_list=results_list,
                method_names=self.retrieval_methods,
                weights=[1/len(self.retrieval_methods)] * len(self.retrieval_methods) if self.config.get("weights", None) is None else self.config.get("weights"), 
                normalization_method=self.config.get("normalization_method", "minmax"),
                )
        except Exception as e:
            logger.error(f"Convex combination failed: {e}")
            return []
    
    def _combine_with_rrf(
        self, 
        results_list: List[List[Dict[str, Any]]]
    ) -> List[Dict[str, Any]]:
        """Combine results using Reciprocal Rank Fusion"""
        try:
            return HybridUtils.combine_with_rrf(
                results_list=results_list,
                method_names=self.retrieval_methods,
            )
            
        except Exception as e:
            logger.error(f"RRF combination failed: {e}")
            return []
    
    def _combine_with_borda_count(
        self, 
        results_list: List[List[Dict[str, Any]]]
    ) -> List[Dict[str, Any]]:
        """Combine results using Borda count"""
        try:
            return HybridUtils.combine_with_borda_count(
                results_list=results_list,
                method_names=self.retrieval_methods,
            )
        except Exception as e:
            logger.error(f"Borda count combination failed: {e}")
            return []