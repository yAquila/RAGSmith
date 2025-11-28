# RAG Evaluation Pipeline

A clean, extensible evaluation pipeline for Retrieval-Augmented Generation (RAG) systems.

## 🚀 Features

- **Multi-Model Testing**: Automatically tests all combinations of embedding models × LLM models
- **Component-Based Architecture**: Easy to extend with new RAG techniques
- **Dual Reranking Support**: Optional document reranking with both cross-encoder models and LLM-based reranking
- **Comprehensive Evaluation**: Both retrieval and generation metrics
- **Efficient Processing**: Batch processing and parallel execution
- **Clean Results**: Organized results with best-performing combinations identified

## 📁 Architecture

### Core Components

```
rag_pipeline/
├── core/                    # Core RAG pipeline components
│   ├── models.py           # Data models (RAGConfig, Results, etc.)
│   ├── modular_framework.py # Base component interfaces
│   ├── modular_pipeline.py # Pipeline orchestration
│   ├── modular_configs.py  # Configuration management
│   ├── evaluator.py        # Evaluation logic
│   ├── dataset.py          # Dataset loading and management
│   └── modular_implementations/ # Component implementations
│       ├── pre_embedding.py
│       ├── query_expansion.py
│       ├── retrieval.py
│       └── ... (10 component types)
├── util/                   # Utility modules
│   ├── api/               # API clients (Ollama, Gemini)
│   ├── vectorstore/       # Vector store implementations
│   ├── rerank/            # Reranking utilities
│   └── comparison/        # Semantic comparison utilities
├── default_datasets/      # Default test datasets (6 domains)
├── main.py               # FastAPI server entry point
└── requirements.txt      # Python dependencies

# Configuration loaded from project root:
../gen_search_config.yml   # Centralized configuration
../config_loader.py        # Configuration parser
```

### Key Classes

- **`RAGPipeline`**: Main orchestrator that runs the complete evaluation
- **`RAGConfig`**: Configuration for models, settings, and parameters
- **`RetrievalComponent`**: Abstract base for retrieval implementations
- **`GenerationComponent`**: Abstract base for generation implementations
- **`RAGEvaluator`**: Handles both retrieval and generation evaluation

## 🛠️ Usage

### Basic Usage

```python
import asyncio
from core import RAGPipeline, RAGConfig

# Configure evaluation
config = RAGConfig(
    embedding_models=["nomic-embed-text", "mxbai-embed-large"],
    llm_models=["llama3.2:1b", "gemma3:4b"],
    eval_llm_model="gemma3:4b",
    retrieval_k=10,
    eval_batch_size=5
)

# Run evaluation
pipeline = RAGPipeline(config)
results = await pipeline.run_evaluation()

# Print results
pipeline.print_results_summary(results)
```

### Using Gemini Models

The pipeline now supports Google's Gemini models as an alternative to Ollama:

```python
import asyncio
from core.components import ComponentFactory
from core.config import RAGConfig

# Set your Gemini API key
import os
os.environ["GEMINI_API_KEY"] = "your-api-key-here"

# Create Gemini generation component
config = RAGConfig()
gemini_gen = ComponentFactory.create_generation_component(
    "gemini-1.5-flash",  # Model name
    config,
    "gemini"  # Component type
)

# Generate response
result = await gemini_gen.generate(
    query="What is machine learning?",
    context="Machine learning is a subset of AI...",
    embedding_model="test-embedding"
)

print(result.generated_answer)
```

**Available Gemini Models:**
- `gemini-1.5-flash`: Fast, good for most tasks
- `gemini-1.5-pro`: More capable, slower
- `gemini-2.0-flash-exp`: Experimental, very fast
- `gemini-2.0-pro`: Most capable, slowest

**Model Name Mapping:**
- Your existing `gemini3:4b` maps to `gemini-1.5-flash`
- Your existing `gemini3:2b` maps to `gemini-1.5-flash`

**Free Tier Limits:**
- 100 requests per day with Gemini API key
- 1,000 requests per day with Google account authentication

**Testing Gemini Integration:**
```bash
# Test the integration
python test_gemini_integration.py

# Run example usage
python example_gemini_usage.py
```

### Command Line Usage

```bash
# Full evaluation
python main.py

# Quick test (minimal models and test cases)
python main.py --quick
```

## 📊 Evaluation Metrics

### Retrieval Metrics
- **Recall@K**: Proportion of relevant documents retrieved
- **mAP**: Mean Average Precision across all relevant documents  
- **nDCG@K**: Normalized Discounted Cumulative Gain
- **MRR**: Mean Reciprocal Rank

### Generation Metrics
- **LLM Score**: LLM-based evaluation of answer quality (0-1)
- **Semantic Similarity**: Embedding-based similarity to ground truth (0-1)

### Combined Metrics
- **Overall Score**: Weighted combination of retrieval (30%) and generation (70%)

