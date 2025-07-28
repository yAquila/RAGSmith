
import logging
from typing import List, TypedDict

from rag_pipeline.core.modular_framework import (
    PassageFilterComponent, Document, Query
)

logger = logging.getLogger(__name__)

class PassageFilterResult(TypedDict):
    documents: List[Document]
    embedding_token_count: float
    llm_input_token_count: float
    llm_output_token_count: float

class SimpleThresholdFilter(PassageFilterComponent):
    """✅ CURRENTLY IMPLEMENTED - Simple top-k threshold filtering"""
    
    async def filter_passages(self, documents: List[Document], query: Query) -> PassageFilterResult:
        """Filter documents by keeping top-k by score"""
        top_k = self.config.get("top_k", 5)
        
        # Sort documents by score (descending) and take top k
        sorted_docs = sorted(documents, key=lambda d: d.score or 0.0, reverse=True)
        result = PassageFilterResult(
            documents=sorted_docs[:top_k],
                embedding_token_count=0.0,
                llm_input_token_count=0.0,  
                llm_output_token_count=0.0
            )
        return result


class SimilarityThresholdFilter(PassageFilterComponent):
    """Filter documents by similarity threshold"""
    
    async def filter_passages(self, documents: List[Document], query: Query) -> PassageFilterResult:
        """Filter documents by similarity threshold"""
        threshold = self.config.get("similarity_threshold", 0.7)
        min_passages = self.config.get("min_passages", 1)
        max_passages = self.config.get("max_passages", 10)
        
        logger.info(f"Docs have scores: {[doc.score for doc in documents]}")
        # Filter by threshold
        filtered = [doc for doc in documents if (doc.score or 0.0) >= threshold]
        
        # Ensure we have at least min_passages
        if len(filtered) < min_passages:
            sorted_docs = sorted(documents, key=lambda d: d.score or 0.0, reverse=True)
            filtered = sorted_docs[:min_passages]
        logger.info(f"Filtered passages: {len(filtered)}")
        # Ensure we don't exceed max_passages
        result = PassageFilterResult(
            documents=filtered[:max_passages],
                embedding_token_count=0.0,
                llm_input_token_count=0.0,
                llm_output_token_count=0.0
            )
        return result
