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
from typing import List, Dict, Any, Optional, Union, TypedDict
from abc import ABC, abstractmethod

from .modular_framework import (
    PreEmbeddingComponent, QueryExpansionComponent, RetrievalComponent,
    PassageAugmentComponent, PassageRerankComponent, PassageFilterComponent,
    PassageCompressComponent, PromptMakerComponent, GeneratorComponent,
    PostGenerationComponent, Document, Query, Context
)

logger = logging.getLogger(__name__)


# ==================== PRE-EMBEDDING IMPLEMENTATIONS ====================

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


# ==================== QUERY EXPANSION IMPLEMENTATIONS ====================

class QueryExpansionResult(TypedDict):
    query: Query
    embedding_token_count: float
    llm_input_token_count: float
    llm_output_token_count: float

class NoneQueryExpansion(QueryExpansionComponent):
    """No query expansion - return original query"""
    
    async def expand_query(self, query: str) -> QueryExpansionResult:
        """Return original query unchanged"""
        result = QueryExpansionResult(
            query=Query(
                original_text=query,
                processed_text=query,
                expanded_queries=None,
                metadata={}
            ),
            embedding_token_count=0.0,
            llm_input_token_count=0.0,
            llm_output_token_count=0.0
        )
        return result


class SimpleMultiQuery(QueryExpansionComponent):
    """Generate multiple variations of the query"""
    
    async def expand_query(self, query: str) -> QueryExpansionResult:
        """Generate multiple query variations"""
        # For now, just create simple variations
        # In a full implementation, this would use an LLM
        expanded_queries = [
            query,
            f"What is {query}?",
            f"Tell me about {query}",
            f"Explain {query}"
        ][:self.config.get("num_expanded_queries", 3)]
        
        result = QueryExpansionResult(
            query=Query(
                original_text=query,
                processed_text=query,
                expanded_queries=expanded_queries,
                metadata={"technique": "simple_multi_query"}
            ),
            embedding_token_count=0.0,
            llm_input_token_count=0.0,
            llm_output_token_count=0.0
        )
        return result


# ==================== RETRIEVAL IMPLEMENTATIONS ====================

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
            from util.vectorstore.qdrant_store import QdrantVectorStore
            from util.vectorstore.dataset_utils import generate_dataset_hash_from_file
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
    
    async def retrieve(self, query: Query, k: Optional[int] = None) -> RetrievalResult:
        """Retrieve documents using BM25 keyword search"""
        # Placeholder implementation
        # In a full implementation, this would use libraries like rank_bm25
        logger.warning("KeywordSearchBM25 not fully implemented yet")
        result = RetrievalResult(
            documents=[],
            embedding_token_count=0.0,
            llm_input_token_count=0.0,
            llm_output_token_count=0.0
        )
        return result
    
    async def index_documents(self, documents: List[Document]) -> bool:
        """Index documents for BM25 search"""
        # Placeholder implementation
        logger.warning("KeywordSearchBM25 indexing not fully implemented yet")
        return False


# ==================== PASSAGE AUGMENT IMPLEMENTATIONS ====================

class PassageAugmentResult(TypedDict):
    documents: List[Document]
    embedding_token_count: float
    llm_input_token_count: float
    llm_output_token_count: float

class NonePassageAugment(PassageAugmentComponent):
    """No passage augmentation - pass documents through unchanged"""
    
    async def augment_passages(self, documents: List[Document], query: Query) -> PassageAugmentResult:
        """Pass documents through unchanged"""
        result = PassageAugmentResult(
            documents=documents,
            embedding_token_count=0.0,
            llm_input_token_count=0.0,
            llm_output_token_count=0.0
        )
        return result


class PrevNextAugmenter(PassageAugmentComponent):
    """Augment passages with previous and next chunks"""
    
    async def augment_passages(self, documents: List[Document], query: Query) -> PassageAugmentResult:
        """Augment passages with surrounding context"""
        # Placeholder implementation
        logger.warning("PrevNextAugmenter not fully implemented yet")
        result = PassageAugmentResult(
            documents=documents,
            embedding_token_count=0.0,
            llm_input_token_count=0.0,
            llm_output_token_count=0.0
        )
        return result


