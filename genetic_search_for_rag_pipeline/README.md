# Genetic Algorithm for Component Combination Search

A comprehensive, modular genetic algorithm system designed for finding optimal combinations of components from different categories. Perfect for problems like RAG pipeline optimization, where you need to select one component from each of several categories to maximize overall performance.

## 🚀 Key Features

- **Modular Design**: Easily swap between different selection, crossover, and mutation methods
- **Professional Architecture**: Clean, well-documented code structure following best practices
- **Comprehensive Configuration**: Extensive configuration options with sensible defaults
- **Ready to Run**: Works out of the box with example evaluation functions
- **Statistics Tracking**: Detailed evolution statistics and performance analysis
- **Multiple Termination Criteria**: Generation limits, convergence detection, target fitness
- **Production Ready**: Robust error handling and validation

## 📦 Installation

Simply clone or download this repository. The system is self-contained and requires only Python 3.7+ with standard libraries.

```bash
git clone <repository-url>
cd genetic_search_for_rag_pipeline
```

## 🎯 Quick Start

### Basic Usage

```python
from genetic_algorithm import GeneticAlgorithm
from config import GAConfig

# Define your evaluation function
def evaluate(candidate):
    """Evaluate a combination and return fitness score (0-100)"""
    # Your evaluation logic here
    return sum(candidate) * 2.0  # Simple example

# Create configuration
config = GAConfig.create_default()

# Run genetic algorithm
ga = GeneticAlgorithm(config, evaluate)
results = ga.run()

print(f"Best combination: {results['best_combination']}")
print(f"Best fitness: {results['best_fitness']:.2f}")
```

### Advanced Configuration

```python
from genetic_algorithm import GeneticAlgorithm
from config import GAConfig
from selection import TournamentSelection
from crossover import UniformCrossover
from mutation import AdaptiveMutation

# Custom configuration
config = GAConfig(
    category_sizes=[5, 8, 6, 10, 3, 12],  # Boxes per category
    population_size=100,
    generations=200,
    crossover_rate=0.85,
    mutation_rate=0.12,
    elitism_count=5,
    selection_method=TournamentSelection(tournament_size=5),
    crossover_method=UniformCrossover(probability=0.6),
    mutation_method=AdaptiveMutation(base_mutation_rate=0.12),
    convergence_threshold=25,
    random_seed=42,
    verbose=True
)

ga = GeneticAlgorithm(config, your_evaluate_function)
results = ga.run()
```

## 🏗️ Architecture

The system is built with a modular architecture:

### Core Components

- **`GeneticAlgorithm`**: Main orchestrator class
- **`Individual`**: Represents a single solution
- **`Population`**: Manages groups of individuals
- **`GAConfig`**: Configuration management

### Genetic Operators

#### Selection Methods
- `TournamentSelection`: Tournament-based selection
- `RouletteWheelSelection`: Fitness-proportional selection
- `RankSelection`: Rank-based selection
- `EliteSelection`: Best individuals selection

#### Crossover Methods
- `SinglePointCrossover`: Classic single-point crossover
- `MultiPointCrossover`: Multiple crossover points
- `UniformCrossover`: Gene-by-gene random selection
- `OrderCrossover`: Order-preserving crossover
- `SegmentCrossover`: Segment-based exchange

#### Mutation Methods
- `RandomMutation`: Simple random gene changes
- `AdaptiveMutation`: Self-adjusting mutation rate
- `GaussianMutation`: Gaussian noise-based mutation
- `SwapMutation`: Gene position swapping
- `InversionMutation`: Segment inversion
- `CompositeMutation`: Multiple mutation strategies

## 📊 Configuration Options

### YAML Configuration (Recommended)

Configuration is now centralized in `gen_search_config.yml` in the project root:

