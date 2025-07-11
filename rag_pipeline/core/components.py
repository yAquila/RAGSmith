from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, TYPE_CHECKING
import time
import logging

from .models import (
    RAGConfig, RAGDocument, RetrievalResult, GenerationResult, ModelCombination
)

logger = logging.getLogger(__name__)

class RetrievalComponent(ABC):
    """Abstract base class for retrieval components"""
    
    def __init__(self, embedding_model: str, config: RAGConfig):
        self.embedding_model = embedding_model
        self.config = config
    
    @abstractmethod
    async def retrieve(self, query: str, k: Optional[int] = None, combination: Optional[ModelCombination] = None) -> RetrievalResult:
        """Retrieve relevant documents for a query"""
        pass
    
    @abstractmethod
    async def index_documents(self, documents: List[RAGDocument]) -> bool:
        """Index documents in the retrieval system"""
        pass

class GenerationComponent(ABC):
    """Abstract base class for generation components"""
    
    def __init__(self, llm_model: str, config: RAGConfig):
        self.llm_model = llm_model
        self.config = config
    
    @abstractmethod
    async def generate(self, query: str, context: str, embedding_model: str) -> GenerationResult:
        """Generate answer given query and retrieved context"""
        pass

# Concrete implementations

class VectorStoreRetrieval(RetrievalComponent):
    """Vector store based retrieval using embeddings"""
    
    def __init__(self, embedding_model: str, config: RAGConfig):
        super().__init__(embedding_model, config)
        self.vectorstore = None
        self._setup_vectorstore()
    
    def _setup_vectorstore(self):
        """Setup the vector store (Qdrant in this case)"""
        try:
            from util.vectorstore.qdrant_store import QdrantVectorStore
            from util.vectorstore.dataset_utils import generate_dataset_hash_from_file
            import os
            
            # Use default docs if no dataset path specified
            docs_path = self.config.dataset_path or os.path.join(
                os.path.dirname(os.path.dirname(__file__)), 
                "default_datasets", 
                "retrieval_docs.csv"
            )
            
            dataset_hash = generate_dataset_hash_from_file(docs_path)
            self.vectorstore = QdrantVectorStore(self.embedding_model, dataset_hash)
            
        except Exception as e:
            logger.error(f"Failed to setup vectorstore for {self.embedding_model}: {e}")
            raise
    
    async def retrieve(self, query: str, k: Optional[int] = None, combination: Optional['ModelCombination'] = None) -> RetrievalResult:
        """Retrieve documents using vector similarity search with optional reranking"""
        start_time = time.time()
        k = k or self.config.retrieval_k
        
        try:
            results = self.vectorstore.similarity_search(query, k)
            
            retrieved_docs = []
            for result in results:
                retrieved_docs.append({
                    "doc_id": result.get("doc_id"),
                    "content": result.get("page_content", ""),
                    "score": result.get("score", 0.0),
                    "metadata": result.get("metadata", {})
                })
            
            retrieval_time = time.time() - start_time
            rerank_time = 0.0
            reranked = False
            rerank_model = None
            llm_rerank_time = 0.0
            llm_reranked = False
            llm_rerank_model = None
            parallel_reranked = False
            ensemble_time = 0.0
            ensemble_method = None
            
            # Check if parallel reranking should be applied
            if (combination and 
                combination.use_parallel_reranking and 
                combination.use_reranking and combination.rerank_model and
                combination.use_llm_reranking and combination.llm_rerank_model and
                retrieved_docs):
                
                try:
                    # Apply parallel reranking
                    parallel_start = time.time()
                    from util.rerank.parallel_reranker import get_parallel_reranker
                    
                    parallel_reranker = get_parallel_reranker(
                        ce_model=combination.rerank_model,
                        llm_model=combination.llm_rerank_model,
                        ensemble_method=self.config.rerank_ensemble_method,
                        ce_weight=self.config.ce_rerank_weight,
                        llm_weight=self.config.llm_rerank_weight,
                        ce_cache_dir=self.config.rerank_cache_dir,
                        ce_force_cpu=self.config.rerank_force_cpu,
                        llm_max_tokens=self.config.llm_rerank_max_tokens,
                        llm_temperature=self.config.llm_rerank_temperature
                    )
                    
                    # Determine top_k for parallel reranking
                    parallel_top_k = min(self.config.rerank_top_k, self.config.llm_rerank_top_k)
                    
                    retrieved_docs, timing_info = parallel_reranker.rerank_documents(
                        query, retrieved_docs, top_k=parallel_top_k
                    )
                    
                    rerank_time = timing_info.get("ce_time", 0.0)
                    llm_rerank_time = timing_info.get("llm_time", 0.0) 
                    ensemble_time = timing_info.get("ensemble_time", 0.0)
                    
                    reranked = True
                    rerank_model = combination.rerank_model
                    llm_reranked = True
                    llm_rerank_model = combination.llm_rerank_model
                    parallel_reranked = True
                    ensemble_method = self.config.rerank_ensemble_method
                    
                    logger.info(f"Applied parallel reranking: CE({combination.rerank_model}) + LLM({combination.llm_rerank_model}), "
                               f"ensemble method: {self.config.rerank_ensemble_method}")
                    
                except Exception as e:
                    logger.warning(f"Parallel reranking failed, using original results: {e}")
            
            # If parallel reranking was not applied, check for individual reranking
            elif not parallel_reranked and retrieved_docs:
                
                # Apply cross-encoder reranking if enabled
                if combination and combination.use_reranking and combination.rerank_model:
                    try:
                        rerank_start = time.time()
                        from util.rerank.reranker import get_reranker
                        
                        reranker = get_reranker(
                            combination.rerank_model, 
                            cache_dir=self.config.rerank_cache_dir,
                            force_cpu=self.config.rerank_force_cpu
                        )
                        retrieved_docs = reranker.rerank_documents(
                            query, 
                            retrieved_docs, 
                            top_k=self.config.rerank_top_k
                        )
                        
                        rerank_time = time.time() - rerank_start
                        reranked = True
                        rerank_model = combination.rerank_model
                        
                        logger.info(f"Applied cross-encoder reranking with {combination.rerank_model}, kept top {len(retrieved_docs)} docs")
                        
                    except Exception as e:
                        logger.warning(f"Cross-encoder reranking failed, using original results: {e}")
                
                # Apply LLM reranking if enabled (and not already done in parallel)
                if combination and combination.use_llm_reranking and combination.llm_rerank_model:
                    try:
                        llm_rerank_start = time.time()
                        from util.rerank.llm_reranker import get_llm_reranker
                        
                        llm_reranker = get_llm_reranker(
                            model_name=combination.llm_rerank_model, 
                            max_tokens=self.config.llm_rerank_max_tokens,
                            temperature=self.config.llm_rerank_temperature
                        )
                        retrieved_docs = llm_reranker.rerank_documents(
                            query, 
                            retrieved_docs, 
                            top_k=self.config.llm_rerank_top_k
                        )
                        
                        llm_rerank_time = time.time() - llm_rerank_start
                        llm_reranked = True
                        llm_rerank_model = combination.llm_rerank_model
                        
                        logger.info(f"Applied LLM reranking with {combination.llm_rerank_model}, kept top {len(retrieved_docs)} docs")
                        
                    except Exception as e:
                        logger.warning(f"LLM reranking failed, using previous results: {e}")
            
            return RetrievalResult(
                query=query,
                retrieved_docs=retrieved_docs,
                embedding_model=self.embedding_model,
                retrieval_time=retrieval_time,
                rerank_model=rerank_model,
                rerank_time=rerank_time,
                reranked=reranked,
                llm_rerank_model=llm_rerank_model,
                llm_rerank_time=llm_rerank_time,
                llm_reranked=llm_reranked,
                parallel_reranked=parallel_reranked,
                ensemble_time=ensemble_time,
                ensemble_method=ensemble_method
            )
            
        except Exception as e:
            logger.error(f"Retrieval failed for {self.embedding_model}: {e}")
            return RetrievalResult(
                query=query,
                retrieved_docs=[],
                embedding_model=self.embedding_model,
                retrieval_time=time.time() - start_time,
                error=str(e)
            )
    
    async def index_documents(self, documents: List[RAGDocument]) -> bool:
        """Index documents in the vector store"""
        try:
            # Convert to pandas DataFrame for existing indexing logic
            import pandas as pd
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

