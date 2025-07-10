"""Dataset Management Service"""

import os
import logging
import traceback
import pandas as pd
from typing import Union, List, Dict, Optional, Any
import json

from models import DatasetValidationResult

logger = logging.getLogger(__name__)


class DatasetService:
    """Service for handling dataset operations"""
    
    def __init__(self, uploaded_files_ref=None):
        self.logger = logging.getLogger(__name__)
        self._uploaded_files = uploaded_files_ref
        self._retrieval_docs_file_path = None
    
    def set_uploaded_files_reference(self, uploaded_files_dict: Dict[str, Any]):
        """Set reference to uploaded files dictionary from main module"""
        self._uploaded_files = uploaded_files_dict
    
    def validate_dataset(self, data: Union[List[Dict], pd.DataFrame], available_tasks: List[Dict] = None) -> DatasetValidationResult:
        """Validate a custom dataset DataFrame or list of dictionaries"""
        try:
            # Convert to DataFrame if it's a list
            if isinstance(data, list):
                df = pd.DataFrame(data)
            else:
                df = data
                
            required_base_fields = ["task", "user_prompt"]
            optional_fields = ["context", "ground_truth", "tests", "additional_args"]
            
            # Check required fields
            missing_fields = [field for field in required_base_fields if field not in df.columns]
            
            # Check for extra fields (not necessarily bad, but worth noting)
            expected_fields = set(required_base_fields + optional_fields)
            extra_fields = [field for field in df.columns if field not in expected_fields]
            
            warnings = []
            
            # Check task types if available_tasks is provided
            if available_tasks and "task" in df.columns:
                valid_tasks = [task["id"] for task in available_tasks]
                invalid_tasks = df[~df["task"].isin(valid_tasks)]["task"].unique()
                if len(invalid_tasks) > 0:
                    warnings.append(f"Unknown task types found: {list(invalid_tasks)}")
            
            # Check for empty required fields
            for field in required_base_fields:
                if field in df.columns and df[field].isna().any():
                    warnings.append(f"Missing values found in required field '{field}'")
            
            is_valid = len(missing_fields) == 0
            message = f"Dataset validation {'passed' if is_valid else 'failed'}"
            
            return DatasetValidationResult(
                isValid=is_valid,
                missingFields=missing_fields,
                extraFields=extra_fields,
                rowCount=len(df),
                message=message,
                warnings=warnings
            )
            
        except Exception as e:
            logger.error(f"Failed to validate dataset: {str(e)}")
            return DatasetValidationResult(
                isValid=False,
                missingFields=[],
                extraFields=[],
                rowCount=0,
                message=f"Dataset validation failed: {str(e)}"
            )
    
    def get_default_dataset_path(self, task_type: str) -> str:
        """Get the path to the default dataset CSV file for a given task type"""
        # Special mapping for retrieval task
        if task_type == "retrieval":
            csv_filename = "retrieval_withgen.csv"
            
        # Construct the full path to the CSV file
        default_datasets_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "default_datasets")
        csv_path = os.path.join(default_datasets_dir, csv_filename)
        
        if not os.path.exists(csv_path):
            csv_path = os.path.join(default_datasets_dir, task_type + ".csv")
            if not os.path.exists(csv_path):
                raise ValueError(f"Default dataset file not found: {csv_path}")
        
        return csv_path

    def load_dataset(self, config, task_id: Optional[str] = None) -> pd.DataFrame:
        """Load dataset based on per-task configuration only"""
        task_type = config.task
        
        retrieval_docs_file_id = None
        retrieval_queries_file_id = None
        if hasattr(config, 'retrieval_docs_file_id') and config.retrieval_docs_file_id:
            retrieval_docs_file_id = config.retrieval_docs_file_id
        if hasattr(config, 'retrieval_queries_file_id') and config.retrieval_queries_file_id:
            retrieval_queries_file_id = config.retrieval_queries_file_id
        
        sample_count = getattr(config, 'sample_count', None)
        
        # Handle retrieval task dual file upload
        if task_type == "retrieval":
            return self.load_retrieval_dataset(retrieval_docs_file_id, retrieval_queries_file_id, sample_count)
        return None

    def load_retrieval_dataset(self, docs_file_id: Optional[str], queries_file_id: Optional[str], sample_count: Optional[int] = None) -> pd.DataFrame:
        """Load retrieval dataset from dual files (documents and queries)"""
        try:
            # For retrieval tasks, we need the queries file for evaluation
            # The documents file is used for vectorstore indexing
            
            if not queries_file_id:
                # If no queries file provided, use default
                logger.info("No retrieval queries file provided, using default queries")
                default_queries_path = self.get_default_dataset_path("retrieval")
                dataset = pd.read_csv(
                    default_queries_path, 
                    quotechar='"',
                    escapechar=None,
                    skipinitialspace=True,
                    na_filter=False,
                    keep_default_na=False,
                    encoding='utf-8',
                )
                logger.info(f"Loaded default retrieval queries: {len(dataset)} queries")
            else:
                # Load uploaded queries file
                if queries_file_id not in self._uploaded_files:
                    raise ValueError(f"Queries file ID '{queries_file_id}' not found or expired")
                
                queries_file_info = self._uploaded_files[queries_file_id]
                queries_file_path = queries_file_info["file_path"]
                
                if not os.path.exists(queries_file_path):
                    raise ValueError(f"Queries file no longer exists: {queries_file_path}")
                
                dataset = pd.read_csv(
                    queries_file_path,
                    quotechar='"',
                    escapechar=None,
                    skipinitialspace=True,
                    na_filter=False,
                    keep_default_na=False,
                    encoding='utf-8',
                )
                logger.info(f"Loaded uploaded retrieval queries: {len(dataset)} queries")
            
            # Store the documents file ID for vectorstore indexing
            if docs_file_id:
                if docs_file_id not in self._uploaded_files:
                    logger.warning(f"Documents file ID '{docs_file_id}' not found, will use default documents")
                else:
                    # Store the docs file path for later vectorstore indexing
                    docs_file_info = self._uploaded_files[docs_file_id]
                    docs_file_path = docs_file_info["file_path"]
                    if os.path.exists(docs_file_path):
                        # Store this information for vectorstore creation
                        self._retrieval_docs_file_path = docs_file_path
                        logger.info(f"Using uploaded documents file for vectorstore: {docs_file_path}")
                    else:
                        logger.warning(f"Documents file no longer exists: {docs_file_path}")
            
            # Apply sample count limitation if specified
            if sample_count is not None and sample_count > 0:
                original_count = len(dataset)
                if sample_count < original_count:
                    dataset = dataset.head(sample_count)
                    logger.info(f"Limited retrieval queries to {sample_count} samples")
            
            return dataset
            
        except Exception as e:
            logger.error(f"Failed to load retrieval dataset: {str(e)}")
            logger.error(traceback.format_exc())
            # Fall back to default retrieval data
            logger.warning("Falling back to default retrieval sample data")
            return self.create_fallback_sample_data("retrieval")

    def create_fallback_sample_data(self, task_type: str) -> pd.DataFrame:
        """Create minimal fallback sample data for a task type"""
        
        return pd.DataFrame([{
            "task": task_type,
            "user_prompt": "Sample prompt",
            "ground_truth": "Sample response"
        }])
    

    async def prepare_dataset(self, config, vectorstore_service) -> tuple:
        """Prepare dataset for a single model"""

        vectorstore = None
        embedding_models_to_prepare = []
            
        # Use embedding_model_names for retrieval mode comparison, or embedding_model_name for LLM mode
        if hasattr(config, 'embedding_model_names') and config.embedding_model_names:
            embedding_models_to_prepare = config.embedding_model_names
        elif hasattr(config, 'embedding_model_name') and config.embedding_model_name:
            embedding_models_to_prepare = [config.embedding_model_name]
        
        if embedding_models_to_prepare:
            # Pre-create vectorstores for all embedding models to ensure they're ready
            for embedding_model in embedding_models_to_prepare:
                try:
                    vectorstore = vectorstore_service.get_or_create_vectorstore(embedding_model)
                    logger.info(f"Prepared vectorstore for embedding model: {embedding_model}")
                except Exception as e:
                    logger.error(f"Failed to prepare vectorstore for {embedding_model}: {e}")
        else:
            logger.warning("No embedding model specified for retrieval task")
        
        task_dataset = self.load_dataset(config, config.task)
        task_test_count = len(task_dataset) if task_dataset is not None else 0
        return task_dataset, task_test_count, vectorstore

    def get_retrieval_docs_file_path(self) -> Optional[str]:
        """Get the retrieval documents file path"""
        return getattr(self, '_retrieval_docs_file_path', None) 