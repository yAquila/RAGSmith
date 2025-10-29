# RAG Pipeline with Genetic Algorithm Optimization

A comprehensive system for evaluating and optimizing Retrieval-Augmented Generation (RAG) pipelines using genetic algorithms. This project combines a modular RAG evaluation framework with an intelligent optimization engine to automatically discover the best RAG component configurations.

## 🎯 Overview

This project consists of two main components:

1. **Modular RAG Pipeline**: A flexible, component-based RAG evaluation system with 10 configurable stages
2. **Genetic Algorithm Optimizer**: An intelligent search system that finds optimal RAG configurations automatically

The genetic algorithm communicates with the RAG pipeline API to evaluate different component combinations and progressively discovers better configurations through evolutionary optimization.

### How It Works

```
┌─────────────────────────────────────────────────────────────┐
│  Genetic Algorithm Optimizer                                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ 1. Generate candidate configurations                  │  │
│  │    [pre-embed, query-exp, retrieval, ... ]          │  │
│  └────────────────┬─────────────────────────────────────┘  │
│                   │ HTTP POST                               │
│                   ▼                                          │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ 2. Send to RAG Pipeline API                          │  │
│  │    POST /api/evaluate                                │  │
│  └────────────────┬─────────────────────────────────────┘  │
└───────────────────┼──────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  RAG Pipeline Service                                       │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ 3. Build pipeline from configuration                 │  │
│  │    ↓ Pre-Embedding   (e.g., contextual headers)     │  │
│  │    ↓ Query Expansion (e.g., HyDE)                   │  │
│  │    ↓ Retrieval       (e.g., hybrid search)          │  │
│  │    ↓ Reranking       (e.g., cross-encoder)          │  │
│  │    ↓ Filtering       (e.g., threshold)              │  │
│  │    ↓ Augmentation    (e.g., prev/next chunks)       │  │
│  │    ↓ Compression     (e.g., tree summarize)         │  │
│  │    ↓ Prompt Making   (e.g., reordering)             │  │
│  │    ↓ Generation      (e.g., Qwen3-30B)              │  │
│  │    ↓ Post-Generation (e.g., reflection)             │  │
│  └────────────────┬─────────────────────────────────────┘  │
│                   │                                          │
│  ┌────────────────▼─────────────────────────────────────┐  │
│  │ 4. Run on test dataset (military_10)                │  │
│  │    • Load 10 test questions and documents           │  │
│  │    • Execute pipeline on each test case             │  │
│  │    • Compute retrieval metrics (Recall, nDCG, etc.) │  │
│  │    • Compute generation metrics (LLM score, etc.)   │  │
│  └────────────────┬─────────────────────────────────────┘  │
│                   │                                          │
│  ┌────────────────▼─────────────────────────────────────┐  │
│  │ 5. Return final score (0-1)                         │  │
│  │    {evaluation: {final_score: 0.85}}                │  │
│  └────────────────┬─────────────────────────────────────┘  │
└───────────────────┼──────────────────────────────────────────┘
                    │ HTTP Response
                    ▼
┌─────────────────────────────────────────────────────────────┐
│  Genetic Algorithm Optimizer                                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ 6. Update population based on fitness               │  │
│  │    • Selection (tournament, roulette wheel, etc.)   │  │
│  │    • Crossover (uniform, single-point, etc.)        │  │
│  │    • Mutation (adaptive, random, etc.)              │  │
│  │    • Elitism (keep best candidates)                 │  │
│  └────────────────┬─────────────────────────────────────┘  │
│                   │                                          │
│  ┌────────────────▼─────────────────────────────────────┐  │
│  │ 7. Repeat until convergence                         │  │
│  │    • Track best configuration found                 │  │
│  │    • Cache evaluations for efficiency               │  │
│  │    • Save results to markdown report                │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Key Benefits

- **Automated Discovery**: No manual testing of 381,024 configurations
- **Intelligent Search**: GA explores promising regions of search space
- **Persistent Caching**: Previously evaluated configurations are cached
- **Parallel Evaluation**: Multiple GPUs for faster optimization
- **Comprehensive Results**: Detailed markdown reports with evolution statistics

## 📦 Project Structure

```
rag_pipeline_deneme/
├── rag_pipeline/                    # RAG evaluation system
│   ├── core/                        # Core pipeline components
│   │   ├── modular_framework.py    # Base component interfaces
│   │   ├── modular_pipeline.py     # Pipeline orchestration
│   │   ├── modular_configs.py      # Configuration management
│   │   ├── evaluator.py            # Evaluation metrics
│   │   ├── dataset.py              # Dataset loading
│   │   └── modular_implementations/ # Component implementations
│   │       ├── pre_embedding.py    # Document preprocessing
│   │       ├── query_expansion.py  # Query enhancement
│   │       ├── retrieval.py        # Retrieval strategies
│   │       ├── passage_rerank.py   # Result reranking
│   │       ├── passage_filter.py   # Result filtering
│   │       ├── passage_augment.py  # Context augmentation
│   │       ├── passage_compress.py # Context compression
│   │       ├── prompt_maker.py     # Prompt construction
│   │       ├── generator.py        # Answer generation
│   │       └── post_generation.py  # Post-processing
│   ├── util/                       # Utility modules
│   │   ├── api/                    # LLM API clients (Ollama, Gemini)
│   │   ├── vectorstore/            # Vector database utilities
│   │   ├── rerank/                 # Reranking implementations
│   │   └── comparison/             # Evaluation utilities
│   ├── default_datasets/           # Test datasets (finance, law, maths, medicine, military, programming)
│   ├── main.py                     # FastAPI server entry point
│   ├── Dockerfile                  # Container definition
│   └── requirements.txt            # Python dependencies
├── genetic_search_for_rag_pipeline/ # Genetic algorithm optimizer
│   ├── genetic_algorithm.py        # Main GA implementation
│   ├── config.py                   # GA configuration
│   ├── individual.py               # Solution representation
│   ├── population.py               # Population management
│   ├── selection.py                # Selection methods
│   ├── crossover.py                # Crossover operators
│   ├── mutation.py                 # Mutation operators
│   ├── rag_evaluator.py            # RAG API integration
│   ├── run.py                      # Optimization runner
│   ├── api.py                      # Optional REST API
│   ├── Dockerfile                  # Container definition
│   └── requirements.txt            # Python dependencies
├── docker-compose.yml              # Multi-service orchestration
└── README.md                       # This file
```

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose
- NVIDIA GPU with CUDA support
- nvidia-docker runtime

### 0. Configure API Keys (Important!)

⚠️ **Security Note**: Never commit API keys to version control!

The repository uses environment variables for sensitive credentials. Create a `.env` file in the root directory:

```bash
# Create .env file
cat > .env << 'EOF'
# Google Gemini API Key (optional, only if using Gemini models)
# Get your key from: https://makersuite.google.com/app/apikey
GEMINI_API_KEY=your-actual-gemini-api-key-here

