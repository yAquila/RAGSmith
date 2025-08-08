#!/usr/bin/env python3
"""
RAG Pipeline Genetic Algorithm Optimization

This script runs genetic algorithm optimization to find the best RAG pipeline
configuration by communicating with the RAG evaluation API.
"""

import time
import logging
from typing import Dict, Any

from genetic_algorithm import GeneticAlgorithm
from config import GAConfig
from rag_evaluator import RAGPipelineEvaluator
from selection import TournamentSelection, RouletteWheelSelection, RankSelection
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
    Create and configure the RAG pipeline evaluator with real API endpoint.
    
    Args:
        api_endpoint: URL of the RAG evaluation API
        
    Returns:
        Configured RAGPipelineEvaluator instance
    """
    # Create evaluator with real API endpoint
    evaluator = RAGPipelineEvaluator(
        api_endpoint=api_endpoint,
        timeout=12000,  # 10 minutes timeout for RAG evaluation
        max_retries=3
    )
    
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
        generations=15,               # Fewer generations for initial testing
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
    
    # Create and run genetic algorithm
    start_time = time.time()
    ga = GeneticAlgorithm(config, evaluator.evaluate)
    
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
        
        # Add additional info to results
        results['total_time'] = total_time
        results['api_endpoint'] = api_endpoint
        results['search_space_size'] = eval('*'.join(map(str, category_sizes)))
        results['configuration'] = config_dict if results['best_combination'] else None
        
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
        population_size=50,           # Larger population
        generations=30,               # More generations
        crossover_rate=0.8,
        mutation_rate=0.08,           # Lower mutation rate for convergence
        elitism_count=5,              # Keep more elite individuals
        selection_method=TournamentSelection(tournament_size=4),
        crossover_method=UniformCrossover(probability=0.6),
        mutation_method=AdaptiveMutation(
            base_mutation_rate=0.08,
            min_mutation_rate=0.01,
            max_mutation_rate=0.2
        ),
        convergence_threshold=10,     # More patience for convergence
        target_fitness=0.98,          # Higher target
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
    
    # Create and run genetic algorithm
    start_time = time.time()
    ga = GeneticAlgorithm(config, evaluator.evaluate)
    
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
        
        # Add additional info to results
        results['total_time'] = total_time
        results['api_endpoint'] = api_endpoint
        results['search_space_size'] = eval('*'.join(map(str, category_sizes)))
        results['configuration'] = config_dict if results['best_combination'] else None
        
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