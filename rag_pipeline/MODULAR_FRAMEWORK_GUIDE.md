# Advanced RAG Modular Framework - Extension Guide

## Overview

This guide explains how to add new techniques to the Advanced RAG Modular Framework. The framework is designed to be highly extensible, allowing you to implement new techniques for each category of the RAG pipeline.

## Architecture Overview

The modular framework consists of 10 categories, each representing a stage in the RAG pipeline:

1. **Pre-Embedding** - Document preprocessing before embedding
2. **Query Expansion/Refinement** - Query modification and expansion
3. **Retrieval** - Document retrieval from knowledge base
4. **Passage Augment** - Enhancement of retrieved passages
5. **Passage Rerank** - Reordering of retrieved passages
6. **Passage Filter** - Filtering of passages based on criteria
7. **Passage Compress** - Compression/summarization of passages
8. **Prompt Maker** - Construction of prompts for generation
9. **Generator** - Answer generation using LLMs
10. **Post-generation** - Refinement of generated answers

## Framework Structure

```
rag_pipeline/core/
├── modular_framework.py       # Abstract base classes for each category
├── modular_configs.py         # Configuration classes for each category
├── modular_implementations.py # Concrete implementations of techniques
├── modular_pipeline.py        # Main pipeline orchestrator
└── MODULAR_FRAMEWORK_GUIDE.md # This guide
```

## Adding a New Technique

### Step 1: Choose Your Category

First, determine which category your technique belongs to. Each category has specific responsibilities:

- **Pre-Embedding**: Document chunking, metadata extraction, context enrichment
- **Query Expansion**: Query rewriting, multi-query generation, semantic routing
- **Retrieval**: Vector search, keyword search, hybrid retrieval
- **Passage Augment**: Context expansion, segment extraction, related content
- **Passage Rerank**: Cross-encoder, LLM-based, or custom reranking
- **Passage Filter**: Threshold-based, relevance-based, or content-based filtering
- **Passage Compress**: Summarization, truncation, key information extraction
- **Prompt Maker**: Template-based, dynamic, or multi-modal prompt construction
- **Generator**: LLM providers, model ensembles, specialized generators
- **Post-generation**: Answer validation, fact-checking, formatting

### Step 2: Implement the Abstract Interface

Create a new class that inherits from the appropriate abstract base class in `modular_framework.py`.

#### Example: Adding a New Retrieval Technique

```python
# In modular_implementations.py

class HybridRetrievalBM25Vector(RetrievalComponent):
    """Hybrid retrieval combining BM25 and vector search"""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.bm25_index = None
        self.vector_store = None
        self._setup_indices()
    
    def _setup_indices(self):
        """Setup both BM25 and vector indices"""
        # Initialize BM25
        from rank_bm25 import BM25Okapi
        # Initialize vector store
        # ... implementation details
    
    async def retrieve(self, query: Query, k: Optional[int] = None) -> List[Document]:
        """Retrieve using both BM25 and vector search, then combine"""
        k = k or self.config.get("top_k", 10)
        
        # Get BM25 results
        bm25_docs = await self._bm25_search(query.processed_text, k)
        
        # Get vector results
        vector_docs = await self._vector_search(query.processed_text, k)
        
        # Combine results using configured strategy
        combined_docs = self._combine_results(bm25_docs, vector_docs)
        
        return combined_docs[:k]
    
    async def index_documents(self, documents: List[Document]) -> bool:
        """Index documents in both BM25 and vector indices"""
        # Implementation for indexing
        pass
    
    def _bm25_search(self, query: str, k: int) -> List[Document]:
        """Perform BM25 search"""
        # Implementation
        pass
    
    def _vector_search(self, query: str, k: int) -> List[Document]:
        """Perform vector search"""
        # Implementation
        pass
    
    def _combine_results(self, bm25_docs: List[Document], vector_docs: List[Document]) -> List[Document]:
        """Combine BM25 and vector results"""
        # Implementation using RRF, weighted scoring, etc.
        pass
```

### Step 3: Update Configuration

Add configuration options for your new technique in `modular_configs.py`.

#### Example: Adding Configuration for Hybrid Retrieval

```python
# In modular_configs.py

class RetrievalConfig(BaseModel):
    """Configuration for retrieval techniques"""
    enabled: bool = True
    techniques: List[str] = ["simple_vector_rag"]  # Add "hybrid_bm25_vector"
    
    # ... existing config options ...
    
    # New configuration for hybrid retrieval
    hybrid_alpha: float = 0.5  # Weight for BM25 vs vector
    hybrid_strategy: str = "rrf"  # "rrf", "weighted", "max"
    bm25_k1: float = 1.2
    bm25_b: float = 0.75
```