# Other configurations (already set in docker-compose.yml)
QDRANT_URL=http://rag-pipeline-qdrant:6333
OLLAMA_API_URL=http://rag-pipeline-ollama-gpu:11434/api
OLLAMA_API_URL2=http://rag-pipeline-ollama-gpu-2:11434/api
EOF
```

**Note**: The `.env` file is already in `.gitignore` and will not be committed. The `docker-compose.yml` now references `${GEMINI_API_KEY}` from your environment.

### 1. Start All Services

```bash
# Build and start all containers
docker-compose up -d
```

This will start:
- **rag_pipeline**: RAG evaluation API (port 8060)
- **genetic_search_rag**: Genetic algorithm optimizer
- **qdrant**: Vector database (port 6335)
- **rag-pipeline-ollama-gpu**: Ollama LLM server on GPU 1 (port 11435)
- **rag-pipeline-ollama-gpu-2**: Secondary Ollama server on GPU 2-3 (port 11436)
- **neo4j**: Graph database for GraphRAG (ports 7474, 7687)

### 1.5. Pull Required Ollama Models

Before running optimization, ensure the required models are available in Ollama:

```bash
# Pull the main generator model (Qwen3 30B)
docker exec -it rag-pipeline-ollama-gpu ollama pull alibayram/Qwen3-30B-A3B-Instruct-2507:latest

