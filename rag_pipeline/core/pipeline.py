import asyncio
import logging
import time
from typing import List, Dict, Any, Optional
from itertools import product

from .models import (
    RAGConfig, RAGTestCase, RAGEvaluationResult, 
    RAGBenchmarkResult, RetrievalResult, GenerationResult,
    ModelCombination
)
from .components import ComponentFactory
from .evaluator import RAGEvaluator
from .dataset import RAGDataset

logger = logging.getLogger(__name__)

class RAGPipeline:
    """Main RAG evaluation pipeline that orchestrates retrieval, generation, and evaluation"""
    
    def __init__(self, config: RAGConfig):
        self.config = config
        self.dataset = RAGDataset(config.dataset_path)
        self.evaluator = RAGEvaluator(config)
        
        # Initialize components for all model combinations
        self.retrieval_components = {}
        self.generation_components = {}
        self._initialize_components()
    
    def _initialize_components(self):
        """Initialize retrieval and generation components for all models"""
        logger.info("Initializing RAG components...")
        
        # Initialize retrieval components for each embedding model
        for embedding_model in self.config.embedding_models:
            try:
                component = ComponentFactory.create_retrieval_component(
                    embedding_model, self.config
                )
                self.retrieval_components[embedding_model] = component
                logger.info(f"Initialized retrieval component for {embedding_model}")
            except Exception as e:
                logger.error(f"Failed to initialize retrieval component for {embedding_model}: {e}")
        
        # Initialize generation components for each LLM model
        for llm_model in self.config.llm_models:
            try:
                component_type = "gemini" if llm_model.lower().startswith("gemini") else "ollama"
                component = ComponentFactory.create_generation_component(
                    llm_model, self.config, component_type
                )
                self.generation_components[llm_model] = component
                logger.info(f"Initialized generation component for {llm_model}")
            except Exception as e:
                logger.error(f"Failed to initialize generation component for {llm_model}: {e}")
    
    def _generate_model_combinations(self) -> List[ModelCombination]:
        """Generate exactly 4 model combinations when both rerankers are enabled:
        1. No reranking
        2. Only LLM reranking  
        3. Only cross-encoder reranking
        4. Parallel LLM + CE reranking
        """
        combinations = []
        
        # Check if both rerankers are available
        has_cross_encoder = self.config.rerank_model is not None
        has_llm_reranker = self.config.llm_rerank_model is not None
        
        # Generate combinations for each embedding × LLM pair
        for embedding_model in self.config.embedding_models:
            for llm_model in self.config.llm_models:
                
                if has_cross_encoder and has_llm_reranker:
                    # When both rerankers are available, create exactly 4 combinations:
                    
                    # 1. No reranking
                    combinations.append(ModelCombination(
                        embedding_model=embedding_model,
                        llm_model=llm_model,
                        use_reranking=False,
                        rerank_model=None,
                        use_llm_reranking=False,
                        llm_rerank_model=None,
                        use_parallel_reranking=False
                    ))
                    
                    # 2. Only LLM reranking
                    combinations.append(ModelCombination(
                        embedding_model=embedding_model,
                        llm_model=llm_model,
                        use_reranking=False,
                        rerank_model=None,
                        use_llm_reranking=True,
                        llm_rerank_model=self.config.llm_rerank_model,
                        use_parallel_reranking=False
                    ))
                    
                    # 3. Only cross-encoder reranking
                    combinations.append(ModelCombination(
                        embedding_model=embedding_model,
                        llm_model=llm_model,
                        use_reranking=True,
                        rerank_model=self.config.rerank_model,
                        use_llm_reranking=False,
                        llm_rerank_model=None,
                        use_parallel_reranking=False
                    ))
                    
                    # 4. Parallel LLM + CE reranking (only if enabled in config)
                    if self.config.enable_parallel_reranking:
                        combinations.append(ModelCombination(
                            embedding_model=embedding_model,
                            llm_model=llm_model,
                            use_reranking=True,
                            rerank_model=self.config.rerank_model,
                            use_llm_reranking=True,
                            llm_rerank_model=self.config.llm_rerank_model,
                            use_parallel_reranking=True
                        ))
                        
                elif has_cross_encoder:
                    # Only cross-encoder available
                    combinations.append(ModelCombination(
                        embedding_model=embedding_model,
                        llm_model=llm_model,
                        use_reranking=False,
                        rerank_model=None,
                        use_llm_reranking=False,
                        llm_rerank_model=None,
                        use_parallel_reranking=False
                    ))
                    
                    if self.config.test_with_and_without_reranking:
                        combinations.append(ModelCombination(
                            embedding_model=embedding_model,
                            llm_model=llm_model,
                            use_reranking=True,
                            rerank_model=self.config.rerank_model,
                            use_llm_reranking=False,
                            llm_rerank_model=None,
                            use_parallel_reranking=False
                        ))
                        
                elif has_llm_reranker:
                    # Only LLM reranker available
                    combinations.append(ModelCombination(
                        embedding_model=embedding_model,
                        llm_model=llm_model,
                        use_reranking=False,
                        rerank_model=None,
                        use_llm_reranking=False,
                        llm_rerank_model=None,
                        use_parallel_reranking=False
                    ))
                    
                    if self.config.test_with_and_without_llm_reranking:
                        combinations.append(ModelCombination(
                            embedding_model=embedding_model,
                            llm_model=llm_model,
                            use_reranking=False,
                            rerank_model=None,
                            use_llm_reranking=True,
                            llm_rerank_model=self.config.llm_rerank_model,
                            use_parallel_reranking=False
                        ))
                        
                else:
                    # No reranking available
                    combinations.append(ModelCombination(
                        embedding_model=embedding_model,
                        llm_model=llm_model,
                        use_reranking=False,
                        rerank_model=None,
                        use_llm_reranking=False,
                        llm_rerank_model=None,
                        use_parallel_reranking=False
                    ))
        
        return combinations
    
    async def run_evaluation(self) -> RAGBenchmarkResult:
        """Run complete RAG evaluation pipeline"""
        
        start_time = time.time()
        logger.info("Starting RAG evaluation pipeline...")
        
        # Load and validate dataset
        test_cases = self.dataset.get_test_cases(self.config.max_test_cases)
        documents = self.dataset.get_documents()
        
        validation_result = self.dataset.validate_dataset()
        if not validation_result["valid"]:
            logger.error(f"Dataset validation failed: {validation_result['issues']}")
            raise ValueError(f"Invalid dataset: {validation_result['issues']}")
        
        logger.info(f"Loaded {len(test_cases)} test cases and {len(documents)} documents")
        
        # Generate all model combinations including reranking variations
        model_combinations = self._generate_model_combinations()
        logger.info(f"Testing {len(model_combinations)} model combinations:")
        for combo in model_combinations:
            logger.info(f"  - {combo.get_combination_name()}")
        
        # Run evaluation for all combinations
        all_results = []
        
        for combination in model_combinations:
            logger.info(f"Evaluating combination: {combination.get_combination_name()}")
            
            combination_results = await self._evaluate_model_combination(
                combination, test_cases
            )
            all_results.extend(combination_results)
        
        # Aggregate results
        aggregated_metrics = await self.evaluator.aggregate_results(all_results)
        
        # Find best performing combinations
        best_combos = self._find_best_combinations(aggregated_metrics)
        
        # Calculate summary statistics
        successful_cases = sum(1 for result in all_results if not result.error)
        failed_cases = len(all_results) - successful_cases
        
        total_runtime = time.time() - start_time
        
        # Calculate timing breakdown
        successful_results = [r for r in all_results if not r.error]
        total_retrieval_prediction_time = sum(r.retrieval_result.retrieval_time for r in successful_results)
        total_generation_prediction_time = sum(r.generation_result.generation_time for r in successful_results)
        total_retrieval_evaluation_time = sum(r.retrieval_eval_time for r in successful_results)
        total_generation_evaluation_time = sum(r.generation_eval_time for r in successful_results)
        
        benchmark_result = RAGBenchmarkResult(
            config=self._config_to_dict(),
            individual_results=all_results,
            aggregated_metrics=aggregated_metrics,
            total_test_cases=len(test_cases),
            successful_cases=successful_cases,
            failed_cases=failed_cases,
            total_runtime=total_runtime,
            total_retrieval_prediction_time=total_retrieval_prediction_time,
            total_generation_prediction_time=total_generation_prediction_time,
            total_retrieval_evaluation_time=total_retrieval_evaluation_time,
            total_generation_evaluation_time=total_generation_evaluation_time,
            best_retrieval_combo=best_combos.get("retrieval"),
            best_generation_combo=best_combos.get("generation"), 
            best_overall_combo=best_combos.get("overall")
        )
        
        logger.info(f"RAG evaluation completed in {total_runtime:.2f}s")
        logger.info(f"Success rate: {successful_cases}/{len(all_results)} ({successful_cases/len(all_results)*100:.1f}%)")
        logger.info(f"Best overall combination: {best_combos.get('overall')}")
        
        return benchmark_result
    
    async def _evaluate_model_combination(
        self, 
        combination: ModelCombination, 
        test_cases: List[RAGTestCase]
    ) -> List[RAGEvaluationResult]:
        """Evaluate a specific model combination"""
        
        results = []
        
        # Get components for this combination
        retrieval_component = self.retrieval_components.get(combination.embedding_model)
        generation_component = self.generation_components.get(combination.llm_model)
        
        if not retrieval_component:
            logger.error(f"No retrieval component for {combination.embedding_model}")
            return []
        
        if not generation_component:
            logger.error(f"No generation component for {combination.llm_model}")
            return []
        
        # Process test cases in batches for efficiency
        batch_size = self.config.eval_batch_size
        for i in range(0, len(test_cases), batch_size):
            batch = test_cases[i:i + batch_size]
            
            # Process batch
            batch_results = await self._process_test_batch(
                batch, retrieval_component, generation_component, combination
            )
            results.extend(batch_results)
            
            logger.info(f"Processed batch {i//batch_size + 1}/{(len(test_cases)-1)//batch_size + 1} "
                       f"for {combination.get_combination_name()}")
        
        return results
    
    async def _process_test_batch(
        self,
        test_cases: List[RAGTestCase],
        retrieval_component,
        generation_component,
        combination: ModelCombination
    ) -> List[RAGEvaluationResult]:
        """Process a batch of test cases"""
        
        batch_results = []
        
        for test_case in test_cases:
            try:
                # Step 1: Retrieve relevant documents with reranking configuration
                retrieval_result = await retrieval_component.retrieve(
                    test_case.query, self.config.retrieval_k, combination
                )
                
                # Step 2: Format context from retrieved documents
                context = self._format_context(retrieval_result)
                
                # Step 3: Generate answer using LLM
                generation_result = await generation_component.generate(
                    test_case.query, context, retrieval_component.embedding_model
                )
                
                # Step 4: Evaluate the results
                evaluation_result = await self.evaluator.evaluate_single_case(
                    test_case, retrieval_result, generation_result
                )
                
                batch_results.append(evaluation_result)
                
            except Exception as e:
                logger.error(f"Failed to process test case {test_case.id}: {e}")
                # Create error result
                error_result = RAGEvaluationResult(
                    embedding_model=retrieval_component.embedding_model,
                    llm_model=generation_component.llm_model,
                    test_case_id=test_case.id,
                    retrieval_result=RetrievalResult(
                        query=test_case.query,
                        retrieved_docs=[],
                        embedding_model=retrieval_component.embedding_model,
                        retrieval_time=0.0,
                        error=str(e)
                    ),
                    generation_result=GenerationResult(
                        query=test_case.query,
                        context="",
                        generated_answer="",
                        llm_model=generation_component.llm_model,
                        embedding_model=retrieval_component.embedding_model,
                        generation_time=0.0,
                        error=str(e)
                    ),
                    metrics=None,
                    retrieval_eval_time=0.0,
                    generation_eval_time=0.0,
                    total_eval_time=0.0,
                    error=str(e)
                )
                batch_results.append(error_result)
        
        return batch_results
    
    def _format_context(self, retrieval_result: RetrievalResult) -> str:
        """Format retrieved documents into context string"""
        if retrieval_result.error or not retrieval_result.retrieved_docs:
            return ""
        
        context_parts = []
        for i, doc in enumerate(retrieval_result.retrieved_docs, 1):
            content = doc.get('content', '').strip()
            if content:
                context_parts.append(f"Document {i}:\n{content}")
        
        return "\n\n".join(context_parts)
    
    def _find_best_combinations(self, aggregated_metrics: Dict[str, Dict[str, float]]) -> Dict[str, str]:
        """Find best performing model combinations"""
        
        if not aggregated_metrics:
            return {}
        
        best_combinations = {}
        
        # Find best for retrieval (based on recall@k)
        best_retrieval_score = -1
        best_retrieval_combo = None
        
        # Find best for generation (based on llm_score + semantic_similarity)
        best_generation_score = -1
        best_generation_combo = None
        
        # Find best overall (based on overall_score)
        best_overall_score = -1
        best_overall_combo = None
        
        for combo, metrics in aggregated_metrics.items():
            # Use the averaged component scores
            retrieval_score = metrics.get('retrieval_score', 0)
            generation_score = metrics.get('generation_score', 0)
            
            if retrieval_score > best_retrieval_score:
                best_retrieval_score = retrieval_score
                best_retrieval_combo = combo
            
            if generation_score > best_generation_score:
                best_generation_score = generation_score
                best_generation_combo = combo
            
            # Overall score
            overall_score = metrics.get('overall_score', 0)
            
            if overall_score > best_overall_score:
                best_overall_score = overall_score
                best_overall_combo = combo
        
        return {
            'retrieval': best_retrieval_combo,
            'generation': best_generation_combo,
            'overall': best_overall_combo
        }
    
    def _config_to_dict(self) -> Dict[str, Any]:
        """Convert config to dictionary for serialization"""
        return {
            'embedding_models': self.config.embedding_models,
            'llm_models': self.config.llm_models,
            'eval_llm_model': self.config.eval_llm_model,
            'retrieval_k': self.config.retrieval_k,
            'retrieval_threshold': self.config.retrieval_threshold,
            'rerank_model': self.config.rerank_model,
            'rerank_top_k': self.config.rerank_top_k,
            'max_tokens': self.config.max_tokens,
            'temperature': self.config.temperature,
            'eval_batch_size': self.config.eval_batch_size,
            'max_test_cases': self.config.max_test_cases
        }
    
    def print_results_summary(self, result: RAGBenchmarkResult):
        """Print a nice summary of the evaluation results"""
        
        print("\n" + "="*60)
        print("              RAG EVALUATION RESULTS")
        print("="*60)
        
        print(f"\nDataset: {result.total_test_cases} test cases")
        total_results = len(result.individual_results)
        print(f"Success rate: {result.successful_cases}/{total_results} "
              f"({result.successful_cases/total_results*100:.1f}%)")
        print(f"Total runtime: {result.total_runtime:.2f}s")
        
        print(f"\nModel combinations tested: {len(result.aggregated_metrics)}")
        for combo in result.aggregated_metrics.keys():
            # Parse combination key that may include multiple rerank models (using || delimiter)
            combo_parts = combo.split('||')
            if len(combo_parts) == 2:
                # Format: embedding_model||llm_model (no reranking)
                emb_model, llm_model = combo_parts
                print(f"  • {emb_model} + {llm_model}")
            elif len(combo_parts) == 3:
                # Format: embedding_model||rerank_model||llm_model (single reranking)
                emb_model, rerank_model, llm_model = combo_parts
                print(f"  • {emb_model} + {rerank_model} + {llm_model}")
            elif len(combo_parts) == 4:
                # Format: embedding_model||ce_rerank||llm_rerank||llm_model (dual reranking)
                emb_model, ce_rerank, llm_rerank, llm_model = combo_parts
                print(f"  • {emb_model} + {ce_rerank} + {llm_rerank} + {llm_model}")
            else:
                # Fallback for unexpected format
                print(f"  • {combo.replace('||', ' + ')}")
        
        print(f"\n🏆 BEST PERFORMING COMBINATIONS:")
        print(f"  Retrieval: {result.best_retrieval_combo}")
        print(f"  Generation: {result.best_generation_combo}")
        print(f"  Overall: {result.best_overall_combo}")
        
        print(f"\n📊 DETAILED METRICS BY COMBINATION:")
        for combo, metrics in result.aggregated_metrics.items():
            # Parse combination key that may include multiple rerank models (using || delimiter)
            combo_parts = combo.split('||')
            if len(combo_parts) == 2:
                # Format: embedding_model||llm_model (no reranking)
                emb_model, llm_model = combo_parts
                combo_display = f"{emb_model} + {llm_model}"
            elif len(combo_parts) == 3:
                # Format: embedding_model||rerank_model||llm_model (single reranking)
                emb_model, rerank_model, llm_model = combo_parts
                combo_display = f"{emb_model} + {rerank_model} + {llm_model}"
            elif len(combo_parts) == 4:
                # Format: embedding_model||ce_rerank||llm_rerank||llm_model (dual reranking)
                emb_model, ce_rerank, llm_rerank, llm_model = combo_parts
                combo_display = f"{emb_model} + {ce_rerank} + {llm_rerank} + {llm_model}"
            else:
                # Fallback for unexpected format
                combo_display = combo.replace('||', ' + ')
            
            print(f"\n{combo_display}:")
            eval_k = metrics.get('eval_k', self.config.retrieval_k)
            print(f"  Retrieval: R@{eval_k}={metrics['recall_at_k']:.3f}, "
                  f"mAP={metrics['map_score']:.3f}, "
                  f"nDCG@{eval_k}={metrics['ndcg_at_k']:.3f}, "
                  f"MRR={metrics['mrr']:.3f}")
            if metrics['reranked']:
                print(f"  Cross-encoder Reranking: Model={metrics['rerank_model']}, "
                      f"Avg Time={metrics['rerank_time']:.3f}s")
            if metrics.get('llm_reranked', False):
                print(f"  LLM Reranking: Model={metrics.get('llm_rerank_model', 'N/A')}, "
                      f"Avg Time={metrics.get('llm_rerank_time', 0.0):.3f}s")
            print(f"  Generation: LLM={metrics['llm_score']:.3f}, "
                  f"Semantic={metrics['semantic_similarity']:.3f}")
            print(f"  Component Scores: Retrieval={metrics['retrieval_score']:.3f}, "
                  f"Generation={metrics['generation_score']:.3f}")
            print(f"  Overall Score: {metrics['overall_score']:.3f}")
            print(f"  Success Rate: {metrics['success_rate']:.1%}")
            print(f"  Avg Prediction Times: Retrieval={metrics['retrieval_prediction_time']:.3f}s, "
                  f"Generation={metrics['generation_prediction_time']:.3f}s")
            if metrics['reranked'] or metrics.get('llm_reranked', False):
                rerank_time_str = ""
                if metrics['reranked']:
                    rerank_time_str += f"CE: {metrics['rerank_time']:.3f}s"
                if metrics.get('llm_reranked', False):
                    if rerank_time_str:
                        rerank_time_str += ", "
                    rerank_time_str += f"LLM: {metrics.get('llm_rerank_time', 0.0):.3f}s"
                print(f"  Avg Rerank Times: {rerank_time_str}")
            print(f"  Avg Evaluation Times: Retrieval={metrics['retrieval_evaluation_time']:.3f}s, "
                  f"Generation={metrics['generation_evaluation_time']:.3f}s")
        
        # Timing breakdown summary
        total_prediction_time = result.total_retrieval_prediction_time + result.total_generation_prediction_time
        total_evaluation_time = result.total_retrieval_evaluation_time + result.total_generation_evaluation_time
        
        print(f"\n⏱️  TIMING BREAKDOWN:")
        print(f"  Prediction Times:")
        print(f"    Retrieval: {result.total_retrieval_prediction_time:.2f}s")
        print(f"    Generation: {result.total_generation_prediction_time:.2f}s")
        print(f"    Total Prediction: {total_prediction_time:.2f}s")
        print(f"  Evaluation Times:")
        print(f"    Retrieval: {result.total_retrieval_evaluation_time:.2f}s")
        print(f"    Generation: {result.total_generation_evaluation_time:.2f}s")
        print(f"    Total Evaluation: {total_evaluation_time:.2f}s")
        print(f"  Pipeline Total: {result.total_runtime:.2f}s")
        
        print("\n" + "="*60) 