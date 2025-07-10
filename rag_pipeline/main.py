import time
import logging
import asyncio
from fastapi import File, Form, UploadFile
from typing import Optional
from services.file_service import FileService
from models import BenchmarkConfigModel, TestInputModel
from datetime import datetime, timedelta, timezone
from services.vectorstore_service import VectorstoreService
from services.dataset_service import DatasetService
from services.gen_prediction_service import GenPredictionService
from services.retr_prediction_service import RetrPredictionService
from services.gen_evaluation_service import GenEvaluationService
from services.retr_evaluation_service import RetrEvaluationService

logger = logging.getLogger(__name__)
GMT_PLUS_3 = timezone(timedelta(hours=3))


logging.basicConfig(level=logging.INFO)


# file_service = FileService()


# async def upload_retrieval_dataset(
#     docs_file: Optional[UploadFile] = File(None),
#     queries_file: Optional[UploadFile] = File(None),
#     file_type: str = Form(...)  # "documents" or "queries"
# ):
#     """Upload retrieval dataset files (documents or queries)"""
#     try:
#         if file_type not in ["documents", "queries"]:
#             raise Exception(f"file_type must be 'documents' or 'queries'")
        
#         # Determine which file to process
#         file_to_process = docs_file if file_type == "documents" else queries_file
        
#         if not file_to_process:
#             raise Exception(f"No {file_type} file provided")
        
#         logger.info(f"Retrieval {file_type} upload started: filename='{file_to_process.filename}', size={file_to_process.size} bytes")
        
#         # Validate file upload
#         #TODO file_service.validate_file_upload(file_to_process)
#         #logger.info(f"File upload validation passed for retrieval {file_type}: {file_to_process.filename}")
        
#         # Read and validate CSV content based on file type
#         content = await file_to_process.read()
#         logger.info(f"Read {len(content)} bytes from uploaded retrieval {file_type} file")
        
#         await file_to_process.seek(0)  # Reset file pointer for saving
        
#         # Validate CSV structure based on file type
#         #TODO validation_result = await validation_service.validate_retrieval_csv_structure(content, file_type)
#         #logger.info(f"Retrieval {file_type} CSV validation completed: valid={validation_result.isValid}")
        
#         # Save the file regardless of validation result 
#         file_id = await file_service.save_uploaded_file(file_to_process)
#         logger.info(f"Retrieval {file_type} file saved successfully with ID: {file_id}")
        
#         # Store file type information
#         file_service.add_file_metadata(file_id, {"file_type": f"retrieval_{file_type}"})
        
#         logger.info(f"Retrieval {file_type} upload completed successfully: file_id={file_id}")
#         return file_id
        
#     except Exception as e:
#         logger.error(f"Unexpected error during retrieval {file_type} upload: {str(e)}", exc_info=True)
#         raise Exception(f"Upload failed: {str(e)}")

async def execute_benchmark(config, run_id):
    
    
    vectorstore_service = VectorstoreService()
    dataset_service = DatasetService()

    preparation_start_time = datetime.now(GMT_PLUS_3)
    task_dataset, task_test_count, _ = await dataset_service.prepare_dataset(
        config, vectorstore_service
    )
        
    gen_prediction_service = GenPredictionService()
    retr_prediction_service = RetrPredictionService(vectorstore_service)
    retr_evaluation_service = RetrEvaluationService(vectorstore_service)
    gen_evaluation_service = GenEvaluationService()
    
    preparation_end_time = datetime.now(GMT_PLUS_3)
    preparation_time = (preparation_end_time - preparation_start_time).total_seconds()
    
    # Phase 2: Model Prediction - Generate predictions for all models
    prediction_start_time = datetime.now(GMT_PLUS_3)

    all_predictions = await retr_prediction_service.generate_all_predictions(
        config, task_dataset, task_test_count, run_id
    )
    
    # Debug: Log retrieval predictions summary
    predictions_by_model = {}
    for pred in all_predictions:
        model_name = pred.get('model_name', 'unknown')
        if model_name not in predictions_by_model:
            predictions_by_model[model_name] = []
        predictions_by_model[model_name].append(pred)
    
    logger.info("=== RETRIEVAL PREDICTIONS SUMMARY ===")
    for model_name, preds in predictions_by_model.items():
        logger.info(f"Model {model_name}: {len(preds)} predictions")
        if preds and preds[0].get('prediction'):
            first_pred = preds[0]['prediction']
            if isinstance(first_pred, list) and len(first_pred) > 0:
                first_doc = first_pred[0]
                if isinstance(first_doc, dict) and 'page_content' in first_doc:
                    sample_content = first_doc['page_content'][:100] + "..." if len(first_doc['page_content']) > 100 else first_doc['page_content']
                    logger.info(f"  Sample content: '{sample_content}'")
                    logger.info(f"  Doc ID: {first_doc.get('doc_id', 'N/A')}")
    logger.info("=====================================")
    
    gen_config = BenchmarkConfigModel(task="retrieval", llm_model_name="llama3.2:1b", eval_llm_model_name="gemma3:4b", vectorstore="qdrant", retrieval_k=10, retrieval_threshold=0.5)
    all_predictions_gen = await gen_prediction_service.generate_all_predictions(
        gen_config, task_dataset, task_test_count, all_predictions, run_id
    )
    logger.info(f"All predictions: {all_predictions[0]}")
    logger.info(f"All predictions gen: {all_predictions_gen[0]}")
    prediction_end_time = datetime.now(GMT_PLUS_3)
    prediction_time = (prediction_end_time - prediction_start_time).total_seconds()
    
    # Phase 3: Model Evaluation - Run evaluations
    evaluation_start_time = datetime.now(GMT_PLUS_3)
    all_results = await retr_evaluation_service.evaluate_all_predictions(
        config, all_predictions
    )
    all_results_gen = await gen_evaluation_service.evaluate_all_predictions(
        config, all_predictions_gen
    )
    logger.info(f"All results: {all_results}")
    logger.info(f"All results gen: {all_results_gen}")
    evaluation_end_time = datetime.now(GMT_PLUS_3)
    evaluation_time = (evaluation_end_time - evaluation_start_time).total_seconds()
    
    return {
        "preparation_time": preparation_time,
        "prediction_time": prediction_time,
        "evaluation_time": evaluation_time
    }

async def run_benchmark():
    """Async wrapper function to run the benchmark"""
    config = BenchmarkConfigModel(task="retrieval", llm_model_name="llama3.2:1b", eval_llm_model_name="gemma3:4b", eval_embedding_model_name="mxbai-embed-large", embedding_model_names=["nomic-embed-text", "mxbai-embed-large"], vectorstore="qdrant", retrieval_k=10, retrieval_threshold=0.5)

    result = await execute_benchmark(config, "1")
    logging.info(f"Benchmark result: {result}")
    return result

if __name__ == "__main__":
    logging.info("RAG pipeline started.")
    while True:
        logging.info("RAG pipeline is running...")
        try:
            # Run the async benchmark using asyncio.run()
            asyncio.run(run_benchmark())
        except Exception as e:
            logging.error(f"Error running benchmark: {e}")
            import traceback
            logging.error(traceback.format_exc())
        
        time.sleep(600)
        
        # upload_retrieval_dataset(docs_file=File(...),file_type="documents")
        # upload_retrieval_dataset(queries_file=File(...), file_type="queries")


#0.6873
#0.7675