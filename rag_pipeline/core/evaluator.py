import logging
import json
import time
from typing import List, Dict, Any, Optional

from .models import (
    RAGTestCase, RetrievalResult, GenerationResult, 
    RAGMetrics, RAGEvaluationResult, RAGConfig
)

logger = logging.getLogger(__name__)

class RAGEvaluator:
    """Evaluates both retrieval and generation components of RAG pipeline"""
    
    def __init__(self, config: RAGConfig):
        self.config = config
        self._setup_evaluators()
    
    def _setup_evaluators(self):
        """Setup evaluation utilities"""
        try:
            # Setup LLM evaluator for generation
            
            # Setup semantic similarity evaluator
            from util.comparison.semantic_comparison import SemanticComparison
            # Use the first embedding model for evaluation similarity
            eval_embedding_model = self.config.embedding_models[0] if self.config.embedding_models else "nomic-embed-text"
            self.semantic_evaluator = SemanticComparison(eval_embedding_model)
            
        except Exception as e:
            logger.error(f"Failed to setup evaluators: {e}")
            raise
    
    async def evaluate_single_case(
        self, 
        test_case: RAGTestCase,
        retrieval_result: RetrievalResult,
        generation_result: GenerationResult
    ) -> RAGEvaluationResult:
        """Evaluate a single test case with both retrieval and generation results"""
        
        total_eval_start = time.time()
        
        try:
            # Evaluate retrieval with timing
            retrieval_eval_start = time.time()
            retrieval_metrics = self._evaluate_retrieval(test_case, retrieval_result)
            retrieval_eval_time = time.time() - retrieval_eval_start
            
            # Evaluate generation with timing
            generation_eval_start = time.time()
            generation_metrics = self._evaluate_generation(test_case, generation_result)
            generation_eval_time = time.time() - generation_eval_start
            
            # Calculate component scores
            retrieval_score = self._calculate_retrieval_score(retrieval_metrics)
            generation_score = self._calculate_generation_score(generation_metrics)
            
            # Combine metrics
            combined_metrics = RAGMetrics(
                # Retrieval metrics
                recall_at_k=retrieval_metrics['recall_at_k'],
                map_score=retrieval_metrics['map_score'],
                ndcg_at_k=retrieval_metrics['ndcg_at_k'],
                mrr=retrieval_metrics['mrr'],
                eval_k=retrieval_metrics.get('eval_k', self.config.retrieval_k),
                
                # Generation metrics
                llm_score=generation_metrics['llm_score'],
                semantic_similarity=generation_metrics['semantic_similarity'],
                
                # Component scores
                retrieval_score=retrieval_score,
                generation_score=generation_score,
                
                # Combined score (weighted average)
                overall_score=self._calculate_overall_score(retrieval_metrics, generation_metrics)
            )
            
            total_eval_time = time.time() - total_eval_start
            
            return RAGEvaluationResult(
                embedding_model=retrieval_result.embedding_model,
                llm_model=generation_result.llm_model,
                test_case_id=test_case.id,
                retrieval_result=retrieval_result,
                generation_result=generation_result,
                metrics=combined_metrics,
                retrieval_eval_time=retrieval_eval_time,
                generation_eval_time=generation_eval_time,
                total_eval_time=total_eval_time
            )
            
        except Exception as e:
            logger.error(f"Evaluation failed for test case {test_case.id}: {e}")
            total_eval_time = time.time() - total_eval_start
            return RAGEvaluationResult(
                embedding_model=retrieval_result.embedding_model,
                llm_model=generation_result.llm_model,
                test_case_id=test_case.id,
                retrieval_result=retrieval_result,
                generation_result=generation_result,
                metrics=RAGMetrics(
                    recall_at_k=0.0, map_score=0.0, ndcg_at_k=0.0, mrr=0.0, eval_k=self.config.retrieval_k,
                    llm_score=0.0, semantic_similarity=0.0,
                    retrieval_score=0.0, generation_score=0.0, overall_score=0.0
                ),
                retrieval_eval_time=0.0,
                generation_eval_time=0.0,
                total_eval_time=total_eval_time,
                error=str(e)
            )
    
    def _evaluate_retrieval(self, test_case: RAGTestCase, retrieval_result: RetrievalResult) -> Dict[str, float]:
        """Evaluate retrieval performance"""
        if retrieval_result.error or not retrieval_result.retrieved_docs:
            return {'recall_at_k': 0.0, 'map_score': 0.0, 'ndcg_at_k': 0.0, 'mrr': 0.0}
        
        try:
            retrieved_doc_ids = [doc['doc_id'] for doc in retrieval_result.retrieved_docs]
            relevant_doc_ids = test_case.relevant_doc_ids
            
            # Convert to strings for comparison
            retrieved_doc_ids = [str(doc_id) for doc_id in retrieved_doc_ids if doc_id is not None]
            relevant_doc_ids_str = [str(doc_id) for doc_id in relevant_doc_ids]
            
            # Determine the appropriate k value based on which reranking methods were applied
            # Priority: LLM reranking > Cross-encoder reranking > No reranking
            if hasattr(retrieval_result, 'llm_reranked') and retrieval_result.llm_reranked:
                # Use llm_rerank_top_k since LLM reranking was applied (highest priority)
                eval_k = self.config.llm_rerank_top_k
                logger.debug(f"Using llm_rerank_top_k={eval_k} for evaluation since LLM reranking was applied")
            elif retrieval_result.reranked:
                # Use rerank_top_k since cross-encoder reranking was applied
                eval_k = self.config.rerank_top_k
                logger.debug(f"Using rerank_top_k={eval_k} for evaluation since cross-encoder reranking was applied")
            else:
                # Use retrieval_k for non-reranked results
                eval_k = self.config.retrieval_k
                logger.debug(f"Using retrieval_k={eval_k} for evaluation since no reranking was applied")
            
            # Use existing metrics calculation
            from util.vectorstore.metrics import RetrievalMetrics
            k_values = [eval_k]
            metrics = RetrievalMetrics.calculate_all_metrics(retrieved_doc_ids, relevant_doc_ids_str, k_values)
            
            return {
                'recall_at_k': metrics.get(f'recall@{eval_k}', 0.0),
                'map_score': metrics.get('map', 0.0),  # Use mAP instead of precision@k
                'ndcg_at_k': metrics.get(f'ndcg@{eval_k}', 0.0),
                'mrr': metrics.get('mrr', 0.0),
                'eval_k': eval_k  # Store the k value used for evaluation
            }
            
        except Exception as e:
            logger.error(f"Retrieval evaluation failed: {e}")
            return {'recall_at_k': 0.0, 'map_score': 0.0, 'ndcg_at_k': 0.0, 'mrr': 0.0}
    
    def _evaluate_generation(self, test_case: RAGTestCase, generation_result: GenerationResult) -> Dict[str, float]:
        """Evaluate generation performance"""
        if generation_result.error or not generation_result.generated_answer:
            return {'llm_score': 0.0, 'semantic_similarity': 0.0}
        
        try:
            # LLM-based evaluation
            llm_score = self._llm_evaluate(
                generation_result.generated_answer, 
                test_case.ground_truth_answer
            )
            
            # Semantic similarity evaluation
            semantic_score = self.semantic_evaluator.get_similarity_score(
                generation_result.generated_answer,
                test_case.ground_truth_answer
            )
            
            return {
                'llm_score': llm_score,
                'semantic_similarity': semantic_score
            }
            
        except Exception as e:
            logger.error(f"Generation evaluation failed: {e}")
            return {'llm_score': 0.0, 'semantic_similarity': 0.0}
    
    def _llm_evaluate(self, generated_answer: str, ground_truth: str) -> float:
        """Use LLM to evaluate generated answer quality"""
        try:
            eval_prompt = f"""Evaluate the following LLM response against the ground truth and return a score between 0 and 1. 
Consider accuracy, completeness, and relevance. Return ONLY a JSON response with the score.

LLM Response: {generated_answer}

Ground Truth: {ground_truth}

Return format: {{"score": 0.85}}"""
            
            # Patch: Use Gemini or Ollama based on model name
            from util.api.gemini_client import GeminiUtil
            from util.api.ollama_client import OllamaUtil
            model = self.config.eval_llm_model
            if model.lower().startswith("gemini"):
                response = GeminiUtil.get_gemini_response(model, eval_prompt)
            else:
                response = OllamaUtil.get_ollama_response(model, eval_prompt)
            
            if isinstance(response, dict):
                response_text = response.get('response', '')
            else:
                response_text = str(response)
            
            # Extract JSON from response
            try:
                # Try to find JSON in the response
                if '```json' in response_text:
                    json_str = response_text.split('```json')[1].split('```')[0].strip()
                else:
                    json_str = response_text
                
                result = json.loads(json_str)
                score = float(result.get('score', 0.0))
                return max(0.0, min(1.0, score))  # Clamp between 0 and 1
                
            except (json.JSONDecodeError, ValueError, KeyError) as e:
                logger.warning(f"Failed to parse LLM evaluation response: {e}")
                return 0.5  # Default score if parsing fails
                
        except Exception as e:
            logger.error(f"LLM evaluation failed: {e}")
            return 0.0
    
    def _calculate_retrieval_score(self, retrieval_metrics: Dict[str, float]) -> float:
        """Calculate average retrieval score"""
        return (
            retrieval_metrics['recall_at_k'] + 
            retrieval_metrics['map_score'] + 
            retrieval_metrics['ndcg_at_k'] +
            retrieval_metrics['mrr']
        ) / 4.0
    
    def _calculate_generation_score(self, generation_metrics: Dict[str, float]) -> float:
        """Calculate average generation score"""
        return (
            generation_metrics['llm_score'] + 
            generation_metrics['semantic_similarity']
        ) / 2.0
    
    def _calculate_overall_score(self, retrieval_metrics: Dict[str, float], generation_metrics: Dict[str, float]) -> float:
        """Calculate weighted overall score"""
        # Weighted combination of retrieval and generation metrics
        retrieval_weight = 0.3
        generation_weight = 0.7
        
        # Use the component score calculation methods
        retrieval_score = self._calculate_retrieval_score(retrieval_metrics)
        generation_score = self._calculate_generation_score(generation_metrics)
        
        overall_score = (retrieval_weight * retrieval_score) + (generation_weight * generation_score)
        return overall_score
    
    async def aggregate_results(self, results: List[RAGEvaluationResult]) -> Dict[str, Dict[str, float]]:
        """Aggregate results by model combination"""
        aggregated = {}
        
        # Group by model combination (including both types of reranking information)
        by_combination = {}
        for result in results:
            # Build combination key including both cross-encoder and LLM reranking
            # Use || as delimiter to avoid conflicts with model names that contain underscores, slashes, etc.
            key_parts = [result.embedding_model]
            
            # Add cross-encoder reranking if applied
            if result.retrieval_result.reranked and result.retrieval_result.rerank_model:
                key_parts.append(result.retrieval_result.rerank_model)
            
            # Add LLM reranking if applied
            if (hasattr(result.retrieval_result, 'llm_reranked') and 
                result.retrieval_result.llm_reranked and 
                hasattr(result.retrieval_result, 'llm_rerank_model') and
                result.retrieval_result.llm_rerank_model):
                key_parts.append(f"LLM-rerank({result.retrieval_result.llm_rerank_model})")
            
            key_parts.append(result.llm_model)
            combo_key = "||".join(key_parts)
            
            if combo_key not in by_combination:
                by_combination[combo_key] = []
            by_combination[combo_key].append(result)
        
        # Calculate averages for each combination
        for combo_key, combo_results in by_combination.items():
            if not combo_results:
                continue
                
            # Filter successful results
            successful_results = [r for r in combo_results if not r.error]
            
            if not successful_results:
                aggregated[combo_key] = {
                    'recall_at_k': 0.0, 'map_score': 0.0, 'ndcg_at_k': 0.0, 'mrr': 0.0, 'eval_k': self.config.retrieval_k,
                    'llm_score': 0.0, 'semantic_similarity': 0.0,
                    'retrieval_score': 0.0, 'generation_score': 0.0, 'overall_score': 0.0,
                    'retrieval_prediction_time': 0.0, 'generation_prediction_time': 0.0,
                    'rerank_time': 0.0, 'reranked': False, 'rerank_model': None,
                    'retrieval_evaluation_time': 0.0, 'generation_evaluation_time': 0.0,
                    'total_eval_time': 0.0,
                    'success_rate': 0.0, 'test_count': len(combo_results)
                }
                continue
            
            # Calculate averages
            avg_metrics = {
                'recall_at_k': sum(r.metrics.recall_at_k for r in successful_results) / len(successful_results),
                'map_score': sum(r.metrics.map_score for r in successful_results) / len(successful_results),
                'ndcg_at_k': sum(r.metrics.ndcg_at_k for r in successful_results) / len(successful_results),
                'mrr': sum(r.metrics.mrr for r in successful_results) / len(successful_results),
                'eval_k': successful_results[0].metrics.eval_k if successful_results else self.config.retrieval_k,  # Use the eval_k from first result (should be same for all in combo)
                'llm_score': sum(r.metrics.llm_score for r in successful_results) / len(successful_results),
                'semantic_similarity': sum(r.metrics.semantic_similarity for r in successful_results) / len(successful_results),
                'retrieval_score': sum(r.metrics.retrieval_score for r in successful_results) / len(successful_results),
                'generation_score': sum(r.metrics.generation_score for r in successful_results) / len(successful_results),
                'overall_score': sum(r.metrics.overall_score for r in successful_results) / len(successful_results),
                'retrieval_prediction_time': sum(r.retrieval_result.retrieval_time for r in successful_results) / len(successful_results),
                'generation_prediction_time': sum(r.generation_result.generation_time for r in successful_results) / len(successful_results),
                'rerank_time': sum(r.retrieval_result.rerank_time for r in successful_results) / len(successful_results),
                'reranked': any(r.retrieval_result.reranked for r in successful_results),
                'rerank_model': successful_results[0].retrieval_result.rerank_model if successful_results else None,
                'llm_rerank_time': sum(getattr(r.retrieval_result, 'llm_rerank_time', 0.0) for r in successful_results) / len(successful_results),
                'llm_reranked': any(getattr(r.retrieval_result, 'llm_reranked', False) for r in successful_results),
                'llm_rerank_model': successful_results[0].retrieval_result.llm_rerank_model if successful_results and hasattr(successful_results[0].retrieval_result, 'llm_rerank_model') else None,
                'retrieval_evaluation_time': sum(r.retrieval_eval_time for r in successful_results) / len(successful_results),
                'generation_evaluation_time': sum(r.generation_eval_time for r in successful_results) / len(successful_results),
                'total_eval_time': sum(r.total_eval_time for r in successful_results) / len(successful_results),
                'success_rate': len(successful_results) / len(combo_results),
                'test_count': len(combo_results)
            }
            
            aggregated[combo_key] = avg_metrics
        
        return aggregated 