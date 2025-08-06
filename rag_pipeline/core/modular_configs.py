"""
Configuration classes for the Advanced RAG Modular Framework

This module defines configuration classes for each category in the RAG pipeline.
Each category has its own configuration class to manage technique-specific settings.
"""

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List, Union
from dataclasses import dataclass


# ==================== CATEGORY CONFIGURATIONS ====================

class PreEmbeddingConfig(BaseModel):
    """Configuration for pre-embedding techniques"""
    name: str = ""
    enabled: bool = True
    technique: str = "none"  # Options: "none", "contextual_chunk_headers", "different_chunking", "parent_document", "hype"
    
    # Contextual Chunk Headers settings
    add_headers: bool = False
    header_template: str = "Document Section: {title}\nContext: {context}\n\n"
    header_generation_strategy: str = "semantic"  # Options: "semantic", "query_aware", "structural"
    header_generation_model: str = "gemma3:4b"
    header_provider: str = "ollama"  # Options: "ollama", "gemini"
    header_max_length: int = 50
    header_min_relevance_score: float = 0.7
    enable_header_deduplication: bool = True
    header_diversity_threshold: float = 0.8
    
    # Header generation prompts
    header_semantic_prompt: str = """Generate a concise header (3-5 words) that captures the main topic of this document section. 
The header should be descriptive and help with information retrieval.

Document content:
{content}

Header:"""
    
    header_query_aware_prompt: str = """Generate a header that would help answer questions about this content. 
The header should be relevant for search and retrieval purposes.

Document content:
{content}

Header:"""
    
    header_structural_prompt: str = """Extract or generate a section title for this content. 
If the content has a clear title or heading, use it. Otherwise, generate a descriptive title.

Document content:
{content}

Title:"""
    
    # Parent Document Retriever settings
    pdr_chunk_size: int = 100
    pdr_chunk_overlap: int = 20
    
    # HyPE (Hypothetical Passage Embeddings) settings
    num_hype_questions: int = 3
    hype_prompt: str = """
    Analyze the input text and generate {num_hype_questions} essential questions that, when answered, capture the main points of the text. Each question should be one line, without numbering or prefixes.
    Input Text: {document}
    {num_hype_questions} Essential Questions:
    """
    hype_model: str = "gemma3:4b"

class QueryExpansionConfig(BaseModel):
    """Configuration for query expansion/refinement techniques"""
    name: str = ""
    enabled: bool = True
    technique: str = "none"  # Can use multiple: ["none", "multi_query", "rag_fusion", "hyde", "decomposition"]
    
    # Combination method
    combination_method: str = "none"  # Options: "none", "convex_combination", "reciprocal_rank_fusion", "borda_count"
    normalization_method: str = "minmax"  # Options: "minmax", "zscore" # Only used for convex combination
    excessive_k: int = 60 # Only used for all combination methods

    # Simple Multi-Query settings
    num_expanded_queries: int = 3
    model: str = "gemma3:4b"
    prompt: str = """
You are an efficient Query Expander. Your task is to read the query provided below and expand it into only {num_expanded_queries} variations.

### Output Format
You must output the expanded queries in the following format:
1. ...
2. ...
...
...
{num_expanded_queries}. ...

### Query to Expand
{query}

### Expanded Queries
        """

    # RAG Fusion settings
    # fusion_weights: List[float] = [0.5, 0.3, 0.2]
    # fusion_method: str = "weighted"  # Options: "weighted", "rrf", "max"
    
    # HyDE (Hypothetical Document Embeddings) settings
    hyde_prompt: str = """Imagine you are an expert writing a detailed explanation on the topic: '{query}'
Your responses should be comprehensive and include all key points that would be found in the top search result. You should output ONLY {num_expanded_queries} documents in the following format:

Document 1:
...
Document {num_expanded_queries}:
...

Do not add any other text.
"""
    
    # Decomposition settings
    decomposition_prompt: str = """
Your task is to rewrite a user's query into {num_expanded_queries} more specific queries. Your output must be ONLY a numbered list of the new queries. Do not add any other text.

---
Example:
User Query: "benefits of intermittent fasting"
Number of Queries: 3
New Queries:
1. What are the weight loss results of intermittent fasting?
2. Risks and side effects of intermittent fasting.
3. How does intermittent fasting affect metabolic health?
---

Now, do this for the following query.

User Query: "{query}"
Number of Queries: {num_expanded_queries}
New Queries:
        """
    
    # Step Back Prompting settings
    step_back_prompting_prompt: str = """
    You are an expert at answering all kind of Questions. Your task is to step back and paraphrase a question to at most {num_expanded_queries} more generic step-back questions, which is easier to answer. Here are a few examples:
    "input": "Could the members of The Police perform lawful arrests?",
    "output": "what can the members of The Police do?",
    "input": "Jan Sindel's was born in what country?",
    "output": "what is Jan Sindel's personal history?",

    Now, do this for the following query and output at most {num_expanded_queries} step-back questions in the following format:
    1. ...
    2. ...
    ...
    {num_expanded_queries}. ...

    User Query: "{query}"
    1. 
"""

    # Simple Query Refinement/Rewriting settings -> Clarification
    refinement_prompt: str = """
You are an expert at improving search queries. Your task is to rewrite the given query to make it more search-friendly and clear.

### Guidelines:
- Keep the original intent
- Make it more specific if needed
- Use clear, searchable terms
- Maintain the same meaning
- Output ONLY the improved query, nothing else

### Original Query:
{query}

### Improved Query:
"""
    refinement_rephrasing_prompt: str = """ 
You are an expert at rephrasing queries to make them clearer and more search-friendly.

### Task:
Rephrase the following query in a clearer, more specific way while maintaining the original intent.

### Guidelines:
- Keep the same meaning and intent
- Make it more specific and clear
- Use proper grammar and structure
- Output ONLY the rephrased query, nothing else

### Original Query:
{query}

### Rephrased Query:
"""
    refinement_keyword_extraction_prompt: str = """
You are an expert at extracting key search terms from queries.

### Task:
Extract the most important keywords and phrases from the given query that would be useful for search.

### Guidelines:
- Focus on the main concepts and entities
- Include synonyms if relevant
- Keep terms in a searchable format
- Output ONLY the key terms separated by spaces, nothing else

### Original Query:
{query}

### Key Terms:
"""
    refinement_strategy: str = "clarification"  # Options: "clarification", "rephrasing", "keyword_extraction"
    refinement_model: str = "gemma3:4b"
    refinement_temperature: float = 0.1
    refinement_max_tokens: int = 1000






	





