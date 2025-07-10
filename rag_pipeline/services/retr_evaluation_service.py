"""Evaluation Processing Service - Retrieval Tasks Only"""

import asyncio
import logging
import time
import dataclasses
from typing import Dict, List, Optional, Any

from models import (
    EvaluationResults,
    TaskResult
)

logger = logging.getLogger(__name__)


class RetrEvaluationService:
    """Service for handling retrieval task evaluation processing"""
    
    def __init__(self, vectorstore_service):
        self.vectorstore_service = vectorstore_service
        self.logger = logging.getLogger(__name__)
    
    async def evaluate_all_predictions(
        self,
        config,
        all_predictions: list,
        progress_callback: Optional[Any] = None
    ) -> list:
        """Evaluate all retrieval predictions"""
        all_results = []
        
        # Group predictions by model and task for aggregation
        predictions_by_model_task = {}
        for prediction in all_predictions:
            if prediction.get('error'):
                # Handle error predictions
                error_result = EvaluationResults(
                    task_id="retrieval",
                    model_id=prediction['model_name'],
                    error=prediction['error']
                )
                all_results.append(error_result)
                continue
                
            model_name = prediction['model_name']
            task_type = prediction['task_type']
            
            # Only handle retrieval tasks
            if task_type != "retrieval":
                logger.warning(f"Skipping non-retrieval task: {task_type}")
                continue
                
            key = (model_name, task_type)
            
            if key not in predictions_by_model_task:
                predictions_by_model_task[key] = []
            predictions_by_model_task[key].append(prediction)
        
        # Process each model-task combination
        total_combinations = len(predictions_by_model_task)
        
        for idx, (key, predictions) in enumerate(predictions_by_model_task.items()):
            model_name, task_type = key
            
            try:
                # Evaluate all predictions for this model-task combination
                task_results = await self.evaluate_retrieval_predictions(predictions, config, model_name)
                
                # Aggregate results for this task and model
                aggregated_result = self.aggregate_retrieval_results(task_results, model_name)
                all_results.append(aggregated_result)
                
            except Exception as e:
                logger.error(f"Failed to evaluate {model_name} - {task_type}: {str(e)}")
                error_result = EvaluationResults(
                    task_id="retrieval",
                    model_id=model_name,
                    error=str(e)
                )
                all_results.append(error_result)
        
        return all_results
    
    async def evaluate_retrieval_predictions(self, predictions: list, config, model_name) -> list:
        """Evaluate retrieval predictions"""
        task_results = []
        vectorstore = self.vectorstore_service.get_or_create_vectorstore(model_name)
        for prediction in predictions:
            try:
                # Extract prediction data
                test_input = prediction['test_input']
                task_type = prediction['task_type']
                prediction_text = prediction['prediction']
                
                # Set the prediction in test_input for evaluation
                test_input.prediction = prediction_text
                
                # Get vectorstore for retrieval evaluation
                
                # Create retrieval test instance directly
                from retrieval_tests import RetrievalTest
                test_instance = RetrievalTest(config=config, vectorstore=vectorstore)
                
                start_time_pipeline = time.time()
                eval_result_data = test_instance._evaluate_prediction(test_input)
                end_time_pipeline = time.time()
                execution_time_ms = (end_time_pipeline - start_time_pipeline) * 1000
                
                # Convert retrieval evaluation results
                converted_result = self.convert_retrieval_result(eval_result_data)
                
                # Extract TPS data if available
                tps_data = test_input.tps_data if hasattr(test_input, 'tps_data') else []
                
                # Create TaskResult
                task_result_obj = TaskResult(
                    task_id=prediction['task_data'].get("id", f"retrieval_{str(prediction['task_data'].get('user_prompt', ''))[:20]}"),
                    task_name=prediction['task_data'].get("task_name", "retrieval"),
                    task_type=task_type,
                    dataset_name=prediction['dataset_name'],
                    embedding_model_name=model_name,
                    llm_model_name=config.llm_model_name,
                    eval_llm_model_name=config.eval_llm_model_name,
                    evaluation_config=config.dict() if hasattr(config, 'dict') else dataclasses.asdict(config) if hasattr(config, '__dataclass_fields__') else {},
                    metrics=converted_result.get("metrics", {}),
                    overall_score=converted_result.get("overall_score"),
                    retrieval_score=converted_result.get("retrieval_score"),
                    
                    # Individual retrieval metrics
                    recall_at_10=converted_result.get("recall_at_10"),
                    ndcg_at_10=converted_result.get("ndcg_at_10"),
                    map_score=converted_result.get("map_score"),
                    
                    # TPS (Tokens Per Second) metrics
                    tps=tps_data,
                    
                    error=converted_result.get("error"),
                    execution_time=execution_time_ms
                )
                task_results.append(task_result_obj)
                
            except Exception as e:
                logger.error(f"Failed to evaluate retrieval prediction: {str(e)}")
                # Create error task result
                error_task_result = TaskResult(
                    task_id=prediction.get('task_type', 'retrieval'),
                    task_name=prediction.get('task_type', 'retrieval'),
                    task_type=prediction.get('task_type', 'retrieval'),
                    dataset_name=prediction.get('dataset_name', 'unknown'),
                    embedding_model_name=model_name,
                    llm_model_name=config.llm_model_name,
                    eval_llm_model_name=config.eval_llm_model_name,
                    evaluation_config={},
                    error=str(e)
                )
                task_results.append(error_task_result)
        
        return task_results
    
    def convert_retrieval_result(self, result_data) -> Dict[str, Any]:
        """Convert retrieval test results to standardized format"""
        output = {}
        error_message = None
        
        if result_data is None:
            error_message = "Retrieval evaluation failed to produce a result."
        elif isinstance(result_data, dict):
            # Handle comprehensive retrieval metrics
            retrieval_score = result_data.get('retrieval_score', 0.0)
            retrieval_metrics = result_data.get('retrieval_metrics', {})
            
            output["retrieval_score"] = retrieval_score
            output["retrieval_metrics"] = retrieval_metrics
            
            # Extract individual metrics for detailed reporting
            individual_scores = []
            if retrieval_metrics:
                output["recall_at_10"] = retrieval_metrics.get('recall@10', None)
                output["ndcg_at_10"] = retrieval_metrics.get('ndcg@10', None)
                output["map_score"] = retrieval_metrics.get('map', None)
                
                # Calculate overall score as average of the individual metrics we care about
                if output["recall_at_10"] is not None:
                    individual_scores.append(output["recall_at_10"])
                if output["ndcg_at_10"] is not None:
                    individual_scores.append(output["ndcg_at_10"])
                if output["map_score"] is not None:
                    individual_scores.append(output["map_score"])
            
            # Set overall score based on our selected individual metrics
            if individual_scores:
                output["overall_score"] = sum(individual_scores) / len(individual_scores)
            else:
                output["overall_score"] = retrieval_score  # Fallback to retrieval_score if no individual metrics
                
        elif isinstance(result_data, float):
            # Legacy single score format
            output["retrieval_score"] = result_data
            output["overall_score"] = result_data
        else:
            error_message = f"Retrieval test returned unexpected type: {type(result_data)}"
        
        if error_message:
            output["error"] = error_message
            self.logger.error(f"Error in convert_retrieval_result: {error_message}")

        return output
    
    def aggregate_retrieval_results(self, task_results: List[TaskResult], model_name: str) -> EvaluationResults:
        """Aggregate multiple retrieval test case results into one EvaluationResults."""
        
        if not task_results:
            return EvaluationResults(
                task_id="retrieval",
                model_id=model_name,
                test_case_count=0,
                error="No test cases processed for this task"
            )
        
        # Collect all scores
        retrieval_scores = []
        recall_at_10_scores = []
        ndcg_at_10_scores = []
        map_scores = []
        tps_scores = []
        overall_scores = []
        execution_times = []
        errors = []
        
        for result in task_results:
            if result.error:
                errors.append(result.error)
                continue
                
            if result.retrieval_score is not None:
                retrieval_scores.append(result.retrieval_score)
                
            # Collect individual retrieval metrics
            if result.recall_at_10 is not None:
                recall_at_10_scores.append(result.recall_at_10)
            if result.ndcg_at_10 is not None:
                ndcg_at_10_scores.append(result.ndcg_at_10)
            if result.map_score is not None:
                map_scores.append(result.map_score)
                
            # Collect TPS metrics - collect ALL individual TPS values from all test cases
            if hasattr(result, 'tps') and result.tps is not None:
                if isinstance(result.tps, list):
                    # New format: list of individual TPS values from this test case
                    tps_scores.extend(result.tps)
                else:
                    # Legacy format: single average TPS value for this test case
                    tps_scores.append(result.tps)
                
            if result.overall_score is not None:
                overall_scores.append(result.overall_score)
            if result.execution_time is not None:
                execution_times.append(result.execution_time)
        
        # Calculate aggregated scores (using mean)
        def safe_mean(scores):
            return sum(scores) / len(scores) if scores else None
        
        # Calculate overall execution time (sum of all test cases)
        total_execution_time = sum(execution_times) if execution_times else None
        
        # Handle errors
        error_message = None
        if errors:
            if len(errors) == len(task_results):
                error_message = f"All {len(task_results)} test cases failed"
            else:
                error_message = f"{len(errors)} out of {len(task_results)} test cases failed"
        
        logger.info(f"Aggregated retrieval results: {len(task_results)} test cases processed, "
                   f"Overall score: {safe_mean(overall_scores)}, Errors: {len(errors)}")
        
        return EvaluationResults(
            task_id="retrieval",
            model_id=model_name,
            retrieval_score=safe_mean(retrieval_scores),
            
            # Individual retrieval metrics
            recall_at_10=safe_mean(recall_at_10_scores),
            ndcg_at_10=safe_mean(ndcg_at_10_scores),
            map_score=safe_mean(map_scores),
            
            # TPS (Tokens Per Second) metrics
            average_tps=safe_mean(tps_scores),
            prediction_count=len(tps_scores),
            
            overall_score=safe_mean(overall_scores),
            execution_time=total_execution_time,
            test_case_count=len(task_results),
            error=error_message
        ) 