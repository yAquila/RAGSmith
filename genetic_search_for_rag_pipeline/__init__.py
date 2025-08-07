"""
Genetic Algorithm for Component Combination Search

A modular genetic algorithm system for finding optimal
combinations of components from different categories. Designed for problems
like RAG pipeline optimization where you need to select one component from
each of several categories to maximize overall performance.

Key Features:
- Modular design with pluggable selection, crossover, and mutation methods
- Comprehensive configuration system with sensible defaults
- Professional code structure with extensive documentation
- Ready-to-run examples and demonstrations
- Extensive statistics tracking and analysis capabilities

Basic Usage:
    from genetic_search_for_rag_pipeline import GeneticAlgorithm, GAConfig
    
    def evaluate(candidate):
        # Your evaluation logic here
        return fitness_score  # 0-100
    
    config = GAConfig.create_default()
    ga = GeneticAlgorithm(config, evaluate)
    results = ga.run()
    
    best_combination = results['best_combination']
    best_fitness = results['best_fitness']

Advanced Usage:
    from genetic_search_for_rag_pipeline import (
        GeneticAlgorithm, GAConfig,
        TournamentSelection, UniformCrossover, AdaptiveMutation
    )
    
    config = GAConfig(
        category_sizes=[5, 8, 6, 10],
        population_size=100,
        generations=200,
        selection_method=TournamentSelection(tournament_size=5),
        crossover_method=UniformCrossover(probability=0.6),
        mutation_method=AdaptiveMutation(base_mutation_rate=0.12)
    )
    
    ga = GeneticAlgorithm(config, your_evaluate_function)
    results = ga.run()
"""

# Core classes
from .genetic_algorithm import GeneticAlgorithm, GenerationStatistics
from .config import GAConfig
from .individual import Individual
from .population import Population

# Selection methods
from .selection import (
    SelectionMethod,
    TournamentSelection,
    RouletteWheelSelection,
    RankSelection,
    EliteSelection
)

# Crossover methods
from .crossover import (
    CrossoverMethod,
    SinglePointCrossover,
    MultiPointCrossover,
    UniformCrossover,
    OrderCrossover,
    SegmentCrossover
)

# Mutation methods
from .mutation import (
    MutationMethod,
    RandomMutation,
    AdaptiveMutation,
    CategoricalMutation,
    SwapMutation,
    InversionMutation,
    CompositeMutation
)

# Version information
__version__ = "1.0.0"
__author__ = "Generated for Component Combination Search"
__description__ = "Modular genetic algorithm system for component combination optimization"

# Package metadata
__all__ = [
    # Core classes
    "GeneticAlgorithm",
    "GenerationStatistics", 
    "GAConfig",
    "Individual",
    "Population",
    
    # Selection methods
    "SelectionMethod",
    "TournamentSelection",
    "RouletteWheelSelection", 
    "RankSelection",
    "EliteSelection",
    
    # Crossover methods
    "CrossoverMethod",
    "SinglePointCrossover",
    "MultiPointCrossover",
    "UniformCrossover",
    "OrderCrossover",
    "SegmentCrossover",
    
    # Mutation methods
    "MutationMethod",
    "RandomMutation",
    "AdaptiveMutation",
    "CategoricalMutation",
    "SwapMutation",
    "InversionMutation",
    "CompositeMutation"
]

# Convenience functions for quick setup
def create_basic_ga(category_sizes, evaluate_func, **kwargs):
    """
    Create a basic genetic algorithm with default settings.
    
    Args:
        category_sizes: List of integers specifying boxes per category
        evaluate_func: Function that evaluates candidates and returns fitness
        **kwargs: Additional configuration parameters
        
    Returns:
        Configured GeneticAlgorithm instance
    """
    config = GAConfig(category_sizes=category_sizes, **kwargs)
    return GeneticAlgorithm(config, evaluate_func)


def create_high_performance_ga(category_sizes, evaluate_func, **kwargs):
    """
    Create a high-performance genetic algorithm configuration.
    
    Args:
        category_sizes: List of integers specifying boxes per category
        evaluate_func: Function that evaluates candidates and returns fitness
        **kwargs: Additional configuration parameters
        
    Returns:
        Configured GeneticAlgorithm instance with performance-oriented settings
    """
    default_config = {
        'population_size': 200,
        'generations': 500,
        'crossover_rate': 0.9,
        'mutation_rate': 0.05,
        'elitism_count': 10,
        'convergence_threshold': 50,
        'selection_method': TournamentSelection(tournament_size=5),
        'crossover_method': UniformCrossover(probability=0.6),
        'mutation_method': AdaptiveMutation()
    }
    default_config.update(kwargs)
    
    config = GAConfig(category_sizes=category_sizes, **default_config)
    return GeneticAlgorithm(config, evaluate_func)


def create_exploratory_ga(category_sizes, evaluate_func, **kwargs):
    """
    Create an exploratory genetic algorithm that emphasizes diversity.
    
    Args:
        category_sizes: List of integers specifying boxes per category
        evaluate_func: Function that evaluates candidates and returns fitness
        **kwargs: Additional configuration parameters
        
    Returns:
        Configured GeneticAlgorithm instance with exploration-oriented settings
    """
    default_config = {
        'population_size': 100,
        'generations': 300,
        'crossover_rate': 0.7,
        'mutation_rate': 0.2,
        'elitism_count': 1,
        'selection_method': RouletteWheelSelection(),
        'crossover_method': UniformCrossover(probability=0.5),
        'mutation_method': AdaptiveMutation(base_mutation_rate=0.2)
    }
    default_config.update(kwargs)
    
    config = GAConfig(category_sizes=category_sizes, **default_config)
    return GeneticAlgorithm(config, evaluate_func)


# Package information for help
def get_package_info():
    """Return package information."""
    return {
        'name': 'genetic_search_for_rag_pipeline',
        'version': __version__,
        'description': __description__,
        'author': __author__,
        'classes': len(__all__),
        'features': [
            'Modular genetic operators',
            'Comprehensive configuration system',
            'Statistics tracking and analysis',
            'Multiple termination criteria',
            'Professional documentation',
            'Ready-to-run examples'
        ]
    } 