class RetrievalConfig(BaseModel):
    """Configuration for retrieval techniques"""
    name: str = ""
    enabled: bool = True
    technique: str = "simple_vector_rag"  # Can combine: ["simple_vector_rag", "keyword_search", "hybrid_cc", "hybrid_rrf", "graph_rag"]
    
    # Common settings
    top_k: int = 10
    score_threshold: float = 0.5
    
    # Simple VectorRAG settings
    embedding_model: str = "mxbai-embed-large"
    similarity_metric: str = "cosine"  # Options: "cosine", "euclidean", "dot_product"
    
    # Keyword Search (BM25) settings
    bm25_k1: float = 1.2
    bm25_b: float = 0.75
    remove_stopwords: bool = True
    apply_stemming: bool = False
    use_advanced_tokenization: bool = False
    
    # Hybrid Search settings
    combination_method: str = "convex_combination"  # Options: "convex_combination", "reciprocal_rank_fusion", "borda_count"
    excessive_k: int = 60 # Excessive k for hybrid search
    weights: List[float] = None
    retrieval_methods: List[str] = None
    normalization_method: str = "minmax"  # Options: "minmax", "zscore" # Only used for convex combination

    # Graph RAG settings
    graph_rag_retrieval_method: str = "basic"  # Options: "basic", "traversal"
    graph_rag_similarity_threshold: float = 0.7
    graph_rag_max_depth: int = 2
    graph_rag_vector_index_name: str = "entity_embeddings"
    graph_rag_embedding_dimension: int = 1024 #TODO make this dynamic
    graph_rag_neo4j_uri: str = "bolt://neo4j:7687"
    graph_rag_neo4j_user: str = "neo4j"
    graph_rag_neo4j_password: str = "admin123"
    graph_rag_ollama_embedding_url: str = "http://ollama-gpu-3:11435/api/embeddings"
    graph_rag_embedding_model: str = "mxbai-embed-large"
    graph_rag_ollama_model: str = "gemma3:12b"

    # HyperGraph settings
    hypergraph_retrieval_method: str = "basic"  # Options: "basic", "expansion"
    hypergraph_similarity_threshold: float = 0.7
    hypergraph_max_depth: int = 2
    hypergraph_vector_index_name: str = "hypergraph_entity_embeddings"
    hypergraph_embedding_dimension: int = 1024 #TODO make this dynamic
    hypergraph_neo4j_uri: str = "bolt://neo4j:7687"
    hypergraph_neo4j_user: str = "neo4j"
    hypergraph_neo4j_password: str = "admin123"
    hypergraph_ollama_embedding_url: str = "http://ollama-gpu-3:11435/api/embeddings"
    hypergraph_ollama_model: str = "gemma3:12b"
    hypergraph_embedding_model: str = "mxbai-embed-large"
    hypergraph_min_entities: int = 2