# ==================== PASSAGE RERANK IMPLEMENTATIONS ====================

class PassageRerankResult(TypedDict):
    documents: List[Document]
    embedding_token_count: float
    llm_input_token_count: float
    llm_output_token_count: float

class NonePassageRerank(PassageRerankComponent):
    """No reranking - pass documents through unchanged"""
    
    async def rerank_passages(self, documents: List[Document], query: Query) -> PassageRerankResult:
        """Pass documents through unchanged"""
        result = PassageRerankResult(
            documents=documents,
            embedding_token_count=0.0,
            llm_input_token_count=0.0,
            llm_output_token_count=0.0
        )
        return result


class CrossEncoderRerank(PassageRerankComponent):
    """✅ CURRENTLY IMPLEMENTED - Cross-encoder based reranking"""
    
    async def rerank_passages(self, documents: List[Document], query: Query) -> PassageRerankResult:
        """Rerank documents using cross-encoder model"""
        try:
            from util.rerank.reranker import get_reranker
            
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
            
            # Embedding token count: sum of tokens in all input docs
            embedding_token_count = sum(len(doc["content"].split()) for doc in docs_for_rerank)
            result = PassageRerankResult(
                documents=[Document(
                doc_id=doc_data.get("doc_id", ""),
                content=doc_data.get("content", ""),
                score=doc_data.get("score", 0.0),
                metadata=doc_data.get("metadata", {})
                ) for doc_data in reranked_docs],
                embedding_token_count=float(embedding_token_count),
                llm_input_token_count=0.0,
                llm_output_token_count=0.0
            )
            return result
            
        except Exception as e:
            logger.error(f"Cross-encoder reranking failed: {e}")
            result = PassageRerankResult(
                documents=documents,
                embedding_token_count=0.0,
                llm_input_token_count=0.0,
                llm_output_token_count=0.0
            )
            return result


class LLMRerank(PassageRerankComponent):    
    """✅ CURRENTLY IMPLEMENTED - LLM-based reranking"""
    
    async def rerank_passages(self, documents: List[Document], query: Query) -> PassageRerankResult:
        """Rerank documents using LLM"""
        try:
            from util.rerank.llm_reranker import get_llm_reranker
            
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
            llm_input_token_count = len(query.processed_text.split()) + sum(len(doc["content"].split()) for doc in docs_for_rerank)
            llm_output_token_count = len(str(reranked_docs).split())
            result = PassageRerankResult(
                documents=[Document(
                doc_id=doc_data.get("doc_id", ""),
                content=doc_data.get("content", ""),
                score=doc_data.get("score", 0.0),
                metadata=doc_data.get("metadata", {})
                ) for doc_data in reranked_docs],
                embedding_token_count=0.0,
                llm_input_token_count=llm_input_token_count,
                llm_output_token_count=llm_output_token_count
            )
            return result
            
        except Exception as e:
            logger.error(f"LLM reranking failed: {e}")
            result = PassageRerankResult(
                documents=documents,
                embedding_token_count=0.0,
                llm_input_token_count=0.0,
                llm_output_token_count=0.0
            )
            return result

