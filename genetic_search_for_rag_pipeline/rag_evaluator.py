"""
RAG Pipeline Evaluator Template

This module provides a template for evaluating RAG pipeline configurations
by interfacing with an external RAG evaluation API. The evaluator takes
a combination of component selections and returns a performance score.
"""

import requests
import json
import time
from typing import List, Dict, Any, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RAGPipelineEvaluator:
    """
    Template class for evaluating RAG pipeline configurations via external API.
    
    This evaluator takes a combination of component selections (one from each
    category) and sends it to an external RAG evaluation service to get a
    performance score.
    """
    
    def __init__(self, 
                 api_endpoint: str = "http://example.com/api/evaluate",
                 timeout: int = 15000,
                 max_retries: int = 3):
        """
        Initialize the RAG pipeline evaluator.
        
        Args:
            api_endpoint: URL of the external RAG evaluation API
            timeout: Request timeout in seconds
            max_retries: Maximum number of retry attempts
        """
        self.api_endpoint = api_endpoint
        self.timeout = timeout
        self.max_retries = max_retries
        
        # Component category mappings
        self.component_categories = {
            0: "pre-embedding",
            1: "query-expansion",       
            2: "retrieval",        
            3: "passage-rerank",    
            4: "passage-filter",      
            5: "passage-augment",             
            6: "passage-compress",        
            7: "prompt-maker",   
            8: "generator",     
            9: "post-generation"      
        }
        
        # Component selections mapping (customize based on your actual components)
        self.component_options = {
            "pre-embedding": [
                "pre-embedding_none",
                # "pre-embedding_contextual_chunk_headers",
                # "pre-embedding_hype",
                "pre-embedding_parent_document_retriever"
            ],
            "query-expansion": [
                "query-expansion_none",
                "query-expansion_simple_multi_query_cc_dbsf", 
                # "query-expansion_simple_multi_query_borda",
                # "query-expansion_rag_fusion",
                "query-expansion_decomposition_cc",
                # "query-expansion_hyde_cc",
                # "query-expansion_step_back_prompting_cc",
                # "query-expansion_graph_as_qe_cc",
                "query-expansion_refinement_clarification",
                "query-expansion_refinement_rephrasing"
            ],
            "retrieval": [
                "retrieval-vector_mxbai",
                # "retrieval-vector_nomic",
                "retrieval-keyword_bm25",
                "retrieval-hybrid_vector_keyword_cc",
                # "retrieval-hybrid_vector_graph_simply",
                # "retrieval-hybrid_graph_hypergraph_simply",
                # "retrieval-hybrid_vector_graph_hypergraph_simply",
                # "retrieval-hybrid_vector_keyword_graph_simply",
                # "retrieval-hybrid_vector_keyword_hypergraph_simply",
                # "retrieval-hybrid_vector_keyword_graph_hypergraph_simply"
            ],
            "passage-rerank": [
                "passage-rerank_none",
                "passage-rerank_ce_rerank_bge",
                "passage-rerank_llm_rerank_gemma", 
                "passage-rerank_cellm_parallel_rerank"
            ],
            "passage-filter": [
                "passage-filter_simple_threshold",
                "passage-filter_similarity_threshold"
            ],
            "passage-augment": [
                "passage-augment_none",
                "passage-augment_prev_next_augmenter",
                # "passage-augment_relevant_segment_extractor"
            ],
            "passage-compress": [
                "passage-compress_none",
                # "passage-compress_llm_summarize",
                # "passage-compress_tree_summarize",
                "passage-compress_llm_lingua"
            ],
            "prompt-maker": [
                "prompt-maker_simple_listing",
                "prompt-maker_long_context_reorder_1", 
                "prompt-maker_long_context_reorder_2"
            ],
            "generator": [
                "generator_llama3.2:1b",
                "generator_gemma3:4b",
                # "generator_gemma3:12b",
                # "generator_multi_llm_llama3.2:1b-gemma3:4b-Ensemble:gemma3:12b"
            ],
            "post-generation": [
                "post-generation_none",
                "post-generation_reflection_revising"
            ]
        }
    
    def candidate_to_configuration(self, candidate: List[int]) -> Dict[str, str]:
        """
        Convert a candidate (list of box indices) to a structured configuration.
        
        Args:
            candidate: List of integers, each representing selected box index
                      for the corresponding category
            
        Returns:
            Dictionary mapping component categories to selected options
        """
        if len(candidate) != len(self.component_categories):
            raise ValueError(f"Candidate must have {len(self.component_categories)} components, "
                           f"got {len(candidate)}")
        
        configuration = {}
        
        for i, selection_index in enumerate(candidate):
            category_name = self.component_categories[i]
            available_options = self.component_options[category_name]
            
            # Ensure selection is within bounds
            if selection_index >= len(available_options):
                selection_index = len(available_options) - 1
            elif selection_index < 0:
                selection_index = 0
            
            selected_option = available_options[selection_index]
            configuration[category_name] = selected_option
        
        return configuration
    
    def prepare_evaluation_request(self, configuration: Dict[str, str]) -> Dict[str, Any]:
        """
        Prepare the request payload for the RAG evaluation API.
        
        Args:
            configuration: RAG pipeline configuration
            
        Returns:
            Request payload dictionary
        """

        request_payload = {
            "evaluation_request": {
                "pipeline_config": configuration,
            }
        }
        
        return request_payload
    
    def send_evaluation_request(self, request_payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Send evaluation request to the external RAG API.
        
        Args:
            request_payload: Request data to send
            
        Returns:
            API response data
        """
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        
        # Add any custom headers if needed
        # headers["Custom-Header"] = "value"
        
        for attempt in range(self.max_retries):
            try:
                logger.info(f"Sending evaluation request (attempt {attempt + 1}/{self.max_retries})")
                
                response = requests.post(
                    self.api_endpoint,
                    json=request_payload,
                    headers=headers,
                    timeout=self.timeout
                )
                
                response.raise_for_status()
                
                # Parse JSON response
                result = response.json()
                logger.info("Evaluation request successful")
                
                return result
                
            except requests.exceptions.RequestException as e:
                logger.warning(f"Request attempt {attempt + 1} failed: {e}")
                
                if attempt == self.max_retries - 1:
                    logger.error(f"All {self.max_retries} attempts failed")
                    raise
                
                # Wait before retry (exponential backoff)
                wait_time = 2 ** attempt
                logger.info(f"Waiting {wait_time} seconds before retry...")
                time.sleep(wait_time)
    
    def extract_score_from_response(self, response_data: Dict[str, Any]) -> float:
        """
        Extract the evaluation score from the API response.
        
        Args:
            response_data: Response from the evaluation API
            
        Returns:
            Extracted score as float (0-1 range)
        """
        try:
            if "evaluation" in response_data:
                # Extract from nested evaluation object
                evaluation = response_data["evaluation"]
                
                if "final_score" in evaluation:
                    score = float(evaluation["final_score"])
                else:
                    score = 0.0
                    print(f"WARNING : No final score found in response: {response_data}")
            else:
                # Alternative response structure
                score = float(response_data.get("score", response_data.get("final_score", 0.0)))
            
            
            logger.info(f"Extracted score: {score}")
            return score
            
        except (KeyError, ValueError, TypeError) as e:
            logger.error(f"Failed to extract score from response: {e}")
            logger.error(f"Response data: {json.dumps(response_data, indent=2)}")
            
            # Return a default low score if extraction fails
            return 0.0
    
    def evaluate(self, candidate: List[int]) -> float:
        """
        Main evaluation function for the genetic algorithm.
        
        This function takes a candidate solution (list of component selections)
        and returns a fitness score by calling the external RAG evaluation API.
        
        Args:
            candidate: List of integers representing selected components
                      [preprocessor_idx, embedding_idx, vector_db_idx, ...]
            
        Returns:
            Fitness score as float (0-100 range)
        """
        try:
            logger.info(f"Evaluating candidate: {candidate}")
            
            # Step 1: Convert candidate to structured configuration
            configuration = self.candidate_to_configuration(candidate)
            logger.info(f"Configuration: {configuration}")
            
            # Step 2: Prepare API request
            request_payload = self.prepare_evaluation_request(configuration)
            
            # Step 3: Send request to external API
            response_data = self.send_evaluation_request(request_payload)
            
            # Step 4: Extract score from response
            score = self.extract_score_from_response(response_data)
            
            logger.info(f"Final score for candidate {candidate}: {score}")
            return score
            
        except Exception as e:
            logger.error(f"Evaluation failed for candidate {candidate}: {e}")
            
            # Return a low score for failed evaluations
            # In production, you might want to retry or handle this differently
            return 0.0


# Factory function for easy integration with genetic algorithm
def create_rag_evaluator(**kwargs) -> RAGPipelineEvaluator:
    """
    Factory function to create a RAG pipeline evaluator.
    
    Args:
        **kwargs: Configuration parameters for the evaluator
        
    Returns:
        Configured RAGPipelineEvaluator instance
    """
    return RAGPipelineEvaluator(**kwargs)


# Template evaluation function for direct use with genetic algorithm
def evaluate_rag_pipeline(candidate: List[int], 
                         api_endpoint: str = "http://example.com/api/evaluate") -> float:
    """
    Template evaluation function for RAG pipeline optimization.
    
    This is the main function that the genetic algorithm will call for each candidate.
    
    Args:
        candidate: List of component selection indices
        api_endpoint: RAG evaluation API endpoint
        
    Returns:
        Fitness score (0-100)
    """
    # Create evaluator instance
    evaluator = RAGPipelineEvaluator(
        api_endpoint=api_endpoint
    )
    
    # Evaluate the candidate
    return evaluator.evaluate(candidate)


# Example usage and configuration
if __name__ == "__main__":
    """
    Example usage of the RAG pipeline evaluator.
    """
    
    # Example candidate: [preprocessor, embedding, vector_db, retrieval, rerank, llm, prompt, context, output, metrics]
    example_candidate = [1, 3, 2, 4, 1, 5, 2, 3, 1, 2]
    
    # Create evaluator
    evaluator = create_rag_evaluator(
        api_endpoint="https://your-rag-evaluation-service.com/api/evaluate",
        timeout=3000
    )
    
    # Test evaluation
    print("Testing RAG pipeline evaluation...")
    score = evaluator.evaluate(example_candidate)
    print(f"Evaluation score: {score}")
    
    # Show configuration mapping
    config = evaluator.candidate_to_configuration(example_candidate)
    print("\nConfiguration mapping:")
    for category, selection in config.items():
        print(f"  {category}: {selection}") 