```yaml
genetic_algorithm:
  # Population settings
  population_size: 50
  generations: 100
  
  # Genetic operator probabilities
  crossover_rate: 0.8
  mutation_rate: 0.1
  elitism_count: 2
  
  # Selection method (tournament, roulette_wheel, rank, elite)
  selection:
    method: "tournament"
    tournament_size: 3
  
  # Crossover method (single_point, multi_point, uniform, order, segment)
  crossover:
    method: "single_point"
    num_points: 2
    probability: 0.5
  
  # Mutation method (random, adaptive, categorical, swap, inversion)
  mutation:
    method: "random"
    base_mutation_rate: 0.1
    min_mutation_rate: 0.01
    max_mutation_rate: 0.5
  
  # Termination criteria
  convergence_threshold: 20
  target_fitness: null  # Set to a value (0-1) to stop early
  
  # Runtime settings
  random_seed: null  # Set for reproducibility
  verbose: true

# Search space - available RAG techniques
search_space:
  pre-embedding:
    - "pre-embedding_none"
    - "pre-embedding_contextual_chunk_headers"
  retrieval:
    - "retrieval-vector_mxbai"
    - "retrieval-hybrid_vector_keyword_cc"
  # ... more categories
```

### Python Configuration (Programmatic)

```python
config = GAConfig(
    category_sizes=[3, 5, 4, 6, 2, 7, 3, 5, 4, 6],  # Boxes per category
    population_size=50,                               # Population size
    generations=100,                                  # Max generations
    crossover_rate=0.8,                              # Crossover probability
    mutation_rate=0.1,                               # Mutation probability
    elitism_count=2,                                 # Elite individuals preserved
    random_seed=None,                                # For reproducibility
    verbose=True                                     # Progress output
)
```

### Termination Criteria

```python
config = GAConfig(
    convergence_threshold=20,    # Stop if no improvement for N generations
    target_fitness=95.0,         # Stop if this fitness is reached
    generations=1000             # Maximum generations
)
```

### Pre-configured Setups

```python
# Quick testing
config = GAConfig.create_small_test()

# High performance
config = GAConfig.create_large_scale()

# High diversity exploration
config = GAConfig.create_high_diversity()
```

## 🔧 Usage Examples

### Example 1: Simple Optimization

```python
def simple_evaluate(candidate):
    """Maximize sum with balanced selection bonus"""
    base_score = sum(candidate) * 3.0
    
    # Bonus for balanced selections
    balance_bonus = 10.0 if all(0 < gene < max_gene-1 for gene, max_gene in 
                                zip(candidate, [3,5,4,6,2,7,3,5,4,6])) else 0.0
    
    return min(100.0, base_score + balance_bonus)

config = GAConfig.create_default()
ga = GeneticAlgorithm(config, simple_evaluate)
results = ga.run()
```

### Example 2: RAG Pipeline Optimization

```python
def evaluate_rag_pipeline(candidate):
    """Evaluate RAG pipeline configuration"""
    # candidate[0]: Embedding model (0-4)
    # candidate[1]: Vector database (0-2) 
    # candidate[2]: Retrieval strategy (0-5)
    # candidate[3]: LLM model (0-6)
    # candidate[4]: Prompt template (0-2)
    
    scores = {
        'embedding': [10, 25, 30, 35, 20][candidate[0]],
        'vector_db': [15, 25, 20][candidate[1]],
        'retrieval': [12, 18, 22, 28, 15, 20][candidate[2]],
        'llm': [20, 35, 30, 40, 25, 45, 35][candidate[3]],
        'prompt': [10, 20, 25][candidate[4]]
    }
    
    base_score = sum(scores.values())
    
    # Synergy bonuses for good combinations
    synergy = 0.0
    if candidate[0] >= 2 and candidate[3] >= 4:  # Good embedding + good LLM
        synergy += 15.0
    if candidate[1] == 1 and candidate[2] in [2, 3]:  # Good DB + retrieval
        synergy += 10.0
    
    total = base_score + synergy
    return min(100.0, (total / 200.0) * 100.0)  # Normalize to 0-100

config = GAConfig(
    category_sizes=[5, 3, 6, 7, 3],
    population_size=80,
    generations=150
)

ga = GeneticAlgorithm(config, evaluate_rag_pipeline)
results = ga.run()
```

## 📈 Results and Analysis

The `run()` method returns a comprehensive results dictionary:

