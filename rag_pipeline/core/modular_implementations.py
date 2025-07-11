"""
Concrete implementations for the Advanced RAG Modular Framework

This module contains concrete implementations of each category's techniques.
Currently implemented techniques (marked as ✅ in the original system):
- Simple VectorRAG with Semantic Score (Retrieval)
- Simple threshold (top_k) (Passage Filter) 
- Cross-Encoder Models (Passage Rerank)
- Simple Listing (Prompt Maker)
- LLM model (Generator)
"""

import time
import logging
from typing import List, Dict, Any, Optional, Union
from abc import ABC, abstractmethod

from .modular_framework import (
    PreEmbeddingComponent, QueryExpansionComponent, RetrievalComponent,
    PassageAugmentComponent, PassageRerankComponent, PassageFilterComponent,
    PassageCompressComponent, PromptMakerComponent, GeneratorComponent,
    PostGenerationComponent, Document, Query, Context
)

logger = logging.getLogger(__name__)


# ==================== PRE-EMBEDDING IMPLEMENTATIONS ====================

class NonePreEmbedding(PreEmbeddingComponent):
    """No pre-embedding processing - pass documents through unchanged"""
    
    async def process_documents(self, documents: List[Document]) -> List[Document]:
        """Pass documents through unchanged"""
        return documents


class ContextualChunkHeaders(PreEmbeddingComponent):
    """Add contextual headers to document chunks"""
    
    async def process_documents(self, documents: List[Document]) -> List[Document]:
        """Add contextual headers to documents"""
        processed = []
        for doc in documents:
            if self.config.get("add_headers", False):
                template = self.config.get("header_template", "Document: {title}\n\n{content}")
                title = doc.metadata.get("title", f"Document {doc.doc_id}") if doc.metadata else f"Document {doc.doc_id}"
                
                new_content = template.format(title=title, content=doc.content)
                processed_doc = Document(
                    doc_id=doc.doc_id,
                    content=new_content,
                    metadata=doc.metadata,
                    score=doc.score
                )
                processed.append(processed_doc)
            else:
                processed.append(doc)
        return processed


# ==================== QUERY EXPANSION IMPLEMENTATIONS ====================

class NoneQueryExpansion(QueryExpansionComponent):
    """No query expansion - return original query"""
    
    async def expand_query(self, query: str) -> Query:
        """Return original query unchanged"""
        return Query(
            original_text=query,
            processed_text=query,
            expanded_queries=None,
            metadata={}
        )


class SimpleMultiQuery(QueryExpansionComponent):
    """Generate multiple variations of the query"""
    
    async def expand_query(self, query: str) -> Query:
        """Generate multiple query variations"""
        # For now, just create simple variations
        # In a full implementation, this would use an LLM
        expanded_queries = [
            query,
            f"What is {query}?",
            f"Tell me about {query}",
            f"Explain {query}"
        ][:self.config.get("num_expanded_queries", 3)]
        
        return Query(
            original_text=query,
            processed_text=query,
            expanded_queries=expanded_queries,
            metadata={"technique": "simple_multi_query"}
        )


# ==================== RETRIEVAL IMPLEMENTATIONS ====================

class SimpleVectorRAG(RetrievalComponent):
    """✅ CURRENTLY IMPLEMENTED - Simple vector-based retrieval with semantic scoring"""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.vectorstore = None
        self._setup_vectorstore()
    
    def _setup_vectorstore(self):
        """Setup the vector store"""
        try:
            from ..util.vectorstore.qdrant_store import QdrantVectorStore
            from ..util.vectorstore.dataset_utils import generate_dataset_hash_from_file
            import os
            
            # Use embedding model from config
            embedding_model = self.config.get("embedding_model", "sentence-transformers/all-mpnet-base-v2")
            
            # Use dataset path from config or default
            dataset_path = self.config.get("dataset_path")
            if not dataset_path:
                dataset_path = os.path.join(
                    os.path.dirname(os.path.dirname(__file__)), 
                    "default_datasets", 
                    "retrieval_docs.csv"
                )
            
            dataset_hash = generate_dataset_hash_from_file(dataset_path)
            self.vectorstore = QdrantVectorStore(embedding_model, dataset_hash)
            
        except Exception as e:
            logger.error(f"Failed to setup vectorstore: {e}")
            raise
    
    async def retrieve(self, query: Query, k: Optional[int] = None) -> List[Document]:
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
            
            return documents
            
        except Exception as e:
            logger.error(f"Retrieval failed: {e}")
            return []
    
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
    
    async def retrieve(self, query: Query, k: Optional[int] = None) -> List[Document]:
        """Retrieve documents using BM25 keyword search"""
        # Placeholder implementation
        # In a full implementation, this would use libraries like rank_bm25
        logger.warning("KeywordSearchBM25 not fully implemented yet")
        return []
    
    async def index_documents(self, documents: List[Document]) -> bool:
        """Index documents for BM25 search"""
        # Placeholder implementation
        logger.warning("KeywordSearchBM25 indexing not fully implemented yet")
        return False