class PassageRerankConfig(BaseModel):
    """Configuration for passage reranking techniques"""
    name: str = ""
    enabled: bool = True
    technique: str = "none"  # Can combine: ["none", "cross_encoder", "llm_rerank", "parallel_rerank"]
    top_k: int = 5
    
    # Cross-Encoder settings
    cross_encoder_model: str = "BAAI/bge-reranker-v2-m3"
    cross_encoder_top_k: int = 5
    cross_encoder_batch_size: int = 32
    cross_encoder_force_cpu: bool = False
    cross_encoder_cache_dir: Optional[str] = None
    
    # LLM Rerank settings
    llm_rerank_model: str = "gpt-3.5-turbo"
    llm_rerank_top_k: int = 5
    llm_rerank_template: str = "Rank these passages by relevance to the query: {query}\n\nPassages:\n{passages}"
    llm_rerank_max_tokens: int = 2048
    llm_rerank_temperature: float = 0.1
    
    # Parallel Rerank settings (combines CE + LLM)
    parallel_ensemble_method: str = "weighted"  # Options: "weighted", "average", "max"
    ce_weight: float = 0.7
    llm_weight: float = 0.3
    
    # Other/Special Rerank settings
    use_special_rerank: bool = False
    special_rerank_method: str = "custom"


class PassageFilterConfig(BaseModel):
    """Configuration for passage filtering techniques"""
    name: str = ""
    enabled: bool = True
    technique: str = "simple_threshold"  # Can combine: ["simple_threshold", "similarity_threshold", "tree_summarize", "llm_summarize", "window_replacement"]
    
    # Simple threshold (top_k) settings - CURRENTLY IMPLEMENTED
    top_k: int = 5
    
    # Similarity threshold settings
    similarity_threshold: float = 0.7
    min_passages: int = 1
    max_passages: int = 10
    
    # Tree Summarize settings
    use_tree_summarize: bool = False
    tree_chunk_size: int = 1000
    summarize_template: str = "Summarize the key information from these passages: {passages}"
    
    # LLM Summarize/Refining settings
    use_llm_filter: bool = False
    llm_filter_model: str = "gpt-3.5-turbo"
    filter_prompt: str = "Filter these passages to keep only those relevant to: {query}\n\nPassages:\n{passages}"
    
    # Window Replacement settings
    use_window_replacement: bool = False
    window_size: int = 3
    replacement_strategy: str = "best"  # Options: "best", "random", "diverse"

class PassageAugmentConfig(BaseModel):
    """Configuration for passage augmentation techniques"""
    name: str = ""
    enabled: bool = True
    technique: str = "none"  # Options: "none", "prev_next_augmenter", "relevant_segment_extraction"
    
    # Prev-Next Augmenter settings
    n: int = 1  # Number of chunks before/after
    
    # Relevant Segment Extraction settings
    max_chunk_number_in_segment: int = 5
    irrelevant_chunk_penalty: float = 0.18
    decay_rate: int = 30
    overall_max_chunk_number: int = 10


class PassageCompressConfig(BaseModel):
    """Configuration for passage compression techniques"""
    name: str = ""
    enabled: bool = True
    technique: str = "none"  # Options: "none", "tree_summarize", "long_context", "multi_llm_ensemble", "multi_llm_fusion", "window_replacement", "step_back"
    
    # Tree Summarize settings
    tree_summarize_model: str = "gemma3:4b"
    max_fan_in: int = 3
    
    # LLM Summarize settings
    provider: str = "ollama"
    llm_summarize_model: str = "gemma3:4b"
    llm_summarize_prompt: str = "Summarize the following document: {document}"
    llm_summarize_max_tokens: int = 500
    llm_summarize_temperature: float = 0.1
    
    # LLMLingua settings
    llm_lingua_model: str = "microsoft/llmlingua-2-xlm-roberta-large-meetingbank"
    llm_lingua_compression_rate: float = 0.33


class PromptMakerConfig(BaseModel):
    """Configuration for prompt construction techniques"""
    name: str = ""
    enabled: bool = True
    technique: str = "simple_listing"  # Options: "simple_listing", "multi_llm_ensemble", "multi_llm_fusion"
    
    # Simple Listing settings - CURRENTLY IMPLEMENTED
    template: str = "Context:\n{context}\n\nQuestion: {query}\n\nAnswer:"
    separator: str = "\n\n"
    include_doc_numbers: bool = True
    include_scores: bool = False

    # Long Context Reorder settings
    reinforce_top_n_passages: int = 1

