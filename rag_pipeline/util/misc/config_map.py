from rag_pipeline.core.modular_configs import PreEmbeddingConfig, QueryExpansionConfig, RetrievalConfig, PassageRerankConfig, PassageFilterConfig, PassageAugmentConfig, PassageCompressConfig, PromptMakerConfig, GeneratorConfig, PostGenerationConfig


PRE_EMBEDDING_CONFIGS = {
    "pre-embedding_none": PreEmbeddingConfig(
        name="pre_embedding_none",
        enabled=True,
        technique="none",
    ),
    "pre-embedding_contextual_chunk_headers": PreEmbeddingConfig(
        name="pre_embedding_contextual_chunk_headers",
        enabled=True,
        technique="contextual_chunk_headers",
        add_headers=True,
        header_generation_strategy="semantic",
        header_generation_model="gemma3:4b",
        header_provider="ollama",
        header_max_length=50,
    ),
    "pre-embedding_hype": PreEmbeddingConfig(
        name="pre_embedding_hype",
        enabled=True,
        technique="hype",
        num_hype_questions=3,
        hype_model="gemma3:4b",
    ),
    "pre-embedding_parent_document_retriever": PreEmbeddingConfig(
        name="pre_embedding_parent_document_retriever",
        enabled=True,
        technique="parent_document_retriever",
        pdr_chunk_size=100,
        pdr_chunk_overlap=20,
    ),
}

QUERY_EXPANSION_CONFIGS = {
    "query-expansion_none": QueryExpansionConfig(
        name="query_expansion_none",
        enabled=True,
        technique="none",
    ),
    "query-expansion_simple_multi_query_cc_dbsf": QueryExpansionConfig(
        name="query_expansion_simple_multi_query_cc_dbsf",
        enabled=True,
        technique="simple_multi_query",
        num_expanded_queries=3,
        combination_method="convex_combination",
        normalization_method="dbsf",
        excessive_k=60,
    ),
    "query-expansion_simple_multi_query_borda": QueryExpansionConfig(
        name="query_expansion_simple_multi_query_borda",
        enabled=True,
        technique="simple_multi_query",
        num_expanded_queries=3,
        combination_method="borda_count",
        excessive_k=60,
    ),
    "query-expansion_rag_fusion": QueryExpansionConfig(
        name="rag_fusion",
        enabled=True,
        technique="rag_fusion",
        num_expanded_queries=3,
        combination_method="reciprocal_rank_fusion",
        excessive_k=60,
    ),
    "query-expansion_decomposition_cc": QueryExpansionConfig(
        name="decomposition_cc",
        enabled=True,
        technique="decomposition",
        num_expanded_queries=3,
        combination_method="convex_combination",
        normalization_method="dbsf",
        excessive_k=60,
    ),
    "query-expansion_hyde_cc": QueryExpansionConfig(
        name="hyde_cc",
        enabled=True,
        technique="hyde",
        num_expanded_queries=3,
        combination_method="convex_combination",
        normalization_method="dbsf",
        excessive_k=60,
    ),
    "query-expansion_step_back_prompting_cc": QueryExpansionConfig(
        name="step_back_prompting_cc",
        enabled=True,
        technique="step_back_prompting",
        num_expanded_queries=3,
        combination_method="convex_combination",
        normalization_method="dbsf",
        excessive_k=60,
    ),
    "query-expansion_graph_as_qe_cc": QueryExpansionConfig(
        name="graph_as_qe_cc",
        enabled=True,
        technique="graph_as_query_expansion",
        provider="ollama",
        num_expanded_queries=3,
        combination_method="convex_combination",
        normalization_method="dbsf",
        excessive_k=60,
    ),
    "query-expansion_refinement_clarification": QueryExpansionConfig(
        name="simple_query_refinement_clarification",
        enabled=True,
        technique="simple_query_refinement",
        provider="ollama",
        refinement_strategy="clarification",
        refinement_model="gemma3:4b",
    ),
    "query-expansion_refinement_rephrasing": QueryExpansionConfig(
        name="simple_query_refinement_rephrasing",
        enabled=True,
        technique="simple_query_refinement",
        provider="ollama",
        refinement_strategy="rephrasing",
        refinement_model="gemma3:4b",
    ),
}

