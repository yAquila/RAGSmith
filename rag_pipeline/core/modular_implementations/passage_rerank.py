
import logging
from typing import List, TypedDict

from rag_pipeline.core.modular_framework import (
    PassageRerankComponent, Document, Query
)

logger = logging.getLogger(__name__)

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
            from rag_pipeline.util.rerank.reranker import get_reranker
            
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
            from rag_pipeline.util.rerank.llm_reranker import get_llm_reranker
            
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
            from rag_pipeline.util.rerank.parallel_reranker import get_parallel_reranker
            
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