# ==================== PASSAGE AUGMENT IMPLEMENTATIONS ====================

class NonePassageAugment(PassageAugmentComponent):
    """No passage augmentation - pass documents through unchanged"""
    
    async def augment_passages(self, documents: List[Document], query: Query) -> List[Document]:
        """Pass documents through unchanged"""
        return documents


class PrevNextAugmenter(PassageAugmentComponent):
    """Augment passages with previous and next chunks"""
    
    async def augment_passages(self, documents: List[Document], query: Query) -> List[Document]:
        """Augment passages with surrounding context"""
        # Placeholder implementation
        # In a full implementation, this would fetch neighboring chunks
        logger.warning("PrevNextAugmenter not fully implemented yet")
        return documents


# ==================== PASSAGE RERANK IMPLEMENTATIONS ====================

class NonePassageRerank(PassageRerankComponent):
    """No reranking - pass documents through unchanged"""
    
    async def rerank_passages(self, documents: List[Document], query: Query) -> List[Document]:
        """Pass documents through unchanged"""
        return documents


class CrossEncoderRerank(PassageRerankComponent):
    """✅ CURRENTLY IMPLEMENTED - Cross-encoder based reranking"""
    
    async def rerank_passages(self, documents: List[Document], query: Query) -> List[Document]:
        """Rerank documents using cross-encoder model"""
        try:
            from ..util.rerank.reranker import get_reranker
            
            # Get reranker configuration
            model_name = self.config.get("cross_encoder_model", "BAAI/bge-reranker-v2-m3")
            top_k = self.config.get("cross_encoder_top_k", 5)
            cache_dir = self.config.get("cross_encoder_cache_dir")
            force_cpu = self.config.get("cross_encoder_force_cpu", False)
            
            # Initialize reranker
            reranker = get_reranker(model_name, cache_dir=cache_dir, force_cpu=force_cpu)
            
            # Convert documents to format expected by existing reranker
            docs_for_rerank = []
            for doc in documents:
                docs_for_rerank.append({
                    "doc_id": doc.doc_id,
                    "content": doc.content,
                    "score": doc.score or 0.0,
                    "metadata": doc.metadata or {}
                })
            
            # Perform reranking
            reranked_docs = reranker.rerank_documents(query.processed_text, docs_for_rerank, top_k=top_k)
            
            # Convert back to Document objects
            result_documents = []
            for doc_data in reranked_docs:
                doc = Document(
                    doc_id=doc_data.get("doc_id", ""),
                    content=doc_data.get("content", ""),
                    score=doc_data.get("score", 0.0),
                    metadata=doc_data.get("metadata", {})
                )
                result_documents.append(doc)
            
            return result_documents
            
        except Exception as e:
            logger.error(f"Cross-encoder reranking failed: {e}")
            return documents