# Pull the embedding model
docker exec -it rag-pipeline-ollama-gpu ollama pull mxbai-embed-large

# Pull the LLM evaluator model (GPT-OSS 120B)
docker exec -it rag-pipeline-ollama-gpu ollama pull gpt-oss:120B

# Optional: Pull alternative models
docker exec -it rag-pipeline-ollama-gpu ollama pull gemma3:27b

# Verify models are available
docker exec -it rag-pipeline-ollama-gpu ollama list
```

**Note**: Model pulling can take significant time depending on your internet connection. The Qwen3-30B model is approximately 17GB.

### 2. Run Genetic Algorithm Optimization

```bash
# Quick test run (20 individuals, 3 generations)
docker exec -itd rag-pipeline-genetic-search-rag python run.py

# Comprehensive search (16 individuals, 20 generations)
docker exec -itd rag-pipeline-genetic-search-rag python run.py --comprehensive
```

**Note**: The `-d` flag runs the optimization in detached mode. The process will continue running in the background.

### 3. Monitor Progress

```bash
# View genetic algorithm logs
docker logs -f rag-pipeline-genetic-search-rag

# View RAG pipeline logs
docker logs -f rag-pipeline

# Check results
ls -la genetic_algorithm_results/
```

Results are saved to `genetic_algorithm_results/` with detailed markdown reports and cached evaluations.

## 🧬 RAG Pipeline Components

The modular pipeline consists of 10 configurable stages, each with multiple implementation options:

### 1. Pre-Embedding (4 options)
- **none**: No preprocessing
- **contextual_chunk_headers**: Add contextual headers to chunks
- **hype**: Hypothetical Embeddings
- **parent_document_retriever**: Parent document context

### 2. Query Expansion (9 options)
- **none**: Original query only
- **simple_multi_query_cc_dbsf**: Multiple queries with convex combination
- **simple_multi_query_borda**: Multiple queries with Borda count
- **rag_fusion**: Reciprocal rank fusion
- **decomposition_cc**: Query decomposition with convex combination
- **hyde_cc**: Hypothetical Document Embeddings
- **step_back_prompting_cc**: Step-back reasoning with convex combination
- **graph_as_qe_cc**: Graph-based expansion with convex combination
- **refinement**: Query refinement (clarification/rephrasing)

### 3. Retrieval (11 options)
- **vector_mxbai**: Basic vector similarity search
- **keyword_bm25**: BM25 keyword search
- **graph_rag**: Knowledge graph retrieval
- **hypergraph_rag**: Advanced hypergraph retrieval
- **hybrid_vector_keyword_cc**: Vector + BM25 hybrid
- **hybrid_vector_graph_simply**: Vector + Graph hybrid
- **hybrid_graph_hypergraph_simply**: Graph + Hypergraph hybrid
- **hybrid_vector_graph_hypergraph_simply**: Vector + Graph + Hypergraph
- **hybrid_vector_keyword_graph_simply**: Vector + BM25 + Graph
- **hybrid_vector_keyword_hypergraph_simply**: Vector + BM25 + Hypergraph
- **hybrid_vector_keyword_graph_hypergraph_simply**: All four methods combined

### 4. Passage Reranking (4 options)
- **none**: No reranking
- **cross_encoder**: Neural cross-encoder models (BGE-reranker-v2-m3)
- **llm_rerank**: LLM-based reranking
- **cellm_parallel_rerank**: Combined cross-encoder + LLM parallel reranking

### 5. Passage Filtering (2 options)
- **simple_threshold**: Basic top-k filtering
- **similarity_threshold**: Adaptive similarity-based filtering

### 6. Passage Augmentation (3 options)
- **none**: No augmentation
- **prev_next_augmenter**: Add surrounding context chunks
- **relevant_segment_extractor**: Extract relevant segments with decay

### 7. Passage Compression (3 options)
- **none**: No compression
- **llm_summarize**: LLM-based chunk summarization
- **tree_summarize**: Hierarchical tree summarization

### 8. Prompt Making (3 options)
- **simple_listing**: Simple context listing
- **long_context_reorder_1**: Lost-in-the-middle reordering (top 1 reinforced)
- **long_context_reorder_2**: Lost-in-the-middle reordering (top 2 reinforced)

### 9. Generator (3 options)
- **gemma3:27b**: Gemma3 27B model
- **alibayram/Qwen3-30B-A3B-Instruct-2507:latest**: Qwen3 30B model
- **multi_llm_ensemble**: Multi-LLM ensemble with Qwen3 aggregation

### 10. Post-Generation (2 options)
- **none**: No post-processing
- **reflection_revising**: Self-reflection and iterative revision

**Total Search Space**: 4 × 9 × 11 × 4 × 2 × 3 × 3 × 3 × 3 × 2 = **381,024 possible configurations**

## 🔧 Manual Testing

### Test a Single Configuration

You can test specific RAG configurations manually using curl:

```bash
# From host machine (replace with your server IP if remote)
curl -X POST http://localhost:8060/api/evaluate \
  -H "Content-Type: application/json" \
  -d '{
    "evaluation_request": {
      "pipeline_config": {
        "pre-embedding": "pre-embedding_none",
        "query-expansion": "query-expansion_none",
        "retrieval": "retrieval-vector_mxbai",
        "passage-rerank": "passage-rerank_none",
        "passage-filter": "passage-filter_simple_threshold",
        "passage-augment": "passage-augment_none",
        "passage-compress": "passage-compress_none",
        "prompt-maker": "prompt-maker_simple_listing",
        "generator": "generator_alibayram/Qwen3-30B-A3B-Instruct-2507:latest",
        "post-generation": "post-generation_none"
      }
    }
  }'

