"""
Modular RAG Pipeline

This module implements the main pipeline that orchestrates all RAG components
using the modular framework. It handles component initialization, execution,
and result aggregation.
"""

import asyncio
import logging
import time
from typing import List, Dict, Any, Optional, Type
from dataclasses import asdict

from .modular_framework import (
    PreEmbeddingComponent, QueryExpansionComponent, RetrievalComponent,
    PassageAugmentComponent, PassageRerankComponent, PassageFilterComponent,
    PassageCompressComponent, PromptMakerComponent, GeneratorComponent,
    PostGenerationComponent, Document, Query, Context, RAGExecutionResult
)
from .modular_configs import ModularRAGConfig
from .modular_implementations import COMPONENT_REGISTRY
# Add TypedDict imports for result types
from rag_pipeline.core.modular_implementations.pre_embedding import PreEmbeddingResult
from rag_pipeline.core.modular_implementations.query_expansion import QueryExpansionResult
from rag_pipeline.core.modular_implementations.retrieval import RetrievalResult as RetrievalComponentResult
from rag_pipeline.core.modular_implementations.passage_augment import PassageAugmentResult
from rag_pipeline.core.modular_implementations.passage_rerank import PassageRerankResult
from rag_pipeline.core.modular_implementations.passage_filter import PassageFilterResult
from rag_pipeline.core.modular_implementations.passage_compress import PassageCompressResult
from rag_pipeline.core.modular_implementations.prompt_maker import PromptMakerResult
from rag_pipeline.core.modular_implementations.generator import GeneratorResult
from rag_pipeline.core.modular_implementations.post_generation import PostGenerationResult
from .dataset import RAGDataset
from .evaluator import RAGEvaluator
from rag_pipeline.core.models import RetrievalResult, GenerationResult, RAGMetrics

logger = logging.getLogger(__name__)


class ModularComponentFactory:
    """Factory for creating modular RAG components"""
    
    @staticmethod
    def create_component(category: str, technique: str, config: Dict[str, Any]) -> Any:
        """
        Create a component instance based on category and technique.
        
        Args:
            category: Component category (e.g., 'retrieval', 'passage_rerank')
            technique: Specific technique (e.g., 'simple_vector_rag', 'cross_encoder')
            config: Configuration dictionary for the component
            
        Returns:
            Component instance
            
        Raises:
            ValueError: If category or technique is not found
        """
        if category not in COMPONENT_REGISTRY:
            raise ValueError(f"Unknown component category: {category}")
        
        category_components = COMPONENT_REGISTRY[category]
        if technique not in category_components:
            available = list(category_components.keys())
            raise ValueError(f"Unknown technique '{technique}' for category '{category}'. Available: {available}")
        
        component_class = category_components[technique]
        return component_class(config)
    
    @staticmethod
    def get_available_techniques(category: str) -> List[str]:
        """Get list of available techniques for a category"""
        if category not in COMPONENT_REGISTRY:
            return []
        return list(COMPONENT_REGISTRY[category].keys())
    
    @staticmethod
    def get_all_categories() -> List[str]:
        """Get list of all available categories"""
        return list(COMPONENT_REGISTRY.keys())


