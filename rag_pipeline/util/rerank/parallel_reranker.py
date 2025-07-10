"""
Parallel reranking utilities that combine cross-encoder and LLM reranking
"""

import logging
import time
from typing import List, Dict, Any, Optional, Tuple
from .reranker import get_reranker
from .llm_reranker import get_llm_reranker

logger = logging.getLogger(__name__)

class ParallelRerankerUtil:
    """Utility class for parallel reranking using both cross-encoder and LLM methods"""
    
    def __init__(self, 
                 ce_model: str = 'BAAI/bge-reranker-v2-m3',
                 llm_model: str = 'llama3.2:1b',
                 ensemble_method: str = "weighted",
                 ce_weight: float = 0.7,
                 llm_weight: float = 0.3,
                 ce_cache_dir: Optional[str] = None,
                 ce_force_cpu: bool = False,
                 llm_max_tokens: int = 2048,
                 llm_temperature: float = 0.1):
        """
        Initialize the parallel reranker
        
        Args:
            ce_model: Cross-encoder model name
            llm_model: LLM model name for reranking
            ensemble_method: Method to combine scores ("weighted", "average", "max")
            ce_weight: Weight for cross-encoder scores
            llm_weight: Weight for LLM scores
            ce_cache_dir: Cache directory for cross-encoder models
            ce_force_cpu: Force CPU usage for cross-encoder
            llm_max_tokens: Max tokens for LLM
            llm_temperature: Temperature for LLM
        """
        self.ce_model = ce_model
        self.llm_model = llm_model
        self.ensemble_method = ensemble_method
        self.ce_weight = ce_weight
        self.llm_weight = llm_weight
        
        # Initialize rerankers
        self.ce_reranker = get_reranker(ce_model, cache_dir=ce_cache_dir, force_cpu=ce_force_cpu)
        self.llm_reranker = get_llm_reranker(llm_model, max_tokens=llm_max_tokens, temperature=llm_temperature)
    
    def _normalize_scores(self, documents: List[Dict[str, Any]], score_field: str) -> List[Dict[str, Any]]:
        """Normalize scores to 0-1 range"""
        scores = [doc.get(score_field, 0.0) for doc in documents]
        if not scores or max(scores) == min(scores):
            return documents
        
        min_score = min(scores)
        max_score = max(scores)
        score_range = max_score - min_score
        
        normalized_docs = []
        for doc in documents:
            normalized_doc = doc.copy()
            original_score = doc.get(score_field, 0.0)
            normalized_score = (original_score - min_score) / score_range
            normalized_doc[f"normalized_{score_field}"] = normalized_score
            normalized_docs.append(normalized_doc)
        
        return normalized_docs
    
    def _ensemble_scores(self, documents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Combine cross-encoder and LLM scores using the specified ensemble method"""
        if self.ensemble_method == "weighted":
            for doc in documents:
                ce_score = doc.get('normalized_rerank_score', 0.0)
                llm_score = doc.get('normalized_llm_rerank_score', 0.0)
                ensemble_score = (self.ce_weight * ce_score) + (self.llm_weight * llm_score)
                doc['ensemble_score'] = ensemble_score
        
        elif self.ensemble_method == "average":
            for doc in documents:
                ce_score = doc.get('normalized_rerank_score', 0.0)
                llm_score = doc.get('normalized_llm_rerank_score', 0.0)
                ensemble_score = (ce_score + llm_score) / 2.0
                doc['ensemble_score'] = ensemble_score
        
        elif self.ensemble_method == "max":
            for doc in documents:
                ce_score = doc.get('normalized_rerank_score', 0.0)
                llm_score = doc.get('normalized_llm_rerank_score', 0.0)
                ensemble_score = max(ce_score, llm_score)
                doc['ensemble_score'] = ensemble_score
        
        else:
            raise ValueError(f"Unknown ensemble method: {self.ensemble_method}")
        
        return documents
    
    def rerank_documents(self, 
                        query: str, 
                        documents: List[Dict[str, Any]], 
                        top_k: Optional[int] = None) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
        """
        Apply parallel reranking using both cross-encoder and LLM methods
        
        Args:
            query: The search query
            documents: List of documents to rerank
            top_k: Number of top documents to return
            
        Returns:
            Tuple of (reranked_documents, timing_info)
        """
        if not documents:
            return documents, {}
        
        if len(documents) == 1:
            # Single document, just add ensemble score
            doc = documents[0].copy()
            doc['ensemble_score'] = 1.0
            doc['rerank_score'] = 1.0
            doc['llm_rerank_score'] = 1.0
            return [doc], {"ce_time": 0.0, "llm_time": 0.0, "ensemble_time": 0.0}
        
        logger.info(f"Parallel reranking {len(documents)} documents with CE({self.ce_model}) + LLM({self.llm_model})")
        
        # Apply cross-encoder reranking
        ce_start = time.time()
        ce_reranked = self.ce_reranker.rerank_documents(query, documents, top_k=None)  # Get all for ensembling
        ce_time = time.time() - ce_start
        
        # Apply LLM reranking (to original documents, not CE results)
        llm_start = time.time()
        llm_reranked = self.llm_reranker.rerank_documents(query, documents, top_k=None)  # Get all for ensembling
        llm_time = time.time() - llm_start
        
        # Merge scores back to original documents
        ensemble_start = time.time()
        
        # Create mapping for CE scores
        ce_scores = {doc.get('doc_id'): doc.get('rerank_score', 0.0) for doc in ce_reranked}
        
        # Create mapping for LLM scores
        llm_scores = {doc.get('doc_id'): doc.get('llm_rerank_score', 0.0) for doc in llm_reranked}
        
        # Merge scores into original documents
        merged_docs = []
        for doc in documents:
            merged_doc = doc.copy()
            doc_id = doc.get('doc_id')
            merged_doc['rerank_score'] = ce_scores.get(doc_id, 0.0)
            merged_doc['llm_rerank_score'] = llm_scores.get(doc_id, 0.0)
            merged_docs.append(merged_doc)
        
        # Normalize scores
        merged_docs = self._normalize_scores(merged_docs, 'rerank_score')
        merged_docs = self._normalize_scores(merged_docs, 'llm_rerank_score')
        
        # Ensemble scores
        merged_docs = self._ensemble_scores(merged_docs)
        
        # Sort by ensemble score
        merged_docs.sort(key=lambda x: x.get('ensemble_score', 0.0), reverse=True)
        
        # Apply top_k filtering
        if top_k is not None:
            merged_docs = merged_docs[:top_k]
        
        ensemble_time = time.time() - ensemble_start
        
        timing_info = {
            "ce_time": ce_time,
            "llm_time": llm_time, 
            "ensemble_time": ensemble_time,
            "total_time": ce_time + llm_time + ensemble_time
        }
        
        logger.info(f"Parallel reranking completed: CE={ce_time:.3f}s, LLM={llm_time:.3f}s, Ensemble={ensemble_time:.3f}s")
        
        return merged_docs, timing_info


# Global instance for efficient reranker reuse
_parallel_reranker_instance = None

def get_parallel_reranker(**kwargs) -> ParallelRerankerUtil:
    """Get a singleton parallel reranker instance"""
    global _parallel_reranker_instance
    
    # For simplicity, always create new instance (can be optimized later)
    logger.info("Creating parallel reranker instance")
    _parallel_reranker_instance = ParallelRerankerUtil(**kwargs)
    return _parallel_reranker_instance
