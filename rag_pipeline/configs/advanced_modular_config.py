"""
Advanced Modular RAG Configuration

This configuration demonstrates how to use multiple techniques and enable
more advanced features of the modular framework. It includes:
- Multiple reranking techniques
- Query expansion 
- Multiple filtering strategies
- All timing and logging enabled

This shows the full potential of the modular framework.
"""

from rag_pipeline.core.modular_configs import (
    RAGConfig, PreEmbeddingConfig, QueryExpansionConfig, RetrievalConfig,
    PassageAugmentConfig, PassageRerankConfig, PassageFilterConfig,
    PassageCompressConfig, PromptMakerConfig, GeneratorConfig, PostGenerationConfig
)

def get_advanced_config() -> RAGConfig:
    """Get advanced configuration with multiple techniques enabled"""
    
    return RAGConfig(
        # Pipeline settings
        pipeline_name="advanced_modular_rag",
        enable_logging=True,
        log_level="DEBUG",  # More detailed logging
        enable_timing=True,
        
        # Pre-embedding: Basic chunking with headers
        pre_embedding=PreEmbeddingConfig(
            enabled=True,
            technique="contextual_chunk_headers",
            chunk_size=512,
            chunk_overlap=50,
            add_headers=True,
            header_template="Document Section: {title}\nContext: {context}\n\n"
        ),
        
        # Query expansion: Multiple query generation
        query_expansion=QueryExpansionConfig(
            enabled=True,
            techniques=["multi_query"],  # Could add more techniques in the future
            num_expanded_queries=3,
            expansion_template="Generate {num} different ways to ask: {query}"
        ),
        
        # Retrieval: Simple VectorRAG (extensible to hybrid in the future)
        retrieval=RetrievalConfig(
            enabled=True,
            techniques=["simple_vector_rag"],
            top_k=20,  # Retrieve more since we'll rerank and filter
            embedding_model="mxbai-embed-large",
            similarity_metric="cosine",
            score_threshold=0.1  # Lower threshold for initial retrieval
        ),
        
        # Passage augment: Future extension point
        passage_augment=PassageAugmentConfig(
            enabled=False,  # Could enable prev_next_augmenter
            technique="none"
        ),
        
        # Passage rerank: Multiple reranking techniques
        passage_rerank=PassageRerankConfig(
            enabled=True,
            techniques=["cross_encoder", "llm_rerank"],  # Both techniques will run
            
            # Cross-encoder settings
            cross_encoder_model="BAAI/bge-reranker-v2-m3",
            cross_encoder_top_k=10,
            cross_encoder_force_cpu=False,
            
            # LLM rerank settings
            llm_rerank_model="gemma3:4b",
            llm_rerank_top_k=8,
            llm_rerank_template="Rank these passages by relevance to the query: {query}\n\nPassages:\n{passages}",
            llm_rerank_max_tokens=2048,
            llm_rerank_temperature=0.1
        ),
        
        # Passage filter: Multiple filtering strategies
        passage_filter=PassageFilterConfig(
            enabled=True,
            techniques=["similarity_threshold"],  # More sophisticated than simple threshold
            similarity_threshold=0.6,
            min_passages=3,
            max_passages=6
        ),
        
        # Passage compress: Future extension for long contexts
        passage_compress=PassageCompressConfig(
            enabled=False,  # Could enable tree_summarize for very long contexts
            technique="none"
        ),
        
        # Prompt maker: Enhanced with scoring information
        prompt_maker=PromptMakerConfig(
            enabled=True,
            technique="simple_listing",
            template="""Based on the following context documents, please provide a comprehensive answer to the question.

Context Information:
{context}

Question: {query}

Please provide a detailed answer based solely on the information provided in the context. If the context doesn't contain enough information to fully answer the question, please state what information is missing.

Answer:""",
            separator="\n\n",
            include_doc_numbers=True,
            include_scores=True  # Show relevance scores
        ),
        
        # Generator: High-quality model with optimized settings
        generator=GeneratorConfig(
            enabled=True,
            model="gemini-2.0-flash",
            provider="gemini",
            max_tokens=800,  # Allow longer responses
            temperature=0.2,  # Slightly higher for more creativity
            
            # Advanced settings
            use_system_prompt=True,
            system_prompt="You are an expert research assistant. Provide accurate, detailed answers based on the given context. Always cite specific information from the context when possible.",
            timeout=60
        ),
        
        # Post-generation: Future extension for answer refinement
        post_generation=PostGenerationConfig(
            enabled=False,  # Could enable reflection_revising
            technique="none"
        ),
        
        # Dataset settings
        dataset_path=None,  # Use default dataset
        max_test_cases=10,  # Test more cases
        eval_batch_size=3,  # Smaller batches for complex processing
        
        # Evaluation settings
        enable_evaluation=True,
        evaluation_metrics=["recall", "precision", "f1", "semantic_similarity", "llm_score"],
        
        # Performance settings
        parallel_execution=True,
        max_workers=2,  # Fewer workers for complex pipeline
        cache_enabled=True
    )


