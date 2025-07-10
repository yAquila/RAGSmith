from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
from dataclasses import dataclass
import time

@dataclass
class ModelCombination:
    """Represents a combination of models and reranking configuration for testing"""
    embedding_model: str
    llm_model: str
    use_reranking: bool
    rerank_model: Optional[str] = None
    use_llm_reranking: bool = False
    llm_rerank_model: Optional[str] = None
    use_parallel_reranking: bool = False  # NEW: If True, apply CE and LLM reranking in parallel
    
    def get_combination_name(self) -> str:
        """Get a string representation of this combination"""
        name_parts = [self.embedding_model]
        
        if self.use_parallel_reranking:
            # Parallel reranking case
            name_parts.append(f"Parallel({self.rerank_model}+{self.llm_rerank_model})")
        else:
            # Individual reranking cases
            if self.use_reranking and self.rerank_model:
                name_parts.append(self.rerank_model)
            
            if self.use_llm_reranking and self.llm_rerank_model:
                name_parts.append(f"LLM-rerank({self.llm_rerank_model})")
        
        name_parts.append(self.llm_model)
        return " + ".join(name_parts)

@dataclass
class RAGConfig:
    """Configuration for RAG pipeline evaluation"""
    # Models to test
    embedding_models: List[str]
    llm_models: List[str]
    eval_llm_model: str  # Model used for evaluation
    
    # Retrieval settings
    retrieval_k: int = 10
    retrieval_threshold: float = 0.5
    
    # Cross-encoder reranking settings
    rerank_model: Optional[str] = None  # e.g., 'BAAI/bge-reranker-v2-m3', if None skip cross-encoder reranking
    rerank_top_k: int = 5  # Number of top documents to keep after cross-encoder reranking
    test_with_and_without_reranking: bool = True  # If True and rerank_model is set, test both with and without cross-encoder reranking
    rerank_cache_dir: Optional[str] = None  # Directory to cache reranker models (if None, uses default ~/.cache/rag_pipeline/reranker_models)
    rerank_force_cpu: bool = False  # If True, force reranker to use CPU instead of GPU
    
    # LLM reranking settings
    llm_rerank_model: Optional[str] = None  # e.g., 'llama3.2:1b', if None skip LLM reranking
    llm_rerank_top_k: int = 5  # Number of top documents to keep after LLM reranking
    test_with_and_without_llm_reranking: bool = True  # If True and llm_rerank_model is set, test both with and without LLM reranking
    llm_rerank_max_tokens: int = 2048  # Max tokens for LLM reranking
    llm_rerank_temperature: float = 0.1  # Temperature for LLM reranking
    
    # Generation settings
    max_tokens: int = 500
    temperature: float = 0.1
    
    # Evaluation settings
    eval_batch_size: int = 10
    
    # Dataset settings
    dataset_path: Optional[str] = None
    max_test_cases: Optional[int] = None

    # Parallel reranking settings
    enable_parallel_reranking: bool = True  # If True, create parallel combination when both rerankers are enabled
    rerank_ensemble_method: str = "weighted"  # "weighted", "average", "max"
    ce_rerank_weight: float = 0.7  # Weight for cross-encoder scores in ensemble
    llm_rerank_weight: float = 0.3  # Weight for LLM scores in ensemble

class RAGTestCase(BaseModel):
    """Individual test case for RAG evaluation"""
    id: str
    query: str
    ground_truth_answer: str
    relevant_doc_ids: List[str]  # Document IDs that should be retrieved
    metadata: Optional[Dict[str, Any]] = None

class RetrievalResult(BaseModel):
    """Result from retrieval component"""
    query: str
    retrieved_docs: List[Dict[str, Any]]  # [{"doc_id": str, "content": str, "score": float, "rerank_score": float?, "llm_rerank_score": float?}]
    embedding_model: str
    retrieval_time: float
    rerank_model: Optional[str] = None  # Cross-encoder model used for reranking (if any)
    rerank_time: float = 0.0  # Time spent on cross-encoder reranking
    reranked: bool = False  # Whether documents were reranked with cross-encoder
    llm_rerank_model: Optional[str] = None  # LLM model used for reranking (if any)
    llm_rerank_time: float = 0.0  # Time spent on LLM reranking
    llm_reranked: bool = False  # Whether documents were reranked with LLM
    # NEW: Parallel reranking fields
    parallel_reranked: bool = False  # Whether parallel reranking was applied
    ensemble_time: float = 0.0  # Time spent on ensemble combination
    ensemble_method: Optional[str] = None  # Method used for ensemble
    error: Optional[str] = None

class GenerationResult(BaseModel):
    """Result from generation component"""
    query: str
    context: str  # Combined retrieved documents
    generated_answer: str
    llm_model: str
    embedding_model: str  # Which embedding model provided the context
    generation_time: float
    token_count: Optional[int] = None
    tokens_per_second: Optional[float] = None
    error: Optional[str] = None

class RAGMetrics(BaseModel):
    """Evaluation metrics for a single test case"""
    # Retrieval metrics
    recall_at_k: float
    map_score: float  # Mean Average Precision (mAP)
    ndcg_at_k: float
    mrr: float  # Mean Reciprocal Rank
    eval_k: int  # The k value used for evaluation (retrieval_k or rerank_top_k)
    
    # Generation metrics
    llm_score: float  # LLM-based evaluation score (0-1)
    semantic_similarity: float  # Embedding-based similarity (0-1)
    
    # Component scores (averages)
    retrieval_score: float  # Average of retrieval metrics
    generation_score: float  # Average of generation metrics
    
    # Combined metrics
    overall_score: float  # Weighted combination of retrieval and generation

class RAGEvaluationResult(BaseModel):
    """Complete evaluation result for a model combination"""
    embedding_model: str
    llm_model: str
    test_case_id: str
    
    # Components results
    retrieval_result: RetrievalResult
    generation_result: GenerationResult
    
    # Evaluation metrics
    metrics: RAGMetrics
    
    # Timing breakdown
    retrieval_eval_time: float  # Time spent evaluating retrieval
    generation_eval_time: float  # Time spent evaluating generation
    total_eval_time: float  # Total evaluation time
    error: Optional[str] = None

class RAGBenchmarkResult(BaseModel):
    """Aggregated results for entire benchmark"""
    config: Dict[str, Any]  # Configuration used
    
    # Individual results
    individual_results: List[RAGEvaluationResult]
    
    # Aggregated metrics by model combination
    aggregated_metrics: Dict[str, Dict[str, Any]]  # {f"{emb_model}_{llm_model}": metrics}
    
    # Summary statistics
    total_test_cases: int
    successful_cases: int
    failed_cases: int
    total_runtime: float
    
    # Timing breakdown
    total_retrieval_prediction_time: float
    total_generation_prediction_time: float
    total_retrieval_evaluation_time: float
    total_generation_evaluation_time: float
    
    # Best performing combinations
    best_retrieval_combo: Optional[str] = None
    best_generation_combo: Optional[str] = None
    best_overall_combo: Optional[str] = None

class RAGDocument(BaseModel):
    """Document in the RAG knowledge base"""
    doc_id: str
    content: str
    metadata: Optional[Dict[str, Any]] = None
    
    def __hash__(self):
        return hash(self.doc_id) 