### Step 4: Register Your Implementation

Add your new technique to the component registry in `modular_implementations.py`.

```python
# At the end of modular_implementations.py

COMPONENT_REGISTRY = {
    "retrieval": {
        "simple_vector_rag": SimpleVectorRAG,
        "keyword_search": KeywordSearchBM25,
        "hybrid_bm25_vector": HybridRetrievalBM25Vector,  # Add your new technique
    },
    # ... other categories
}
```

### Step 5: Test Your Implementation

Create a test configuration to verify your technique works:

```python
# Example usage
from rag_pipeline.core.modular_configs import RAGConfig, RetrievalConfig
from rag_pipeline.core.modular_pipeline import ModularRAGPipeline

# Configure pipeline to use your new technique
config = RAGConfig(
    retrieval=RetrievalConfig(
        enabled=True,
        techniques=["hybrid_bm25_vector"],
        hybrid_alpha=0.6,
        hybrid_strategy="rrf"
    )
)

# Create and run pipeline
pipeline = ModularRAGPipeline(config)
result = await pipeline.execute_pipeline("What is machine learning?")
```

## Advanced Implementation Patterns

### Pattern 1: Multi-Technique Components

Some categories support multiple techniques running in sequence (e.g., multiple rerankers):

```python
# In configuration
passage_rerank=PassageRerankConfig(
    enabled=True,
    techniques=["cross_encoder", "llm_rerank"]  # Both will run sequentially
)
```

### Pattern 2: Configurable Algorithms

Make your techniques highly configurable:

```python
class AdaptiveReranker(PassageRerankComponent):
    """Reranker that adapts strategy based on query characteristics"""
    
    async def rerank_passages(self, documents: List[Document], query: Query) -> List[Document]:
        # Analyze query to choose strategy
        if self._is_factual_query(query):
            return await self._factual_rerank(documents, query)
        elif self._is_complex_query(query):
            return await self._complex_rerank(documents, query)
        else:
            return await self._default_rerank(documents, query)
```

### Pattern 3: External Service Integration

Integrate with external APIs or services:

```python
class ExternalAPIReranker(PassageRerankComponent):
    """Reranker using external API service"""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.api_client = self._setup_api_client()
    
    def _setup_api_client(self):
        api_key = self.config.get("api_key")
        base_url = self.config.get("base_url")
        return APIClient(api_key=api_key, base_url=base_url)
    
    async def rerank_passages(self, documents: List[Document], query: Query) -> List[Document]:
        # Call external API
        response = await self.api_client.rerank(
            query=query.processed_text,
            documents=[doc.content for doc in documents]
        )
        # Process response and return reranked documents
        return self._process_api_response(response, documents)
```

## Best Practices

### 1. Error Handling

Always include proper error handling:

```python
async def retrieve(self, query: Query, k: Optional[int] = None) -> List[Document]:
    try:
        # Your implementation
        pass
    except Exception as e:
        logger.error(f"Retrieval failed: {e}")
        return []  # Return empty list or fallback results
```

### 2. Logging

Use structured logging for debugging:

```python
logger.info(f"Starting retrieval with technique: {self.__class__.__name__}")
logger.debug(f"Query: {query.processed_text}, k: {k}")
# ... implementation ...
logger.info(f"Retrieved {len(documents)} documents in {elapsed_time:.3f}s")
```

### 3. Configuration Validation

Validate configuration in your constructor:

```python
def __init__(self, config: Dict[str, Any]):
    super().__init__(config)
    
    # Validate required configuration
    if "api_key" not in config:
        raise ValueError("API key is required for ExternalAPIReranker")
    
    if config.get("timeout", 30) < 1:
        raise ValueError("Timeout must be at least 1 second")
```

### 4. Resource Management

Properly manage resources (connections, models, etc.):

```python
def __init__(self, config: Dict[str, Any]):
    super().__init__(config)
    self.model = None
    self._load_model()

def _load_model(self):
    """Load model once during initialization"""
    model_path = self.config.get("model_path")
    self.model = load_model(model_path)

def __del__(self):
    """Clean up resources"""
    if hasattr(self, 'model') and self.model:
        del self.model
```

### 5. Async/Await Best Practices

Use async/await properly for I/O operations:

