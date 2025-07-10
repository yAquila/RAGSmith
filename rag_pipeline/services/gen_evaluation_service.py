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


class GenEvaluationService:
    """Service for handling retrieval task evaluation processing"""
    
    def __init__(self):
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
                    task_id="generation",
                    model_id=prediction['model_name'],
                    error=prediction['error']
                )
                all_results.append(error_result)
                continue
                
            model_name = prediction['model_name']
            task_type = prediction['task_type']
                
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
                    task_id="generation",
                    model_id=model_name,
                    error=str(e)
                )
                all_results.append(error_result)
        
        return all_results
    
    async def evaluate_retrieval_predictions(self, predictions: list, config, model_name) -> list:
        """Evaluate retrieval predictions"""
        task_results = []
        for prediction in predictions:
            try:
                # Extract prediction data
                test_input = prediction['test_input']
                task_type = prediction['task_type']
                prediction_text = prediction['prediction']
                execution_time_ms = prediction['execution_time']
                # Set the prediction in test_input for evaluation
                test_input.prediction = prediction_text
                
                # Create retrieval test instance directly
                from generation_tests import GenerationTest
                test_instance = GenerationTest(config=config, embedding_model_name=config.eval_embedding_model_name, llm_model_name=model_name)
                
                eval_result_data = test_instance._evaluate_prediction(test_input)
                
                # Convert retrieval evaluation results
                converted_result = self.convert_generation_result(eval_result_data)
                
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
                    score=converted_result.get("score"),
                    
                    # Individual retrieval metrics
                    llm_score=converted_result.get("llm_score"),
                    semantic_score=converted_result.get("semantic_score"),
                    
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
    
    def convert_generation_result(self, result_data) -> Dict[str, Any]:
        """Convert retrieval test results to standardized format"""
        output = {}
        error_message = None
        
        if result_data is None:
            error_message = "Retrieval evaluation failed to produce a result."
        elif isinstance(result_data, dict):
            # Handle comprehensive retrieval metrics
            score = result_data.get('score', 0.0)
            metrics = result_data.get('metrics', {})
            
            output["score"] = score
            output["metrics"] = metrics
            
            # Extract individual metrics for detailed reporting
            individual_scores = []
            if metrics:
                output["llm_score"] = metrics.get('llm_score', None)
                output["semantic_score"] = metrics.get('semantic_score', None)

                # Calculate overall score as average of the individual metrics we care about
                if output["llm_score"] is not None:
                    individual_scores.append(output["llm_score"])
                if output["semantic_score"] is not None:
                    individual_scores.append(output["semantic_score"])
            
            # Set overall score based on our selected individual metrics
            if individual_scores:
                output["overall_score"] = sum(individual_scores) / len(individual_scores)
            else:
                output["overall_score"] = score  # Fallback to retrieval_score if no individual metrics
                
        elif isinstance(result_data, float):
            # Legacy single score format
            output["score"] = result_data
            output["overall_score"] = result_data
        else:
            error_message = f"Generation test returned unexpected type: {type(result_data)}"
        
        if error_message:
            output["error"] = error_message
            self.logger.error(f"Error in convert_generation_result: {error_message}")

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
        scores = []
        llm_scores = []
        semantic_scores = []
        tps_scores = []
        overall_scores = []
        execution_times = []
        errors = []
        
        for result in task_results:
            if result.error:
                errors.append(result.error)
                continue
                
            if result.score is not None:
                scores.append(result.score)
                
            # Collect individual retrieval metrics
            if result.llm_score is not None:
                llm_scores.append(result.llm_score)
            if result.semantic_score is not None:
                semantic_scores.append(result.semantic_score)
                
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
            score=safe_mean(scores),
            
            # Individual retrieval metrics
            llm_score=safe_mean(llm_scores),
            semantic_score=safe_mean(semantic_scores),
            
            # TPS (Tokens Per Second) metrics
            average_tps=safe_mean(tps_scores),
            prediction_count=len(tps_scores),
            
            overall_score=safe_mean(overall_scores),
            execution_time=total_execution_time,
            test_case_count=len(task_results),
            error=error_message
        ) 