class LLMRerank(PassageRerankComponent):
    """✅ CURRENTLY IMPLEMENTED - LLM-based reranking"""
    
    async def rerank_passages(self, documents: List[Document], query: Query) -> List[Document]:
        """Rerank documents using LLM"""
        try:
            from ..util.rerank.llm_reranker import get_llm_reranker
            
            # Get LLM reranker configuration
            model_name = self.config.get("llm_rerank_model", "gpt-3.5-turbo")
            top_k = self.config.get("llm_rerank_top_k", 5)
            max_tokens = self.config.get("llm_rerank_max_tokens", 2048)
            temperature = self.config.get("llm_rerank_temperature", 0.1)
            
            # Initialize LLM reranker
            llm_reranker = get_llm_reranker(
                model_name=model_name,
                max_tokens=max_tokens,
                temperature=temperature
            )
            
            # Convert documents to format expected by existing reranker
            docs_for_rerank = []
            for doc in documents:
                docs_for_rerank.append({
                    "doc_id": doc.doc_id,
                    "content": doc.content,
                    "score": doc.score or 0.0,
                    "metadata": doc.metadata or {}
                })
            
            # Perform reranking
            reranked_docs = llm_reranker.rerank_documents(query.processed_text, docs_for_rerank, top_k=top_k)
            
            # Convert back to Document objects
            result_documents = []
            for doc_data in reranked_docs:
                doc = Document(
                    doc_id=doc_data.get("doc_id", ""),
                    content=doc_data.get("content", ""),
                    score=doc_data.get("score", 0.0),
                    metadata=doc_data.get("metadata", {})
                )
                result_documents.append(doc)
            
            return result_documents
            
        except Exception as e:
            logger.error(f"LLM reranking failed: {e}")
            return documents


# ==================== PASSAGE FILTER IMPLEMENTATIONS ====================

class SimpleThresholdFilter(PassageFilterComponent):
    """✅ CURRENTLY IMPLEMENTED - Simple top-k threshold filtering"""
    
    async def filter_passages(self, documents: List[Document], query: Query) -> List[Document]:
        """Filter documents by keeping top-k by score"""
        top_k = self.config.get("top_k", 5)
        
        # Sort documents by score (descending) and take top k
        sorted_docs = sorted(documents, key=lambda d: d.score or 0.0, reverse=True)
        return sorted_docs[:top_k]


class SimilarityThresholdFilter(PassageFilterComponent):
    """Filter documents by similarity threshold"""
    
    async def filter_passages(self, documents: List[Document], query: Query) -> List[Document]:
        """Filter documents by similarity threshold"""
        threshold = self.config.get("similarity_threshold", 0.7)
        min_passages = self.config.get("min_passages", 1)
        max_passages = self.config.get("max_passages", 10)
        
        # Filter by threshold
        filtered = [doc for doc in documents if (doc.score or 0.0) >= threshold]
        
        # Ensure we have at least min_passages
        if len(filtered) < min_passages:
            sorted_docs = sorted(documents, key=lambda d: d.score or 0.0, reverse=True)
            filtered = sorted_docs[:min_passages]
        
        # Ensure we don't exceed max_passages
        return filtered[:max_passages]


# ==================== PASSAGE COMPRESS IMPLEMENTATIONS ====================

class NonePassageCompress(PassageCompressComponent):
    """No passage compression - pass documents through unchanged"""
    
    async def compress_passages(self, documents: List[Document], query: Query) -> List[Document]:
        """Pass documents through unchanged"""
        return documents


class TreeSummarize(PassageCompressComponent):
    """Compress passages using tree summarization"""
    
    async def compress_passages(self, documents: List[Document], query: Query) -> List[Document]:
        """Compress documents using tree summarization"""
        # Placeholder implementation
        logger.warning("TreeSummarize not fully implemented yet")
        return documents


# ==================== PROMPT MAKER IMPLEMENTATIONS ====================

class SimpleListingPromptMaker(PromptMakerComponent):
    """✅ CURRENTLY IMPLEMENTED - Simple listing of documents in prompt"""
    
    async def make_prompt(self, query: Query, documents: List[Document]) -> str:
        """Create a simple prompt by listing documents"""
        template = self.config.get("template", "Context:\n{context}\n\nQuestion: {query}\n\nAnswer:")
        separator = self.config.get("separator", "\n\n")
        include_doc_numbers = self.config.get("include_doc_numbers", True)
        include_scores = self.config.get("include_scores", False)
        
        # Format context from documents
        context_parts = []
        for i, doc in enumerate(documents, 1):
            content = doc.content.strip()
            if content:
                if include_doc_numbers:
                    if include_scores:
                        context_parts.append(f"Document {i} (Score: {doc.score:.3f}):\n{content}")
                    else:
                        context_parts.append(f"Document {i}:\n{content}")
                else:
                    context_parts.append(content)
        
        context = separator.join(context_parts)
        
        # Format final prompt
        prompt = template.format(context=context, query=query.processed_text)
        return prompt