RETRIEVAL_CONFIGS = {
    "retrieval-vector_mxbai": RetrievalConfig(
        name="vector_mxbai",
        enabled=True,
        technique="simple_vector_rag",
        top_k=10,
        embedding_model="mxbai-embed-large",
        similarity_metric="cosine"
    ),
    "retrieval-vector_nomic": RetrievalConfig(
        name="vector_nomic",
        enabled=True,
        technique="simple_vector_rag",
        top_k=10,
        embedding_model="nomic-embed-text",
        similarity_metric="cosine"
    ),
    "retrieval-keyword_bm25": RetrievalConfig(
        name="keyword_bm25",
        enabled=True,
        technique="keyword_search_bm25",
        top_k=10,
        bm25_k1=1.2,
        bm25_b=0.75,
        remove_stopwords=True,
        apply_stemming=False,
        use_advanced_tokenization=False
    ),
    "retrieval-hybrid_vector_keyword_cc": RetrievalConfig(
        name="hybrid_vector_keyword_cc",
        enabled=True,
        technique="complete_hybrid",
        embedding_model="mxbai-embed-large",
        top_k=10,
        weights=[0.7, 0.3],
        combination_method="convex_combination",
        normalization_method="dbsf",
        retrieval_methods=["vector", "keyword"]
    ),
    "retrieval-hybrid_vector_graph_simply": RetrievalConfig(
        name="hybrid_vector_graph_simply",
        enabled=True,
        technique="complete_hybrid",
        embedding_model="mxbai-embed-large",
        top_k=10,
        combination_method="simply",
        normalization_method="dbsf",
        retrieval_methods=["vector", "graph"]
    ),
    "retrieval-hybrid_graph_hypergraph_simply": RetrievalConfig(
        name="hybrid_graph_hypergraph_simply",
        enabled=True,
        technique="complete_hybrid",
        embedding_model="mxbai-embed-large",
        top_k=10,
        combination_method="simply",
        normalization_method="dbsf",
        retrieval_methods=["graph", "hypergraph"]
    ),
    "retrieval-hybrid_vector_graph_hypergraph_simply": RetrievalConfig(
        name="hybrid_vector_graph_hypergraph_simply",
        enabled=True,
        technique="complete_hybrid",
        embedding_model="mxbai-embed-large",
        top_k=10,
        combination_method="simply",
        normalization_method="dbsf",
        retrieval_methods=["vector", "graph", "hypergraph"]
    ),
    "retrieval-hybrid_vector_keyword_graph_simply": RetrievalConfig(
        name="hybrid_vector_keyword_graph_simply",
        enabled=True,
        technique="complete_hybrid",
        embedding_model="mxbai-embed-large",
        top_k=10,
        combination_method="simply",
        normalization_method="dbsf",
        retrieval_methods=["vector", "keyword", "graph"]
    ),
    "retrieval-hybrid_vector_keyword_hypergraph_simply": RetrievalConfig(
        name="hybrid_vector_keyword_hypergraph_simply",
        enabled=True,
        technique="complete_hybrid",
        embedding_model="mxbai-embed-large",
        top_k=10,
        combination_method="simply",
        normalization_method="dbsf",
        retrieval_methods=["vector", "keyword", "hypergraph"]
    ),
    "retrieval-hybrid_vector_keyword_graph_hypergraph_simply": RetrievalConfig(
        name="hybrid_vector_keyword_graph_hypergraph_simply",
        enabled=True,
        technique="complete_hybrid",
        embedding_model="mxbai-embed-large",
        top_k=10,
        combination_method="simply",
        normalization_method="dbsf",
        retrieval_methods=["vector", "keyword", "graph", "hypergraph"]
    ),
}

PASSAGE_RERANK_CONFIGS = {
    "passage-rerank_none": PassageRerankConfig(
        name="passage_rerank_none",
        enabled=True,
        technique="none",
    ),
    "passage-rerank_ce_rerank_bge": PassageRerankConfig(
        name="ce_rerank_bge",
        enabled=True,
        technique="cross_encoder",
        cross_encoder_top_k=5,
        cross_encoder_model="BAAI/bge-reranker-v2-m3",
    ), 
    "passage-rerank_llm_rerank_gemma": PassageRerankConfig(
        name="llm_rerank_gemma",
        enabled=True,
        technique="llm_rerank",
        llm_rerank_top_k=5,
        llm_rerank_model="gemma3:4b",
    ),
    "passage-rerank_cellm_parallel_rerank": PassageRerankConfig(
        name="cellm_parallel_rerank",
        enabled=True,
        technique="cellm_parallel_rerank",
        ce_model="BAAI/bge-reranker-v2-m3",
        llm_model="gemma3:4b",
        top_k=5,
        parallel_ensemble_method="weighted",
        ce_weight=0.7,
        llm_weight=0.3,
        ce_force_cpu=False,
        llm_max_tokens=2048,
        llm_temperature=0.1,
    ),
}

PASSAGE_FILTER_CONFIGS = {
    "passage-filter_simple_threshold": PassageFilterConfig(
        name="simple_threshold",
        enabled=True,
        technique="simple_threshold",
        top_k=10,
    ),
    "passage-filter_similarity_threshold": PassageFilterConfig(
        name="similarity_threshold",
        enabled=True,
        technique="similarity_threshold",
        top_k=10,
        similarity_threshold=0.6,
    )
}

