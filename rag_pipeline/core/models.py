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
    retrieved_docs: List[Dict[str, Any]]  # [{"doc_id": str, "content": str, "score": float, ...}]
    embedding_model: str
    # Canonical per-component timing fields
    pre_embedding_time: float = 0.0
    query_expansion_time: float = 0.0
    retrieval_time: float = 0.0
    passage_augment_time: float = 0.0
    passage_rerank_time: float = 0.0
    passage_filter_time: float = 0.0
    passage_compress_time: float = 0.0
    prompt_maker_time: float = 0.0
    generation_time: float = 0.0
    post_generation_time: float = 0.0
    # Token counts
    embedding_token_counts: Dict[str, float] = {}
    llm_input_token_counts: Dict[str, float] = {}
    llm_output_token_counts: Dict[str, float] = {}
    error: Optional[str] = None

class GenerationResult(BaseModel):
    """Result from generation component"""
    query: str
    context: str  # Combined retrieved documents
    generated_answer: str
    llm_model: str
    embedding_model: str  # Which embedding model provided the context
    combo_name: str
    # Canonical per-component timing fields
    pre_embedding_time: float = 0.0
    query_expansion_time: float = 0.0
    retrieval_time: float = 0.0
    passage_augment_time: float = 0.0
    passage_rerank_time: float = 0.0
    passage_filter_time: float = 0.0
    passage_compress_time: float = 0.0
    prompt_maker_time: float = 0.0
    generation_time: float = 0.0
    post_generation_time: float = 0.0
    # Token counts
    embedding_token_counts: Dict[str, float] = {}
    llm_input_token_counts: Dict[str, float] = {}
    llm_output_token_counts: Dict[str, float] = {}
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
    combo_name: Optional[str] = None
    retrieval_result: RetrievalResult
    generation_result: GenerationResult
    metrics: RAGMetrics
    # Timing breakdown
    retrieval_eval_time: float  # Time spent evaluating retrieval
    generation_eval_time: float  # Time spent evaluating generation
    total_eval_time: float  # Total evaluation time
    # Canonical per-component timing fields
    pre_embedding_time: float = 0.0
    query_expansion_time: float = 0.0
    retrieval_time: float = 0.0
    passage_augment_time: float = 0.0
    passage_rerank_time: float = 0.0
    passage_filter_time: float = 0.0
    passage_compress_time: float = 0.0
    prompt_maker_time: float = 0.0
    generation_time: float = 0.0
    post_generation_time: float = 0.0
    # Token counts
    embedding_token_counts: Dict[str, float] = {}
    llm_input_token_counts: Dict[str, float] = {}
    llm_output_token_counts: Dict[str, float] = {}
    error: Optional[str] = None

class RAGBenchmarkResult(BaseModel):
    """Aggregated results for entire benchmark"""
    config: Dict[str, Any]  # Configuration used
    individual_results: List[RAGEvaluationResult]
    aggregated_metrics: Dict[str, Dict[str, Any]]  # {f"{emb_model}_{llm_model}": metrics}
    total_test_cases: int
    successful_cases: int
    failed_cases: int
    total_runtime: float
    # Timing breakdown (only evaluation times remain)
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