class CELLM_ParallelRerank(PassageRerankComponent):
    """✅ CURRENTLY IMPLEMENTED - CELLM-based parallel reranking"""
    
    async def rerank_passages(self, documents: List[Document], query: Query) -> PassageRerankResult:
        """Rerank documents using CELLM-based parallel reranking"""
        try:
            from util.rerank.parallel_reranker import get_parallel_reranker
            
            # Get reranker configuration
            ce_model = self.config.get("ce_model", "BAAI/bge-reranker-v2-m3")
            llm_model = self.config.get("llm_model", "gemma3:4b")
            ensemble_method = self.config.get("parallel_ensemble_method", "weighted")
            ce_weight = self.config.get("ce_weight", 0.7)
            llm_weight = self.config.get("llm_weight", 0.3)
            top_k = self.config.get("top_k", 5)
            ce_cache_dir = self.config.get("cross_encoder_cache_dir")
            ce_force_cpu = self.config.get("cross_encoder_force_cpu", False)
            llm_max_tokens = self.config.get("llm_max_tokens", 2048)
            llm_temperature = self.config.get("llm_temperature", 0.1)

            # Initialize parallel reranker
            reranker = get_parallel_reranker(
                ce_model=ce_model,
                llm_model=llm_model,
                ensemble_method=ensemble_method,
                ce_weight=ce_weight,
                llm_weight=llm_weight,
                ce_cache_dir=ce_cache_dir,
                ce_force_cpu=ce_force_cpu,
                llm_max_tokens=llm_max_tokens,
                llm_temperature=llm_temperature
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


            reranked_docs, _ = reranker.rerank_documents(query.processed_text, docs_for_rerank, top_k=top_k)
            ce_embedding_token_count = len(query.processed_text.split()) + sum(len(doc["content"].split()) for doc in docs_for_rerank)
            llm_input_token_count = len(query.processed_text.split()) + sum(len(doc["content"].split()) for doc in docs_for_rerank)
            llm_output_token_count = len(str(reranked_docs).split())
            result = PassageRerankResult(
                documents=[Document(
                doc_id=doc_data.get("doc_id", ""),
                content=doc_data.get("content", ""),
                score=doc_data.get("score", 0.0),
                metadata=doc_data.get("metadata", {})
                ) for doc_data in reranked_docs],
                embedding_token_count=ce_embedding_token_count,
                llm_input_token_count=llm_input_token_count,
                llm_output_token_count=llm_output_token_count
            )
            return result

        except Exception as e:
            logger.error(f"CELLM-based parallel reranking failed: {e}")
            result = PassageRerankResult(
                documents=documents,
                embedding_token_count=0.0,
                llm_input_token_count=0.0,
                llm_output_token_count=0.0
            )
            return result


# ==================== PASSAGE FILTER IMPLEMENTATIONS ====================

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


# ==================== PASSAGE COMPRESS IMPLEMENTATIONS ====================

class PassageCompressResult(TypedDict):
    documents: List[Document]
    embedding_token_count: float
    llm_input_token_count: float
    llm_output_token_count: float

class NonePassageCompress(PassageCompressComponent):
    """No passage compression - pass documents through unchanged"""
    
    async def compress_passages(self, documents: List[Document], query: Query) -> PassageCompressResult:
        """Pass documents through unchanged"""
        result = PassageCompressResult(
            documents=documents,
            embedding_token_count=0.0,
            llm_input_token_count=0.0,
            llm_output_token_count=0.0
        )
        return result


class TreeSummarize(PassageCompressComponent):
    """Compress passages using tree summarization"""
    
    async def compress_passages(self, documents: List[Document], query: Query) -> PassageCompressResult:
        """Compress documents using tree summarization"""
        # Placeholder implementation
        logger.warning("TreeSummarize not fully implemented yet")
        result = PassageCompressResult(
            documents=documents,
                embedding_token_count=0.0,
                llm_input_token_count=0.0,
                llm_output_token_count=0.0
            )
        return result

class LLMSummarize(PassageCompressComponent):
    """Compress passages using LLM"""
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.client = None
        self._setup_client()
    
    def _setup_client(self):    
        """Setup the appropriate LLM client"""
        provider = self.config.get("provider", "ollama")
        
        try:
            if provider.lower() == "ollama":
                from util.api.ollama_client import OllamaUtil
                self.client = OllamaUtil
            elif provider.lower() == "gemini":
                from util.api.gemini_client import GeminiUtil
                self.client = GeminiUtil
            else:
                raise ValueError(f"Unsupported provider: {provider}")
                
        except Exception as e:
            logger.error(f"Failed to setup {provider} client: {e}")
            raise

    async def compress_passages(self, documents: List[Document], query: Query) -> PassageCompressResult:
        """Compress documents using LLM"""
        compressed_documents = []
        total_prompt_tokens = 0
        total_eval_count = 0
        for doc in documents:
            default_prompt = """
You are an efficient Document Compressor. Your task is to read the document provided below and extract its key information.

### Instructions
1.  Identify and list the main facts, figures, names, and core concepts from the text.
2.  Present these points as a concise, factual list.
3.  Do not add any information, opinions, or interpretations not present in the original text.
4.  The output should be a dense, information-rich summary.

### Document to Compress
{document}

### Compressed Summary
            """
            prompt = self.config.get("prompt", default_prompt)
            response = self.client.get_ollama_response(self.config.get("model", "gemma3:4b"), prompt.format(document=doc.content))
            if isinstance(response, dict):
                total_prompt_tokens += float(response.get('prompt_tokens', len(prompt.split())))
                total_eval_count += float(response.get('eval_count', 0))
                compressed_documents.append(Document(
                    doc_id=doc.doc_id,
                    content=response.get('response', ''),
                    score=doc.score,
                    metadata=doc.metadata
                ))
            else:
                compressed_documents.append(doc)

        result = PassageCompressResult(
            documents=compressed_documents,
            embedding_token_count=0.0,
            llm_input_token_count=total_prompt_tokens,
            llm_output_token_count=total_eval_count
        )
        return result

# ==================== PROMPT MAKER IMPLEMENTATIONS ====================

class PromptMakerResult(TypedDict):
    prompt: str
    embedding_token_count: float
    llm_input_token_count: float
    llm_output_token_count: float

class SimpleListingPromptMaker(PromptMakerComponent):
    """✅ CURRENTLY IMPLEMENTED - Simple listing of documents in prompt"""
    
    async def make_prompt(self, query: Query, documents: List[Document]) -> PromptMakerResult:
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
        result = PromptMakerResult(
            prompt=prompt,
            embedding_token_count=0.0,
            llm_input_token_count=0.0,
            llm_output_token_count=0.0
        )
        return result


class MultiLLMEnsemblePromptMaker(PromptMakerComponent):
    """Create multiple prompts for ensemble generation"""
    
    async def make_prompt(self, query: Query, documents: List[Document]) -> PromptMakerResult:
        """Create ensemble prompts"""
        # Placeholder implementation
        logger.warning("MultiLLMEnsemblePromptMaker not fully implemented yet")
        result = PromptMakerResult(
            prompt=prompt,
            embedding_token_count=0.0,
            llm_input_token_count=0.0,
            llm_output_token_count=0.0
        )
        return result


# ==================== GENERATOR IMPLEMENTATIONS ====================

class GeneratorResult(TypedDict):
    generated_text: str
    embedding_token_count: float
    llm_input_token_count: float
    llm_output_token_count: float


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
                from util.api.ollama_client import OllamaUtil
                self.client = OllamaUtil
            elif provider.lower() == "gemini":
                from util.api.gemini_client import GeminiUtil
                self.client = GeminiUtil
            else:
                raise ValueError(f"Unsupported provider: {provider}")
                
        except Exception as e:
            logger.error(f"Failed to setup {provider} client: {e}")
            raise
    
    async def generate(self, prompt: str, query: Query) -> GeneratorResult:
        """Generate answer using LLM. Returns (generated_text, prompt_tokens, eval_count)"""
        try:
            model = self.config.get("model", "gpt-3.5-turbo")
            if self.config.get("provider", "ollama").lower() == "ollama":
                response = self.client.get_ollama_response(model, prompt)
                if isinstance(response, dict):
                    result = GeneratorResult(
                        generated_text=response.get('response', ''),
                        embedding_token_count=0.0,
                        llm_input_token_count=float(response.get('prompt_tokens', len(prompt.split()))),
                        llm_output_token_count=float(response.get('eval_count', 0))
                    )
                    return result
                else:
                    result = GeneratorResult(
                        generated_text=str(response),
                        embedding_token_count=0.0,
                        llm_input_token_count=float(len(prompt.split())),
                        llm_output_token_count=float(len(str(response).split()))
                    )
                    return result
            else:  # gemini
                response = self.client.get_gemini_response(model, prompt)
                if isinstance(response, dict):
                    result = GeneratorResult(
                        generated_text=response.get('response', ''),
                        embedding_token_count=0.0,
                        llm_input_token_count=float(len(prompt.split())),
                        llm_output_token_count=float(len(response.get('response', '').split()))
                    )
                    return result
                else:
                    result = GeneratorResult(
                        generated_text=str(response),
                        embedding_token_count=0.0,
                        llm_input_token_count=float(len(prompt.split())),
                        llm_output_token_count=float(len(str(response).split()))
                    )
                    return result
        except Exception as e:
            logger.error(f"Generation failed: {e}")
            result = GeneratorResult(
                generated_text="",
                embedding_token_count=0.0,
                llm_input_token_count=float(len(prompt.split())),
                llm_output_token_count=0.0
            )
            return result

class MultiLLMGenerator(GeneratorComponent):
    """Generate answer using multiple LLMs"""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.clients = {}
        self._setup_client()
    
    def _setup_client(self):
        """Setup the appropriate LLM client"""
        models = self.config.get("models", ["llama3.2:1b", "gemma3:4b"])
        ensemble_llm_model = self.config.get("ensemble_llm_model", "gemma3:4b")
        if ensemble_llm_model.lower().startswith("gemini"):
            from util.api.gemini_client import GeminiUtil
            self.clients[ensemble_llm_model] = GeminiUtil
        else:
            from util.api.ollama_client import OllamaUtil
            self.clients[ensemble_llm_model] = OllamaUtil

        for model in models:
            if model.lower().startswith("gemini"):
                from util.api.gemini_client import GeminiUtil
                self.clients[model] = GeminiUtil
            else:
                from util.api.ollama_client import OllamaUtil
                self.clients[model] = OllamaUtil

    async def generate(self, prompt: str, query: Query) -> GeneratorResult:
        """
        Generate answers using multiple LLMs. 
        Returns a list of tuples: (generated_text, prompt_tokens, eval_count, model_name)
        """
        models = self.config.get("models", ["llama3.2:1b", "gemma3:4b"])
        results = []
        for model in models:
            try:
                client = self.clients.get(model)
                if client is None:
                    logger.error(f"No client found for model: {model}")
                    results.append(("", 0.0, float(len(prompt.split())), 0.0, model))
                    continue

                if model.lower().startswith("gemini"):
                    response = client.get_gemini_response(model, prompt)
                    if isinstance(response, dict):
                        generated_text = response.get('response', '')
                        prompt_tokens = float(len(prompt.split()))
                        eval_count = float(len(generated_text.split()))
                        results.append((generated_text, 0.0, prompt_tokens, eval_count, model))
                    else:
                        results.append((str(response), 0.0, float(len(prompt.split())), 0.0, model))
                else:  # ollama
                    response = client.get_ollama_response(model, prompt)
                    if isinstance(response, dict):
                        generated_text = response.get('response', '')
                        prompt_tokens = float(response.get('prompt_tokens', len(prompt.split())))
                        eval_count = float(response.get('eval_count', len(generated_text.split())))
                        results.append((generated_text, 0.0, prompt_tokens, eval_count, model))
                    else:
                        results.append((str(response), 0.0, float(len(prompt.split())), 0.0, model))
            except Exception as e:
                logger.error(f"Generation failed for model {model}: {e}")
                results.append(("", 0.0, float(len(prompt.split())), 0.0, model))



        original_prompt_with_context = prompt
        total_prompt_tokens = sum([result[2] for result in results])
        total_eval_count = sum([result[3] for result in results])
        logger.info(f"Total prompt tokens: {total_prompt_tokens}")
        logger.info(f"Total eval count: {total_eval_count}")
        ensemble_prompt = """
You are a response synthesizer. Your task is to create one high-quality final answer from several different drafts.

**[THE ORIGINAL PROMPT]**
---
{original_prompt_with_context}
---

**[DRAFT RESPONSES TO COMBINE]**
---
"""

        for draft_response in results:
            ensemble_prompt += f"**Response from {draft_response[4]}:**\n{draft_response[0]}\n\n"

        ensemble_prompt += """      
---


**[YOUR TASK]**
1.  Read the **[THE ORIGINAL PROMPT]** to understand the user's goal.
2.  Review each **[DRAFT RESPONSE]**.
3.  Identify the best and most correct parts from all drafts.
4.  Combine these best parts into a single, clear, and helpful answer.
5.  Remove any repeated information.
6.  Your output must ONLY be the final, combined answer. Do not add any explanation of your process.

**[FINAL ANSWER]**

"""
        ensemble_prompt = ensemble_prompt.format(original_prompt_with_context=original_prompt_with_context)
        ensemble_llm_client = self.clients[self.config.get("ensemble_llm_model", "gemma3:4b")]
        if self.config.get("ensemble_llm_model", "gemma3:4b").lower().startswith("gemini"):
            ensemble_llm_response = ensemble_llm_client.get_gemini_response(self.config.get("ensemble_llm_model", "gemma3:4b"), ensemble_prompt)
        else:
            ensemble_llm_response = ensemble_llm_client.get_ollama_response(self.config.get("ensemble_llm_model", "gemma3:4b"), ensemble_prompt)
        logger.debug(f"Ensemble LLM prompt: {ensemble_prompt}")
        logger.debug(f"Ensemble LLM response: {ensemble_llm_response}")
        if isinstance(ensemble_llm_response, dict):
            ensemble_llm_generated_text = ensemble_llm_response.get('response', '')
            ensemble_llm_prompt_tokens = float(ensemble_llm_response.get('prompt_tokens', len(ensemble_prompt.split())))
            ensemble_llm_eval_count = float(ensemble_llm_response.get('eval_count', len(ensemble_llm_generated_text.split())))
            logger.info(f"Ensemble LLM prompt tokens: {ensemble_llm_prompt_tokens}")
            logger.info(f"Ensemble LLM eval count: {ensemble_llm_eval_count}")
            result = GeneratorResult(
                generated_text=ensemble_llm_generated_text,
                embedding_token_count=0.0,
                llm_input_token_count=total_prompt_tokens + ensemble_llm_prompt_tokens,
                llm_output_token_count=total_eval_count + ensemble_llm_eval_count
            )
            return result
        else:
            result = GeneratorResult(
                generated_text=str(ensemble_llm_response),
                embedding_token_count=0.0,
                llm_input_token_count=total_prompt_tokens + len(ensemble_prompt.split()),
                llm_output_token_count=total_eval_count + len(str(ensemble_llm_response).split())
            )
            return result


# ==================== POST-GENERATION IMPLEMENTATIONS ====================

class PostGenerationResult(TypedDict):
    generated_text: str
    embedding_token_count: float
    llm_input_token_count: float
    llm_output_token_count: float

class NonePostGeneration(PostGenerationComponent):
    """No post-generation processing - return answer unchanged"""
    
    async def post_process(self, generated_answer: str, query: Query, context: Context) -> PostGenerationResult:
        """Return answer unchanged"""
        result = PostGenerationResult(
            generated_text=generated_answer,
            embedding_token_count=0.0,
            llm_input_token_count=0.0,
            llm_output_token_count=0.0
        )
        return result


class ReflectionRevising(PostGenerationComponent):
    """Refine answer using reflection and revising"""
    
    async def post_process(self, generated_answer: str, query: Query, context: Context) -> PostGenerationResult:
        """Post-process answer using reflection"""
        # Placeholder implementation
        logger.warning("ReflectionRevising not fully implemented yet")
        result = PostGenerationResult(
            generated_text=generated_answer,
            embedding_token_count=0.0,
            llm_input_token_count=0.0,
            llm_output_token_count=0.0
        )
        return result


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
        "cellm_parallel_rerank": CELLM_ParallelRerank,
    },
    "passage_filter": {
        "simple_threshold": SimpleThresholdFilter,
        "similarity_threshold": SimilarityThresholdFilter,
    },
    "passage_compress": {
        "none": NonePassageCompress,
        "tree_summarize": TreeSummarize,
        "llm_summarize": LLMSummarize,
    },
    "prompt_maker": {
        "simple_listing": SimpleListingPromptMaker,
        "multi_llm_ensemble": MultiLLMEnsemblePromptMaker,
    },
    "generator": {
        "llm": LLMGenerator,
        "multi_llm": MultiLLMGenerator,
    },
    "post_generation": {
        "none": NonePostGeneration,
        "reflection_revising": ReflectionRevising,
    },
} 