def get_research_config() -> RAGConfig:
    """Configuration optimized for research/academic queries"""
    
    config = get_advanced_config()
    
    # Optimize for research
    config.pipeline_name = "research_rag"
    config.retrieval.top_k = 25  # More comprehensive retrieval
    config.passage_filter.max_passages = 8  # Keep more context
    config.generator.max_tokens = 1000  # Longer, detailed answers
    config.generator.system_prompt = """You are an academic research assistant. Provide thorough, well-structured answers with:
1. Clear explanations of key concepts
2. Citations to specific context passages
3. Acknowledgment of limitations in the available information
4. Suggestions for further research if relevant"""
    
    return config


def get_fast_config() -> RAGConfig:
    """Configuration optimized for speed"""
    
    config = get_advanced_config()
    
    # Optimize for speed
    config.pipeline_name = "fast_rag"
    config.log_level = "INFO"  # Less verbose logging
    
    # Reduce retrieval scope
    config.retrieval.top_k = 10
    
    # Disable expensive reranking
    config.passage_rerank.techniques = ["cross_encoder"]  # Only cross-encoder, not LLM
    config.passage_rerank.cross_encoder_top_k = 5
    
    # Simpler filtering
    config.passage_filter.techniques = ["simple_threshold"]
    config.passage_filter.top_k = 4
    
    # Faster generation
    config.generator.model = "gemma3:4b"  # Faster model
    config.generator.provider = "ollama"
    config.generator.max_tokens = 400
    config.generator.timeout = 30
    
    # Smaller batches for responsiveness
    config.eval_batch_size = 1
    config.max_workers = 4
    
    return config


def get_comprehensive_config() -> RAGConfig:
    """Configuration that enables all available techniques"""
    
    config = get_advanced_config()
    
    # Enable everything
    config.pipeline_name = "comprehensive_rag"
    
    # Enable pre-embedding
    config.pre_embedding.enabled = True
    config.pre_embedding.technique = "contextual_chunk_headers"
    
    # Enable query expansion
    config.query_expansion.enabled = True
    
    # Enable passage augmentation (when implemented)
    # config.passage_augment.enabled = True
    # config.passage_augment.technique = "prev_next_augmenter"
    
    # All reranking techniques
    config.passage_rerank.techniques = ["cross_encoder", "llm_rerank"]
    
    # Enable compression (when implemented)
    # config.passage_compress.enabled = True
    # config.passage_compress.technique = "tree_summarize"
    
    # Enable post-generation (when implemented)
    # config.post_generation.enabled = True
    # config.post_generation.technique = "reflection_revising"
    
    return config


if __name__ == "__main__":
    # Example usage and comparison
    import asyncio
    from rag_pipeline.core.modular_pipeline import ModularRAGPipeline
    
    async def compare_configurations():
        """Compare different configurations"""
        
        configs = {
            "Advanced": get_advanced_config(),
            "Research": get_research_config(),
            "Fast": get_fast_config(),
            "Comprehensive": get_comprehensive_config()
        }
        
        test_query = "What are the main applications of machine learning in healthcare?"
        
        for name, config in configs.items():
            print(f"\n{'='*50}")
            print(f"🧪 Testing {name} Configuration")
            print(f"{'='*50}")
            
            # Create pipeline
            pipeline = ModularRAGPipeline(config)
            
            # Validate
            validation = pipeline.validate_configuration()
            if not validation["valid"]:
                print(f"❌ {name} config errors: {validation['errors']}")
                continue
            
            if validation["warnings"]:
                print(f"⚠️ {name} warnings: {validation['warnings']}")
            
            # Get info
            info = pipeline.get_pipeline_info()
            print(f"🔧 Components: {list(info['enabled_components'].keys())}")
            
            # Test execution
            try:
                result = await pipeline.execute_pipeline(test_query)
                
                print(f"⏱️ Total time: {result.total_time:.3f}s")
                print(f"🔍 Documents: {len(result.retrieved_documents)} → {len(result.final_documents)}")
                print(f"📝 Answer preview: {result.final_answer[:150]}...")
                
                # Timing breakdown
                if result.retrieval_time > 0:
                    print(f"   📊 Retrieval: {result.retrieval_time:.3f}s")
                if result.passage_rerank_time > 0:
                    print(f"   🔄 Reranking: {result.passage_rerank_time:.3f}s")
                if result.generation_time > 0:
                    print(f"   🤖 Generation: {result.generation_time:.3f}s")
                
            except Exception as e:
                print(f"❌ {name} execution failed: {e}")
    
    # Run comparison
    asyncio.run(compare_configurations()) 