class OllamaGeneration(GenerationComponent):
    """Ollama-based text generation"""
    
    def __init__(self, llm_model: str, config: RAGConfig):
        super().__init__(llm_model, config)
        self._setup_client()
    
    def _setup_client(self):
        """Setup Ollama client"""
        try:
            from util.api.ollama_client import OllamaUtil
            self.client = OllamaUtil
        except Exception as e:
            logger.error(f"Failed to setup Ollama client: {e}")
            raise
    
    def _create_rag_prompt(self, query: str, context: str) -> str:
        """Create a RAG prompt from query and context"""
        if not context.strip():
            return f"Question: {query}\n\nAnswer:"
        
        return f"""Context Information:
{context}

Based on the context information provided above, please answer the following question. If the context doesn't contain enough information to answer the question, please state that clearly.

Question: {query}

Answer:"""
    
    async def generate(self, query: str, context: str, embedding_model: str) -> GenerationResult:
        """Generate answer using LLM with retrieved context"""
        start_time = time.time()
        
        try:
            prompt = self._create_rag_prompt(query, context)
            
            # Call Ollama API
            response = self.client.get_ollama_response(self.llm_model, prompt)
            
            # Extract response text and metrics
            if isinstance(response, dict):
                generated_text = response.get('response', '')
                tokens_per_second = response.get('tps')
                token_count = response.get('eval_count')
            else:
                generated_text = str(response)
                tokens_per_second = None
                token_count = None
            
            return GenerationResult(
                query=query,
                context=context,
                generated_answer=generated_text,
                llm_model=self.llm_model,
                embedding_model=embedding_model,
                generation_time=time.time() - start_time,
                token_count=token_count,
                tokens_per_second=tokens_per_second
            )
            
        except Exception as e:
            logger.error(f"Generation failed for {self.llm_model}: {e}")
            return GenerationResult(
                query=query,
                context=context,
                generated_answer="",
                llm_model=self.llm_model,
                embedding_model=embedding_model,
                generation_time=time.time() - start_time,
                error=str(e)
            )