```python
results = ga.run()

print(f"Best combination: {results['best_combination']}")
print(f"Best fitness: {results['best_fitness']:.2f}")
print(f"Generations completed: {results['generations_completed']}")
print(f"Total time: {results['total_time']:.2f} seconds")
print(f"Converged: {results['converged']}")

# Access detailed statistics
for stat in results['statistics']:
    print(f"Gen {stat.generation}: Best={stat.best_fitness:.2f}, "
          f"Avg={stat.average_fitness:.2f}, Diversity={stat.diversity_score:.3f}")

# Get summary statistics
summary = ga.get_statistics_summary()
print(f"Fitness improvement: {summary['fitness_improvement']:.2f}")
print(f"Total evaluations: {summary['total_evaluations']}")
```

## 🎮 Running Examples

The package includes comprehensive examples:

```bash
python example.py
```

This will run:
- Small test example (quick verification)
- Basic example with default configuration  
- Advanced example with custom configuration
- Comparison of different algorithm configurations

## 🔬 Advanced Features

### Custom Genetic Operators

```python
from selection import SelectionMethod
from individual import Individual
from population import Population

class CustomSelection(SelectionMethod):
    def select(self, population: Population, num_parents: int):
        # Your custom selection logic
        return selected_parents

config = GAConfig(selection_method=CustomSelection())
```

### Adaptive Parameters

```python
from mutation import AdaptiveMutation

# Mutation rate adapts based on population diversity and fitness improvement
adaptive_mutation = AdaptiveMutation(
    base_mutation_rate=0.1,
    min_mutation_rate=0.01,
    max_mutation_rate=0.5
)

config = GAConfig(mutation_method=adaptive_mutation)
```

### Statistics Tracking

```python
config = GAConfig(
    track_statistics=True,
    statistics_interval=1  # Record every generation
)

ga = GeneticAlgorithm(config, evaluate_func)
results = ga.run()

# Plot evolution curves, analyze diversity trends, etc.
import matplotlib.pyplot as plt

generations = [s.generation for s in results['statistics']]
best_fitness = [s.best_fitness for s in results['statistics']]
diversity = [s.diversity_score for s in results['statistics']]

plt.subplot(2, 1, 1)
plt.plot(generations, best_fitness)
plt.title('Fitness Evolution')

plt.subplot(2, 1, 2)
plt.plot(generations, diversity)
plt.title('Population Diversity')

plt.show()
```

## 🎯 Use Cases

This genetic algorithm system is ideal for:

- **RAG Pipeline Optimization**: Select optimal components for retrieval-augmented generation
- **Hyperparameter Tuning**: Find best parameter combinations for ML models
- **System Configuration**: Optimize complex system configurations
- **Resource Allocation**: Optimal assignment of resources to categories
- **Product Configuration**: Find optimal product feature combinations
- **Architecture Search**: Neural architecture search and similar problems

## ⚡ Performance Tips

1. **Start Small**: Use `GAConfig.create_small_test()` to verify your evaluation function
2. **Set Random Seed**: Use `random_seed` parameter for reproducible results
3. **Monitor Convergence**: Use `convergence_threshold` to avoid unnecessary generations
4. **Use Elitism**: Keep best solutions with `elitism_count`
5. **Adaptive Mutation**: Use `AdaptiveMutation` for better exploration/exploitation balance
6. **Parallel Evaluation**: Consider parallelizing your evaluation function for large populations

## 📝 Best Practices

### Evaluation Function Design

```python
def good_evaluate_function(candidate):
    """
    Best practices for evaluation functions:
    1. Return float values between 0 and 100
    2. Handle edge cases gracefully
    3. Be deterministic or use controlled randomness
    4. Scale appropriately for your problem
    """
    
    # Validate input
    if not candidate or len(candidate) != expected_length:
        return 0.0
    
    # Your evaluation logic
    score = calculate_score(candidate)
    
    # Ensure proper range
    return max(0.0, min(100.0, score))
```

### Configuration Guidelines

```python
# For exploration (finding diverse solutions)
config = GAConfig(
    population_size=100,
    mutation_rate=0.2,
    crossover_rate=0.7,
    elitism_count=1,
    selection_method=RouletteWheelSelection()
)

# For exploitation (refining known good solutions)
config = GAConfig(
    population_size=50,
    mutation_rate=0.05,
    crossover_rate=0.9,
    elitism_count=10,
    selection_method=TournamentSelection(tournament_size=5)
)
```

## 🤝 Contributing

