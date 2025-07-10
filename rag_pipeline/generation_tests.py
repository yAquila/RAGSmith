"""
Retrieval-based benchmark tests.

This module contains test implementations for retrieval tasks with comprehensive
metrics including precision, recall, and other IR evaluation measures.
"""

import logging
from typing import Dict, Any, List, Optional, Union

from models import BenchmarkConfigModel, TestInputModel as TestInput
from util.api.ollama_client import OllamaUtil
from util.comparison.semantic_comparison import SemanticComparison
import json
logger = logging.getLogger(__name__)


class GenerationTest():
    """Test class for retrieval tasks with comprehensive metrics."""
    
    def __init__(self, config: BenchmarkConfigModel, embedding_model_name: str, llm_model_name: str):
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)
        self.semantic_comparison = SemanticComparison(embedding_model_name)
        self.llm_model_name = llm_model_name
        
    def _generate_prompt(self, test_input: TestInput) -> str:
        """Generate prompt for generation tasks - include context documents if available."""
        
        # Base prompt with the user question
        prompt = test_input.user_prompt
        
        # If documents are available, format them as context
        if test_input.docs and len(test_input.docs) > 0:
            context_section = "\n\nContext Documents:\n"
            for i, doc in enumerate(test_input.docs, 1):
                context_section += f"\nDocument {i}:\n{doc}\n"
            
            # Combine context and question in a RAG-style prompt
            prompt = f"""{context_section}

Based on the context documents provided above, please answer the following question:

Question: {test_input.user_prompt}

Answer:"""
        
        return prompt
    
    def _get_prediction(self, test_input: TestInput) -> Optional[str]:
        """Get LLM response for generation tasks."""
        try:
            query = self._generate_prompt(test_input)
            ollama_response = OllamaUtil.get_ollama_response(self.llm_model_name, query)
            return ollama_response
        except Exception as e:
            logger.error(f"Ollama response failed: {str(e)}")
            return None
    
    def _evaluate_prediction(self, test_input: TestInput) -> Dict[str, Any]:
        """Evaluate generation results using comprehensive metrics."""
        if not test_input.prediction:
            raise ValueError("Prediction is required for evaluation")
        
        if not test_input.ground_truth:
            raise ValueError("ground_truth is required for generation evaluation")
        
        results = test_input.prediction
        ground_truth = test_input.ground_truth
        logger.info(f"Evaluating {results} against {ground_truth}")
        llm_eval = OllamaUtil.get_ollama_response(self.config.eval_llm_model_name, f"Evaluate the following LLM response against the following ground truth and return the score in a json format. The score should be a number between 1 and 10. **ONLY RETURN THE JSON RESPONSE, NO OTHER TEXT**: \n\n LLM Response: {results} \n\n Ground Truth: {ground_truth} ")
        logger.info(f"LLM Eval: {llm_eval}")
        llm_eval_json = json.loads(llm_eval['response'].split('```json\n')[1].split('\n```')[0])
        llm_score = llm_eval_json.get('score', 0)
        semantic_score = self.semantic_comparison.get_similarity_score(results, ground_truth)

        logger.info(f"LLM Score: {llm_score}")
        logger.info(f"Semantic Score: {semantic_score}")
        llm_score = llm_score/10
        # Add additional info
        metrics = {
            'llm_score': llm_score,
            'semantic_score': semantic_score
        }

        return {
            'score': (llm_score + semantic_score) / 2,
            'metrics': metrics,
            'overall_score': (llm_score + semantic_score) / 2
        }