# From inside Docker network
curl -X POST http://rag_pipeline:8060/api/evaluate \
  -H "Content-Type: application/json" \
  -d '...'  # Same payload as above

# From remote machine (replace YOUR_SERVER_IP)
curl -X POST http://YOUR_SERVER_IP:8060/api/evaluate \
  -H "Content-Type: application/json" \
  -d '...'  # Same payload as above
```

The response will include:
```json
{
  "evaluation": {
    "final_score": 0.75,
    "retrieval_metrics": {...},
    "generation_metrics": {...}
  }
}
```

## 🎛️ Configuration

### Changing the Dataset

The system includes multiple test datasets in `rag_pipeline/default_datasets/`:
- `finance_10`: Finance domain
- `law_10`: Legal domain
- `maths_10`: Mathematics domain
- `medicine_10`: Medical domain (11 test cases)
- `military_10`: Military domain (default)
- `programming_10`: Programming domain

The default dataset is `military_10`. To change it:
1. Edit `rag_pipeline/core/dataset.py`
2. Find `"military_10"` (appears in 3 locations: lines 34, 107, and other default locations)
3. Replace with your desired dataset name (e.g., `"finance_10"`, `"law_10"`, etc.)

### Limiting Test Cases

To reduce evaluation time, limit the number of test cases:

Edit `rag_pipeline/main.py` in the `parse_config()` method under the `# Dataset/global settings` section:

```python
max_test_cases=100  # Change this value
```

### Changing the LLM Evaluator Model

The LLM evaluator (judge) model can be changed in `rag_pipeline/main.py` in the `parse_config()` method:

```python
# Around line 144 in main.py
llm_eval_model='gpt-oss:120B'  # Change to your desired model
```

Current default is `gpt-oss:120B`. You can change it to any Ollama model (e.g., `alibayram/Qwen3-30B-A3B-Instruct-2507:latest`, `gemma3:27b`, etc.)

### Changing the Generator LLM

To change the main generation LLM:
1. Search for `alibayram/Qwen3-30B-A3B-Instruct-2507:latest` in the codebase
2. Replace with your desired Ollama model name
3. Ensure the model is available in your Ollama instance

### Genetic Algorithm Parameters

Edit `genetic_search_for_rag_pipeline/run.py` to adjust optimization parameters:

