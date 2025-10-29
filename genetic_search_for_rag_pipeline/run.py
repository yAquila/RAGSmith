#!/usr/bin/env python3
"""
RAG Pipeline Genetic Algorithm Optimization

This script runs genetic algorithm optimization to find the best RAG pipeline
configuration by communicating with the RAG evaluation API.
"""

import time
import logging
import os
from datetime import datetime
from typing import Dict, Any

from genetic_algorithm import GeneticAlgorithm
from config import GAConfig
from rag_evaluator import RAGPipelineEvaluator
from selection import TournamentSelection, RouletteWheelSelection, RankSelection, EliteSelection
from crossover import UniformCrossover, SinglePointCrossover, MultiPointCrossover
from mutation import AdaptiveMutation, RandomMutation, CategoricalMutation

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def create_rag_evaluator(api_endpoint: str = "http://rag_pipeline:8060/api/evaluate") -> RAGPipelineEvaluator:
    """
    Create and configure the RAG pipeline evaluator with real API endpoint and persistent caching.
    
    Args:
        api_endpoint: URL of the RAG evaluation API
        
    Returns:
        Configured RAGPipelineEvaluator instance with persistent cache
    """
    # Get cache file path from environment or use default
    cache_file_path = os.environ.get("CACHE_FILE_PATH", "/app/results/rag_evaluation_cache.json")
    
    # Create evaluator with real API endpoint and persistent caching enabled
    evaluator = RAGPipelineEvaluator(
        api_endpoint=api_endpoint,
        timeout=12000,  # 12 seconds timeout for RAG evaluation
        max_retries=5,   # Increased retries for robustness
        enable_cache=True,  # Enable caching for efficiency
        cache_file_path=cache_file_path,  # Persistent cache file
        auto_save_cache=True  # Auto-save cache after each evaluation
    )
    
    logger.info(f"🔧 RAG Evaluator configured with persistent cache: {cache_file_path}")
    
    return evaluator


def calculate_category_sizes(evaluator: RAGPipelineEvaluator) -> list:
    """Calculate category sizes for genetic algorithm configuration."""
    category_sizes = []
    for i in range(len(evaluator.component_categories)):
        category_name = evaluator.component_categories[i]
        options = evaluator.component_options[category_name]
        category_sizes.append(len(options))
    
    logger.info(f"Category sizes: {category_sizes}")
    logger.info(f"Total search space: {eval('*'.join(map(str, category_sizes)))} combinations")
    
    return category_sizes