class GeminiGeneration(GenerationComponent):
    """Gemini-based text generation"""
    
    def __init__(self, llm_model: str, config: RAGConfig):
        super().__init__(llm_model, config)
        self._setup_client()
    
    def _setup_client(self):
        """Setup Gemini client"""
        try:
            from util.api.gemini_client import GeminiUtil
            self.client = GeminiUtil
        except Exception as e:
            logger.error(f"Failed to setup Gemini client: {e}")
            raise
    
    def _create_rag_prompt(self, query: str, context: str) -> str:
        """Create a RAG prompt from query and context"""
        if not context.strip():
            return f"Question: {query}\n\nAnswer:"
        
        return f"""Context Information:
{context}

Based on the context information provided above, please answer the following question. If the context doesn't contain enough information to answer the question, please state that clearly.

Question: {query}

Answer:"""
    
    async def generate(self, query: str, context: str, embedding_model: str) -> GenerationResult:
        """Generate answer using LLM with retrieved context"""
        start_time = time.time()
        
        try:
            prompt = self._create_rag_prompt(query, context)
            
            # Call Gemini API
            response = self.client.get_gemini_response(self.llm_model, prompt)
            
            # Extract response text and metrics
            if isinstance(response, dict):
                generated_text = response.get('response', '')
                tokens_per_second = response.get('tps')
                token_count = response.get('eval_count')
            else:
                generated_text = str(response)
                tokens_per_second = None
                token_count = None
            
            return GenerationResult(
                query=query,
                context=context,
                generated_answer=generated_text,
                llm_model=self.llm_model,
                embedding_model=embedding_model,
                generation_time=time.time() - start_time,
                token_count=token_count,
                tokens_per_second=tokens_per_second
            )
            
        except Exception as e:
            logger.error(f"Generation failed for {self.llm_model}: {e}")
            return GenerationResult(
                query=query,
                context=context,
                generated_answer="",
                llm_model=self.llm_model,
                embedding_model=embedding_model,
                generation_time=time.time() - start_time,
                error=str(e)
            )


# Component Factory for easy extension
class ComponentFactory:
    """Factory for creating RAG components"""
    
    @staticmethod
    def create_retrieval_component(embedding_model: str, config: RAGConfig, 
                                 component_type: str = "vectorstore") -> RetrievalComponent:
        """Create a retrieval component"""
        if component_type == "vectorstore":
            return VectorStoreRetrieval(embedding_model, config)
        else:
            raise ValueError(f"Unknown retrieval component type: {component_type}")
    
    @staticmethod
    def create_generation_component(llm_model: str, config: RAGConfig, 
                                  component_type: str = "ollama") -> GenerationComponent:
        """Create a generation component"""
        if component_type == "ollama":
            return OllamaGeneration(llm_model, config)
        elif component_type == "gemini":
            return GeminiGeneration(llm_model, config)
        else:
            raise ValueError(f"Unknown generation component type: {component_type}") 