```python
async def retrieve(self, query: Query, k: Optional[int] = None) -> List[Document]:
    # CPU-bound work can be synchronous
    processed_query = self._preprocess_query(query.processed_text)
    
    # I/O-bound work should be async
    results = await self._async_search(processed_query, k)
    
    # Use asyncio.gather for parallel operations
    tasks = [self._enrich_document(doc) for doc in results]
    enriched_docs = await asyncio.gather(*tasks)
    
    return enriched_docs
```

## Configuration Examples

### Basic Configuration (Currently Implemented Techniques)

```python
# Basic config using only currently implemented techniques
config = RAGConfig(
    # Use current implementations
    retrieval=RetrievalConfig(
        enabled=True,
        techniques=["simple_vector_rag"],
        embedding_model="mxbai-embed-large",
        top_k=10
    ),
    passage_rerank=PassageRerankConfig(
        enabled=True,
        techniques=["cross_encoder"],
        cross_encoder_model="BAAI/bge-reranker-v2-m3",
        cross_encoder_top_k=5
    ),
    passage_filter=PassageFilterConfig(
        enabled=True,
        techniques=["simple_threshold"],
        top_k=5
    ),
    prompt_maker=PromptMakerConfig(
        enabled=True,
        technique="simple_listing",
        template="Context:\n{context}\n\nQuestion: {query}\n\nAnswer:"
    ),
    generator=GeneratorConfig(
        enabled=True,
        model="gemini-2.0-flash",
        provider="gemini",
        max_tokens=500,
        temperature=0.1
    )
)
```

### Advanced Configuration (Multiple Techniques)

```python
# Advanced config with multiple techniques per category
config = RAGConfig(
    query_expansion=QueryExpansionConfig(
        enabled=True,
        techniques=["multi_query"],
        num_expanded_queries=3
    ),
    retrieval=RetrievalConfig(
        enabled=True,
        techniques=["hybrid_bm25_vector"],  # Your new technique
        hybrid_alpha=0.6,
        top_k=20
    ),
    passage_rerank=PassageRerankConfig(
        enabled=True,
        techniques=["cross_encoder", "llm_rerank"],  # Multiple rerankers
        cross_encoder_model="BAAI/bge-reranker-v2-m3",
        llm_rerank_model="gemma3:4b"
    ),
    passage_filter=PassageFilterConfig(
        enabled=True,
        techniques=["similarity_threshold"],
        similarity_threshold=0.7,
        min_passages=3,
        max_passages=8
    ),
    passage_compress=PassageCompressConfig(
        enabled=True,
        technique="tree_summarize",
        tree_levels=2
    ),
    post_generation=PostGenerationConfig(
        enabled=True,
        technique="reflection_revising",
        use_reflection=True,
        max_revisions=1
    )
)
```

## Testing Your Implementation

### Unit Tests

Create unit tests for your technique:

```python
import pytest
from unittest.mock import AsyncMock
from rag_pipeline.core.modular_implementations import HybridRetrievalBM25Vector
from rag_pipeline.core.modular_framework import Query, Document

@pytest.mark.asyncio
async def test_hybrid_retrieval():
    config = {
        "top_k": 5,
        "hybrid_alpha": 0.5,
        "hybrid_strategy": "rrf"
    }
    
    retriever = HybridRetrievalBM25Vector(config)
    
    # Mock the internal methods
    retriever._bm25_search = AsyncMock(return_value=[...])
    retriever._vector_search = AsyncMock(return_value=[...])
    
    query = Query(original_text="test", processed_text="test")
    results = await retriever.retrieve(query, k=5)
    
    assert len(results) <= 5
    assert all(isinstance(doc, Document) for doc in results)
```

### Integration Tests

Test your technique within the full pipeline:

```python
@pytest.mark.asyncio
async def test_pipeline_with_hybrid_retrieval():
    config = RAGConfig(
        retrieval=RetrievalConfig(
            enabled=True,
            techniques=["hybrid_bm25_vector"]
        )
    )
    
    pipeline = ModularRAGPipeline(config)
    result = await pipeline.execute_pipeline("What is AI?")
    
    assert result.final_answer
    assert result.components_used["retrieval"] == "hybrid_bm25_vector"
```

## Debugging and Troubleshooting

### Common Issues

1. **Import Errors**: Make sure your technique is properly imported in `modular_implementations.py`
2. **Configuration Errors**: Validate your config schema matches the implementation
3. **Registry Errors**: Ensure your technique is added to `COMPONENT_REGISTRY`
4. **Interface Mismatch**: Verify your class implements all required abstract methods

