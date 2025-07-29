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
    
    # Common settings
    chunk_size: int = 512
    chunk_overlap: int = 50
    
    # Contextual Chunk Headers settings
    add_headers: bool = False
    header_template: str = "Document Section: {title}\nContext: {context}\n\n"
    
    # Different Chunking Strategies settings
    chunking_strategy: str = "fixed"  # Options: "fixed", "semantic", "sentence", "paragraph"
    min_chunk_size: int = 100
    max_chunk_size: int = 1000
    
    # Parent Document Retriever settings
    parent_chunk_size: int = 2048
    child_chunk_size: int = 512
    
    # HyPE (Hypothetical Passage Embeddings) settings
    use_hypothetical_passages: bool = False
    generate_synthetic_queries: bool = False
    synthetic_queries_per_doc: int = 3


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




class RetrievalConfig(BaseModel):
    """Configuration for retrieval techniques"""
    name: str = ""
    enabled: bool = True
    technique: str = "simple_vector_rag"  # Can combine: ["simple_vector_rag", "keyword_search", "hybrid_cc", "hybrid_rrf"]
    
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
    combination_method: str = "convex_combination"  # Options: "convex_combination", "reciprocal_rank_fusion"
    excessive_k: int = 60 # Excessive k for hybrid search
    alpha: float = 0.7  # Vector weight (0.0 = keyword only, 1.0 = vector only) # Only used for convex combination
    normalization_method: str = "minmax"  # Options: "minmax", "zscore" # Only used for convex combination

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
    extract_segments: bool = False
    segment_max_length: int = 200
    relevance_threshold: float = 0.6


class PassageCompressConfig(BaseModel):
    """Configuration for passage compression techniques"""
    name: str = ""
    enabled: bool = True
    technique: str = "none"  # Options: "none", "tree_summarize", "long_context", "multi_llm_ensemble", "multi_llm_fusion", "window_replacement", "step_back"
    
    # Tree Summarize settings
    tree_summarize_chunk_size: int = 2000
    tree_summarize_overlap: int = 200
    tree_levels: int = 3
    
    # LLM Summarize settings
    provider: str = "ollama"
    llm_summarize_model: str = "gemma3:4b"
    llm_summarize_prompt: str = "Summarize the following document: {document}"
    llm_summarize_max_tokens: int = 500
    llm_summarize_temperature: float = 0.1
    
    # # Long Context Readers settings
    # use_long_context: bool = False
    # context_length_limit: int = 8192
    # compression_ratio: float = 0.5
    
    # # Multi-LLM Model Ensemble settings
    # ensemble_models: List[str] = []
    # ensemble_method: str = "voting"  # Options: "voting", "weighted", "consensus"
    
    # # Multi-LLM Model Fusion settings
    # fusion_models: List[str] = []
    # fusion_weights: List[float] = []
    
    # # Window Replacement settings
    # window_size: int = 512
    # stride: int = 256
    
    # # Step-back Prompting settings
    # use_step_back: bool = False
    # step_back_template: str = "What are the key concepts related to: {query}"


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
    use_reflection: bool = False
    reflection_model: str = "gpt-3.5-turbo"
    reflection_prompt: str = "Review and improve this answer: {answer}\n\nOriginal question: {query}\nContext: {context}"
    max_revisions: int = 2
    
    # Quality checks
    check_hallucination: bool = False
    check_relevance: bool = False
    relevance_threshold: float = 0.8
    
    # Answer formatting
    format_answer: bool = False
    output_format: str = "text"  # Options: "text", "markdown", "json"


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
    pipeline_name: str = "advanced_rag_pipeline"
    enable_logging: bool = True
    log_level: str = "INFO"
    enable_timing: bool = True
    
    # Evaluation settings
    enable_evaluation: bool = True
    evaluation_metrics: List[str] = ["recall", "precision", "f1", "semantic_similarity", "llm_score"]
    llm_eval_model: str = "gemma3:4b"
    
    # Dataset settings
    dataset_path: Optional[str] = None
    max_test_cases: Optional[int] = None
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