def save_results_to_markdown(results: Dict[str, Any], evaluator: RAGPipelineEvaluator, 
                           run_type: str = "optimization", output_dir: str = None) -> str:
    """
    Save genetic algorithm results to a markdown file.
    
    Args:
        results: GA results dictionary
        evaluator: RAGPipelineEvaluator instance with cache statistics
        run_type: Type of run (basic, comprehensive, test)
        output_dir: Directory to save the results (defaults to /app/results or GA_RESULTS_DIR env var)
        
    Returns:
        Path to the saved markdown file
    """
    # Use environment variable or default directory
    if output_dir is None:
        output_dir = os.getenv('GA_RESULTS_DIR', '/app/results')
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"genetic_search_result_{timestamp}.md"
    filepath = os.path.join(output_dir, filename)
    
    # Get cache statistics
    cache_stats = evaluator.get_cache_statistics()
    
    # Generate markdown content
    markdown_content = f"""# RAG Genetic Algorithm Optimization Results

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  
**Run Type:** {run_type.title()}  
**API Endpoint:** {results.get('api_endpoint', 'N/A')}  
**Cache File:** {evaluator.cache_file_path}

## 🎯 Optimization Summary

| Metric | Value |
|--------|-------|
| **Best Fitness** | {results.get('best_fitness', 'N/A'):.4f} |
| **Generations Completed** | {results.get('generations_completed', 'N/A')} |
| **Converged** | {'✅ Yes' if results.get('converged', False) else '❌ No'} |
| **Total Time** | {results.get('total_time', 'N/A'):.2f} seconds ({results.get('total_time', 0)/60:.1f} minutes) |
| **Search Space Size** | {results.get('search_space_size', 'N/A'):,} combinations |

## 📋 Best RAG Configuration

"""
    
    # Add best configuration if available
    if results.get('configuration'):
        markdown_content += "| Component Category | Selected Option |\n"
        markdown_content += "|-------------------|----------------|\n"
        
        for category, selection in results['configuration'].items():
            markdown_content += f"| **{category.replace('-', ' ').title()}** | `{selection}` |\n"
    else:
        markdown_content += "*No best configuration found.*\n"
    
    # Add cache performance statistics
    markdown_content += f"""

## 🚀 Cache Performance Statistics

| Metric | Value |
|--------|-------|
| **Total Evaluations** | {cache_stats['total_evaluations']:,} |
| **Cache Hits** | {cache_stats['cache_hits']:,} |
| **Cache Misses** | {cache_stats['cache_misses']:,} |
| **API Calls Made** | {cache_stats['api_calls']:,} |
| **Cache Hit Rate** | {cache_stats['hit_rate_percent']:.1f}% |
| **Efficiency Gain** | {cache_stats['efficiency_percent']:.1f}% |
| **Unique Configurations** | {cache_stats['cache_size']:,} |

### Cache Performance Analysis

"""
    
    if cache_stats['hit_rate_percent'] >= 50:
        markdown_content += "🟢 **Excellent Cache Performance** - High hit rate indicates effective optimization with many similar configurations being explored.\n\n"
    elif cache_stats['hit_rate_percent'] >= 30:
        markdown_content += "🟡 **Good Cache Performance** - Moderate hit rate shows reasonable configuration reuse.\n\n"
    else:
        markdown_content += "🔴 **Low Cache Performance** - Low hit rate suggests high diversity in explored configurations.\n\n"
    
    # Add time savings calculation
    if cache_stats['api_calls'] > 0:
        avg_api_time = 2.0  # Assume 2 seconds per API call
        time_saved = (cache_stats['cache_hits'] * avg_api_time) / 60  # Convert to minutes
        markdown_content += f"**Estimated Time Saved:** ~{time_saved:.1f} minutes (based on {avg_api_time}s per API call)\n\n"
    
    # Add evolution statistics if available
    if 'evolution_stats' in results:
        markdown_content += f"""## 📊 Evolution Statistics

| Generation | Best Fitness | Average Fitness | Improvement |
|------------|-------------|----------------|-------------|
"""
        
        for i, stat in enumerate(results['evolution_stats'][-10:]):  # Last 10 generations
            improvement = "📈" if i > 0 and stat['best_fitness'] > results['evolution_stats'][i-1]['best_fitness'] else "➡️"
            markdown_content += f"| {stat.get('generation', i)} | {stat.get('best_fitness', 0):.4f} | {stat.get('average_fitness', 0):.4f} | {improvement} |\n"
    
    # Add genetic algorithm configuration
    markdown_content += f"""

## ⚙️ Genetic Algorithm Configuration

"""
    
    if 'ga_config' in results:
        config = results['ga_config']
        markdown_content += f"""| Parameter | Value |
|-----------|--------|
| **Population Size** | {config.get('population_size', 'N/A')} |
| **Generations** | {config.get('generations', 'N/A')} |
| **Crossover Rate** | {config.get('crossover_rate', 'N/A')} |
| **Mutation Rate** | {config.get('mutation_rate', 'N/A')} |
| **Elitism Count** | {config.get('elitism_count', 'N/A')} |
| **Selection Method** | {config.get('selection_method', 'N/A')} |
| **Crossover Method** | {config.get('crossover_method', 'N/A')} |
| **Mutation Method** | {config.get('mutation_method', 'N/A')} |

"""
    
    # Add component options summary
    markdown_content += f"""## 🧩 Available Component Options

This optimization explored the following RAG pipeline components:

"""
    
    if hasattr(evaluator, 'component_options'):
        for category, options in evaluator.component_options.items():
            markdown_content += f"### {category.replace('-', ' ').title()}\n"
            for i, option in enumerate(options):
                selected = "✅" if results.get('configuration', {}).get(category) == option else "⬜"
                markdown_content += f"{selected} `{option}`\n"
            markdown_content += "\n"
    
    # Add footer
    markdown_content += f"""---

**Generated by RAG Genetic Algorithm Optimization**  
*Total search space: {results.get('search_space_size', 'N/A'):,} possible combinations*  
*Optimization completed in {results.get('total_time', 0):.2f} seconds*

"""
    
    # Write to file
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        logger.info(f"📝 Results saved to: {filepath}")
        logger.info(f"💾 Cache automatically persisted to: {evaluator.cache_file_path}")
        
        return filepath
        
    except Exception as e:
        logger.error(f"❌ Failed to save results to {filepath}: {e}")
        return ""


