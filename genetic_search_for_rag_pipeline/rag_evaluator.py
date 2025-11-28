"""
RAG Pipeline Evaluator Template

This module provides a template for evaluating RAG pipeline configurations
by interfacing with an external RAG evaluation API. The evaluator takes
a combination of component selections and returns a performance score.
"""

"""
# backup
"retrieval": [
                "retrieval-vector_mxbai",
                "retrieval-keyword_bm25",
                "retrieval-graph_rag",
                "retrieval-hypergraph_rag",
                "retrieval-hybrid_vector_keyword_cc",
                "retrieval-hybrid_vector_graph_simply",
                "retrieval-hybrid_graph_hypergraph_simply",
                "retrieval-hybrid_vector_graph_hypergraph_simply",
                "retrieval-hybrid_vector_keyword_graph_simply",
                "retrieval-hybrid_vector_keyword_hypergraph_simply",
                "retrieval-hybrid_vector_keyword_graph_hypergraph_simply"
            ],

"""

import requests
import json
import time
import sys
import os
from typing import List, Dict, Any, Optional
import logging

# Add parent directory to path for config_loader import
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

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
                 api_endpoint: str = None,
                 timeout: int = None,
                 max_retries: int = 3,
                 enable_cache: bool = True,
                 cache_file_path: str = "/app/results/rag_evaluation_cache.json",
                 auto_save_cache: bool = True,
                 config_path: str = None,
                 use_yaml_config: bool = True):
        """
        Initialize the RAG pipeline evaluator.
        
        Args:
            api_endpoint: URL of the external RAG evaluation API (overrides YAML config)
            timeout: Request timeout in seconds (overrides YAML config)
            max_retries: Maximum number of retry attempts
            enable_cache: Whether to enable evaluation caching
            cache_file_path: Path to persistent cache file
            auto_save_cache: Whether to automatically save cache after each evaluation
            config_path: Path to gen_search_config.yml file
            use_yaml_config: Whether to load search space from YAML config
        """
        # Try to load config from YAML
        self._yaml_config = None
        if use_yaml_config:
            try:
                from config_loader import load_config, get_search_space_as_component_options, get_api_endpoint
                self._yaml_config = load_config(config_path)
                logger.info(f"✅ Loaded configuration from gen_search_config.yml")
            except Exception as e:
                logger.warning(f"⚠️ Could not load YAML config: {e}. Using defaults.")
        
        # Set API endpoint (parameter overrides YAML config)
        if api_endpoint is not None:
            self.api_endpoint = api_endpoint
        elif self._yaml_config is not None:
            self.api_endpoint = get_api_endpoint(self._yaml_config)
        else:
            self.api_endpoint = "http://example.com/api/evaluate"
        
        # Set timeout (parameter overrides YAML config)
        if timeout is not None:
            self.timeout = timeout
        elif self._yaml_config is not None:
            self.timeout = self._yaml_config.api.timeout
        else:
            self.timeout = 15000
        
        self.max_retries = max_retries
        self.enable_cache = enable_cache
        self.cache_file_path = cache_file_path
        self.auto_save_cache = auto_save_cache
        
        # Evaluation cache and statistics
        self.evaluation_cache: Dict[tuple, float] = {}
        self.cache_hits = 0
        self.total_evaluations = 0
        self.api_calls = 0
        
        # Load existing cache if available
        if self.enable_cache:
            self._load_cache_on_startup()
        
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
        
        # Load component options from YAML config or use defaults
        if self._yaml_config is not None:
            self.component_options = get_search_space_as_component_options(self._yaml_config)
            logger.info(f"📋 Loaded search space from YAML config:")
            for category, options in self.component_options.items():
                logger.info(f"   {category}: {len(options)} options")
        else:
            # Fallback to hardcoded defaults
            self.component_options = {
                "pre-embedding": [
                    "pre-embedding_none",
                    "pre-embedding_contextual_chunk_headers",
                    "pre-embedding_hype",
                    "pre-embedding_parent_document_retriever"
                ],
                "query-expansion": [
                    "query-expansion_none",
                    "query-expansion_simple_multi_query_cc_dbsf", 
                    "query-expansion_simple_multi_query_borda",
                    "query-expansion_rag_fusion",
                    "query-expansion_decomposition_cc",
                    "query-expansion_hyde_cc",
                    "query-expansion_step_back_prompting_cc",
                    "query-expansion_graph_as_qe_cc",
                    "query-expansion_refinement_clarification",
                    "query-expansion_refinement_rephrasing"
                ],
                "retrieval": [
                    "retrieval-vector_mxbai",
                    "retrieval-keyword_bm25",
                    "retrieval-graph_rag",
                    "retrieval-hybrid_vector_keyword_cc",
                    "retrieval-hybrid_vector_graph_simply",
                    "retrieval-hybrid_vector_keyword_graph_simply"
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
                    "passage-augment_relevant_segment_extractor"
                ],
                "passage-compress": [
                    "passage-compress_none",
                    "passage-compress_llm_summarize",
                    "passage-compress_tree_summarize",
                ],
                "prompt-maker": [
                    "prompt-maker_simple_listing",
                    "prompt-maker_long_context_reorder_1", 
                    "prompt-maker_long_context_reorder_2"
                ],
                "generator": [
                    "generator_alibayram/Qwen3-30B-A3B-Instruct-2507:latest",
                ],
                "post-generation": [
                    "post-generation_none",
                    "post-generation_reflection_revising"
                ]
            }
    
    def _ensure_cache_directory(self) -> None:
        """Ensure the cache directory exists."""
        try:
            import os
            cache_dir = os.path.dirname(self.cache_file_path)
            if cache_dir and not os.path.exists(cache_dir):
                os.makedirs(cache_dir, exist_ok=True)
                logger.info(f"Created cache directory: {cache_dir}")
        except Exception as e:
            logger.warning(f"Could not create cache directory: {e}")
    
    def _load_cache_on_startup(self) -> None:
        """Load existing cache from file on startup."""
        import os
        if not self.cache_file_path or not os.path.exists(self.cache_file_path):
            logger.info("No existing cache file found, starting with empty cache")
            return
        
        try:
            with open(self.cache_file_path, 'r') as f:
                cache_data = json.load(f)
            
            # Load the cache entries
            loaded_cache = {}
            for key_str, value in cache_data.get("cache", {}).items():
                try:
                    # Safely convert string representation back to tuple
                    key = tuple(json.loads(key_str))
                    loaded_cache[key] = float(value)
                except (json.JSONDecodeError, ValueError, TypeError) as e:
                    logger.warning(f"Skipping invalid cache entry {key_str}: {e}")
                    continue
            
            # Load statistics if available
            stats = cache_data.get("statistics", {})
            self.evaluation_cache = loaded_cache
            self.cache_hits = stats.get("cache_hits", 0)
            self.total_evaluations = stats.get("total_evaluations", 0)
            self.api_calls = stats.get("api_calls", 0)
            
            logger.info(f"✅ Loaded cache from {self.cache_file_path}: "
                       f"{len(loaded_cache)} entries, "
                       f"{self.total_evaluations} total evaluations, "
                       f"{self.cache_hits} cache hits")
            
        except Exception as e:
            logger.error(f"Failed to load cache from {self.cache_file_path}: {e}")
            logger.info("Starting with empty cache")
    
    def _auto_save_cache(self) -> None:
        """Automatically save cache to file if auto_save_cache is enabled."""
        if not self.auto_save_cache or not self.enable_cache:
            return
        
        try:
            import os
            self._ensure_cache_directory()
            
            # Prepare cache data
            cache_data = {
                "cache": {json.dumps(list(k)): v for k, v in self.evaluation_cache.items()},
                "statistics": self.get_cache_statistics(),
                "metadata": {
                    "last_updated": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "cache_file_version": "1.0"
                }
            }
            
            # Write to temporary file first, then rename (atomic operation)
            temp_file = self.cache_file_path + ".tmp"
            with open(temp_file, 'w') as f:
                json.dump(cache_data, f, indent=2)
            
            # Atomic rename
            os.rename(temp_file, self.cache_file_path)
            
            logger.debug(f"Cache auto-saved to {self.cache_file_path} "
                        f"({len(self.evaluation_cache)} entries)")
            
        except Exception as e:
            logger.warning(f"Failed to auto-save cache: {e}")
    
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
        Implements caching to avoid redundant API calls.
        
        Args:
            candidate: List of integers representing selected components
                      [preprocessor_idx, embedding_idx, vector_db_idx, ...]
            
        Returns:
            Fitness score as float (0-100 range)
        """
        
        candidate_key = tuple(candidate)
        
        # Check cache first (if enabled)
        if self.enable_cache and candidate_key in self.evaluation_cache:
            self.cache_hits += 1
            cached_score = self.evaluation_cache[candidate_key]
            hit_rate = (self.cache_hits / self.total_evaluations) * 100
            logger.info(f"Cache HIT for candidate {candidate}: {cached_score:.4f} "
                       f"(hit rate: {hit_rate:.1f}%, {self.cache_hits}/{self.total_evaluations})")
            return cached_score
        else:
            self.total_evaluations += 1

        # Cache miss - evaluate via API
        try:
            logger.info(f"Cache MISS - Evaluating candidate: {candidate}")
            
            # Step 1: Convert candidate to structured configuration
            configuration = self.candidate_to_configuration(candidate)
            logger.info(f"Configuration: {configuration}")
            
            # Step 2: Prepare API request
            request_payload = self.prepare_evaluation_request(configuration)
            
            # Step 3: Send request to external API
            self.api_calls += 1
            response_data = self.send_evaluation_request(request_payload)
            
            # Step 4: Extract score from response
            score = self.extract_score_from_response(response_data)
            
            # Step 5: Cache the result (if enabled)
            if self.enable_cache:
                self.evaluation_cache[candidate_key] = score
                logger.info(f"Cached result for candidate {candidate}: {score:.4f} "
                           f"(cache size: {len(self.evaluation_cache)})")
                
                # Auto-save cache after new evaluation
                self._auto_save_cache()
            
            logger.info(f"Final score for candidate {candidate}: {score}")
            return score
            
        except Exception as e:
            logger.error(f"Evaluation failed for candidate {candidate}: {e}")
            
            # Return a low score for failed evaluations
            # In production, you might want to retry or handle this differently
            return 0.0
    
    def get_cache_statistics(self) -> Dict[str, Any]:
        """
        Get detailed cache performance statistics.
        
        Returns:
            Dictionary containing cache statistics
        """
        if self.total_evaluations == 0:
            hit_rate = 0.0
            efficiency = 0.0
        else:
            hit_rate = (self.cache_hits / self.total_evaluations) * 100
            efficiency = ((self.total_evaluations - self.api_calls) / self.total_evaluations) * 100
        
        return {
            "total_evaluations": self.total_evaluations,
            "cache_hits": self.cache_hits,
            "cache_misses": self.total_evaluations - self.cache_hits,
            "api_calls": self.api_calls,
            "cache_size": len(self.evaluation_cache),
            "hit_rate_percent": hit_rate,
            "efficiency_percent": efficiency,
            "cache_enabled": self.enable_cache
        }
    
    def clear_cache(self) -> None:
        """Clear the evaluation cache and reset statistics."""
        self.evaluation_cache.clear()
        self.cache_hits = 0
        self.total_evaluations = 0
        self.api_calls = 0
        logger.info("Evaluation cache cleared")
    
    def get_cache_size(self) -> int:
        """Get the current number of cached evaluations."""
        return len(self.evaluation_cache)
    
    def get_best_from_cache(self) -> tuple:
        """
        Get the best individual and score from cache.
        
        Returns:
            Tuple of (candidate_genes, fitness_score) for the best cached individual,
            or (None, 0.0) if cache is empty
        """
        if not self.evaluation_cache:
            return None, 0.0
        
        # Find the candidate with the highest score
        best_candidate_key = max(self.evaluation_cache.keys(), 
                               key=lambda k: self.evaluation_cache[k])
        best_score = self.evaluation_cache[best_candidate_key]
        best_candidate = list(best_candidate_key)
        
        logger.info(f"🏆 Best from cache: {best_candidate} with score {best_score:.4f}")
        return best_candidate, best_score
    
    def save_cache_to_file(self, filepath: str) -> None:
        """
        Save the current cache to a JSON file.
        
        Args:
            filepath: Path to save the cache file
        """
        try:
            import os
            # Ensure directory exists
            cache_dir = os.path.dirname(filepath)
            if cache_dir and not os.path.exists(cache_dir):
                os.makedirs(cache_dir, exist_ok=True)
            
            cache_data = {
                "cache": {json.dumps(list(k)): v for k, v in self.evaluation_cache.items()},
                "statistics": self.get_cache_statistics(),
                "metadata": {
                    "last_updated": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "cache_file_version": "1.0"
                }
            }
            
            # Atomic write using temporary file
            temp_file = filepath + ".tmp"
            with open(temp_file, 'w') as f:
                json.dump(cache_data, f, indent=2)
            
            os.rename(temp_file, filepath)
            logger.info(f"💾 Cache saved to {filepath} ({len(self.evaluation_cache)} entries)")
            
        except Exception as e:
            logger.error(f"Failed to save cache to {filepath}: {e}")
    
    def load_cache_from_file(self, filepath: str) -> None:
        """
        Load cache from a JSON file.
        
        Args:
            filepath: Path to the cache file
        """
        import os
        if not os.path.exists(filepath):
            logger.info(f"Cache file {filepath} does not exist")
            return
            
        try:
            with open(filepath, 'r') as f:
                cache_data = json.load(f)
            
            # Convert string keys back to tuples
            loaded_cache = {}
            for key_str, value in cache_data.get("cache", {}).items():
                try:
                    # Safely convert JSON string back to tuple
                    key = tuple(json.loads(key_str))
                    loaded_cache[key] = float(value)
                except (json.JSONDecodeError, ValueError, TypeError) as e:
                    logger.warning(f"Skipping invalid cache entry {key_str}: {e}")
                    continue
            
            # Load statistics if available
            stats = cache_data.get("statistics", {})
            old_size = len(self.evaluation_cache)
            self.evaluation_cache.update(loaded_cache)
            
            # Update statistics (merge with existing)
            self.cache_hits = max(self.cache_hits, stats.get("cache_hits", 0))
            self.total_evaluations = max(self.total_evaluations, stats.get("total_evaluations", 0))
            self.api_calls = max(self.api_calls, stats.get("api_calls", 0))
            
            logger.info(f"📂 Cache loaded from {filepath}: "
                       f"{len(loaded_cache)} entries loaded, "
                       f"{len(self.evaluation_cache)} total entries in cache")
            
        except Exception as e:
            logger.error(f"Failed to load cache from {filepath}: {e}")


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