```python
# Quick mode
config = GAConfig(
    category_sizes=category_sizes,
    population_size=20,      # Number of candidates per generation
    generations=3,           # Number of generations
    crossover_rate=0.8,      # Probability of crossover
    mutation_rate=0.1,       # Probability of mutation
    elitism_count=2          # Best individuals preserved
)

# Comprehensive mode
config = GAConfig(
    population_size=16,
    generations=20,
    crossover_rate=0.8,
    mutation_rate=0.1,
    elitism_count=2
)
```

## 🐳 Docker Configuration

### GPU Assignment

The system uses multiple GPUs:

- **GPU 0**: `rag_pipeline` container (for reranking models)
- **GPU 1**: `rag-pipeline-ollama-gpu` (primary LLM server)
- **GPU 2-3**: `rag-pipeline-ollama-gpu-2` (secondary LLM server)

To change GPU assignments, edit `docker-compose.yml`:

```yaml
deploy:
  resources:
    reservations:
      devices:
        - driver: nvidia
          device_ids: ['0']  # Change GPU ID here
          capabilities: [gpu]
```

### Persistent Storage

The system uses several volumes for persistent data:

- `rag_pipeline_reranker_cache`: Cached reranker models
- `genetic_algorithm_results`: GA optimization results and cache
- `rag_pipeline_qdrant_storage`: Vector database storage
- `ollama_storage_rag_pipeline`: Ollama model storage
- `neo4j_storage`: Neo4j graph database storage

### Environment Variables

Key environment variables in `docker-compose.yml`:

```yaml
# RAG Pipeline
QDRANT_URL=http://rag-pipeline-qdrant:6333
OLLAMA_API_URL=http://rag-pipeline-ollama-gpu:11434/api
OLLAMA_API_URL2=http://rag-pipeline-ollama-gpu-2:11434/api
GEMINI_API_KEY=your-api-key-here

# Genetic Algorithm
RAG_PIPELINE_URL=http://rag_pipeline:8060
GA_RESULTS_DIR=/app/results
CACHE_FILE_PATH=/app/results/rag_evaluation_cache.json
```

## 🧬 Genetic Algorithm Features

### Selection Methods
- **Tournament Selection**: Compete small groups, select winner
- **Roulette Wheel Selection**: Fitness-proportional selection
- **Rank Selection**: Rank-based selection
- **Elite Selection**: Always select the best

### Crossover Methods
- **Single Point Crossover**: One crossover point
- **Multi-Point Crossover**: Multiple crossover points
- **Uniform Crossover**: Gene-by-gene random selection
- **Order Crossover**: Preserve gene ordering
- **Segment Crossover**: Exchange gene segments

### Mutation Methods
- **Random Mutation**: Random gene changes
- **Adaptive Mutation**: Self-adjusting mutation rate
- **Gaussian Mutation**: Gaussian noise-based
- **Swap Mutation**: Swap gene positions
- **Inversion Mutation**: Reverse gene segments
- **Composite Mutation**: Multiple strategies

### Caching System

The genetic algorithm includes intelligent caching:

- **Persistent Cache**: Evaluations saved to `genetic_algorithm_results/rag_evaluation_cache.json`
- **Auto-save**: Cache updated after each evaluation
- **Resume Support**: Can resume optimization using cached results
- **Statistics**: Cache hit rate and performance metrics tracked

### Termination Criteria

Optimization stops when:
1. Maximum generations reached
2. Target fitness achieved
3. No improvement for N generations (convergence)
4. Manual interruption (results saved)

## 📊 Results and Analysis

### Result Files

After optimization, results are saved to `genetic_algorithm_results/`:

- `optimization_results_TIMESTAMP.md`: Detailed markdown report
- `rag_evaluation_cache.json`: Cached evaluations for resume
- `generation_*.json`: Per-generation statistics

### Result Format

The markdown report includes:

