"""
Basic Modular RAG Configuration

This configuration uses only the currently implemented techniques (green background in your image):
- Simple VectorRAG with Semantic Score (Retrieval)
- Cross-Encoder Models (Passage Rerank)
- Simple threshold (top_k) (Passage Filter)
- Simple Listing (Prompt Maker)
- LLM model (Generator)

This is equivalent to your current system but using the new modular framework.
"""

from rag_pipeline.core.modular_configs import (
    RAGConfig, PreEmbeddingConfig, QueryExpansionConfig, RetrievalConfig,
    PassageAugmentConfig, PassageRerankConfig, PassageFilterConfig,
    PassageCompressConfig, PromptMakerConfig, GeneratorConfig, PostGenerationConfig
)

def get_basic_config() -> RAGConfig:
    """Get basic configuration using only currently implemented techniques"""
    
    return RAGConfig(
        # Pipeline settings
        pipeline_name="basic_modular_rag",
        enable_logging=True,
        log_level="INFO",
        enable_timing=True,
        
        # Pre-embedding: Disabled (use "none" when enabled)
        pre_embedding=PreEmbeddingConfig(
            enabled=False,
            technique="none"
        ),
        
        # Query expansion: Disabled (use "none" when enabled)
        query_expansion=QueryExpansionConfig(
            enabled=False,
            techniques=["none"]
        ),
        
        # Retrieval: ✅ Simple VectorRAG (currently implemented)
        retrieval=RetrievalConfig(
            enabled=True,
            techniques=["simple_vector_rag"],
            top_k=10,
            embedding_model="mxbai-embed-large",
            similarity_metric="cosine"
        ),
        
        # Passage augment: Disabled
        passage_augment=PassageAugmentConfig(
            enabled=False,
            technique="none"
        ),
        
        # Passage rerank: ✅ Cross-Encoder (currently implemented)
        passage_rerank=PassageRerankConfig(
            enabled=True,
            techniques=["cross_encoder"],
            cross_encoder_model="BAAI/bge-reranker-v2-m3",
            cross_encoder_top_k=5,
            cross_encoder_force_cpu=False
        ),
        
        # Passage filter: ✅ Simple threshold (currently implemented)
        passage_filter=PassageFilterConfig(
            enabled=True,
            techniques=["simple_threshold"],
            top_k=5
        ),
        
        # Passage compress: Disabled
        passage_compress=PassageCompressConfig(
            enabled=False,
            technique="none"
        ),
        
        # Prompt maker: ✅ Simple listing (currently implemented)
        prompt_maker=PromptMakerConfig(
            enabled=True,
            technique="simple_listing",
            template="Context:\n{context}\n\nQuestion: {query}\n\nAnswer:",
            separator="\n\n",
            include_doc_numbers=True,
            include_scores=False
        ),
        
        # Generator: ✅ LLM model (currently implemented)
        generator=GeneratorConfig(
            enabled=True,
            model="gemini-2.0-flash",
            provider="gemini",
            max_tokens=500,
            temperature=0.1
        ),
        
        # Post-generation: Disabled
        post_generation=PostGenerationConfig(
            enabled=False,
            technique="none"
        ),
        
        # Dataset settings
        dataset_path=None,  # Use default dataset
        max_test_cases=5,
        eval_batch_size=5,
        
        # Performance settings
        parallel_execution=True,
        max_workers=4,
        cache_enabled=True
    )


def get_gemma_config() -> RAGConfig:
    """Basic config using Gemma instead of Gemini"""
    
    config = get_basic_config()
    
    # Switch to Ollama/Gemma
    config.generator.model = "gemma3:4b"
    config.generator.provider = "ollama"
    
    return config


def get_no_rerank_config() -> RAGConfig:
    """Basic config without reranking for faster execution"""
    
    config = get_basic_config()
    
    # Disable reranking
    config.passage_rerank.enabled = False
    
    # Increase retrieval k since we're not reranking
    config.retrieval.top_k = 5
    config.passage_filter.top_k = 5
    
    return config


if __name__ == "__main__":
    # Example usage
    import asyncio
    from rag_pipeline.core.modular_pipeline import ModularRAGPipeline
    
    async def test_basic_config():
        """Test the basic configuration"""
        
        # Get configuration
        config = get_basic_config()
        
        # Create pipeline
        pipeline = ModularRAGPipeline(config)
        
        # Validate configuration
        validation = pipeline.validate_configuration()
        if not validation["valid"]:
            print("❌ Configuration errors:", validation["errors"])
            return
        
        print("✅ Configuration is valid")
        
        # Get pipeline info
        info = pipeline.get_pipeline_info()
        print(f"📊 Pipeline: {info['pipeline_name']}")
        print(f"🔧 Enabled components: {list(info['enabled_components'].keys())}")
        
        # Test execution
        print("\n🧪 Testing pipeline execution...")
        result = await pipeline.execute_pipeline("What is machine learning?")
        
        print(f"⏱️ Total execution time: {result.total_time:.3f}s")
        print(f"🔍 Retrieved {len(result.retrieved_documents)} documents")
        print(f"📝 Final answer: {result.final_answer[:100]}...")
        print(f"🛠️ Components used: {result.components_used}")
        
        return result
    
    # Run test
    result = asyncio.run(test_basic_config()) 