class MultiLLMEnsemblePromptMaker(PromptMakerComponent):
    """Create multiple prompts for ensemble generation"""
    
    async def make_prompt(self, query: Query, documents: List[Document]) -> str:
        """Create ensemble prompts"""
        # Placeholder implementation
        logger.warning("MultiLLMEnsemblePromptMaker not fully implemented yet")
        return await SimpleListingPromptMaker(self.config).make_prompt(query, documents)


# ==================== GENERATOR IMPLEMENTATIONS ====================

class LLMGenerator(GeneratorComponent):
    """✅ CURRENTLY IMPLEMENTED - LLM-based generation (Ollama/Gemini)"""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.client = None
        self._setup_client()
    
    def _setup_client(self):
        """Setup the appropriate LLM client"""
        provider = self.config.get("provider", "ollama")
        
        try:
            if provider.lower() == "ollama":
                from ..util.api.ollama_client import OllamaUtil
                self.client = OllamaUtil
            elif provider.lower() == "gemini":
                from ..util.api.gemini_client import GeminiUtil
                self.client = GeminiUtil
            else:
                raise ValueError(f"Unsupported provider: {provider}")
                
        except Exception as e:
            logger.error(f"Failed to setup {provider} client: {e}")
            raise
    
    async def generate(self, prompt: str, query: Query) -> str:
        """Generate answer using LLM"""
        try:
            model = self.config.get("model", "gpt-3.5-turbo")
            
            # Call the appropriate client
            if self.config.get("provider", "ollama").lower() == "ollama":
                response = self.client.get_ollama_response(model, prompt)
            else:  # gemini
                response = self.client.get_gemini_response(model, prompt)
            
            # Extract response text
            if isinstance(response, dict):
                return response.get('response', '')
            else:
                return str(response)
                
        except Exception as e:
            logger.error(f"Generation failed: {e}")
            return ""


# ==================== POST-GENERATION IMPLEMENTATIONS ====================

class NonePostGeneration(PostGenerationComponent):
    """No post-generation processing - return answer unchanged"""
    
    async def post_process(self, generated_answer: str, query: Query, context: Context) -> str:
        """Return answer unchanged"""
        return generated_answer


class ReflectionRevising(PostGenerationComponent):
    """Refine answer using reflection and revising"""
    
    async def post_process(self, generated_answer: str, query: Query, context: Context) -> str:
        """Post-process answer using reflection"""
        # Placeholder implementation
        logger.warning("ReflectionRevising not fully implemented yet")
        return generated_answer


# ==================== COMPONENT REGISTRY ====================

# Registry for easy component lookup
COMPONENT_REGISTRY = {
    "pre_embedding": {
        "none": NonePreEmbedding,
        "contextual_chunk_headers": ContextualChunkHeaders,
    },
    "query_expansion": {
        "none": NoneQueryExpansion,
        "multi_query": SimpleMultiQuery,
    },
    "retrieval": {
        "simple_vector_rag": SimpleVectorRAG,
        "keyword_search": KeywordSearchBM25,
    },
    "passage_augment": {
        "none": NonePassageAugment,
        "prev_next_augmenter": PrevNextAugmenter,
    },
    "passage_rerank": {
        "none": NonePassageRerank,
        "cross_encoder": CrossEncoderRerank,
        "llm_rerank": LLMRerank,
    },
    "passage_filter": {
        "simple_threshold": SimpleThresholdFilter,
        "similarity_threshold": SimilarityThresholdFilter,
    },
    "passage_compress": {
        "none": NonePassageCompress,
        "tree_summarize": TreeSummarize,
    },
    "prompt_maker": {
        "simple_listing": SimpleListingPromptMaker,
        "multi_llm_ensemble": MultiLLMEnsemblePromptMaker,
    },
    "generator": {
        "llm": LLMGenerator,
    },
    "post_generation": {
        "none": NonePostGeneration,
        "reflection_revising": ReflectionRevising,
    },
} 