## 🔧 Configuration

### Centralized YAML Configuration

The RAG pipeline now loads configuration from `gen_search_config.yml` in the project root:

```yaml
# Dataset settings
dataset:
  path: "rag_pipeline/default_datasets/military_10"

# API settings  
api:
  host: "localhost"
  port: 8060
  timeout: 3600

# Evaluation weights
evaluation:
  retrieval_weights:
    recall_at_k: 0.25
    map_score: 0.25
    ndcg_at_k: 0.25
    mrr: 0.25
  generation_weights:
    llm_score: 0.5
    semantic_similarity: 0.5
  overall_weights:
    retrieval: 0.5
    generation: 0.5
  llm_eval_model: "gpt-oss:120B"
```

### Python Configuration (Advanced)

For programmatic configuration:

```python
RAGConfig(
    # Models to test
    embedding_models=["model1", "model2"],
    llm_models=["llm1", "llm2"], 
    eval_llm_model="evaluation_llm",
    
    # Retrieval settings
    retrieval_k=10,
    retrieval_threshold=0.5,
    
    # Cross-encoder reranking settings (optional)
    rerank_model="BAAI/bge-reranker-v2-m3",  # Set to None to disable cross-encoder reranking
    rerank_top_k=5,  # Keep top 5 after cross-encoder reranking
    test_with_and_without_reranking=True,  # Test both with/without cross-encoder reranking
    rerank_cache_dir=None,  # Custom cache directory (uses ~/.cache/rag_pipeline/reranker_models by default)
    rerank_force_cpu=False,  # Force CPU usage for cross-encoder reranking (useful for debugging)
    
    # LLM reranking settings (optional)
    llm_rerank_model="llama3.2:1b",  # Set to None to disable LLM reranking
    llm_rerank_top_k=5,  # Keep top 5 after LLM reranking
    test_with_and_without_llm_reranking=True,  # Test both with/without LLM reranking
    llm_rerank_max_tokens=2048,  # Max tokens for LLM reranking
    llm_rerank_temperature=0.1,  # Temperature for LLM reranking
    
    # Generation settings  
    max_tokens=500,
    temperature=0.1,
    
    # Evaluation settings
    eval_batch_size=10,
    max_test_cases=None,  # Use all test cases
    
    # Dataset settings
    dataset_path=None  # Loads from YAML config if None
)
```

### 🚀 Dual Reranking System

The pipeline supports both cross-encoder and LLM-based reranking:

#### Cross-encoder Reranking
- **GPU Acceleration**: Automatically detects and uses CUDA/MPS when available
- **Model Caching**: Downloads models once and caches them locally for faster subsequent runs
- **Singleton Pattern**: Reuses model instances across the evaluation pipeline

#### LLM Reranking  
- **Ollama Integration**: Uses any Ollama model for document reranking
- **Intelligent Prompting**: Structured prompts for reliable ranking extraction
- **Fallback Handling**: Graceful degradation when LLM responses are unparseable

#### Combination Testing
When both reranking methods are enabled, the pipeline tests all combinations:
- No reranking
- Cross-encoder only  
- LLM reranking only
- Both cross-encoder + LLM reranking

**Example**: 2 embedding models × 1 LLM model × 4 reranking variants = 8 total combinations

**Model Cache Location**: `~/.cache/rag_pipeline/reranker_models/`

**Testing Reranking Setup**:
```bash
# Test cross-encoder reranking
python test_reranker.py

# Test LLM reranking  
python test_llm_reranker.py
```

This will test model downloading, caching, GPU usage, and performance improvements.

## 🐳 Docker Setup

The pipeline is optimized for Docker with GPU access and persistent model caching:

### GPU Configuration

The `rag_pipeline` container is configured to use GPU device ID `3` (same as ollama). If you want to use a different GPU:

```yaml
# In docker-compose.yml, change device_ids:
deploy:
  resources:
    reservations:
      devices:
        - driver: nvidia
          device_ids: ['0']  # Change to your preferred GPU
          capabilities: [gpu]
```

### Persistent Model Caching

Reranker models are cached in a Docker volume to avoid redownloading:
- **Volume**: `rag_pipeline_reranker_cache`
- **Mount Point**: `/root/.cache/rag_pipeline/reranker_models`
- **Benefits**: 10-50x faster model loading on subsequent runs

### Testing Docker Setup

```bash
# Test GPU access and persistent caching
docker-compose run --rm rag_pipeline python test_docker_setup.py

# Run quick evaluation with reranking
docker-compose run --rm rag_pipeline python main.py --quick
```

The test will verify:
- ✅ GPU access in container
- ✅ Persistent cache volume mounting
- ✅ Reranker model caching
- ✅ GPU acceleration for reranking

### Docker Commands

