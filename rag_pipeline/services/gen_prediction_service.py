"""Prediction Generation Service"""

import asyncio
import logging
import time
from typing import Dict, List, Optional, Any
import pandas as pd
from models import BenchmarkConfigModel, TestInputModel
from generation_tests import GenerationTest

logger = logging.getLogger(__name__)


class GenPredictionService:
    """Service for handling prediction generation"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    async def generate_all_predictions(
        self, 
        config, 
        task_dataset, 
        task_test_count: int, 
        retrieval_predictions: list,
        run_id: str = "temp_run_id"
    ) -> list:
        """Generate predictions for all models and tasks (Phase 1)"""
        all_predictions = []
        
        # Get LLM models to use for generation
        llm_models_to_use = []
        if config.llm_model_names:
            llm_models_to_use = config.llm_model_names
        elif config.llm_model_name:
            llm_models_to_use = [config.llm_model_name]
        
        if not llm_models_to_use:
            logger.error("No LLM models specified for generation tasks")
            return all_predictions
        
        # Get embedding models from retrieval predictions
        embedding_models_used = set()
        for prediction in retrieval_predictions:
            if prediction.get('model_name'):
                embedding_models_used.add(prediction['model_name'])
        
        embedding_models_list = list(embedding_models_used)
        
        if not embedding_models_list:
            logger.error("No embedding models found in retrieval predictions")
            return all_predictions
        
        logger.info(f"Processing {len(llm_models_to_use)} LLM models with {len(embedding_models_list)} embedding models")
        
        # Process each combination of embedding model and LLM model
        for emb_idx, embedding_model in enumerate(embedding_models_list):
            for llm_idx, llm_model in enumerate(llm_models_to_use):
                # Create config for this specific model combination
                model_config = BenchmarkConfigModel(
                    task="generation",  # Changed from "retrieval" to "generation"
                    llm_model_name=llm_model,
                    embedding_model_name=embedding_model,
                    vectorstore="qdrant",
                    retrieval_k=10,
                    retrieval_threshold=0.5
                )
                
                # Generate predictions for this model combination
                model_predictions = await self.generate_model_predictions(
                    llm_model, 
                    model_config, 
                    task_dataset, 
                    task_test_count, 
                    run_id, 
                    retrieval_predictions,
                    embedding_model,
                    config.eval_llm_model_name,
                    llm_idx + emb_idx * len(llm_models_to_use), 
                    len(llm_models_to_use) * len(embedding_models_list)
                )
                
                all_predictions.extend(model_predictions)
        
        return all_predictions
        
    
    async def generate_model_predictions(
        self,
        llm_model_name: str,
        model_config,
        task_dataset,
        task_test_count: int,
        run_id: str,
        retrieval_predictions: list,
        embedding_model_name: str,
        eval_llm_model_name: str,
        model_idx: int = 0,
        total_models: int = 1
    ) -> list:
        """Generate predictions for a single model across all tasks"""
        model_predictions = []
        
        try:
            if task_dataset is None:
                # Dataset loading failed for this task, create error prediction
                error_prediction = {
                    'model_name': model_name,
                    'task_type': model_config.task,
                    'error': f"Failed to load dataset for task {model_config.task}",
                    'prediction_data': None
                }
                model_predictions.append(error_prediction)

            if len(task_dataset) > 0:
                # Process each test case for this task
                for j, (_, row) in enumerate(task_dataset.iterrows()):
                    task_data = row.to_dict()
                    
                    # Generate prediction only (no evaluation yet)
                    prediction_data = await self.generate_single_prediction(
                        llm_model_name, model_config, task_data, run_id, retrieval_predictions, embedding_model_name, eval_llm_model_name
                    )
                    
                    model_predictions.append(prediction_data)
            else:
                # Create a default task_data if no matching rows found
                logger.error(f"No matching rows found for task {model_config.task} with model {model_name}")
                
        except Exception as e:
            logger.error(f"Failed to generate predictions for task {model_config.task} with model {model_name}: {str(e)}")
            error_prediction = {
                'model_name': model_name,
                'task_type': model_config.task,
                'error': str(e),
                'prediction_data': None
            }
            model_predictions.append(error_prediction)
        
        return model_predictions
    
    async def generate_single_prediction(
        self,
        llm_model_name: str,
        model_config,
        task_data: dict,
        run_id: str,
        retrieval_predictions: list,
        embedding_model_name: str,
        eval_llm_model_name: str
    ) -> dict:
        """Generate a single prediction without evaluation"""
        try:
            # Parse additional_args if it's a JSON string
            additional_args = task_data.get("additional_args")
            if additional_args and isinstance(additional_args, str):
                try:
                    import json
                    additional_args = json.loads(additional_args)
                except (json.JSONDecodeError, ValueError) as e:
                    self.logger.warning(f"Failed to parse additional_args as JSON: {additional_args}, error: {e}")
                    additional_args = None
            
            # Extract page_contents from retrieval predictions for this specific query/task
            context_documents = []
            user_prompt = task_data.get("user_prompt", "")
            
            # Debug: Log which embedding model we're looking for
            logger.info(f"Looking for retrieval predictions from embedding model: {embedding_model_name} for query: '{user_prompt[:50]}...'")
            
            # Find matching retrieval predictions for this embedding model and query
            matching_predictions = []
            for prediction in retrieval_predictions:
                pred_model = prediction.get('model_name')
                pred_prompt = prediction.get('task_data', {}).get('user_prompt')
                if pred_model == embedding_model_name and pred_prompt == user_prompt:
                    matching_predictions.append(prediction)
                    
            logger.info(f"Found {len(matching_predictions)} matching retrieval predictions for {embedding_model_name}")
            
            for prediction in matching_predictions:
                # Extract page_content from the prediction
                prediction_result = prediction.get('prediction')
                if prediction_result and isinstance(prediction_result, list):
                    for result in prediction_result:
                        if isinstance(result, dict) and 'page_content' in result:
                            context_documents.append(result['page_content'])
                            # Debug: Log first 100 chars of each document
                            logger.debug(f"Added context doc from {embedding_model_name}: '{result['page_content'][:100]}...'")
            
            # Create context string from documents
            context_string = "\n\n".join(context_documents) if context_documents else ""
            
            logger.info(f"Generated {len(context_documents)} context documents for {llm_model_name} with {embedding_model_name} (total chars: {len(context_string)})")
            
            task_input_args = {
                "task": model_config.task,
                "user_prompt": user_prompt,
                "ground_truth": task_data.get("ground_truth"),
                "additional_args": additional_args,
                "docs": context_documents  # Pass the retrieved documents as docs
            }
            
            test_input = TestInputModel(**task_input_args)
            
            # Convert to modular config for this task
            modular_config = model_config
            
            test_instance = GenerationTest(config=model_config, embedding_model_name=embedding_model_name, llm_model_name=llm_model_name)

            start_time = time.time()
            prediction = test_instance._get_prediction(test_input)
            end_time = time.time()
            execution_time = end_time - start_time
            logger.info(f"Execution time: {execution_time}")
            
            logger.info(f"MyPrediction: {prediction}")

            # Store all data needed for later evaluation
            prediction_data = {
                'model_name': llm_model_name,
                'task_type': model_config.task,
                'task_data': task_data,
                'test_input': test_input,
                'modular_config': modular_config,
                'api_config': model_config,
                'prediction': prediction,
                'dataset_name': run_id,
                'context_documents': context_documents,  # Store the context for reference
                'error': None,
                'execution_time': execution_time
            }
            
            return prediction_data
            
        except Exception as e:
            logger.error(f"Failed to generate prediction for {model_config.task} with {model_name}: {str(e)}")
            return {
                'model_name': model_name,
                'task_type': model_config.task,
                'task_data': task_data,
                'error': str(e),
                'prediction_data': None
            } 