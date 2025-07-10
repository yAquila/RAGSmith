"""Prediction Generation Service"""

import asyncio
import logging
import time
from typing import Dict, List, Optional, Any
import pandas as pd
from models import BenchmarkConfigModel, TestInputModel
from retrieval_tests import RetrievalTest

logger = logging.getLogger(__name__)


class RetrPredictionService:
    """Service for handling prediction generation"""
    
    def __init__(self, vectorstore_service):
        self.vectorstore_service = vectorstore_service
        self.logger = logging.getLogger(__name__)
    
    async def generate_all_predictions(
        self, 
        config, 
        task_dataset, 
        task_test_count: int, 
        run_id: str = "temp_run_id"
    ) -> list:
        """Generate predictions for all models and tasks (Phase 1)"""
        all_predictions = []
        
        # Get embedding models to use for retrieval comparison
        embedding_models_to_use = []
        if config.embedding_model_names:
            embedding_models_to_use = config.embedding_model_names
        elif config.embedding_model_name:
            embedding_models_to_use = [config.embedding_model_name]
        
        if not embedding_models_to_use:
            logger.error("No embedding models specified for retrieval tasks")
            return all_predictions
        
        # Process each embedding model separately for retrieval comparison
        for emb_idx, embedding_model in enumerate(embedding_models_to_use):
            # Create config for this specific embedding model
            model_config = BenchmarkConfigModel(
                task="retrieval",
                embedding_model_name=embedding_model,
                vectorstore="qdrant",
                retrieval_k=10,
                retrieval_threshold=0.5
            )
            
            # Generate "predictions" for retrieval tasks (which are actually retrieval results)
            model_predictions = await self.generate_model_predictions(
                embedding_model, model_config, task_dataset, task_test_count, run_id, 
                emb_idx, len(embedding_models_to_use)
            )
            
            all_predictions.extend(model_predictions)
        
        return all_predictions
        
    
    async def generate_model_predictions(
        self,
        model_name: str,
        model_config,
        task_dataset,
        task_test_count: int,
        run_id: str,
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
                # Get vectorstore for this specific embedding model
                vectorstore = self.vectorstore_service.get_or_create_vectorstore(model_name)
                
                # Debug: Log collection information
                if vectorstore:
                    collection_info = vectorstore.get_collection_info()
                    logger.info(f"Using vectorstore for {model_name}: Collection={vectorstore.collection_name}, Points={collection_info.get('points_count', 0)}")
                else:
                    logger.error(f"Failed to get vectorstore for {model_name}")
                    return model_predictions
                
                # Process each test case for this task
                for j, (_, row) in enumerate(task_dataset.iterrows()):
                    task_data = row.to_dict()
                    
                    # Generate prediction only (no evaluation yet)
                    prediction_data = await self.generate_single_prediction(
                        model_name, model_config, task_data, vectorstore, run_id
                    )
                    
                    # Debug: Log first few characters of prediction results
                    if prediction_data and prediction_data.get('prediction'):
                        prediction_sample = prediction_data['prediction'][:3] if prediction_data['prediction'] else []
                        logger.info(f"Generated prediction for {model_name}, query='{task_data.get('user_prompt', '')[:50]}...', first_3_results={len(prediction_sample) if isinstance(prediction_sample, list) else 'not_list'}")
                    
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
        
        logger.info(f"Generated {len(model_predictions)} predictions for embedding model {model_name}")
        return model_predictions
    
    async def generate_single_prediction(
        self,
        model_name: str,
        model_config,
        task_data: dict,
        vectorstore,
        run_id: str
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
            
            task_input_args = {
                "task": model_config.task,
                "user_prompt": task_data.get("user_prompt", ""),
                "ground_truth": task_data.get("ground_truth"),
                "additional_args": additional_args
            }
            
            test_input = TestInputModel(**task_input_args)
            
            # Convert to modular config for this task
            modular_config = model_config
            
            test_instance = RetrievalTest(config=model_config, vectorstore=vectorstore)
             
            prediction = test_instance._get_prediction(test_input)
            
            # Store all data needed for later evaluation
            prediction_data = {
                'model_name': model_name,
                'task_type': model_config.task,
                'task_data': task_data,
                'test_input': test_input,
                'modular_config': modular_config,
                'api_config': model_config,
                'prediction': prediction,
                'dataset_name': run_id,
                'error': None
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