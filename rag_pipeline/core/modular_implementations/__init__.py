from rag_pipeline.core.modular_implementations.pre_embedding import NonePreEmbedding, ContextualChunkHeaders, PreEmbeddingResult, HyPE
from rag_pipeline.core.modular_implementations.query_expansion import NoneQueryExpansion, SimpleMultiQuery, Decomposition, RAGFusion, HyDE, StepBackPrompting, QueryExpansionResult
from rag_pipeline.core.modular_implementations.retrieval import SimpleVectorRAG, KeywordSearchBM25, HybridSearch, GraphRAG, HyperGraphRAG, RetrievalResult
from rag_pipeline.core.modular_implementations.passage_augment import NonePassageAugment, PrevNextAugmenter, RelevantSegmentExtractor, PassageAugmentResult
from rag_pipeline.core.modular_implementations.passage_rerank import NonePassageRerank, CrossEncoderRerank, LLMRerank, CELLM_ParallelRerank, PassageRerankResult
from rag_pipeline.core.modular_implementations.passage_filter import SimpleThresholdFilter, SimilarityThresholdFilter, PassageFilterResult
from rag_pipeline.core.modular_implementations.passage_compress import NonePassageCompress, TreeSummarize, LLMSummarizeEachChunk, LLMLinguaCompress, PassageCompressResult
from rag_pipeline.core.modular_implementations.prompt_maker import SimpleListingPromptMaker, LongContextReorder, PromptMakerResult
from rag_pipeline.core.modular_implementations.generator import LLMGenerator, MultiLLMGenerator, GeneratorResult
from rag_pipeline.core.modular_implementations.post_generation import NonePostGeneration, ReflectionRevising, PostGenerationResult

COMPONENT_REGISTRY = {
    "pre_embedding": {
        "none": NonePreEmbedding,
        "contextual_chunk_headers": ContextualChunkHeaders,
        "hype": HyPE,
    },
    "query_expansion": {
        "none": NoneQueryExpansion,
        "simple_multi_query": SimpleMultiQuery,
        "decomposition": Decomposition,
        "rag_fusion": RAGFusion,
        "hyde": HyDE,   
        "step_back_prompting": StepBackPrompting,
    },
    "retrieval": {
        "simple_vector_rag": SimpleVectorRAG,
        "keyword_search_bm25": KeywordSearchBM25,
        "hybrid_search": HybridSearch,
        "graph_rag": GraphRAG,
        "hypergraph_rag": HyperGraphRAG,
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
        "relevant_segment_extractor": RelevantSegmentExtractor,
    },
    "passage_compress": {
        "none": NonePassageCompress,
        "tree_summarize": TreeSummarize,
        "llm_summarize": LLMSummarizeEachChunk,
        "llm_lingua": LLMLinguaCompress,
    },
    "prompt_maker": {
        "simple_listing": SimpleListingPromptMaker,
        "long_context_reorder": LongContextReorder,
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