def run_rag_optimization_basic(api_endpoint: str = "http://rag_pipeline:8060/api/evaluate") -> Dict[str, Any]:
    """
    Run basic RAG pipeline optimization using genetic algorithm.
    
    Args:
        api_endpoint: URL of the RAG evaluation API
        
    Returns:
        Optimization results
    """
    logger.info("🚀 Starting RAG Pipeline Optimization with Genetic Algorithm")
    logger.info("=" * 70)
    
    # Create RAG evaluator
    evaluator = create_rag_evaluator(api_endpoint)
    category_sizes = calculate_category_sizes(evaluator)
    
    # Configure genetic algorithm
    config = GAConfig(
        category_sizes=category_sizes,
        population_size=20,           # Smaller population for faster testing
        generations=3,               # Fewer generations for initial testing
        crossover_rate=0.8,
        mutation_rate=0.1,
        elitism_count=3,
        selection_method=TournamentSelection(tournament_size=3),
        crossover_method=UniformCrossover(probability=0.6),
        mutation_method=AdaptiveMutation(base_mutation_rate=0.1),
        convergence_threshold=5,      # Stop if no improvement for 5 generations
        target_fitness=0.95,          # Stop if we reach 95% fitness
        verbose=True,
        track_statistics=True,
        random_seed=42
    )
    
    logger.info(f"Configuration:")
    logger.info(f"  Population size: {config.population_size}")
    logger.info(f"  Generations: {config.generations}")
    logger.info(f"  Crossover rate: {config.crossover_rate}")
    logger.info(f"  Mutation rate: {config.mutation_rate}")
    logger.info(f"  API endpoint: {api_endpoint}")
    logger.info("")
    
    # Create genetic algorithm
    start_time = time.time()
    ga = GeneticAlgorithm(config, evaluator.evaluate)
    
    # Initialize GA with knowledge from cache (if available)
    best_cached_candidate, best_cached_score = evaluator.get_best_from_cache()
    if best_cached_candidate is not None:
        logger.info(f"🔄 Initializing GA with cached best: {best_cached_candidate} (score: {best_cached_score:.4f})")
        from individual import Individual
        cached_best = Individual(category_sizes, best_cached_candidate)
        cached_best.fitness = best_cached_score
        ga.best_ever_individual = cached_best
    
    try:
        results = ga.run()
        
        # Calculate total time
        total_time = time.time() - start_time
        
        # Print results
        logger.info("🎉 Optimization completed!")
        logger.info("=" * 50)
        logger.info(f"Best fitness: {results['best_fitness']:.4f}")
        logger.info(f"Best combination: {results['best_combination']}")
        logger.info(f"Generations completed: {results['generations_completed']}")
        logger.info(f"Converged: {results['converged']}")
        logger.info(f"Total time: {total_time:.2f} seconds")
        
        # Decode best combination to readable format
        if results['best_combination']:
            logger.info("\n📋 Best RAG Configuration:")
            logger.info("-" * 40)
            config_dict = evaluator.candidate_to_configuration(results['best_combination'])
            for category, selection in config_dict.items():
                logger.info(f"  {category}: {selection}")
        
        # Print cache performance statistics
        cache_stats = evaluator.get_cache_statistics()
        logger.info("\n🚀 Cache Performance Statistics:")
        logger.info("=" * 40)
        logger.info(f"  Total evaluations: {cache_stats['total_evaluations']}")
        logger.info(f"  Cache hits: {cache_stats['cache_hits']}")
        logger.info(f"  Cache misses: {cache_stats['cache_misses']}")
        logger.info(f"  API calls made: {cache_stats['api_calls']}")
        logger.info(f"  Cache hit rate: {cache_stats['hit_rate_percent']:.1f}%")
        logger.info(f"  Efficiency gain: {cache_stats['efficiency_percent']:.1f}%")
        logger.info(f"  Cache size: {cache_stats['cache_size']} unique configurations")
        
        # Add additional info to results
        results['total_time'] = total_time
        results['api_endpoint'] = api_endpoint
        results['search_space_size'] = eval('*'.join(map(str, category_sizes)))
        results['configuration'] = config_dict if results['best_combination'] else None
        results['ga_config'] = {
            'population_size': config.population_size,
            'generations': config.generations,
            'crossover_rate': config.crossover_rate,
            'mutation_rate': config.mutation_rate,
            'elitism_count': config.elitism_count,
            'selection_method': type(config.selection_method).__name__,
            'crossover_method': type(config.crossover_method).__name__,
            'mutation_method': type(config.mutation_method).__name__
        }
        
        # Save results to markdown file
        save_results_to_markdown(results, evaluator, "basic")
        
        return results
        
    except Exception as e:
        logger.error(f"❌ Optimization failed: {e}")
        import traceback
        logger.error(traceback.format_exc())
        raise