```bash
# Build and start services
docker-compose up -d

# Run evaluation (uses cached models after first run)
docker-compose run --rm rag_pipeline python main.py --quick

# Check cache contents
docker-compose run --rm rag_pipeline ls -la /root/.cache/rag_pipeline/reranker_models/

# Monitor GPU usage
nvidia-smi

# View logs
docker-compose logs rag_pipeline
```

### Volume Management

```bash
# List volumes
docker volume ls | grep rag_pipeline

# Inspect cache volume
docker volume inspect rag_pipeline_reranker_cache

# Remove cache (will cause redownload)
docker volume rm rag_pipeline_reranker_cache
```

## 📈 Results

The pipeline produces:

1. **Individual Results**: Per test case, per model combination
2. **Aggregated Metrics**: Averaged metrics by model combination
3. **Best Combinations**: Best performing combinations for retrieval, generation, and overall
4. **Summary Statistics**: Success rates, timing, and error analysis

Example output:
```
===========================================================
              RAG EVALUATION RESULTS
===========================================================

Dataset: 8 test cases
Success rate: 8/8 (100.0%)
Total runtime: 45.23s

🏆 BEST PERFORMING COMBINATIONS:
  Retrieval: mxbai-embed-large_llama3.2:1b
  Generation: nomic-embed-text_gemma3:4b  
  Overall: mxbai-embed-large_gemma3:4b

📊 DETAILED METRICS BY COMBINATION:

mxbai-embed-large + BAAI/bge-reranker-v2-m3 + gemma3:4b:
  Retrieval: R@10=0.875, mAP=0.723, nDCG@10=0.891, MRR=0.734
  Reranking: Model=BAAI/bge-reranker-v2-m3, Avg Time=0.145s
  Generation: LLM=0.750, Semantic=0.842
  Component Scores: Retrieval=0.806, Generation=0.796
  Overall Score: 0.801
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.285s, Generation=2.156s
  Avg Rerank Time: 0.145s
```

## 🧩 Extensibility

### Adding New Retrieval Components

```python
from core.components import RetrievalComponent

class CustomRetrieval(RetrievalComponent):
    async def retrieve(self, query: str, k: int) -> RetrievalResult:
        # Your custom retrieval logic
        pass
    
    async def index_documents(self, documents: List[RAGDocument]) -> bool:
        # Your custom indexing logic  
        pass
```

### Adding New Generation Components

```python
from core.components import GenerationComponent

class CustomGeneration(GenerationComponent):
    async def generate(self, query: str, context: str, embedding_model: str) -> GenerationResult:
        # Your custom generation logic
        pass
```

### Using Different LLM Providers

The pipeline supports multiple LLM providers through the component factory:

```python
# Ollama (local models)
ollama_gen = ComponentFactory.create_generation_component(
    "llama3.2:1b", config, "ollama"
)

# Gemini (Google cloud models)
gemini_gen = ComponentFactory.create_generation_component(
    "gemini-1.5-flash", config, "gemini"
)

# Both use the same interface
result = await ollama_gen.generate(query, context, embedding_model)
result = await gemini_gen.generate(query, context, embedding_model)
```

### RAG Techniques

**Currently Supported:**
- **Cross-encoder Reranking**: Neural cross-encoder models for document reranking  
- **LLM Reranking**: Large language model-based document reranking via Ollama
- **Hybrid Reranking**: Combined cross-encoder + LLM reranking pipeline

**Future Extensions:**
- **Query Expansion**: Expand queries before retrieval
- **Fusion**: Combine multiple retrieval sources  
- **Chain of Thought**: Multi-step reasoning
- **Self-Reflection**: Iterative answer refinement

## 🗂️ Dataset Format

### Test Cases (CSV)
```csv
id,user_prompt,ground_truth,additional_args
1,"What is X?","X is...","{\"true_qrel_list\": [\"doc1\", \"doc2\"]}"
```

### Documents (CSV)  
```csv
text,metadata
"Document content here","{\"doc_id\": \"doc1\"}"
```

## 🔄 Migration from Old Architecture

Key improvements over the original:

1. **Removed Complexity**: Eliminated unnecessary services and abstractions
2. **Fixed Combination Testing**: Now properly tests all embedding × LLM combinations
3. **Unified Evaluation**: Single evaluator for both retrieval and generation
4. **Better Organization**: Clean separation of concerns
5. **Extensible Design**: Easy to add new RAG techniques

## 📋 Requirements

- Python 3.8+
- Ollama (for LLM inference)
- Qdrant (for vector storage)

Install dependencies:
```bash
pip install -r requirements.txt
```

## 🤝 Contributing

The architecture is designed for easy extension. Key extension points:

- `RetrievalComponent`: Add new retrieval methods
- `GenerationComponent`: Add new generation methods  
- `RAGEvaluator`: Add new evaluation metrics
- `ComponentFactory`: Register new component types

## 📄 License

This project is provided as-is for evaluation and extension purposes. 