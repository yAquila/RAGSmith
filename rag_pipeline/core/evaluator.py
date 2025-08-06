import logging
import json
import time
from typing import List, Dict, Any, Optional
import os

from .models import (
    RAGTestCase, RetrievalResult, GenerationResult, 
    RAGMetrics, RAGEvaluationResult
)

logger = logging.getLogger(__name__)

class RAGEvaluator:
    """Evaluates both retrieval and generation components of RAG pipeline"""
    
    def __init__(self, config_dict: dict, global_config=None):
        self.config_dict = config_dict  # Per-run config (one config per category)
        self.global_config = global_config  # Global ModularRAGConfig
        self._setup_evaluators()
    
    def _setup_evaluators(self):
        """Setup evaluation utilities"""
        try:
            # Setup semantic similarity evaluator using the retrieval config for this run
            from rag_pipeline.util.comparison.semantic_comparison import SemanticComparison
            retrieval_cfg = self.config_dict.get('retrieval', None)
            if retrieval_cfg and getattr(retrieval_cfg, 'embedding_model', None):
                eval_embedding_model = retrieval_cfg.embedding_model
            else:
                eval_embedding_model = "mxbai-embed-large"
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
            generation_metrics = self._evaluate_generation(generation_result.generated_answer, test_case.ground_truth_answer, generation_result.combo_name)
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
                eval_k=retrieval_metrics.get('eval_k', self.config_dict['retrieval'].top_k),
                
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
                    recall_at_k=0.0, map_score=0.0, ndcg_at_k=0.0, mrr=0.0, eval_k=self.config_dict['retrieval'].top_k,
                    llm_score=0.0, semantic_similarity=0.0,
                    retrieval_score=0.0, generation_score=0.0, overall_score=0.0
                ),
                retrieval_eval_time=0.0,
                generation_eval_time=0.0,
                total_eval_time=total_eval_time,
                error=str(e)
            )
    
    def remove_duplicates(self, retrieved_doc_ids: List[str]) -> List[str]:
        """Remove duplicates from retrieved doc ids while preserving order"""
        seen = set()
        result = []
        for doc_id in retrieved_doc_ids:
            if doc_id not in seen:
                seen.add(doc_id)
                result.append(doc_id)
        return result

    def _evaluate_retrieval(self, test_case: RAGTestCase, retrieval_result: RetrievalResult) -> Dict[str, float]:
        """Evaluate retrieval performance"""
        if retrieval_result.error or not retrieval_result.retrieved_docs:
            return {'recall_at_k': 0.0, 'map_score': 0.0, 'ndcg_at_k': 0.0, 'mrr': 0.0}
        
        try:
            #if retrieval_result.retrieved_docs[0]["doc_id"].startswith("graph_rel") or retrieval_result.retrieved_docs[0]["doc_id"].startswith("hypergraph") or retrieval_result.retrieved_docs[0].get("metadata", {}).get("hype_doc_id", None):
            #     retrieved_doc_ids = self.remove_duplicates([doc['metadata']['original_doc_id'] for doc in retrieval_result.retrieved_docs])
            # else:
            #     retrieved_doc_ids = self.remove_duplicates([doc['doc_id'] for doc in retrieval_result.retrieved_docs])
            # for rd in retrieval_result.retrieved_docs:
            #     logger.info(f"Retrieval doc: {rd}")
            retrieved_doc_ids = []
            for doc in retrieval_result.retrieved_docs:
                if doc.get('metadata', {}).get('original_doc_id', None):
                    retrieved_doc_ids.append(doc['metadata'].get('original_doc_id', None))
                else: 
                    retrieved_doc_ids.append(doc['doc_id'])
            retrieved_doc_ids = self.remove_duplicates(retrieved_doc_ids)
            relevant_doc_ids = test_case.relevant_doc_ids
            logger.info(f"Retrieved doc ids: {retrieved_doc_ids}")
            logger.info(f"Relevant doc ids: {relevant_doc_ids}")
            # logger.info(f"Retrieval result: {retrieval_result.retrieved_docs}")
            # Convert to strings for comparison
            retrieved_doc_ids = [str(doc_id) for doc_id in retrieved_doc_ids if doc_id is not None]
            relevant_doc_ids_str = [str(doc_id) for doc_id in relevant_doc_ids]
            
            # Determine the appropriate k value based on which reranking methods were applied
            # Priority: LLM reranking > Cross-encoder reranking > No reranking
            if 'passage_rerank' in self.config_dict and hasattr(self.config_dict['passage_rerank'], 'llm_rerank_top_k'):
                eval_k = self.config_dict['passage_rerank'].llm_rerank_top_k
                logger.debug(f"Using llm_rerank_top_k={eval_k} for evaluation since LLM reranking config is present")
            elif 'passage_rerank' in self.config_dict and hasattr(self.config_dict['passage_rerank'], 'cross_encoder_top_k'):
                eval_k = self.config_dict['passage_rerank'].cross_encoder_top_k
                logger.debug(f"Using cross_encoder_top_k={eval_k} for evaluation since cross-encoder reranking config is present")
            else:
                eval_k = self.config_dict['retrieval'].top_k
                logger.debug(f"Using retrieval_k={eval_k} for evaluation since no reranking was applied")
            
            # Use existing metrics calculation
            from rag_pipeline.util.vectorstore.metrics import RetrievalMetrics
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
    
    def _save_generation_eval_sample(self, generated_answer: str, ground_truth_answer: str, combo_name: str, semantic_score: float):
        """Save the generated answer and ground truth to a JSON array file for inspection"""
        save_path = "generation_eval_samples.json"
        # Prepare the new pair
        # Use hash of ground_truth_answer and combo_name to form an id for new_pair
        import hashlib
        hash_input = (ground_truth_answer + "|" + combo_name).encode("utf-8")
        pair_id = hashlib.md5(hash_input).hexdigest()
        new_pair = {
            "id": pair_id,
            "generated_answer": generated_answer,
            "ground_truth_answer": ground_truth_answer,
            "combo_name": combo_name,
            "semantic_score": semantic_score
        }
        # Determine run_name and model
        run_name = getattr(self.global_config, "run_name", None)
        model = getattr(self.global_config, "llm_eval_model", None) or getattr(self.config_dict.get("generator", None), "model", "unknown_model")
        try:
            # Load existing data if present
            if os.path.exists(save_path):
                with open(save_path, "r+", encoding="utf-8") as f:
                    try:
                        data = json.load(f)
                        if not isinstance(data, list):
                            data = []
                    except Exception:
                        data = []
                    # Find if a run with this run_name exists
                    found = False
                    for entry in data:
                        if (
                            entry.get("run_name") == run_name
                            and isinstance(entry.get("gen_gt_pairs"), list)
                        ):
                            # Check if id already present in this run
                            if any(pair.get("id") == pair_id for pair in entry["gen_gt_pairs"]):
                                found = True  # run exists, but do not add duplicate
                                break
                            else:
                                entry["gen_gt_pairs"].append(new_pair)
                                found = True
                                break
                    if not found:
                        data.append({
                            "run_name": run_name,
                            "model": model,
                            "gen_gt_pairs": [new_pair]
                        })
                    f.seek(0)
                    json.dump(data, f, ensure_ascii=False, indent=2)
                    f.truncate()
            else:
                with open(save_path, "w", encoding="utf-8") as f:
                    json.dump([{
                        "run_name": run_name,
                        "model": model,
                        "gen_gt_pairs": [new_pair]
                    }], f, ensure_ascii=False, indent=2)
        except Exception as e:
            logger.error(f"Failed to save generation/ground truth sample: {e}")

    def _evaluate_generation(self, generated_answer: str, ground_truth_answer: str, combo_name: str) -> Dict[str, float]:
        """Evaluate generation performance"""
        if not generated_answer:
            return {'llm_score': 0.0, 'semantic_similarity': 0.0}
        
        try:
            # Semantic similarity evaluation
            semantic_score = self.semantic_evaluator.get_similarity_score(
                generated_answer,
                ground_truth_answer
            )

            if self.global_config.save_eval_cases:
                self._save_generation_eval_sample(
                    generated_answer=generated_answer,
                    ground_truth_answer=ground_truth_answer,
                    combo_name=combo_name,
                    semantic_score=semantic_score
                )
                llm_score = -1.0
            else:
                # LLM-based evaluation
                llm_score = self._llm_evaluate(
                    generated_answer, 
                    ground_truth_answer
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
            from rag_pipeline.util.api.gemini_client import GeminiUtil
            from rag_pipeline.util.api.ollama_client import OllamaUtil
            model = getattr(self.global_config, 'llm_eval_model', None) or getattr(self.config_dict.get('generator', None), 'model', 'gemma3:4b')
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
        weights = self.global_config.retrieval_weights
        return sum(weights[k] * retrieval_metrics[k] for k in weights)
    
    def _calculate_generation_score(self, generation_metrics: Dict[str, float]) -> float:
        """Calculate average generation score"""
        weights = self.global_config.generation_weights
        # Filter out metrics with value < 0.0
        valid_keys = [k for k in weights if generation_metrics[k] >= 0.0]
        if not valid_keys:
            return 0.0
        total_weight = sum(weights[k] for k in valid_keys)
        if total_weight == 0:
            return 0.0
        normalized_weights = {k: weights[k] / total_weight for k in valid_keys}
        score =  sum(normalized_weights[k] * generation_metrics[k] for k in valid_keys)
        logger.debug(f"Generation score: {score}")
        return score
    
    def _calculate_overall_score(self, retrieval_metrics: Dict[str, float], generation_metrics: Dict[str, float]) -> float:
        """Calculate weighted overall score"""
        overall_weights = self.global_config.overall_weights
        # Use the component score calculation methods
        retrieval_score = self._calculate_retrieval_score(retrieval_metrics)
        generation_score = self._calculate_generation_score(generation_metrics)
        
        overall_score = (overall_weights['retrieval'] * retrieval_score) + (overall_weights['generation'] * generation_score)
        return overall_score
    
    async def aggregate_results(self, results: List[RAGEvaluationResult]) -> Dict[str, float]:
        """Aggregate results for a single combo_name (modular pipeline) or multiple combos (legacy)."""
        # Canonical per-component timing keys
        timing_keys = [
            'pre_embedding_time', 'query_expansion_time', 'retrieval_time', 'passage_augment_time',
            'passage_rerank_time', 'passage_filter_time', 'passage_compress_time', 'prompt_maker_time',
            'generation_time', 'post_generation_time'
        ]
        # Canonical token count keys
        token_keys = [
            'embedding_token_counts', 'llm_token_counts'
        ]
        if results and all(hasattr(r, 'combo_name') for r in results):
            combo_names = set(getattr(r, 'combo_name', None) for r in results)
            if len(combo_names) == 1:
                successful_results = [r for r in results if not r.error]
                if not successful_results:
                    return {
                        'recall_at_k': 0.0, 'map_score': 0.0, 'ndcg_at_k': 0.0, 'mrr': 0.0, 'eval_k': self.config_dict['retrieval'].top_k,
                        'llm_score': 0.0, 'semantic_similarity': 0.0,
                        'retrieval_score': 0.0, 'generation_score': 0.0, 'overall_score': 0.0,
                        **{k: 0.0 for k in timing_keys},
                        'total_prediction_time': 0.0,
                        'retrieval_evaluation_time': 0.0, 'generation_evaluation_time': 0.0, 'total_eval_time': 0.0,
                        'success_rate': 0.0, 'test_count': len(results),
                        'embedding_token_counts': {}, 'llm_token_counts': {}
                    }

                avg_metrics = {
                    'recall_at_k': sum(r.metrics.recall_at_k for r in successful_results) / len(successful_results),
                    'map_score': sum(r.metrics.map_score for r in successful_results) / len(successful_results),
                    'ndcg_at_k': sum(r.metrics.ndcg_at_k for r in successful_results) / len(successful_results),
                    'mrr': sum(r.metrics.mrr for r in successful_results) / len(successful_results),
                    'eval_k': successful_results[0].metrics.eval_k if successful_results else self.config_dict['retrieval'].top_k,
                    'llm_score': sum(r.metrics.llm_score for r in successful_results) / len(successful_results),
                    'semantic_similarity': sum(r.metrics.semantic_similarity for r in successful_results) / len(successful_results),
                    'retrieval_score': sum(r.metrics.retrieval_score for r in successful_results) / len(successful_results),
                    'generation_score': sum(r.metrics.generation_score for r in successful_results) / len(successful_results),
                    'overall_score': sum(r.metrics.overall_score for r in successful_results) / len(successful_results),
                }
                # Per-component averages
                for key in timing_keys:
                    vals = [getattr(r.retrieval_result, key, 0.0) for r in successful_results]
                    avg_metrics[key] = sum(vals) / len(vals) if vals else 0.0
                # Total prediction time (sum of all per-component times)
                total_pred_times = [sum(getattr(r.retrieval_result, k, 0.0) for k in timing_keys) for r in successful_results]
                avg_metrics['total_prediction_time'] = sum(total_pred_times) / len(total_pred_times) if total_pred_times else 0.0
                # Evaluation timing
                avg_metrics['retrieval_evaluation_time'] = sum(r.retrieval_eval_time for r in successful_results) / len(successful_results)
                avg_metrics['generation_evaluation_time'] = sum(r.generation_eval_time for r in successful_results) / len(successful_results)
                avg_metrics['total_eval_time'] = sum(r.total_eval_time for r in successful_results) / len(successful_results)
                avg_metrics['success_rate'] = len(successful_results) / len(results)
                avg_metrics['test_count'] = len(results)
                # Aggregate token counts per component
                for token_key in token_keys:
                    if token_key == 'embedding_token_counts':
                        # Handle embedding token counts (simple dict)
                        all_keys = set()
                        for r in successful_results:
                            d = getattr(r.retrieval_result, token_key, {})
                            all_keys.update(d.keys())
                            d2 = getattr(r.generation_result, token_key, {})
                            all_keys.update(d2.keys())
                        avg_token_counts = {}
                        for comp in all_keys:
                            vals = []
                            for r in successful_results:
                                v1 = getattr(r.retrieval_result, token_key, {}).get(comp, 0.0)
                                v2 = getattr(r.generation_result, token_key, {}).get(comp, 0.0)
                                if v1 > 0.0:
                                    vals.append(v1)
                                if v2 > 0.0:
                                    vals.append(v2)
                            avg_token_counts[comp] = sum(vals) / len(vals) if vals else 0.0
                        avg_metrics[token_key] = avg_token_counts
                    elif token_key == 'llm_token_counts':
                        # Handle LLM token counts (nested dict structure)
                        all_components = set()
                        all_models = set()
                        for r in successful_results:
                            d1 = getattr(r.retrieval_result, token_key, {})
                            d2 = getattr(r.generation_result, token_key, {})
                            all_components.update(d1.keys())
                            all_components.update(d2.keys())
                            for comp in d1:
                                all_models.update(d1[comp].keys())
                            for comp in d2:
                                all_models.update(d2[comp].keys())
                        
                        avg_llm_token_counts = {}
                        for comp in all_components:
                            avg_llm_token_counts[comp] = {}
                            for model in all_models:
                                in_vals = []
                                out_vals = []
                                for r in successful_results:
                                    d1 = getattr(r.retrieval_result, token_key, {}).get(comp, {})
                                    d2 = getattr(r.generation_result, token_key, {}).get(comp, {})
                                    model_data1 = d1.get(model, {})
                                    model_data2 = d2.get(model, {})
                                    if model_data1.get('in', 0.0) > 0.0:
                                        in_vals.append(model_data1['in'])
                                    if model_data1.get('out', 0.0) > 0.0:
                                        out_vals.append(model_data1['out'])
                                    if model_data2.get('in', 0.0) > 0.0:
                                        in_vals.append(model_data2['in'])
                                    if model_data2.get('out', 0.0) > 0.0:
                                        out_vals.append(model_data2['out'])
                                avg_llm_token_counts[comp][model] = {
                                    'in': sum(in_vals) / len(in_vals) if in_vals else 0.0,
                                    'out': sum(out_vals) / len(out_vals) if out_vals else 0.0
                                }
                        avg_metrics[token_key] = avg_llm_token_counts
                return avg_metrics
        return {}