PASSAGE_AUGMENT_CONFIGS = {
    "passage-augment_none": PassageAugmentConfig(
        name="no_augment",
        enabled=True,
        technique="none",
    ),
    "passage-augment_prev_next_augmenter": PassageAugmentConfig(
        name="prev_next_augmenter",
        enabled=True,
        technique="prev_next_augmenter",
        n=1
    ),
    "passage-augment_relevant_segment_extractor": PassageAugmentConfig(
        name="relevant_segment_extractor",
        enabled=True,
        technique="relevant_segment_extractor",
        max_chunk_number_in_segment=5,
        irrelevant_chunk_penalty=0.18,
        decay_rate=30,
        overall_max_chunk_number=10
    )
}

PASSAGE_COMPRESS_CONFIGS = {
    "passage-compress_none": PassageCompressConfig(
        name="passage_compress_none",
        enabled=True,
        technique="none",
    ),
    "passage-compress_llm_summarize": PassageCompressConfig(
        name="llm_summarize",
        enabled=True,
        technique="llm_summarize",
        provider="ollama",
        llm_summarize_model="gemma3:4b",
        llm_summarize_max_tokens=500,
        llm_summarize_temperature=0.1,
    ),
    "passage-compress_tree_summarize": PassageCompressConfig(
        name="tree_summarize",
        enabled=True,
        technique="tree_summarize",
        provider="ollama",
        tree_summarize_model="gemma3:4b",
        max_fan_in=3
    ),
    "passage-compress_llm_lingua": PassageCompressConfig(
        name="llm_lingua",
        enabled=True,
        technique="llm_lingua",
        llm_lingua_model="microsoft/llmlingua-2-xlm-roberta-large-meetingbank",
        llm_lingua_compression_rate=0.33
    )   
}

PROMPT_MAKER_CONFIGS = {
    "prompt-maker_simple_listing": PromptMakerConfig(
        name="simple_listing",
        enabled=True,
        technique="simple_listing"
    ),
    "prompt-maker_long_context_reorder_1": PromptMakerConfig(
        name="long_context_reorder_1",
        enabled=True,
        technique="long_context_reorder",
        reinforce_top_n_passages=1
    ),
    "prompt-maker_long_context_reorder_2": PromptMakerConfig(
        name="long_context_reorder_2",
        enabled=True,
        technique="long_context_reorder",
        reinforce_top_n_passages=2
    ),
}

GENERATOR_CONFIGS = {
    "generator_llama3.2:1b": GeneratorConfig(
        name="llama3.2:1b",
        enabled=True,
        technique="llm",
        model="llama3.2:1b",
        provider="ollama",
        max_tokens=1000
    ),
    "generator_gemma3:4b": GeneratorConfig(
        name="gemma3:4b",
        enabled=True,
        technique="llm",
        model="gemma3:4b",
        provider="ollama",
        max_tokens=1000
    ),
    "generator_gemma3:12b": GeneratorConfig(
        name="gemma3:12b",
        enabled=True,
        technique="llm",
        model="gemma3:12b",
        provider="ollama",
        max_tokens=1000
    ),
    "generator_multi_llm_llama3.2:1b-gemma3:4b-Ensemble:gemma3:12b": GeneratorConfig(
        name="multi_llm_llama3.2:1b-gemma3:4b-Ensemble:gemma3:12b",
        enabled=True,
        technique="multi_llm",
        models=["llama3.2:1b", "gemma3:4b"],
        ensemble_llm_model="gemma3:12b",
    )
}

POST_GENERATION_CONFIGS = {
    "post-generation_none": PostGenerationConfig(
        name="post_generation_none",
        enabled=True,
        technique="none",
    ),
    "post-generation_reflection_revising": PostGenerationConfig(
        name="reflection_revising",
        enabled=True,
        technique="reflection_revising",
        provider="ollama",
        reflection_revising_model="gemma3:4b",
        max_revisions=2
    )
}

CONFIG_MAP = {
    "pre-embedding": PRE_EMBEDDING_CONFIGS,
    "query-expansion": QUERY_EXPANSION_CONFIGS,
    "retrieval": RETRIEVAL_CONFIGS,
    "passage-rerank": PASSAGE_RERANK_CONFIGS,
    "passage-filter": PASSAGE_FILTER_CONFIGS,
    "passage-augment": PASSAGE_AUGMENT_CONFIGS,
    "passage-compress": PASSAGE_COMPRESS_CONFIGS,
    "prompt-maker": PROMPT_MAKER_CONFIGS,
    "generator": GENERATOR_CONFIGS,
    "post-generation": POST_GENERATION_CONFIGS,
}