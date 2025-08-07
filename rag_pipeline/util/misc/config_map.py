from rag_pipeline.core.modular_configs import PreEmbeddingConfig, QueryExpansionConfig, RetrievalConfig


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

}





CONFIG_MAP = {
    
}