This is a complete, self-contained genetic algorithm system. Feel free to:

- Extend with custom genetic operators
- Add new selection, crossover, or mutation methods
- Implement additional statistics and analysis features
- Optimize performance for specific use cases

## 📄 License

This project is provided as-is for educational and research purposes. Feel free to modify and use according to your needs.

## 🙋 Support

For questions about implementation or usage:

1. Check the example scripts in `example.py`
2. Review the comprehensive documentation in the code
3. Experiment with different configurations using the provided presets
4. Start with small test cases before scaling up

## 🐳 Docker Containerization

The genetic algorithm system is fully containerized for easy deployment and integration with other services.

### Quick Start with Docker

```bash
# Build and run with docker-compose
docker-compose up -d

# Or build and run manually
docker build -t genetic-algorithm-search .
docker run -p 8000:8000 genetic-algorithm-search
```

### API Endpoints

Once containerized, the service exposes a REST API:

- **Base URL**: `http://localhost:8000`
- **Health Check**: `GET /health`
- **Start Optimization**: `POST /optimize`
- **Job Status**: `GET /status/{job_id}`
- **Job Results**: `GET /result/{job_id}`
- **List Jobs**: `GET /jobs`
- **Delete Job**: `DELETE /job/{job_id}`

### API Usage Example

```python
import requests

# Start optimization job
payload = {
    "job_id": "my_optimization_001",
    "config": {
        "category_sizes": [3, 5, 4, 6, 2, 7],
        "population_size": 50,
        "generations": 100,
        "selection_method": "tournament",
        "crossover_method": "single_point",
        "mutation_method": "adaptive"
    },
    "evaluation_function": {
        "function_type": "weighted_sum",
        "parameters": {
            "weights": [2.0, 1.5, 3.0, 2.5, 1.0, 2.0]
        }
    },
    "async_execution": true
}

response = requests.post("http://localhost:8000/optimize", json=payload)
result = response.json()

# Monitor job status
job_id = result["job_id"]
status = requests.get(f"http://localhost:8000/status/{job_id}").json()

# Get results when completed
if status["status"] == "completed":
    results = requests.get(f"http://localhost:8000/result/{job_id}").json()
    print(f"Best combination: {results['best_combination']}")
    print(f"Best fitness: {results['best_fitness']}")
```

### Evaluation Function Types

The API supports several built-in evaluation function types:

1. **simple_sum**: Basic sum with scaling
   ```json
   {
     "function_type": "simple_sum",
     "parameters": {"scale": 2.0, "max_value": 100.0}
   }
   ```

2. **weighted_sum**: Weighted combination
   ```json
   {
     "function_type": "weighted_sum", 
     "parameters": {"weights": [2.0, 1.5, 3.0, 2.5]}
   }
   ```

3. **polynomial**: Polynomial evaluation with interactions
   ```json
   {
     "function_type": "polynomial",
     "parameters": {
       "coefficients": [1.0, 0.1, 0.01],
       "interaction_weight": 0.1
     }
   }
   ```

4. **external_rag_api**: External RAG pipeline evaluation
   ```json
   {
     "function_type": "external_rag_api",
     "parameters": {
       "api_endpoint": "https://your-rag-service.com/api/evaluate",
       "timeout": 300,
       "max_retries": 3
     }
   }
   ```

5. **custom_rag**: Built-in RAG pipeline optimization
   ```json
   {
     "function_type": "custom_rag",
     "parameters": {
       "component_scores": {
         "component_0": [10, 25, 30, 35, 20],
         "component_1": [15, 25, 20]
       }
     }
   }
   ```

### Client Integration

Use the provided `client_example.py` to see complete integration examples:

```bash
# Run client examples (service must be running)
python client_example.py
```

The client demonstrates:
- Health checking
- Asynchronous job submission
- Progress monitoring
- Result retrieval
- Job management

### Production Deployment

For production use, the docker-compose includes optional services:

```bash
# Run with Redis and Nginx (production setup)
docker-compose --profile production up -d
```

This adds:
- **Redis**: For job queuing and caching
- **Nginx**: Reverse proxy with SSL support

### Service Configuration

Environment variables for containerized deployment:

- `LOG_LEVEL`: Logging level (default: info)
- `PYTHONUNBUFFERED`: Python output buffering (default: 1)