class ModularRAGPipeline:
    """
    Modular RAG Pipeline that executes the full RAG workflow
    using configurable components for each stage.
    """
    
    def __init__(self, config_dict: dict, global_config: ModularRAGConfig = None):
        """
        config_dict: dict mapping category name to config object for this run
        global_config: the full ModularRAGConfig (for dataset/global settings)
        """
        self.config_dict = config_dict
        self.global_config = global_config
        self.factory = ModularComponentFactory()
        # Use dataset/global settings from global_config if provided
        dataset_path = global_config.dataset_path if global_config else None
        self.dataset = RAGDataset(dataset_path)
        # self.evaluator = RAGEvaluator(global_config if global_config else config_dict)  # REMOVE THIS LINE
        # Initialize components
        self.components = {}
        self._initialize_components()
        # Setup logging
        if global_config and global_config.enable_logging:
            logging.basicConfig(level=getattr(logging, global_config.log_level))
    
    def _initialize_components(self):
        """Initialize all enabled components based on config_dict"""
        logger.info("Initializing modular RAG components...")
        for category, cfg in self.config_dict.items():
            if hasattr(cfg, "enabled") and not cfg.enabled:
                continue
            if hasattr(cfg, "technique"):
                self.components[category] = self.factory.create_component(
                    category, cfg.technique, cfg.dict()
                )
            elif hasattr(cfg, "model"):
                self.components[category] = self.factory.create_component(
                    category, "llm", cfg.dict()
                )
            else:
                self.components[category] = self.factory.create_component(
                    category, getattr(cfg, "technique", "none"), cfg.dict()
                )
        logger.info(f"Initialized {len(self.components)} component categories")
    
    def _parse_component_result(self, result: dict, component_name: str, embedding_token_counts: dict, llm_input_token_counts: dict, llm_output_token_counts: dict, main_output_key: str, extra_keys: list = None):
        """
        Helper to parse a component result dict, update token count dicts, and return main output (and extras if needed).
        """
        main_output = result.get(main_output_key)
        emb_count = result.get('embedding_token_count', 0.0)
        llm_in_count = result.get('llm_input_token_count', 0.0)
        llm_out_count = result.get('llm_output_token_count', 0.0)
        if emb_count > 0.0:
            embedding_token_counts[component_name] = emb_count
        if llm_in_count > 0.0:
            llm_input_token_counts[component_name] = llm_in_count
        if llm_out_count > 0.0:
            llm_output_token_counts[component_name] = llm_out_count
        extras = {}
        if extra_keys:
            for k in extra_keys:
                extras[k] = result.get(k)
        return (main_output, extras) if extras else main_output

    async def execute_pipeline(self, query: str, documents: Optional[List[Document]] = None) -> RAGExecutionResult:
        """
        Execute the full RAG pipeline for a single query.
        
        Args:
            query: Input query string
            documents: Optional list of documents to index/search (if None, uses existing index)
            
        Returns:
            RAGExecutionResult with all intermediate and final results
        """
        start_time = time.time()
        timing_info = {}
        
        try:
            # Initialize result tracking
            components_used = {}
            embedding_token_counts = {}
            llm_input_token_counts = {}
            llm_output_token_counts = {}
            
            # Step 1: Pre-embedding (document preprocessing)
            if documents and "pre_embedding" in self.components:
                step_start = time.time()
                pre_embedding_result: PreEmbeddingResult = await self.components["pre_embedding"].process_documents(documents)
                documents, extras = self._parse_component_result(
                    pre_embedding_result, "pre_embedding", embedding_token_counts, llm_input_token_counts, llm_output_token_counts,
                    main_output_key='documents_to_embed', extra_keys=['documents_for_metadata']
                )
                documents_for_metadata = extras['documents_for_metadata']
                timing_info["pre_embedding_time"] = time.time() - step_start
                components_used["pre_embedding"] = self.config_dict["pre_embedding"].technique
                logger.debug(f"Pre-embedding completed in {timing_info['pre_embedding_time']:.3f}s")
            else:
                timing_info["pre_embedding_time"] = 0.0
            
            # Step 2: Query expansion/refinement
            if "query_expansion" in self.components:
                step_start = time.time()
                query_expansion_result: QueryExpansionResult = await self.components["query_expansion"].expand_query(query)
                processed_query = self._parse_component_result(
                    query_expansion_result, "query_expansion", embedding_token_counts, llm_input_token_counts, llm_output_token_counts,
                    main_output_key='query'
                )
                timing_info["query_expansion_time"] = time.time() - step_start
                components_used["query_expansion"] = self.config_dict["query_expansion"].technique
                logger.debug(f"Query expansion completed in {timing_info['query_expansion_time']:.3f}s")
            else:
                processed_query = Query(original_text=query, processed_text=query)
                timing_info["query_expansion_time"] = 0.0
            
            # Step 3: Retrieval
            retrieved_documents = []
            if "retrieval" in self.components:
                step_start = time.time()
                if documents:
                    await self.components["retrieval"].index_documents(documents)
                if "query_expansion" not in self.components or self.config_dict["query_expansion"].technique == "none":
                    retrieval_result: RetrievalComponentResult = await self.components["retrieval"].retrieve(
                        processed_query, 
                        k=self.config_dict["retrieval"].top_k
                    )
                    retrieved_documents = self._parse_component_result(
                        retrieval_result, "retrieval", embedding_token_counts, llm_input_token_counts, llm_output_token_counts,
                        main_output_key='documents'
                    )
                else:
                    from rag_pipeline.util.retrieval_utils.combination_utils import HybridUtils
                    results_list = []
                    for expanded_query in processed_query.expanded_queries:
                        retrieval_result: RetrievalComponentResult = await self.components["retrieval"].retrieve(
                            expanded_query, 
                            k=self.config_dict["retrieval"].top_k
                        )
                        parsed_result = self._parse_component_result(
                            retrieval_result, "retrieval", embedding_token_counts, llm_input_token_counts, llm_output_token_counts,
                            main_output_key='documents'
                        )
                        results_list.append(HybridUtils.convert_documents_to_results(parsed_result))
                    combination_method = self.config_dict["query_expansion"].combination_method
                    if combination_method == "convex_combination":
                        weights = [1/len(processed_query.expanded_queries) for _ in range(len(processed_query.expanded_queries))]
                        retrieved_documents = HybridUtils.combine_with_convex_combination(
                            results_list=results_list,
                            method_names=[f"retrieval_query_{i}" for i in range(len(processed_query.expanded_queries))],
                            weights=weights,
                            normalization_method=self.config_dict["query_expansion"].normalization_method,
                            excessive_k=self.config_dict["query_expansion"].excessive_k
                        )
                    elif combination_method == "reciprocal_rank_fusion":
                        retrieved_documents = HybridUtils.combine_with_rrf(
                            results_list=results_list,
                            method_names=[f"retrieval_query_{i}" for i in range(len(processed_query.expanded_queries))],
                            excessive_k=self.config_dict["query_expansion"].excessive_k
                        )
                    elif combination_method == "borda_count":
                        retrieved_documents = HybridUtils.combine_with_borda_count(
                            results_list=results_list,
                            method_names=[f"retrieval_query_{i}" for i in range(len(processed_query.expanded_queries))],
                            excessive_k=self.config_dict["query_expansion"].excessive_k
                        )
                    else:
                        retrieved_documents = results_list[0]
                        raise ValueError(f"Invalid combination method: {combination_method}")
                    retrieved_documents = HybridUtils.convert_to_documents(retrieved_documents)

                timing_info["retrieval_time"] = time.time() - step_start
                components_used["retrieval"] = self.config_dict["retrieval"].technique
                logger.debug(f"Retrieval completed in {timing_info['retrieval_time']:.3f}s, found {len(retrieved_documents)} documents")
            else:
                timing_info["retrieval_time"] = 0.0
            
            # Step 4: Passage augmentation
            if "passage_augment" in self.components and retrieved_documents:
                step_start = time.time()
                passage_augment_result: PassageAugmentResult = await self.components["passage_augment"].augment_passages(
                    retrieved_documents, processed_query
                )
                retrieved_documents = self._parse_component_result(
                    passage_augment_result, "passage_augment", embedding_token_counts, llm_input_token_counts, llm_output_token_counts,
                    main_output_key='documents'
                )
                timing_info["passage_augment_time"] = time.time() - step_start
                components_used["passage_augment"] = self.config_dict["passage_augment"].technique
                logger.debug(f"Passage augmentation completed in {timing_info['passage_augment_time']:.3f}s")
            else:
                timing_info["passage_augment_time"] = 0.0
            
            # Step 5: Passage reranking (can have multiple rerankers)
            if "passage_rerank" in self.components and retrieved_documents:
                step_start = time.time()
                passage_rerank_result: PassageRerankResult = await self.components["passage_rerank"].rerank_passages(retrieved_documents, processed_query)
                retrieved_documents = self._parse_component_result(
                    passage_rerank_result, "passage_rerank", embedding_token_counts, llm_input_token_counts, llm_output_token_counts,
                    main_output_key='documents'
                )
                timing_info["passage_rerank_time"] = time.time() - step_start
                components_used["passage_rerank"] = self.config_dict["passage_rerank"].technique
                logger.debug(f"Passage reranking completed in {timing_info['passage_rerank_time']:.3f}s")
            else:
                timing_info["passage_rerank_time"] = 0.0
            
            # Step 6: Passage filtering (can have multiple filters)
            if "passage_filter" in self.components and retrieved_documents:
                step_start = time.time()
                passage_filter_result: PassageFilterResult = await self.components["passage_filter"].filter_passages(retrieved_documents, processed_query)
                retrieved_documents = self._parse_component_result(
                    passage_filter_result, "passage_filter", embedding_token_counts, llm_input_token_counts, llm_output_token_counts,
                    main_output_key='documents'
                )
                timing_info["passage_filter_time"] = time.time() - step_start
                components_used["passage_filter"] = self.config_dict["passage_filter"].technique
                logger.debug(f"Passage filtering completed in {timing_info['passage_filter_time']:.3f}s, kept {len(retrieved_documents)} documents")
            else:
                timing_info["passage_filter_time"] = 0.0
            
            # Step 7: Passage compression
            final_documents = retrieved_documents
            if "passage_compress" in self.components and retrieved_documents:
                step_start = time.time()
                passage_compress_result: PassageCompressResult = await self.components["passage_compress"].compress_passages(
                    retrieved_documents, processed_query
                )
                final_documents = self._parse_component_result(
                    passage_compress_result, "passage_compress", embedding_token_counts, llm_input_token_counts, llm_output_token_counts,
                    main_output_key='documents'
                )
                timing_info["passage_compress_time"] = time.time() - step_start
                components_used["passage_compress"] = self.config_dict["passage_compress"].technique
                logger.debug(f"Passage compression completed in {timing_info['passage_compress_time']:.3f}s")
            else:
                timing_info["passage_compress_time"] = 0.0
            
            # Step 8: Prompt making
            prompt = ""
            if "prompt_maker" in self.components:
                step_start = time.time()
                prompt_maker_result: PromptMakerResult = await self.components["prompt_maker"].make_prompt(processed_query, final_documents)
                prompt = self._parse_component_result(
                    prompt_maker_result, "prompt_maker", embedding_token_counts, llm_input_token_counts, llm_output_token_counts,
                    main_output_key='text'
                )
                timing_info["prompt_maker_time"] = time.time() - step_start
                components_used["prompt_maker"] = self.config_dict["prompt_maker"].technique
                logger.debug(f"Prompt making completed in {timing_info['prompt_maker_time']:.3f}s")
            else:
                timing_info["prompt_maker_time"] = 0.0
            
            # Step 9: Generation
            generated_answer = ""
            gen_prompt_tokens = 0
            gen_eval_count = 0
            step_start = time.time()
            if "generator" in self.components:
                if prompt:
                    gen_result: GeneratorResult = await self.components["generator"].generate(prompt, processed_query)
                    if isinstance(gen_result, dict):
                        generated_answer = self._parse_component_result(
                            gen_result, "generation", embedding_token_counts, llm_input_token_counts, llm_output_token_counts,
                            main_output_key='text'
                        )
                    else:
                        generated_answer = gen_result if isinstance(gen_result, str) else ""
                else:
                    logger.warning("Prompt is empty, skipping generation step.")
                timing_info["generation_time"] = time.time() - step_start
                components_used["generator"] = self.config_dict["generator"].model
                logger.debug(f"Generation completed in {timing_info['generation_time']:.3f}s")
            else:
                timing_info["generation_time"] = 0.0
            
            # Step 10: Post-generation
            final_answer = generated_answer
            if "post_generation" in self.components and generated_answer:
                step_start = time.time()
                context = Context(documents=final_documents, formatted_text=prompt)
                post_generation_result: PostGenerationResult = await self.components["post_generation"].post_process(
                    generated_answer, processed_query, context
                )
                final_answer = self._parse_component_result(
                    post_generation_result, "post_generation", embedding_token_counts, llm_input_token_counts, llm_output_token_counts,
                    main_output_key='text'
                )
                timing_info["post_generation_time"] = time.time() - step_start
                components_used["post_generation"] = self.config_dict["post_generation"].technique
                logger.debug(f"Post-generation completed in {timing_info['post_generation_time']:.3f}s")
            else:
                timing_info["post_generation_time"] = 0.0
            
            # Calculate total time
            total_time = time.time() - start_time
            
            # Create result
            result = RAGExecutionResult(
                original_query=query,
                processed_query=processed_query,
                retrieved_documents=retrieved_documents,
                final_documents=final_documents,
                prompt=prompt,
                generated_answer=generated_answer,
                final_answer=final_answer,
                components_used=components_used,
                total_time=total_time,
                **timing_info,
                embedding_token_counts=embedding_token_counts,
                llm_input_token_counts=llm_input_token_counts,
                llm_output_token_counts=llm_output_token_counts
            )
            
            logger.info(f"Pipeline execution completed in {total_time:.3f}s")
            return result
            
        except Exception as e:
            logger.error(f"Pipeline execution failed: {e}")
            # Return error result
            return RAGExecutionResult(
                original_query=query,
                processed_query=Query(original_text=query, processed_text=query),
                retrieved_documents=[],
                final_documents=[],
                prompt="",
                generated_answer="",
                final_answer=f"Error: {str(e)}",
                components_used={},
                total_time=time.time() - start_time
            )
    
    @staticmethod
    def build_combo_name(config_dict: dict) -> str:
        """Build a combination name as 'category:name + ...' ignoring None names"""
        parts = []
        for cat, cfg in config_dict.items():
            n = getattr(cfg, "name", None)
            if n:
                parts.append(f"{cat}:{n}")
        return " + ".join(parts)

    @staticmethod
    async def run_evaluation(config_combo: dict, global_config: ModularRAGConfig) -> Any:
        """
        Run evaluation for all technique combinations, aggregate results, and find best combos.
        Returns a RAGBenchmarkResult (or similar structure).
        """
        import copy
        from .models import RAGTestCase, RetrievalResult, GenerationResult, RAGEvaluationResult, RAGBenchmarkResult
        import time

        start_time = time.time()
        logger.info("Starting modular RAG evaluation pipeline...")

        # Load dataset and test cases
        dataset = RAGDataset(global_config.dataset_path)
        test_cases = dataset.get_test_cases(global_config.max_test_cases)
        documents = dataset.get_documents()
        validation_result = dataset.validate_dataset()
        if not validation_result["valid"]:
            logger.error(f"Dataset validation failed: {validation_result['issues']}")
            raise ValueError(f"Invalid dataset: {validation_result['issues']}")
        logger.info(f"Loaded {len(test_cases)} test cases and {len(documents)} documents")

        # Generate all technique combinations
        technique_combos = global_config.create_config_combinations()
        logger.info(f"Testing {len(technique_combos)} technique combinations:")
        for combo in technique_combos:
            logger.debug(f"  - {combo}")

        all_results = []
        for combo in technique_combos:
            combo_name = ModularRAGPipeline.build_combo_name(combo)
            pipeline = ModularRAGPipeline.from_config_combo(combo, global_config)
            batch_size = global_config.eval_batch_size
            evaluator = RAGEvaluator(combo, global_config)
            for i in range(0, len(test_cases), batch_size):
                batch = test_cases[i:i + batch_size]
                logger.info(f"Processing batch {i//batch_size + 1} of {len(test_cases)//batch_size}")
                for test_case in batch:
                    try:
                        exec_result = await pipeline.execute_pipeline(test_case.query, documents)
                        retrieved_docs = [
                            {"doc_id": doc.doc_id, "content": doc.content, "score": getattr(doc, 'score', None)}
                            for doc in exec_result.retrieved_documents
                        ]
                        retrieval_result = RetrievalResult(
                            query=test_case.query,
                            retrieved_docs=retrieved_docs,
                            embedding_model=getattr(combo["retrieval"], 'embedding_model', 'unknown'),
                            pre_embedding_time=getattr(exec_result, 'pre_embedding_time', 0.0),
                            query_expansion_time=getattr(exec_result, 'query_expansion_time', 0.0),
                            retrieval_time=getattr(exec_result, 'retrieval_time', 0.0),
                            passage_augment_time=getattr(exec_result, 'passage_augment_time', 0.0),
                            passage_rerank_time=getattr(exec_result, 'passage_rerank_time', 0.0),
                            passage_filter_time=getattr(exec_result, 'passage_filter_time', 0.0),
                            passage_compress_time=getattr(exec_result, 'passage_compress_time', 0.0),
                            prompt_maker_time=getattr(exec_result, 'prompt_maker_time', 0.0),
                            generation_time=getattr(exec_result, 'generation_time', 0.0),
                            post_generation_time=getattr(exec_result, 'post_generation_time', 0.0),
                            embedding_token_counts=getattr(exec_result, 'embedding_token_counts', {}),
                            llm_input_token_counts=getattr(exec_result, 'llm_input_token_counts', {}),
                            llm_output_token_counts=getattr(exec_result, 'llm_output_token_counts', {}),
                            error=None
                        )
                        generation_result = GenerationResult(
                            query=test_case.query,
                            context=exec_result.prompt,
                            generated_answer=exec_result.generated_answer,
                            llm_model=getattr(combo["generator"], 'model', 'unknown'),
                            embedding_model=getattr(combo["retrieval"], 'embedding_model', 'unknown'),
                            pre_embedding_time=getattr(exec_result, 'pre_embedding_time', 0.0),
                            query_expansion_time=getattr(exec_result, 'query_expansion_time', 0.0),
                            retrieval_time=getattr(exec_result, 'retrieval_time', 0.0),
                            passage_augment_time=getattr(exec_result, 'passage_augment_time', 0.0),
                            passage_rerank_time=getattr(exec_result, 'passage_rerank_time', 0.0),
                            passage_filter_time=getattr(exec_result, 'passage_filter_time', 0.0),
                            passage_compress_time=getattr(exec_result, 'passage_compress_time', 0.0),
                            prompt_maker_time=getattr(exec_result, 'prompt_maker_time', 0.0),
                            generation_time=getattr(exec_result, 'generation_time', 0.0),
                            post_generation_time=getattr(exec_result, 'post_generation_time', 0.0),
                            embedding_token_counts=getattr(exec_result, 'embedding_token_counts', {}),
                            llm_input_token_counts=getattr(exec_result, 'llm_input_token_counts', {}),
                            llm_output_token_counts=getattr(exec_result, 'llm_output_token_counts', {}),
                            error=None
                        )
                        eval_result = await evaluator.evaluate_single_case(
                            test_case, retrieval_result, generation_result
                        )
                        # Attach combo_name to the result for aggregation
                        eval_result.combo_name = combo_name
                        all_results.append(eval_result)
                    except Exception as e:
                        logger.error(f"Failed to process test case {test_case.id} for combo {combo}: {e}")
                        error_result = RAGEvaluationResult(
                            embedding_model=getattr(combo["retrieval"], 'embedding_model', 'unknown'),
                            llm_model=getattr(combo["generator"], 'model', 'unknown'),
                            test_case_id=test_case.id,
                            retrieval_result=RetrievalResult(
                                query=test_case.query,
                                retrieved_docs=[],
                                embedding_model=getattr(combo["retrieval"], 'embedding_model', 'unknown'),
                                retrieval_time=0.0
                            ),
                            generation_result=GenerationResult(
                                query=test_case.query,
                                context="",
                                generated_answer="",
                                llm_model=getattr(combo["generator"], 'model', 'unknown'),
                                embedding_model=getattr(combo["retrieval"], 'embedding_model', 'unknown'),
                                generation_time=0.0
                            ),
                            metrics=RAGMetrics(
                                recall_at_k=0.0, map_score=0.0, ndcg_at_k=0.0, mrr=0.0, eval_k=0,
                                llm_score=0.0, semantic_similarity=0.0,
                                retrieval_score=0.0, generation_score=0.0, overall_score=0.0
                            ),
                            retrieval_eval_time=0.0,
                            generation_eval_time=0.0,
                            total_eval_time=0.0,
                            error=str(e)
                        )
                        error_result.combo_name = combo_name
                        all_results.append(error_result)
        # Aggregate results by combo_name
        from collections import defaultdict
        results_by_combo = defaultdict(list)
        for r in all_results:
            results_by_combo[getattr(r, 'combo_name', 'unknown')].append(r)
        # Use the first evaluator for aggregation (all evaluators are equivalent for aggregation)
        aggregated_metrics = {}
        for combo_name, results in results_by_combo.items():
            aggregated_metrics[combo_name] = await evaluator.aggregate_results(results)
        # Find best performing combinations (reuse logic from previous pipeline)
        def _find_best_combinations(aggregated_metrics):
            if not aggregated_metrics:
                return {}
            best_combinations = {}
            best_retrieval_score = -1
            best_retrieval_combo = None
            best_generation_score = -1
            best_generation_combo = None
            best_overall_score = -1
            best_overall_combo = None
            for combo, metrics in aggregated_metrics.items():
                retrieval_score = metrics.get('retrieval_score', 0)
                generation_score = metrics.get('generation_score', 0)
                if retrieval_score > best_retrieval_score:
                    best_retrieval_score = retrieval_score
                    best_retrieval_combo = combo
                if generation_score > best_generation_score:
                    best_generation_score = generation_score
                    best_generation_combo = combo
                overall_score = metrics.get('overall_score', 0)
                if overall_score > best_overall_score:
                    best_overall_score = overall_score
                    best_overall_combo = combo
            return {
                'retrieval': best_retrieval_combo,
                'generation': best_generation_combo,
                'overall': best_overall_combo
            }
        best_combos = _find_best_combinations(aggregated_metrics)
        # Timing breakdown
        successful_results = [r for r in all_results if not getattr(r, 'error', None)]
        # Only evaluation times are aggregated here
        total_retrieval_evaluation_time = sum(getattr(r, 'retrieval_eval_time', 0.0) for r in successful_results)
        total_generation_evaluation_time = sum(getattr(r, 'generation_eval_time', 0.0) for r in successful_results)
        total_runtime = time.time() - start_time
        benchmark_result = RAGBenchmarkResult(
            config=global_config.dict() if hasattr(global_config, 'dict') else str(global_config),
            individual_results=all_results,
            aggregated_metrics=aggregated_metrics,
            total_test_cases=len(test_cases),
            successful_cases=len(successful_results),
            failed_cases=len(all_results) - len(successful_results),
            total_runtime=total_runtime,
            total_retrieval_evaluation_time=total_retrieval_evaluation_time,
            total_generation_evaluation_time=total_generation_evaluation_time,
            best_retrieval_combo=best_combos.get('retrieval'),
            best_generation_combo=best_combos.get('generation'),
            best_overall_combo=best_combos.get('overall')
        )
        logger.info(f"Modular RAG evaluation completed in {total_runtime:.2f}s")
        logger.info(f"Success rate: {len(successful_results)}/{len(all_results)} ({len(successful_results)/len(all_results)*100:.1f}%)")
        logger.info(f"Best overall combination: {best_combos.get('overall')}")
        return benchmark_result
    
    def get_pipeline_info(self) -> Dict[str, Any]:
        """Get information about the configured pipeline"""
        info = {
            "pipeline_name": self.global_config.pipeline_name if self.global_config else "N/A",
            "enabled_components": {},
            "component_details": {}
        }
        
        # Add component information
        for category, component in self.components.items():
            if isinstance(component, list):
                info["enabled_components"][category] = f"{len(component)} techniques"
                info["component_details"][category] = [type(c).__name__ for c in component]
            else:
                info["enabled_components"][category] = type(component).__name__
                info["component_details"][category] = type(component).__name__
        
        return info
    
    def validate_configuration(self) -> Dict[str, Any]:
        """Validate the pipeline configuration"""
        validation_result = {
            "valid": True,
            "warnings": [],
            "errors": []
        }
        
        # Check if at least retrieval and generator are enabled
        if not self.config_dict["retrieval"].enabled:
            validation_result["errors"].append("Retrieval component must be enabled")
            validation_result["valid"] = False
        
        if not self.config_dict["generator"].enabled:
            validation_result["errors"].append("Generator component must be enabled")
            validation_result["valid"] = False
        
        # Check for conflicting configurations
        if (self.config_dict["passage_rerank"].enabled and 
            "cross_encoder" in self.config_dict["passage_rerank"].technique and
            "llm_rerank" in self.config_dict["passage_rerank"].technique):
            validation_result["warnings"].append(
                "Both cross-encoder and LLM reranking enabled - may slow down pipeline"
            )
        
        # Check if techniques are available
        for category in ["pre_embedding", "query_expansion", "retrieval", "passage_augment", 
                        "passage_rerank", "passage_filter", "passage_compress", 
                        "prompt_maker", "post_generation"]:
            
            config_obj = getattr(self.global_config, category) if self.global_config else getattr(self.config_dict, category)
            if config_obj.enabled:
                available = self.factory.get_available_techniques(category)
                
                
                technique = config_obj.technique
                if technique not in available:
                    validation_result["errors"].append(
                        f"Unknown technique '{technique}' for {category}. Available: {available}"
                    )
                    validation_result["valid"] = False
        
        return validation_result 

    @staticmethod
    def from_config_combo(config_combo: dict, global_config: ModularRAGConfig):
        """Convenience constructor for a pipeline from a config combo and global config"""
        return ModularRAGPipeline(config_combo, global_config) 