class GeneratorConfig(BaseModel):
    """Configuration for generation techniques"""
    name: str = ""
    enabled: bool = True
    technique: str = "llm"  # Options: "llm", "multi_llm"
    model: str = "gemma3:4b"  # CURRENTLY IMPLEMENTED: supports ollama and gemini models

    # Multi-LLM settings
    models: List[str] = []
    ensemble_llm_model: str = ""

    # Generation settings
    max_tokens: int = 500
    temperature: float = 0.1
    top_p: float = 1.0
    top_k: Optional[int] = None
    frequency_penalty: float = 0.0
    presence_penalty: float = 0.0
    
    # Provider-specific settings
    provider: str = "ollama"  # Options: "ollama", "gemini", "openai", "anthropic"
    base_url: Optional[str] = None
    api_key: Optional[str] = None
    
    # Advanced settings
    use_system_prompt: bool = True
    system_prompt: str = "You are a helpful assistant that answers questions based on the provided context."
    stream: bool = False
    timeout: int = 30


class PostGenerationConfig(BaseModel):
    """Configuration for post-generation techniques"""
    name: str = ""
    enabled: bool = True
    technique: str = "none"  # Options: "none", "reflection_revising"
    
    # Reflection and Revising settings
    provider: str = "ollama"
    reflection_revising_model: str = "gemma3:4b"
    max_revisions: int = 2
    
    # # Quality checks
    # check_hallucination: bool = False
    # check_relevance: bool = False
    # relevance_threshold: float = 0.8
    
    # # Answer formatting
    # format_answer: bool = False
    # output_format: str = "text"  # Options: "text", "markdown", "json"


# ==================== UNIFIED RAG CONFIGURATION ====================

class ModularRAGConfig(BaseModel):
    """Unified configuration for the entire RAG pipeline (all categories are lists of configs)"""
    
    # Category configurations
    pre_embedding: List[PreEmbeddingConfig] = Field(default_factory=list)
    query_expansion: List[QueryExpansionConfig] = Field(default_factory=list)
    retrieval: List[RetrievalConfig] = Field(default_factory=list)
    passage_augment: List[PassageAugmentConfig] = Field(default_factory=list)
    passage_rerank: List[PassageRerankConfig] = Field(default_factory=list)
    passage_filter: List[PassageFilterConfig] = Field(default_factory=list)
    passage_compress: List[PassageCompressConfig] = Field(default_factory=list)
    prompt_maker: List[PromptMakerConfig] = Field(default_factory=list)
    generator: List[GeneratorConfig] = Field(default_factory=list)
    post_generation: List[PostGenerationConfig] = Field(default_factory=list)
    
    # Global settings
    run_name: str = "advanced_rag_pipeline"
    enable_logging: bool = True
    log_level: str = "INFO"
    enable_timing: bool = True
    
    # Evaluation settings
    enable_evaluation: bool = True
    evaluation_metrics: List[str] = ["recall", "precision", "f1", "semantic_similarity", "llm_score"]
    llm_eval_model: str = "gemma3:4b"
    save_eval_cases: bool = False
    
    # Dataset settings
    dataset_path: Optional[str] = None
    qdrant_collection_hash: Optional[str] = None
    max_test_cases: Optional[int] = None
    test_case_offset: Optional[int] = 0
    eval_batch_size: int = 10
    
    # Performance settings
    parallel_execution: bool = True
    max_workers: int = 4
    cache_enabled: bool = True
    cache_dir: Optional[str] = None
    
    # Evaluation settings
    retrieval_weights: Dict[str, float] = {
        'recall_at_k': 0.25,
        'map_score': 0.25,
        'ndcg_at_k': 0.25,
        'mrr': 0.25
    }
    generation_weights: Dict[str, float] = {
        'llm_score': 0.5,
        'semantic_similarity': 0.5
    }
    overall_weights: Dict[str, float] = {
        'retrieval': 0.3,
        'generation': 0.7
    }

    def create_config_combinations(self) -> List[Dict[str, Any]]:
        """Create all possible combinations of enabled configs (full Cartesian product)"""
        from itertools import product
        categories = [
            ("pre_embedding", self.pre_embedding),
            ("query_expansion", self.query_expansion),
            ("retrieval", self.retrieval),
            ("passage_augment", self.passage_augment),
            ("passage_rerank", self.passage_rerank),
            ("passage_filter", self.passage_filter),
            ("passage_compress", self.passage_compress),
            ("prompt_maker", self.prompt_maker),
            ("generator", self.generator),
            ("post_generation", self.post_generation),
        ]
        # Only include categories with at least one enabled config
        filtered = [(cat, [cfg for cfg in cfgs if getattr(cfg, 'enabled', True)]) for cat, cfgs in categories if any(getattr(cfg, 'enabled', True) for cfg in cfgs)]
        if not filtered:
            return []
        cat_names = [cat for cat, cfgs in filtered]
        cfg_lists = [cfgs for cat, cfgs in filtered]
        combos = []
        for prod in product(*cfg_lists):
            combos.append({cat: cfg for cat, cfg in zip(cat_names, prod)})
        return combos 