### Debugging Tools

Use the pipeline's built-in debugging features:

```python
# Enable debug logging
config.log_level = "DEBUG"
config.enable_timing = True

pipeline = ModularRAGPipeline(config)

# Validate configuration
validation = pipeline.validate_configuration()
if not validation["valid"]:
    print("Configuration errors:", validation["errors"])

# Get pipeline info
info = pipeline.get_pipeline_info()
print("Enabled components:", info["enabled_components"])

# Execute with timing
result = await pipeline.execute_pipeline("test query")
print(f"Total time: {result.total_time:.3f}s")
print(f"Components used: {result.components_used}")
```

## Contributing Guidelines

When contributing new techniques to the framework:

1. **Follow naming conventions**: Use descriptive class names (e.g., `HybridBM25VectorRetrieval`)
2. **Add comprehensive docstrings**: Document parameters, return values, and examples
3. **Include configuration options**: Make techniques configurable rather than hard-coded
4. **Add tests**: Include both unit tests and integration tests
5. **Update documentation**: Add your technique to this guide with examples
6. **Consider performance**: Optimize for the expected usage patterns
7. **Handle edge cases**: Consider empty inputs, network failures, etc.

## Example: Complete Implementation

Here's a complete example of adding a new query expansion technique:

```python
# In modular_implementations.py

class HyDEQueryExpansion(QueryExpansionComponent):
    """HyDE (Hypothetical Document Embeddings) query expansion"""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.llm_client = self._setup_llm()
    
    def _setup_llm(self):
        """Setup LLM for generating hypothetical documents"""
        provider = self.config.get("hyde_provider", "ollama")
        model = self.config.get("hyde_model", "llama3.2:1b")
        
        if provider == "ollama":
            from ..util.api.ollama_client import OllamaUtil
            return OllamaUtil
        # Add other providers as needed
    
    async def expand_query(self, query: str) -> Query:
        """Generate hypothetical documents for the query"""
        try:
            # Generate hypothetical document
            hyde_prompt = self.config.get(
                "hyde_template", 
                "Write a detailed passage that would answer the question: {query}"
            ).format(query=query)
            
            response = self.llm_client.get_ollama_response(
                self.config.get("hyde_model", "llama3.2:1b"),
                hyde_prompt
            )
            
            hypothetical_doc = response.get('response', '') if isinstance(response, dict) else str(response)
            
            # Create expanded query with hypothetical document
            expanded_text = f"{query} {hypothetical_doc}"
            
            return Query(
                original_text=query,
                processed_text=expanded_text,
                expanded_queries=[query, hypothetical_doc],
                metadata={
                    "technique": "hyde",
                    "hypothetical_document": hypothetical_doc
                }
            )
            
        except Exception as e:
            logger.error(f"HyDE expansion failed: {e}")
            # Fallback to original query
            return Query(original_text=query, processed_text=query)
```

```python
# Add to configuration in modular_configs.py

class QueryExpansionConfig(BaseModel):
    """Configuration for query expansion/refinement techniques"""
    enabled: bool = True
    techniques: List[str] = ["none"]  # Add "hyde"
    
    # ... existing config ...
    
    # HyDE settings
    hyde_provider: str = "ollama"
    hyde_model: str = "llama3.2:1b"
    hyde_template: str = "Write a detailed passage that would answer the question: {query}"
```

```python
# Add to registry in modular_implementations.py

COMPONENT_REGISTRY = {
    "query_expansion": {
        "none": NoneQueryExpansion,
        "multi_query": SimpleMultiQuery,
        "hyde": HyDEQueryExpansion,  # Add your new technique
    },
    # ... other categories
}
```

This completes the implementation of a new HyDE query expansion technique that can be used in the modular framework!

## Summary

The modular framework provides a clean, extensible architecture for implementing advanced RAG techniques. By following the patterns and best practices outlined in this guide, you can easily add new techniques to any category of the RAG pipeline while maintaining compatibility with existing components.

Key takeaways:
- Each technique is a separate class implementing a category-specific interface
- Configuration is handled through Pydantic models for type safety
- The component registry enables dynamic technique selection
- The pipeline orchestrates all components automatically
- Proper error handling and logging are essential
- Tests ensure reliability and compatibility

Start by implementing simple techniques and gradually add more complex ones as you become familiar with the framework structure. 