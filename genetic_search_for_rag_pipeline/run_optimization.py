"""
RAG Pipeline Optimization Script
===============================

Production-ready script to optimize your RAG pipeline using genetic algorithms.
Configuration is loaded from gen_search_config.yml.

Usage:
    python run_optimization.py
"""

import os
import sys
from typing import List, Dict, Any, Optional

# Add parent directory to path for config_loader import
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from genetic_algorithm import GeneticAlgorithm
from config import GAConfig
from rag_evaluator import RAGPipelineEvaluator
from selection import TournamentSelection, RouletteWheelSelection, EliteSelection
from crossover import SinglePointCrossover, UniformCrossover, MultiPointCrossover
from mutation import RandomMutation, AdaptiveMutation, CategoricalMutation


def load_yaml_config():
    """Load configuration from gen_search_config.yml"""
    try:
        from config_loader import load_config, get_search_space_as_component_options, get_api_endpoint
        config = load_config()
        return config
    except Exception as e:
        print(f"⚠️ Could not load YAML config: {e}. Using defaults.")
        return None


def run_rag_optimization(
    api_endpoint: str,
    component_options: Dict[str, List[str]],
    population_size: int = 50,
    generations: int = 100,
    crossover_rate: float = 0.8,
    mutation_rate: float = 0.1,
    elitism_count: int = 3,
    convergence_threshold: int = 20,
    target_fitness: float = 95.0,
    timeout: int = 300,
    max_retries: int = 3,
    verbose: bool = True,
    evaluation_function: Optional[Any] = None  # For testing only
) -> Dict[str, Any]:
    """
    Run RAG pipeline optimization using genetic algorithm.
    
    Args:
        api_endpoint: URL of your RAG evaluation API
        component_options: Dict mapping component categories to available options
        population_size: Number of candidates per generation
        generations: Maximum number of generations
        crossover_rate: Probability of crossover (0.0-1.0)
        mutation_rate: Probability of mutation (0.0-1.0)
        elitism_count: Number of best individuals to preserve
        convergence_threshold: Stop if no improvement for N generations
        target_fitness: Stop if this fitness score is reached
        timeout: API call timeout in seconds
        max_retries: Maximum API call retries
        verbose: Print progress information
        evaluation_function: Override evaluation function (for testing)
        
    Returns:
        Dictionary containing optimization results
    """
    
    if verbose:
        print("🚀 RAG Pipeline Optimization")
        print("=" * 50)
    
    # Calculate category sizes
    category_sizes = [len(options) for options in component_options.values()]
    
    # Create evaluator
    if evaluation_function:
        # Use provided evaluation function (for testing)
        evaluate_func = evaluation_function
    else:
        # Use RAG API evaluator
        evaluator = RAGPipelineEvaluator(
            api_endpoint=api_endpoint,
            timeout=timeout,
            max_retries=max_retries
        )
        evaluator.component_options = component_options
        evaluate_func = evaluator.evaluate
    
    # Configure genetic algorithm
    config = GAConfig(
        population_size=population_size,
        generations=generations,
        crossover_rate=crossover_rate,
        mutation_rate=mutation_rate,
        elitism_count=elitism_count,
        selection_method=TournamentSelection(tournament_size=3),
        crossover_method=UniformCrossover(probability=0.6),
        mutation_method=AdaptiveMutation(),
        convergence_threshold=convergence_threshold,
        target_fitness=target_fitness,
        verbose=verbose,
        track_statistics=True
    )
    
    if verbose:
        total_combinations = 1
        for size in category_sizes:
            total_combinations *= size
        print(f"📊 Search Space: {total_combinations:,} total combinations")
        print(f"👥 Population: {population_size} candidates")
        print(f"🔄 Max Generations: {generations}")
        print(f"🎯 API: {api_endpoint}")
        print(f"📂 Components: {len(component_options)} categories")
        print()
    
    # Create and run genetic algorithm
    ga = GeneticAlgorithm(
        config=config,
        category_sizes=category_sizes,
        evaluate_function=evaluate_func
    )
    
    results = ga.run()
    
    # Add component decoding to results
    if results['best_combination']:
        results['best_configuration'] = decode_configuration(
            results['best_combination'], 
            component_options
        )
    
    if verbose:
        print_results(results, component_options)
    
    return results


def decode_configuration(combination: List[int], component_options: Dict[str, List[str]]) -> Dict[str, str]:
    """
    Convert genetic algorithm result to readable configuration.
    
    Args:
        combination: List of component indices from GA
        component_options: Available component options
        
    Returns:
        Human-readable configuration mapping
    """
    config = {}
    component_names = list(component_options.keys())
    
    for i, choice_index in enumerate(combination):
        component_name = component_names[i]
        options = component_options[component_name]
        config[component_name] = options[choice_index]
    
    return config


def print_results(results: Dict[str, Any], component_options: Dict[str, List[str]]):
    """Print formatted optimization results."""
    
    print("\n🎉 Optimization Complete!")
    print("=" * 50)
    print(f"🏆 Best Fitness: {results['best_fitness']:.4f}")
    print(f"⏱️  Total Time: {results['total_time']:.2f} seconds")
    print(f"🔄 Generations: {results['generations_completed']}")
    print(f"📈 Converged: {results['converged']}")
    print(f"🎯 Target Reached: {results.get('target_reached', False)}")
    
    if 'best_configuration' in results:
        print(f"\n🔧 Best RAG Configuration:")
        print("-" * 40)
        for i, (component, choice) in enumerate(results['best_configuration'].items(), 1):
            print(f"{i:2}. {component:20}: {choice}")
    
    print(f"\n📊 Final Statistics:")
    final_stats = results.get('final_population_stats', {})
    print(f"   • Population Diversity: {final_stats.get('diversity_score', 'N/A'):.3f}")
    print(f"   • Average Fitness: {final_stats.get('average_fitness', 'N/A'):.4f}")
    print(f"   • Total Evaluations: {results['generations_completed'] * results['config']['population_size']:,}")