def run_rag_optimization_comprehensive(api_endpoint: str = "http://rag_pipeline:8060/api/evaluate") -> Dict[str, Any]:
    """
    Run comprehensive RAG pipeline optimization with larger population and more generations.
    
    Args:
        api_endpoint: URL of the RAG evaluation API
        
    Returns:
        Optimization results
    """
    logger.info("🚀 Starting COMPREHENSIVE RAG Pipeline Optimization")
    logger.info("=" * 70)
    
    # Create RAG evaluator
    evaluator = create_rag_evaluator(api_endpoint)
    category_sizes = calculate_category_sizes(evaluator)
    
    # Configure genetic algorithm for comprehensive search
    config = GAConfig(
        category_sizes=category_sizes,
        population_size=16,           # Larger population
        generations=20,               # More generations
        crossover_rate=0.8,
        mutation_rate=0.08,           # Lower mutation rate for convergence
        elitism_count=5,              # Keep more elite individuals
        # selection_method=TournamentSelection(tournament_size=4),
        selection_method=EliteSelection(),
        crossover_method=UniformCrossover(probability=0.6),
        mutation_method=AdaptiveMutation(
            base_mutation_rate=0.08,
            min_mutation_rate=0.01,
            max_mutation_rate=0.2
        ),
        convergence_threshold=100,     # More patience for convergence
        target_fitness=1.0,          # Higher target
        verbose=True,
        track_statistics=True,
        random_seed=42
    )
    
    logger.info(f"Configuration:")
    logger.info(f"  Population size: {config.population_size}")
    logger.info(f"  Generations: {config.generations}")
    logger.info(f"  Expected evaluations: ~{config.population_size * config.generations}")
    logger.info(f"  Estimated time: ~{config.population_size * config.generations * 2 / 60:.1f} minutes")
    logger.info(f"  API endpoint: {api_endpoint}")
    logger.info("")
    
    # Create genetic algorithm
    start_time = time.time()
    ga = GeneticAlgorithm(config, evaluator.evaluate)
    
    # Initialize GA with knowledge from cache (if available)
    best_cached_candidate, best_cached_score = evaluator.get_best_from_cache()
    if best_cached_candidate is not None:
        logger.info(f"🔄 Initializing GA with cached best: {best_cached_candidate} (score: {best_cached_score:.4f})")
        from individual import Individual
        cached_best = Individual(category_sizes, best_cached_candidate)
        cached_best.fitness = best_cached_score
        ga.best_ever_individual = cached_best
    
    try:
        results = ga.run()
        
        # Calculate total time
        total_time = time.time() - start_time
        
        # Print detailed results
        logger.info("🎉 COMPREHENSIVE Optimization completed!")
        logger.info("=" * 60)
        logger.info(f"Best fitness: {results['best_fitness']:.4f}")
        logger.info(f"Best combination: {results['best_combination']}")
        logger.info(f"Generations completed: {results['generations_completed']}")
        logger.info(f"Converged: {results['converged']}")
        logger.info(f"Total time: {total_time:.2f} seconds ({total_time/60:.1f} minutes)")
        logger.info(f"Evaluations performed: {results.get('total_evaluations', 'N/A')}")
        
        # Decode best combination to readable format
        if results['best_combination']:
            logger.info("\n📋 BEST RAG Configuration Found:")
            logger.info("=" * 50)
            config_dict = evaluator.candidate_to_configuration(results['best_combination'])
            for category, selection in config_dict.items():
                logger.info(f"  {category:20}: {selection}")
        
        # Statistics if available
        if hasattr(ga, 'statistics') and ga.statistics:
            logger.info(f"\n📊 Evolution Statistics:")
            logger.info(f"  Generations tracked: {len(ga.statistics)}")
            best_scores = [stat.best_fitness for stat in ga.statistics]
            logger.info(f"  Best score progression: {' → '.join([f'{s:.3f}' for s in best_scores[-5:]])}")
        
        # Print cache performance statistics
        cache_stats = evaluator.get_cache_statistics()
        logger.info("\n🚀 Cache Performance Statistics:")
        logger.info("=" * 40)
        logger.info(f"  Total evaluations: {cache_stats['total_evaluations']}")
        logger.info(f"  Cache hits: {cache_stats['cache_hits']}")
        logger.info(f"  Cache misses: {cache_stats['cache_misses']}")
        logger.info(f"  API calls made: {cache_stats['api_calls']}")
        logger.info(f"  Cache hit rate: {cache_stats['hit_rate_percent']:.1f}%")
        logger.info(f"  Efficiency gain: {cache_stats['efficiency_percent']:.1f}%")
        logger.info(f"  Cache size: {cache_stats['cache_size']} unique configurations")
        
        # Add additional info to results
        results['total_time'] = total_time
        results['api_endpoint'] = api_endpoint
        results['search_space_size'] = eval('*'.join(map(str, category_sizes)))
        results['configuration'] = config_dict if results['best_combination'] else None
        results['ga_config'] = {
            'population_size': config.population_size,
            'generations': config.generations,
            'crossover_rate': config.crossover_rate,
            'mutation_rate': config.mutation_rate,
            'elitism_count': config.elitism_count,
            'selection_method': type(config.selection_method).__name__,
            'crossover_method': type(config.crossover_method).__name__,
            'mutation_method': type(config.mutation_method).__name__
        }
        
        # Add evolution statistics if available
        if hasattr(ga, 'statistics') and ga.statistics:
            results['evolution_stats'] = [
                {
                    'generation': i * config.statistics_interval,
                    'best_fitness': stat.best_fitness,
                    'average_fitness': stat.average_fitness,
                    'execution_time': stat.execution_time
                }
                for i, stat in enumerate(ga.statistics)
            ]
        
        # Save results to markdown file
        save_results_to_markdown(results, evaluator, "comprehensive")
        
        return results
        
    except Exception as e:
        logger.error(f"❌ Comprehensive optimization failed: {e}")
        import traceback
        logger.error(traceback.format_exc())
        raise


