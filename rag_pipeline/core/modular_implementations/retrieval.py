import time, os, sys
import logging
from typing import List, Dict, Any, Optional, TypedDict
from abc import ABC, abstractmethod

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
                    "gen_programming_10"
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
                    "gen_programming_10"
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
