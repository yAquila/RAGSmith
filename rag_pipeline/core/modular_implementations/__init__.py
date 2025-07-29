from rag_pipeline.core.modular_implementations.pre_embedding import NonePreEmbedding, ContextualChunkHeaders, PreEmbeddingResult
from rag_pipeline.core.modular_implementations.query_expansion import NoneQueryExpansion, SimpleMultiQuery, Decomposition, RAGFusion, HyDE, QueryExpansionResult
from rag_pipeline.core.modular_implementations.retrieval import SimpleVectorRAG, KeywordSearchBM25, HybridSearch, RetrievalResult
from rag_pipeline.core.modular_implementations.passage_augment import NonePassageAugment, PrevNextAugmenter, PassageAugmentResult
from rag_pipeline.core.modular_implementations.passage_rerank import NonePassageRerank, CrossEncoderRerank, LLMRerank, CELLM_ParallelRerank, PassageRerankResult
from rag_pipeline.core.modular_implementations.passage_filter import SimpleThresholdFilter, SimilarityThresholdFilter, PassageFilterResult
from rag_pipeline.core.modular_implementations.passage_compress import NonePassageCompress, TreeSummarize, LLMSummarize, PassageCompressResult
from rag_pipeline.core.modular_implementations.prompt_maker import SimpleListingPromptMaker, PromptMakerResult
from rag_pipeline.core.modular_implementations.generator import LLMGenerator, MultiLLMGenerator, GeneratorResult
from rag_pipeline.core.modular_implementations.post_generation import NonePostGeneration, ReflectionRevising, PostGenerationResult

COMPONENT_REGISTRY = {
    "pre_embedding": {
        "none": NonePreEmbedding,
        "contextual_chunk_headers": ContextualChunkHeaders,
    },
    "query_expansion": {
        "none": NoneQueryExpansion,
        "simple_multi_query": SimpleMultiQuery,
        "decomposition": Decomposition,
        "rag_fusion": RAGFusion,
        "hyde": HyDE,
    },
    "retrieval": {
        "simple_vector_rag": SimpleVectorRAG,
        "keyword_search_bm25": KeywordSearchBM25,
        "hybrid_search": HybridSearch,
    },
    "passage_rerank": {
        "none": NonePassageRerank,
        "cross_encoder": CrossEncoderRerank,
        "llm_rerank": LLMRerank,
        "cellm_parallel_rerank": CELLM_ParallelRerank,
    },
    "passage_filter": {
        "simple_threshold": SimpleThresholdFilter,
        "similarity_threshold": SimilarityThresholdFilter,
    },
    "passage_augment": {
        "none": NonePassageAugment,
        "prev_next_augmenter": PrevNextAugmenter,
    },
    "passage_compress": {
        "none": NonePassageCompress,
        "tree_summarize": TreeSummarize,
        "llm_summarize": LLMSummarize,
    },
    "prompt_maker": {
        "simple_listing": SimpleListingPromptMaker,
    },
    "generator": {
        "llm": LLMGenerator,
        "multi_llm": MultiLLMGenerator,
    },
    "post_generation": {
        "none": NonePostGeneration,
        "reflection_revising": ReflectionRevising,
    },
} 