### Using the Configuration Loader

The genetic search now uses a centralized configuration loader:

```python
# Load configuration from gen_search_config.yml
from config_loader import load_config, get_search_space_as_component_options, get_api_endpoint

config = load_config()

# Access settings
print(f"Dataset: {config.dataset.path}")
print(f"API: {get_api_endpoint(config)}")
print(f"Population: {config.genetic_algorithm.population_size}")

# Get search space for evaluator
component_options = get_search_space_as_component_options(config)
```

### RAG Pipeline Evaluator Template

The system includes a specialized `RAGPipelineEvaluator` for optimizing RAG (Retrieval-Augmented Generation) pipelines:

```python
from rag_evaluator import RAGPipelineEvaluator

# Create evaluator - automatically loads from gen_search_config.yml
evaluator = RAGPipelineEvaluator()

# Or with explicit settings
evaluator = RAGPipelineEvaluator(
    api_endpoint="https://your-rag-service.com/api/evaluate",
    timeout=300,
    use_yaml_config=False  # Disable YAML loading
)

# Use with genetic algorithm
from genetic_algorithm import GeneticAlgorithm
from config import GAConfig

config = GAConfig(
    category_sizes=[3, 5, 4, 6, 2, 7, 3, 5, 4, 6],  # 10 RAG components
    population_size=100,
    generations=200
)

ga = GeneticAlgorithm(config, evaluator.evaluate)
results = ga.run()
```

#### RAG Component Categories

The evaluator maps candidates to 10 RAG component categories:

1. **Text Preprocessor**: Document cleaning and preparation
2. **Embedding Model**: Text-to-vector conversion  
3. **Vector Database**: Vector storage and indexing
4. **Retrieval Strategy**: Document retrieval method
5. **Reranking Method**: Result reordering
6. **LLM Model**: Language model selection
7. **Prompt Template**: Prompt engineering approach
8. **Context Window Management**: Context handling strategy
9. **Output Processor**: Response formatting
10. **Evaluation Metrics**: Assessment methodology

#### API Request Format

The evaluator sends structured requests to your RAG evaluation service:

```json
{
  "evaluation_request": {
    "pipeline_config": {
      "text_preprocessor": "advanced_nlp",
      "embedding_model": "sentence_transformers_large",
      "vector_database": "pinecone",
      "retrieval_strategy": "hybrid_search",
      "reranking_method": "cross_encoder_rerank",
      "llm_model": "gpt_4",
      "prompt_template": "chain_of_thought",
      "context_window_mgmt": "sliding_window",
      "output_processor": "structured_extraction",
      "evaluation_metrics": "comprehensive_metrics"
    },
    "evaluation_settings": {
      "test_dataset": "default",
      "metrics": ["relevance", "accuracy", "latency", "cost"],
      "sample_size": 100
    }
  }
}
```

#### Customizing for Your Domain

Override component options for domain-specific RAG systems:

```python
class CustomRAGEvaluator(RAGPipelineEvaluator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.component_options = {
            "embedding_model": [
                "biobert_embeddings",
                "legal_bert_embeddings", 
                "domain_specific_embeddings"
            ],
            "llm_model": [
                "gpt_4_medical",
                "claude_legal_specialist",
                "domain_expert_llm"
            ]
            # ... customize other components
        }
```

### Integration with Other Projects

The containerized service is designed for easy integration:

1. **Microservices Architecture**: Deploy as independent service
2. **API-First Design**: REST API for language-agnostic integration
3. **Async Processing**: Non-blocking optimization jobs
4. **Health Monitoring**: Built-in health checks for orchestration
5. **Scalable**: Can be deployed multiple instances behind load balancer
6. **RAG-Optimized**: Specialized evaluator for RAG pipeline optimization

## 🔄 Version History

- **v1.0.0**: Initial comprehensive implementation
  - Full genetic algorithm system
  - Multiple selection, crossover, and mutation methods
  - Comprehensive configuration system
  - Statistics tracking and analysis
  - Production-ready code with extensive documentation
  - **NEW**: Docker containerization with REST API
  - **NEW**: FastAPI interface for external communication
  - **NEW**: Client libraries and integration examples 