```markdown
# Best Configuration
- Final Score: 0.85
- Components:
  - pre-embedding: contextual_chunk_headers
  - query-expansion: hyde
  - retrieval: hybrid_search
  ...

# Evolution Statistics
- Total evaluations: 250
- Cache hit rate: 15%
- Search space explored: 0.17%

# Generation Progress
Gen 1: Best=0.65, Avg=0.52, Diversity=0.82
Gen 2: Best=0.71, Avg=0.58, Diversity=0.76
...
```

## 📈 Evaluation Metrics

### Retrieval Metrics
- **Recall@K**: Proportion of relevant documents retrieved
- **mAP**: Mean Average Precision
- **nDCG@K**: Normalized Discounted Cumulative Gain
- **MRR**: Mean Reciprocal Rank

### Generation Metrics
- **LLM Score**: LLM-based answer quality (0-1)
- **Semantic Similarity**: Embedding similarity to ground truth (0-1)

### Combined Score
- **Final Score**: Weighted combination of retrieval (30%) and generation (70%)

## 🔌 API Reference

### RAG Pipeline API

**Endpoint**: `POST /api/evaluate`

**Request**:
```json
{
  "evaluation_request": {
    "pipeline_config": {
      "pre-embedding": "pre-embedding_none",
      "query-expansion": "query-expansion_simple_multi_query",
      "retrieval": "retrieval-vector_mxbai",
      "passage-rerank": "passage-rerank_cross_encoder",
      "passage-filter": "passage-filter_simple_threshold",
      "passage-augment": "passage-augment_none",
      "passage-compress": "passage-compress_none",
      "prompt-maker": "prompt-maker_simple_listing",
      "generator": "generator_alibayram/Qwen3-30B-A3B-Instruct-2507:latest",
      "post-generation": "post-generation_none"
    }
  }
}
```

**Response**:
```json
{
  "evaluation": {
    "final_score": 0.85,
    "retrieval_score": 0.80,
    "generation_score": 0.88,
    "retrieval_metrics": {
      "recall": 0.85,
      "map": 0.78,
      "ndcg": 0.82,
      "mrr": 0.75
    },
    "generation_metrics": {
      "llm_score": 0.90,
      "semantic_similarity": 0.85
    }
  }
}
```

## 🛠️ Development

### Running Tests

```bash
# Test RAG pipeline components
docker exec -it rag-pipeline python -m pytest

# Test genetic algorithm
docker exec -it rag-pipeline-genetic-search-rag python test_implementation.py
```

### Adding New RAG Components

1. Create implementation in `rag_pipeline/core/modular_implementations/`
2. Register in `__init__.py` COMPONENT_REGISTRY
3. Update configuration mapping in `util/misc/config_map.py`

Example:
```python
# In modular_implementations/retrieval.py
class MyCustomRetrieval(RetrievalComponent):
    async def retrieve(self, query: Query, top_k: int) -> RetrievalResult:
        # Your implementation
        pass

# In modular_implementations/__init__.py
COMPONENT_REGISTRY = {
    "retrieval": {
        ...
        "my_custom": MyCustomRetrieval,
    }
}
```

### Adding Custom Evaluation Functions

```python
# In genetic_search_for_rag_pipeline/rag_evaluator.py
class CustomRAGEvaluator(RAGPipelineEvaluator):
    def evaluate(self, candidate: List[int]) -> float:
        # Custom evaluation logic
        config = self._candidate_to_config(candidate)
        # Your scoring logic
        return score
```

## 🔄 Troubleshooting

### Common Issues

**GPU Not Detected**
```bash
# Check GPU availability
nvidia-smi

# Verify Docker can access GPU
docker run --rm --gpus all nvidia/cuda:11.8.0-base-ubuntu22.04 nvidia-smi
```

**Ollama Connection Issues**
```bash
# Check Ollama is running
docker ps | grep ollama

# Test connection
curl http://localhost:11435/api/tags
```

**Cache Not Persisting**
```bash
# Check volume exists
docker volume ls | grep genetic_algorithm

# Verify mount point
docker exec rag-pipeline-genetic-search-rag ls -la /app/results/
```

**Out of Memory**
- Reduce `population_size` and `generations` in GA config
- Reduce `max_test_cases` in RAG pipeline config
- Limit concurrent evaluations

### Logs