# =============================================================================
# CONFIGURATION TEMPLATES
# =============================================================================

def get_minimal_rag_components():
    """Minimal RAG component set for quick testing."""
    return {
        "embedding_model": ["sentence_transformers", "openai_ada002", "cohere"],
        "vector_database": ["faiss", "pinecone", "chroma"], 
        "retrieval_strategy": ["similarity", "mmr", "hybrid"],
        "llm_model": ["gpt_3_5", "gpt_4", "claude"]
    }


def get_comprehensive_rag_components():
    """Comprehensive RAG component set for production optimization."""
    return {
        "text_preprocessor": [
            "basic_cleaning", "advanced_nlp", "domain_specific", "multilingual"
        ],
        "embedding_model": [
            "sentence_transformers", "openai_ada002", "cohere_embed", 
            "custom_bert", "e5_large"
        ],
        "vector_database": [
            "faiss", "pinecone", "weaviate", "chroma", "qdrant"
        ],
        "retrieval_strategy": [
            "similarity_search", "mmr", "hybrid_search", 
            "contextual_retrieval", "multi_query"
        ],
        "reranking_method": [
            "no_reranking", "cross_encoder", "llm_reranking", "feature_based"
        ],
        "prompt_template": [
            "basic_qa", "chain_of_thought", "few_shot", "structured_output"
        ],
        "llm_model": [
            "gpt_3_5_turbo", "gpt_4", "claude_3", "llama_2_70b", "gemini_pro"
        ],
        "generation_config": [
            "conservative", "balanced", "creative", "deterministic"
        ],
        "chunk_strategy": [
            "fixed_size", "semantic_chunking", "sliding_window", "hierarchical"
        ],
        "response_processing": [
            "direct_output", "fact_checking", "citation_formatting", "confidence_scoring"
        ]
    }


def get_quick_config():
    """Quick optimization configuration for testing."""
    return {
        "population_size": 20,
        "generations": 30, 
        "crossover_rate": 0.8,
        "mutation_rate": 0.15,
        "convergence_threshold": 10,
        "verbose": True
    }


def get_production_config():
    """Production optimization configuration for thorough search."""
    return {
        "population_size": 100,
        "generations": 200,
        "crossover_rate": 0.8,
        "mutation_rate": 0.05,
        "elitism_count": 10,
        "convergence_threshold": 30,
        "target_fitness": 95.0,
        "verbose": True
    }


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """
    Main execution function. Configuration is loaded from gen_search_config.yml.
    """
    
    print("🧬 RAG Pipeline Genetic Algorithm Optimizer")
    print("=" * 50)
    
    # Load configuration from YAML file
    yaml_config = load_yaml_config()
    
    if yaml_config is not None:
        try:
            from config_loader import get_search_space_as_component_options, get_api_endpoint
            
            # Get configuration from YAML
            API_ENDPOINT = get_api_endpoint(yaml_config)
            COMPONENTS = get_search_space_as_component_options(yaml_config)
            
            CONFIG = {
                "population_size": yaml_config.genetic_algorithm.population_size,
                "generations": yaml_config.genetic_algorithm.generations,
                "crossover_rate": yaml_config.genetic_algorithm.crossover_rate,
                "mutation_rate": yaml_config.genetic_algorithm.mutation_rate,
                "elitism_count": yaml_config.genetic_algorithm.elitism_count,
                "convergence_threshold": yaml_config.genetic_algorithm.convergence_threshold,
                "target_fitness": yaml_config.genetic_algorithm.target_fitness * 100 if yaml_config.genetic_algorithm.target_fitness else None,  # Convert 0-1 to 0-100
                "verbose": yaml_config.genetic_algorithm.verbose
            }
            
            print(f"✅ Configuration loaded from gen_search_config.yml")
        except Exception as e:
            print(f"⚠️ Error parsing YAML config: {e}. Using fallback.")
            API_ENDPOINT = "http://rag_pipeline:8060/api/evaluate"
            COMPONENTS = get_comprehensive_rag_components()
            CONFIG = get_production_config()
    else:
        # Fallback to hardcoded defaults
        API_ENDPOINT = "http://rag_pipeline:8060/api/evaluate"
        COMPONENTS = get_comprehensive_rag_components()
        CONFIG = get_production_config()
    
    # Run optimization
    try:
        print(f"🎯 Starting optimization...")
        print(f"📡 API Endpoint: {API_ENDPOINT}")
        print(f"📂 Components: {len(COMPONENTS)} categories")
        print(f"⚙️  Config: {CONFIG['population_size']} pop, {CONFIG['generations']} gen")
        print()
        
        results = run_rag_optimization(
            api_endpoint=API_ENDPOINT,
            component_options=COMPONENTS,
            **CONFIG
        )
        
        print(f"\n✅ Optimization completed successfully!")
        print(f"💾 Results saved in returned dictionary")
        
        return results
        
    except Exception as e:
        print(f"\n❌ Error during optimization:")
        print(f"   {str(e)}")
        print(f"\n💡 Troubleshooting:")
        print(f"   1. Check your API endpoint is accessible: {API_ENDPOINT}")
        print(f"   2. Ensure your API returns JSON with 'final_score' field")
        print(f"   3. Verify your API accepts POST requests with candidate data")
        print(f"   4. Check network connectivity and API authentication")
        
        return None


if __name__ == "__main__":
    results = main()