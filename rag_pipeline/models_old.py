from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TestInputModel(BaseModel):
    user_prompt: str = Field(..., description="User prompt/question")
    ground_truth: Optional[str] = Field(None, description="Expected answer/output")
    prediction: Optional[str] = Field(None, description="Model prediction")
    additional_args: Optional[Dict[str, Any]] = Field(None, description="Additional task-specific arguments")
    docs: Optional[List[str]] = Field(None, description="Document IDs")

    class Config:
        use_enum_values = True

class BenchmarkConfigModel(BaseModel):
    """Configuration for benchmark tasks."""
    task: str = Field("retrieval", description="Task type") 
    embedding_model_name: Optional[str] = Field(None, description="Model name")
    llm_model_name: Optional[str] = Field(None, description="Model name")
    llm_model_names: Optional[List[str]] = Field(None, description="Multiple model names")
    embedding_model_names: Optional[List[str]] = Field(None, description="Multiple model names")
    vectorstore: str = Field("qdrant", description="Vectorstore name")
    retrieval_k: int = Field(10, description="Number of top results to retrieve")
    retrieval_threshold: float = Field(0.5, description="Similarity threshold for retrieval")
    eval_llm_model_name: Optional[str] = Field(None, description="LLM model name for evaluation")
    eval_embedding_model_name: Optional[str] = Field(None, description="Embedding model name for evaluation")

class DatasetValidationResult(BaseModel):
    isValid: bool = Field(..., alias="is_valid", description="Whether the dataset is valid")
    missingFields: List[str] = Field(default=[], alias="missing_fields", description="Required fields that are missing")
    extraFields: List[str] = Field(default=[], alias="extra_fields", description="Extra fields found in the dataset")
    rowCount: int = Field(..., alias="row_count", description="Number of rows in the dataset")
    message: str = Field(..., description="Validation message")
    warnings: Optional[List[str]] = Field(None, description="Warning messages")

    class Config:
        populate_by_name = True

# Evaluation Results Model
class EvaluationResults(BaseModel):
    task_id: str = Field("retrieval", description="Task identifier")
    model_id: str = Field(..., description="Model identifier")
    score: Optional[float] = Field(None, description="Overall score")
    llm_score: Optional[float] = Field(None, description="LLM score")
    semantic_score: Optional[float] = Field(None, description="Semantic score")
    retrieval_score: Optional[float] = Field(None, description="Overall retrieval metric score")
    
    # Individual retrieval metrics (only the ones we need)
    recall_at_10: Optional[float] = Field(None, description="Recall@10 for retrieval tasks")
    ndcg_at_10: Optional[float] = Field(None, description="nDCG@10 for retrieval tasks")
    map_score: Optional[float] = Field(None, description="Mean Average Precision for retrieval tasks")
    
    # TPS (Tokens Per Second) metrics
    average_tps: Optional[float] = Field(None, description="Average tokens per second for this task")
    prediction_count: Optional[int] = Field(None, description="Number of predictions made for TPS calculation")
    
    overall_score: Optional[float] = Field(None, description="Overall aggregated score")
    execution_time: Optional[float] = Field(None, description="Execution time in milliseconds")
    test_case_count: Optional[int] = Field(None, description="Number of test cases processed for this task")
    error: Optional[str] = Field(None, description="Error message if evaluation failed")

    class Config:
        use_enum_values = True


class TaskResult(BaseModel):
    """Model for individual task execution results"""
    task_id: str
    task_name: str
    task_type: str
    dataset_name: str
    embedding_model_name: str
    llm_model_name: str
    eval_llm_model_name: Optional[str] = None
    evaluation_config: Dict[str, Any]
    metrics: Dict[str, Any] = {}
    llm_score: Optional[float] = None
    semantic_score: Optional[float] = None
    score: Optional[float] = None
    overall_score: Optional[float] = None
    retrieval_score: Optional[float] = None
    
    # Individual retrieval metrics (only the ones we need)
    recall_at_10: Optional[float] = None
    ndcg_at_10: Optional[float] = None
    map_score: Optional[float] = None
    
    # TPS (Tokens Per Second) metrics
    tps: Optional[Union[float, List[float]]] = None
    
    error: Optional[str] = None
    execution_time: Optional[float] = None