def main():
    """Main entry point for RAG optimization."""
    import sys
    
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        
        # API endpoint (can be overridden)
        api_endpoint = "http://rag_pipeline:8060/api/evaluate"
        if len(sys.argv) > 2:
            api_endpoint = sys.argv[2]
        
        if arg == "--basic":
            logger.info("Running BASIC RAG optimization...")
            results = run_rag_optimization_basic(api_endpoint)
            
        elif arg == "--comprehensive":
            logger.info("Running COMPREHENSIVE RAG optimization...")
            results = run_rag_optimization_comprehensive(api_endpoint)
            
        elif arg == "--test":
            # Quick test to verify API connectivity
            logger.info("Testing API connectivity...")
            evaluator = create_rag_evaluator(api_endpoint)
            test_candidate = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]  # Simple test configuration
            
            try:
                score = evaluator.evaluate(test_candidate)
                logger.info(f"✅ API test successful! Score: {score:.4f}")
                
                # Test cache functionality by evaluating the same candidate again
                score2 = evaluator.evaluate(test_candidate)
                cache_stats = evaluator.get_cache_statistics()
                logger.info(f"✅ Cache test: Second evaluation returned {score2:.4f}")
                logger.info(f"📊 Cache hit rate: {cache_stats['hit_rate_percent']:.1f}% ({cache_stats['cache_hits']}/{cache_stats['total_evaluations']})")
                
                logger.info("You can now run --basic or --comprehensive optimization.")
            except Exception as e:
                logger.error(f"❌ API test failed: {e}")
                logger.error("Make sure the RAG pipeline server is running:")
                logger.error("  python main.py --server")
                
        else:
            print("Usage:")
            print("  python run.py --test [api_endpoint]         # Test API connectivity")
            print("  python run.py --basic [api_endpoint]        # Basic optimization (fast)")
            print("  python run.py --comprehensive [api_endpoint] # Comprehensive optimization (slow)")
            print("")
            print("Default API endpoint: http://rag_pipeline:8060/api/evaluate")
            print("")
            print("Examples:")
            print("  python run.py --test")
            print("  python run.py --basic")
            print("  python run.py --comprehensive")
            print("  python run.py --basic http://rag_pipeline:8060/api/evaluate")
    else:
        print("🧬 RAG Pipeline Genetic Algorithm Optimization")
        print("=" * 50)
        print("Usage:")
        print("  python run.py --test [api_endpoint]         # Test API connectivity")
        print("  python run.py --basic [api_endpoint]        # Basic optimization (fast)")
        print("  python run.py --comprehensive [api_endpoint] # Comprehensive optimization (slow)")
        print("")
        print("Default API endpoint: http://rag_pipeline:8060/api/evaluate")
        print("")
        print("Make sure the RAG pipeline server is running:")
        print("  python main.py --server")


if __name__ == "__main__":
    main() 