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
from .modular_configs import RAGConfig
from .modular_implementations import COMPONENT_REGISTRY

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
    
    def __init__(self, config: RAGConfig):
        self.config = config
        self.factory = ModularComponentFactory()
        
        # Initialize components
        self.components = {}
        self._initialize_components()
        
        # Setup logging
        if config.enable_logging:
            logging.basicConfig(level=getattr(logging, config.log_level))
    
    def _initialize_components(self):
        """Initialize all enabled components based on configuration"""
        logger.info("Initializing modular RAG components...")
        
        # Pre-embedding
        if self.config.pre_embedding.enabled:
            self.components["pre_embedding"] = self.factory.create_component(
                "pre_embedding",
                self.config.pre_embedding.technique,
                asdict(self.config.pre_embedding)
            )
        
        # Query expansion
        if self.config.query_expansion.enabled:
            # For techniques that support multiple, create instances for each
            techniques = self.config.query_expansion.techniques
            if len(techniques) == 1:
                self.components["query_expansion"] = self.factory.create_component(
                    "query_expansion",
                    techniques[0],
                    asdict(self.config.query_expansion)
                )
            else:
                # For multiple techniques, use the first one for now
                # In the future, this could support chaining multiple expansions
                self.components["query_expansion"] = self.factory.create_component(
                    "query_expansion",
                    techniques[0],
                    asdict(self.config.query_expansion)
                )
        
        # Retrieval
        if self.config.retrieval.enabled:
            # For retrieval, we support multiple techniques that can be combined
            techniques = self.config.retrieval.techniques
            self.components["retrieval"] = self.factory.create_component(
                "retrieval",
                techniques[0],  # Use first technique for now
                asdict(self.config.retrieval)
            )
        
        # Passage augment
        if self.config.passage_augment.enabled:
            self.components["passage_augment"] = self.factory.create_component(
                "passage_augment",
                self.config.passage_augment.technique,
                asdict(self.config.passage_augment)
            )
        
        # Passage rerank
        if self.config.passage_rerank.enabled:
            # Support multiple reranking techniques
            techniques = self.config.passage_rerank.techniques
            self.components["passage_rerank"] = []
            for technique in techniques:
                if technique != "none":
                    component = self.factory.create_component(
                        "passage_rerank",
                        technique,
                        asdict(self.config.passage_rerank)
                    )
                    self.components["passage_rerank"].append(component)
        
        # Passage filter
        if self.config.passage_filter.enabled:
            techniques = self.config.passage_filter.techniques
            self.components["passage_filter"] = []
            for technique in techniques:
                if technique != "none":
                    component = self.factory.create_component(
                        "passage_filter",
                        technique,
                        asdict(self.config.passage_filter)
                    )
                    self.components["passage_filter"].append(component)
        
        # Passage compress
        if self.config.passage_compress.enabled:
            self.components["passage_compress"] = self.factory.create_component(
                "passage_compress",
                self.config.passage_compress.technique,
                asdict(self.config.passage_compress)
            )
        
        # Prompt maker
        if self.config.prompt_maker.enabled:
            self.components["prompt_maker"] = self.factory.create_component(
                "prompt_maker",
                self.config.prompt_maker.technique,
                asdict(self.config.prompt_maker)
            )
        
        # Generator
        if self.config.generator.enabled:
            self.components["generator"] = self.factory.create_component(
                "generator",
                "llm",  # Only LLM generator for now
                asdict(self.config.generator)
            )
        
        # Post-generation
        if self.config.post_generation.enabled:
            self.components["post_generation"] = self.factory.create_component(
                "post_generation",
                self.config.post_generation.technique,
                asdict(self.config.post_generation)
            )
        
        logger.info(f"Initialized {len(self.components)} component categories")
    
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
            
            # Step 1: Pre-embedding (document preprocessing)
            if documents and "pre_embedding" in self.components:
                step_start = time.time()
                documents = await self.components["pre_embedding"].process_documents(documents)
                timing_info["pre_embedding_time"] = time.time() - step_start
                components_used["pre_embedding"] = self.config.pre_embedding.technique
                logger.debug(f"Pre-embedding completed in {timing_info['pre_embedding_time']:.3f}s")
            else:
                timing_info["pre_embedding_time"] = 0.0
            
            # Step 2: Query expansion/refinement
            if "query_expansion" in self.components:
                step_start = time.time()
                processed_query = await self.components["query_expansion"].expand_query(query)
                timing_info["query_expansion_time"] = time.time() - step_start
                components_used["query_expansion"] = self.config.query_expansion.techniques[0]
                logger.debug(f"Query expansion completed in {timing_info['query_expansion_time']:.3f}s")
            else:
                processed_query = Query(original_text=query, processed_text=query)
                timing_info["query_expansion_time"] = 0.0
            
            # Step 3: Retrieval
            retrieved_documents = []
            if "retrieval" in self.components:
                step_start = time.time()
                
                # Index documents if provided
                if documents:
                    await self.components["retrieval"].index_documents(documents)
                
                # Retrieve relevant documents
                retrieved_documents = await self.components["retrieval"].retrieve(
                    processed_query, 
                    k=self.config.retrieval.top_k
                )
                timing_info["retrieval_time"] = time.time() - step_start
                components_used["retrieval"] = self.config.retrieval.techniques[0]
                logger.debug(f"Retrieval completed in {timing_info['retrieval_time']:.3f}s, found {len(retrieved_documents)} documents")
            else:
                timing_info["retrieval_time"] = 0.0
            
            # Step 4: Passage augmentation
            if "passage_augment" in self.components and retrieved_documents:
                step_start = time.time()
                retrieved_documents = await self.components["passage_augment"].augment_passages(
                    retrieved_documents, processed_query
                )
                timing_info["passage_augment_time"] = time.time() - step_start
                components_used["passage_augment"] = self.config.passage_augment.technique
                logger.debug(f"Passage augmentation completed in {timing_info['passage_augment_time']:.3f}s")
            else:
                timing_info["passage_augment_time"] = 0.0
            
            # Step 5: Passage reranking (can have multiple rerankers)
            if "passage_rerank" in self.components and retrieved_documents:
                step_start = time.time()
                for reranker in self.components["passage_rerank"]:
                    retrieved_documents = await reranker.rerank_passages(retrieved_documents, processed_query)
                timing_info["passage_rerank_time"] = time.time() - step_start
                components_used["passage_rerank"] = self.config.passage_rerank.techniques
                logger.debug(f"Passage reranking completed in {timing_info['passage_rerank_time']:.3f}s")
            else:
                timing_info["passage_rerank_time"] = 0.0
            
            # Step 6: Passage filtering (can have multiple filters)
            if "passage_filter" in self.components and retrieved_documents:
                step_start = time.time()
                for filter_component in self.components["passage_filter"]:
                    retrieved_documents = await filter_component.filter_passages(retrieved_documents, processed_query)
                timing_info["passage_filter_time"] = time.time() - step_start
                components_used["passage_filter"] = self.config.passage_filter.techniques
                logger.debug(f"Passage filtering completed in {timing_info['passage_filter_time']:.3f}s, kept {len(retrieved_documents)} documents")
            else:
                timing_info["passage_filter_time"] = 0.0
            
            # Step 7: Passage compression
            final_documents = retrieved_documents
            if "passage_compress" in self.components and retrieved_documents:
                step_start = time.time()
                final_documents = await self.components["passage_compress"].compress_passages(
                    retrieved_documents, processed_query
                )
                timing_info["passage_compress_time"] = time.time() - step_start
                components_used["passage_compress"] = self.config.passage_compress.technique
                logger.debug(f"Passage compression completed in {timing_info['passage_compress_time']:.3f}s")
            else:
                timing_info["passage_compress_time"] = 0.0
            
            # Step 8: Prompt making
            prompt = ""
            if "prompt_maker" in self.components:
                step_start = time.time()
                prompt = await self.components["prompt_maker"].make_prompt(processed_query, final_documents)
                timing_info["prompt_maker_time"] = time.time() - step_start
                components_used["prompt_maker"] = self.config.prompt_maker.technique
                logger.debug(f"Prompt making completed in {timing_info['prompt_maker_time']:.3f}s")
            else:
                timing_info["prompt_maker_time"] = 0.0
            
            # Step 9: Generation
            generated_answer = ""
            if "generator" in self.components and prompt:
                step_start = time.time()
                generated_answer = await self.components["generator"].generate(prompt, processed_query)
                timing_info["generation_time"] = time.time() - step_start
                components_used["generator"] = self.config.generator.model
                logger.debug(f"Generation completed in {timing_info['generation_time']:.3f}s")
            else:
                timing_info["generation_time"] = 0.0
            
            # Step 10: Post-generation
            final_answer = generated_answer
            if "post_generation" in self.components and generated_answer:
                step_start = time.time()
                context = Context(documents=final_documents, formatted_text=prompt)
                final_answer = await self.components["post_generation"].post_process(
                    generated_answer, processed_query, context
                )
                timing_info["post_generation_time"] = time.time() - step_start
                components_used["post_generation"] = self.config.post_generation.technique
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
                **timing_info
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
    
    def get_pipeline_info(self) -> Dict[str, Any]:
        """Get information about the configured pipeline"""
        info = {
            "pipeline_name": self.config.pipeline_name,
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
        if not self.config.retrieval.enabled:
            validation_result["errors"].append("Retrieval component must be enabled")
            validation_result["valid"] = False
        
        if not self.config.generator.enabled:
            validation_result["errors"].append("Generator component must be enabled")
            validation_result["valid"] = False
        
        # Check for conflicting configurations
        if (self.config.passage_rerank.enabled and 
            "cross_encoder" in self.config.passage_rerank.techniques and
            "llm_rerank" in self.config.passage_rerank.techniques):
            validation_result["warnings"].append(
                "Both cross-encoder and LLM reranking enabled - may slow down pipeline"
            )
        
        # Check if techniques are available
        for category in ["pre_embedding", "query_expansion", "retrieval", "passage_augment", 
                        "passage_rerank", "passage_filter", "passage_compress", 
                        "prompt_maker", "post_generation"]:
            
            config_obj = getattr(self.config, category)
            if config_obj.enabled:
                available = self.factory.get_available_techniques(category)
                
                if hasattr(config_obj, 'techniques'):
                    # Multiple techniques supported
                    for technique in config_obj.techniques:
                        if technique not in available:
                            validation_result["errors"].append(
                                f"Unknown technique '{technique}' for {category}. Available: {available}"
                            )
                            validation_result["valid"] = False
                else:
                    # Single technique
                    technique = config_obj.technique
                    if technique not in available:
                        validation_result["errors"].append(
                            f"Unknown technique '{technique}' for {category}. Available: {available}"
                        )
                        validation_result["valid"] = False
        
        return validation_result 