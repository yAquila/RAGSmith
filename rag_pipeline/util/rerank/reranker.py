"""
Reranking utilities for RAG pipeline using cross-encoder models
"""

import os
import torch
import logging
from typing import List, Dict, Optional, Any
from sentence_transformers import CrossEncoder

logger = logging.getLogger(__name__)

class RerankerUtil:
    """Utility class for reranking documents using cross-encoder models"""
    
    def __init__(self, model_name: str = 'BAAI/bge-reranker-v2-m3', max_length: int = 2048, cache_dir: Optional[str] = None, force_cpu: bool = False):
        """
        Initialize the reranker
        
        Args:
            model_name: Name of the cross-encoder model to use
            max_length: Maximum sequence length for the model
            cache_dir: Directory to cache downloaded models (if None, uses default)
            force_cpu: If True, force CPU usage instead of GPU
        """
        self.model_name = model_name
        self.max_length = max_length
        self.force_cpu = force_cpu
        
        # Set up model caching directory
        if cache_dir is None:
            cache_dir = os.path.join(os.path.expanduser("~"), ".cache", "rag_pipeline", "reranker_models")
        self.cache_dir = cache_dir
        os.makedirs(self.cache_dir, exist_ok=True)
        
        # Detect and set device
        self.device = self._get_best_device()
        
        # Model will be loaded lazily
        self.model = None
        
    def _get_best_device(self) -> str:
        """Detect the best available device"""
        if torch.cuda.is_available() and not self.force_cpu:
            device = "cuda"
            gpu_name = torch.cuda.get_device_name(0)
            logger.info(f"GPU detected: {gpu_name}. Will use CUDA for reranking.")
        elif hasattr(torch.backends, 'mps') and torch.backends.mps.is_available() and not self.force_cpu:
            device = "mps"
            logger.info("Apple MPS detected. Will use MPS for reranking.")
        else:
            device = "cpu"
            logger.info("No GPU detected or force_cpu is True. Will use CPU for reranking.")
        return device
    
    def _load_model(self):
        """Load the cross-encoder model with caching"""
        if self.model is not None:
            return  # Model already loaded
            
        try:
            logger.info(f"Loading reranker model: {self.model_name} on {self.device}")
            logger.info(f"Model cache directory: {self.cache_dir}")
            
            # Check if model is already cached
            model_cache_path = os.path.join(self.cache_dir, self.model_name.replace("/", "_"))
            
            if os.path.exists(model_cache_path):
                logger.info(f"Loading cached model from: {model_cache_path}")
                # Load from local cache
                self.model = CrossEncoder(
                    model_cache_path,
                    max_length=self.max_length,
                    device=self.device
                )
            else:
                logger.info(f"Downloading and caching model: {self.model_name}")
                # Download and save to cache
                self.model = CrossEncoder(
                    self.model_name,
                    max_length=self.max_length,
                    device=self.device
                )
                # Save to cache for future use
                self.model.save(model_cache_path)
                logger.info(f"Model cached to: {model_cache_path}")
                
            # Log device info
            actual_device = next(self.model.model.parameters()).device
            logger.info(f"Reranker model loaded successfully on device: {actual_device}")
            
        except Exception as e:
            logger.error(f"Failed to load reranker model: {e}")
            raise
    
    def rerank_documents(
        self, 
        query: str, 
        documents: List[Dict[str, Any]], 
        top_k: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Rerank documents based on query relevance
        
        Args:
            query: The search query
            documents: List of documents with 'content' field
            top_k: Number of top documents to return (if None, return all)
            
        Returns:
            List of reranked documents with added 'rerank_score' field
        """
        if not documents:
            return documents
        
        # Load model if not already loaded
        if self.model is None:
            self._load_model()
        
        try:
            # Extract document contents for reranking
            doc_contents = [doc.get('content', '') for doc in documents]
            
            # Create query-document pairs
            sentence_pairs = [[query, content] for content in doc_contents]
            
            logger.info(f"Reranking {len(documents)} documents with {self.model_name} on {self.device}")
            
            # Compute relevance scores
            scores = self.model.predict(
                sentence_pairs, 
                convert_to_tensor=True, 
                show_progress_bar=False  # Set to False to reduce noise in logs
            )
            
            # Add scores to documents
            reranked_docs = []
            for i, doc in enumerate(documents):
                reranked_doc = doc.copy()
                reranked_doc['rerank_score'] = float(scores[i].item())
                reranked_docs.append(reranked_doc)
            
            # Sort by rerank score in descending order
            reranked_docs.sort(key=lambda x: x['rerank_score'], reverse=True)
            
            # Apply top_k filtering if specified
            if top_k is not None:
                reranked_docs = reranked_docs[:top_k]
            
            logger.info(f"Reranking completed. Top document score: {reranked_docs[0]['rerank_score']:.4f}")
            return reranked_docs
            
        except Exception as e:
            logger.error(f"Reranking failed: {e}")
            # Return original documents if reranking fails
            return documents

# Global instance for efficient model reuse across the entire pipeline
_reranker_instance = None

def get_reranker(model_name: str = 'BAAI/bge-reranker-v2-m3', cache_dir: Optional[str] = None, force_cpu: bool = False) -> RerankerUtil:
    """Get a singleton reranker instance for efficient model reuse"""
    global _reranker_instance
    
    # Check if we need to create a new instance
    need_new_instance = (
        _reranker_instance is None or 
        _reranker_instance.model_name != model_name or
        _reranker_instance.cache_dir != (cache_dir or os.path.join(os.path.expanduser("~"), ".cache", "rag_pipeline", "reranker_models")) or
        _reranker_instance.force_cpu != force_cpu
    )
    
    if need_new_instance:
        logger.info(f"Creating new reranker instance for model: {model_name}")
        _reranker_instance = RerankerUtil(model_name, cache_dir=cache_dir, force_cpu=force_cpu)
    else:
        logger.debug(f"Reusing existing reranker instance for model: {model_name}")
    
    return _reranker_instance 