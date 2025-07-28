import logging
from typing import List, TypedDict

from rag_pipeline.core.modular_framework import (
    PreEmbeddingComponent, Document
)

logger = logging.getLogger(__name__)

class PreEmbeddingResult(TypedDict):
    documents_to_embed: List[Document]
    documents_for_metadata: List[Document]
    embedding_token_count: float
    llm_input_token_count: float
    llm_output_token_count: float

class NonePreEmbedding(PreEmbeddingComponent):
    """No pre-embedding processing - pass documents through unchanged"""
    
    async def process_documents(self, documents: List[Document]) -> PreEmbeddingResult:
        """Pass documents through unchanged"""
        result = PreEmbeddingResult(
            documents_to_embed=documents,
            documents_for_metadata=[],
            embedding_token_count=0.0,
            llm_input_token_count=0.0,
            llm_output_token_count=0.0
        )
        return result


class ContextualChunkHeaders(PreEmbeddingComponent):
    """Add contextual headers to document chunks"""
    
    async def process_documents(self, documents: List[Document]) -> PreEmbeddingResult:
        """Add contextual headers to documents"""
        logger.warning("ContextualChunkHeaders not fully implemented yet")
        result = PreEmbeddingResult(
            documents_to_embed=documents,
            documents_for_metadata=[],
            embedding_token_count=0.0,
            llm_input_token_count=0.0,
            llm_output_token_count=0.0
        )
        return result