```bash
# All services
docker-compose logs -f

# Specific service
docker logs -f rag-pipeline
docker logs -f rag-pipeline-genetic-search-rag

# Follow recent logs
docker logs --tail 100 -f rag-pipeline
```

## 📚 Additional Resources

- **Modular Framework Guide**: `rag_pipeline/MODULAR_FRAMEWORK_GUIDE.md`
- **RAG Pipeline README**: `rag_pipeline/README.md`
- **Genetic Algorithm README**: `genetic_search_for_rag_pipeline/README.md`

## 🎯 Use Cases

- **RAG Research**: Systematically evaluate RAG techniques
- **Production Optimization**: Find best configuration for your domain
- **Benchmark Creation**: Compare RAG approaches fairly
- **Component Analysis**: Understand component interactions
- **Hyperparameter Tuning**: Optimize RAG parameters automatically

## ⚡ Performance Tips

1. **Start Small**: Use quick mode first to verify setup
2. **Use Caching**: Enable persistent cache for faster iterations
3. **GPU Allocation**: Distribute load across multiple GPUs
4. **Parallel Evaluation**: Run multiple optimizations in parallel
5. **Dataset Size**: Start with small datasets (10-20 cases)
6. **Incremental Optimization**: Run short optimizations, analyze, then continue

## 🤝 Contributing

This project is designed for research and experimentation. Feel free to:

- Add new RAG components and techniques
- Implement custom evaluation metrics
- Extend the genetic algorithm with new operators
- Improve caching and performance
- Add support for new LLM providers

## 📄 License

This project is provided as-is for research and educational purposes.

## 🙋 Support

For questions or issues:

1. Check the troubleshooting section
2. Review the detailed component READMEs
3. Examine the example configurations
4. Check Docker logs for error details

## 🔬 Citation

If you use this system in your research, please cite:

```
RAG Pipeline with Genetic Algorithm Optimization
A modular framework for evaluating and optimizing Retrieval-Augmented Generation systems
https://github.com/your-repo/rag_pipeline_deneme
```

## 📋 Quick Reference

### Essential Commands

```bash
# Start all services
docker-compose up -d

# Run genetic algorithm optimization
docker exec -itd rag-pipeline-genetic-search-rag python run.py --comprehensive

# Test single RAG configuration
curl -X POST http://localhost:8060/api/evaluate \
  -H "Content-Type: application/json" \
  -d '{"evaluation_request": {"pipeline_config": {...}}}'

# View logs
docker logs -f rag-pipeline-genetic-search-rag
docker logs -f rag-pipeline

# Check GPU usage
nvidia-smi

# Stop all services
docker-compose down
```

### File Locations to Modify

- **Change dataset**: `rag_pipeline/core/dataset.py` (search for `"military_10"`)
- **Change test case limit**: `rag_pipeline/main.py` line ~121 (`max_test_cases=100`)
- **Change LLM evaluator**: `rag_pipeline/main.py` line ~144 (`llm_eval_model='gpt-oss:120B'`)
- **Change generator LLM**: Search for `alibayram/Qwen3-30B-A3B-Instruct-2507:latest` across codebase
- **GA optimization params**: `genetic_search_for_rag_pipeline/run.py` (population_size, generations)

### Key Environment Variables

Set in `docker-compose.yml` or `.env` file:
- `RAG_PIPELINE_URL`: URL of RAG evaluation API (default: http://rag_pipeline:8060)
- `OLLAMA_API_URL`: Primary Ollama server URL
- `OLLAMA_API_URL2`: Secondary Ollama server URL
- `QDRANT_URL`: Vector database URL
- `GEMINI_API_KEY`: Google Gemini API key (optional, set in `.env` file)
- `CACHE_FILE_PATH`: Path for GA evaluation cache
- `GA_RESULTS_DIR`: Directory for saving optimization results

**Security Best Practice**: Store sensitive values like `GEMINI_API_KEY` in a `.env` file (already in `.gitignore`), not in `docker-compose.yml`.

---

**Current Status**: Active development - tracking progress with RAG method experimentation

**Version**: 1.0.0

**Last Updated**: October 2025
