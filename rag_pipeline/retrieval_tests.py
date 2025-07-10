"""
Retrieval-based benchmark tests.

This module contains test implementations for retrieval tasks with comprehensive
metrics including precision, recall, and other IR evaluation measures.
"""

import logging
from typing import Dict, Any, List, Optional, Union

from models import BenchmarkConfigModel, TestInputModel as TestInput

logger = logging.getLogger(__name__)


class RetrievalTest():
    """Test class for retrieval tasks with comprehensive metrics."""
    
    def __init__(self, config: BenchmarkConfigModel, vectorstore):
        self.config = config
        if not vectorstore:
            raise ValueError("Vectorstore is required for retrieval tests")
        self.vectorstore = vectorstore
        self.logger = logging.getLogger(self.__class__.__name__)

    def _generate_prompt(self, test_input: TestInput) -> str:
        """Generate prompt for retrieval tasks - use the query directly."""
        return test_input.user_prompt
    
    def _get_prediction(self, test_input: TestInput) -> Optional[List]:
        """Get top-k retrieval results."""
        try:
            query = self._generate_prompt(test_input)
            k = test_input.additional_args.get('k', 10) if test_input.additional_args else 10
            
            # Debug: Log which embedding model is being used
            logger.info(f"RetrievalTest using vectorstore with embedding model: {self.vectorstore.embedding_model}, collection: {self.vectorstore.collection_name}")
            
            results = self.vectorstore.similarity_search(query, k)
            logger.debug(f"Retrieved {len(results)} results")
            return results
        except Exception as e:
            logger.error(f"Retrieval failed: {str(e)}")
            return None
    
    def _evaluate_prediction(self, test_input: TestInput) -> Dict[str, Any]:
        """Evaluate retrieval results using comprehensive metrics."""
        if not test_input.prediction:
            raise ValueError("Prediction is required for evaluation")
        
        if not test_input.additional_args or 'true_qrel_list' not in test_input.additional_args:
            raise ValueError("true_qrel_list is required in additional_args for retrieval evaluation")
        
        results = test_input.prediction
        true_qrel_list = test_input.additional_args['true_qrel_list']
        
        # Extract retrieved document IDs
        retrieved_doc_ids = self._extract_document_ids(results)
        
        # Convert true_qrel_list to strings for comparison
        true_qrel_list_str = [str(doc_id) for doc_id in true_qrel_list]
        
        logger.debug(f"Evaluating {len(retrieved_doc_ids)} retrieved results against {len(true_qrel_list_str)} ground truth documents")
        
        # Calculate comprehensive metrics
        metrics = self._calculate_retrieval_metrics(retrieved_doc_ids, true_qrel_list_str)
        
        # Add additional info
        metrics.update({
            'num_retrieved': len(retrieved_doc_ids),
            'num_relevant': len(true_qrel_list_str),
            'retrieved_docs': retrieved_doc_ids,
            'relevant_docs': true_qrel_list_str
        })
        
        # Return the main recall@5 score for compatibility
        main_score = metrics.get('recall@5', 0.0)
        
        return {
            'retrieval_score': main_score,
            'retrieval_metrics': metrics,
            'overall_score': main_score
        }

    def _extract_document_ids(self, results: List) -> List[str]:
        """Extract document IDs from retrieval results."""
        retrieved_doc_ids = []
        for result in results:
            doc_id = None
            
            if isinstance(result, dict):
                # Try direct doc_id field first
                doc_id = result.get('doc_id')
                
                # Try metadata.doc_id if direct access failed
                if not doc_id and 'metadata' in result and isinstance(result['metadata'], dict):
                    doc_id = result['metadata'].get('doc_id')
                    
            elif hasattr(result, 'metadata') and hasattr(result.metadata, 'get'):
                doc_id = result.metadata.get('doc_id')
            
            if doc_id:
                retrieved_doc_ids.append(str(doc_id))
            else:
                logger.warning(f"Could not extract doc_id from result: {type(result)}")
        
        return retrieved_doc_ids

    def _calculate_retrieval_metrics(self, retrieved_doc_ids: List[str], true_qrel_list_str: List[str]) -> Dict[str, Any]:
        """Calculate comprehensive retrieval metrics."""
        try:
            # Import RetrievalMetrics
            from util.vectorstore.metrics import RetrievalMetrics
            
            # Calculate comprehensive metrics
            k_values = [1, 3, 5, 10]
            metrics = RetrievalMetrics.calculate_all_metrics(retrieved_doc_ids, true_qrel_list_str, k_values)
            
            # Log summary metrics
            logger.debug(f"Recall@5: {metrics.get('recall@5', 0.0):.4f}")
            logger.debug(f"Precision@5: {metrics.get('precision@5', 0.0):.4f}")
            
            return metrics
        except Exception as e:
            logger.error(f"Failed to calculate retrieval metrics: {str(e)}")
            return {'recall@5': 0.0, 'precision@5': 0.0} 

    
    def run_pipeline(self, test_input: TestInput) -> Optional[Union[Dict[str, Any], float, int]]:
        """
        Run the complete benchmark pipeline.
        
        Args:
            test_input: TestInput object containing all necessary information
            
        Returns:
            Evaluation results or None if prediction failed
        """
        try:
            # Get prediction
            prediction = self._get_prediction(test_input)
            if not prediction:
                self.logger.warning("Failed to generate prediction")
                return None
            
            # Update test input with prediction
            test_input.prediction = prediction
            
            # Evaluate prediction
            return self._evaluate_prediction(test_input)
            
        except Exception as e:
            self.logger.error(f"Pipeline execution failed: {str(e)}")
            return None 