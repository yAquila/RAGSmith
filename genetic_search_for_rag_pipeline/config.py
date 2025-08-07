"""
Configuration module for genetic algorithm.

This module contains the GAConfig class that manages all parameters
and settings for the genetic algorithm.
"""

from typing import List, Optional, Dict, Any
from dataclasses import dataclass, field
from selection import SelectionMethod, TournamentSelection
from crossover import CrossoverMethod, SinglePointCrossover
from mutation import MutationMethod, RandomMutation


@dataclass
class GAConfig:
    """
    Configuration class for genetic algorithm parameters.
    
    This class encapsulates all the parameters needed to configure and run
    a genetic algorithm, including population settings, genetic operators,
    and termination criteria.
    
    Attributes:
        category_sizes: Number of boxes available in each category
        population_size: Number of individuals in the population
        generations: Maximum number of generations to run
        crossover_rate: Probability of crossover between selected parents
        mutation_rate: Probability of mutation for each gene
        elitism_count: Number of best individuals to preserve each generation
        selection_method: Method for selecting parents for reproduction
        crossover_method: Method for creating offspring from parents
        mutation_method: Method for introducing random variations
        random_seed: Seed for random number generation (for reproducibility)
        verbose: Whether to print progress information
        convergence_threshold: Stop if best fitness doesn't improve for this many generations
        target_fitness: Stop if this fitness is reached
    """
    
    # Problem-specific parameters
    category_sizes: List[int] = field(default_factory=lambda: [3, 5, 4, 6, 2, 7, 3, 5, 4, 6])
    
    # Population parameters
    population_size: int = 50
    generations: int = 100
    
    # Genetic operator probabilities
    crossover_rate: float = 0.8
    mutation_rate: float = 0.1
    elitism_count: int = 2
    
    # Genetic operators (will be set to defaults if None)
    selection_method: Optional[SelectionMethod] = None
    crossover_method: Optional[CrossoverMethod] = None
    mutation_method: Optional[MutationMethod] = None
    
    # Runtime parameters
    random_seed: Optional[int] = None
    verbose: bool = True
    
    # Termination criteria
    convergence_threshold: int = 20  # Stop if no improvement for 20 generations
    target_fitness: Optional[float] = None  # Stop if this fitness is reached
    
    # Tracking and statistics
    track_statistics: bool = True
    statistics_interval: int = 1  # Record statistics every N generations
    
    def __post_init__(self):
        """Initialize default genetic operators if not provided."""
        self._validate_parameters()
        
        if self.selection_method is None:
            self.selection_method = TournamentSelection(tournament_size=3)
        
        if self.crossover_method is None:
            self.crossover_method = SinglePointCrossover()
        
        if self.mutation_method is None:
            self.mutation_method = RandomMutation(mutation_rate=self.mutation_rate)
    
    def _validate_parameters(self) -> None:
        """
        Validate configuration parameters.
        
        Raises:
            ValueError: If any parameter is invalid
        """
        # Validate category sizes
        if not self.category_sizes:
            raise ValueError("At least one category must be specified")
        
        if any(size < 1 for size in self.category_sizes):
            raise ValueError("All category sizes must be at least 1")
        
        # Validate population parameters
        if self.population_size < 2:
            raise ValueError("Population size must be at least 2")
        
        if self.generations < 1:
            raise ValueError("Number of generations must be at least 1")
        
        # Validate probabilities
        if not (0.0 <= self.crossover_rate <= 1.0):
            raise ValueError("Crossover rate must be between 0.0 and 1.0")
        
        if not (0.0 <= self.mutation_rate <= 1.0):
            raise ValueError("Mutation rate must be between 0.0 and 1.0")
        
        # Validate elitism
        if self.elitism_count < 0:
            raise ValueError("Elitism count cannot be negative")
        
        if self.elitism_count >= self.population_size:
            raise ValueError("Elitism count must be less than population size")
        
        # Validate termination criteria
        if self.convergence_threshold < 1:
            raise ValueError("Convergence threshold must be at least 1")
        
        if self.target_fitness is not None and self.target_fitness < 0:
            raise ValueError("Target fitness cannot be negative")
        
        # Validate statistics parameters
        if self.statistics_interval < 1:
            raise ValueError("Statistics interval must be at least 1")
    
    def get_num_categories(self) -> int:
        """Get the number of categories."""
        return len(self.category_sizes)
    
    def get_total_combinations(self) -> int:
        """Get the total number of possible combinations."""
        total = 1
        for size in self.category_sizes:
            total *= size
        return total
    
    def update_mutation_rate(self, new_rate: float) -> None:
        """
        Update the mutation rate and update the mutation method if it's RandomMutation.
        
        Args:
            new_rate: New mutation rate (0.0 to 1.0)
        """
        if not (0.0 <= new_rate <= 1.0):
            raise ValueError("Mutation rate must be between 0.0 and 1.0")
        
        self.mutation_rate = new_rate
        
        # Update mutation method if it's RandomMutation
        from mutation import RandomMutation
        if isinstance(self.mutation_method, RandomMutation):
            self.mutation_method.mutation_rate = new_rate
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert configuration to dictionary.
        
        Returns:
            Dictionary representation of the configuration
        """
        return {
            'category_sizes': self.category_sizes,
            'population_size': self.population_size,
            'generations': self.generations,
            'crossover_rate': self.crossover_rate,
            'mutation_rate': self.mutation_rate,
            'elitism_count': self.elitism_count,
            'selection_method': str(self.selection_method),
            'crossover_method': str(self.crossover_method),
            'mutation_method': str(self.mutation_method),
            'random_seed': self.random_seed,
            'verbose': self.verbose,
            'convergence_threshold': self.convergence_threshold,
            'target_fitness': self.target_fitness,
            'track_statistics': self.track_statistics,
            'statistics_interval': self.statistics_interval,
            'num_categories': self.get_num_categories(),
            'total_combinations': self.get_total_combinations()
        }
    
    @classmethod
    def create_default(cls) -> 'GAConfig':
        """
        Create a configuration with default parameters.
        
        Returns:
            GAConfig instance with default settings
        """
        return cls()
    
    @classmethod
    def create_small_test(cls) -> 'GAConfig':
        """
        Create a configuration suitable for small-scale testing.
        
        Returns:
            GAConfig instance with small-scale parameters
        """
        return cls(
            category_sizes=[2, 3, 2, 3],
            population_size=10,
            generations=20,
            convergence_threshold=10
        )
    
    @classmethod
    def create_large_scale(cls) -> 'GAConfig':
        """
        Create a configuration suitable for large-scale optimization.
        
        Returns:
            GAConfig instance with large-scale parameters
        """
        return cls(
            category_sizes=[10, 15, 8, 12, 6, 20, 10, 15, 8, 12],
            population_size=200,
            generations=500,
            crossover_rate=0.9,
            mutation_rate=0.05,
            elitism_count=10,
            convergence_threshold=50
        )
    
    @classmethod
    def create_high_diversity(cls) -> 'GAConfig':
        """
        Create a configuration that promotes high diversity.
        
        Returns:
            GAConfig instance with high diversity parameters
        """
        from selection import RouletteWheelSelection
        from crossover import UniformCrossover
        from mutation import AdaptiveMutation
        
        return cls(
            population_size=100,
            generations=200,
            crossover_rate=0.7,
            mutation_rate=0.2,
            elitism_count=1,
            selection_method=RouletteWheelSelection(),
            crossover_method=UniformCrossover(probability=0.5),
            mutation_method=AdaptiveMutation(base_mutation_rate=0.2),
            convergence_threshold=30
        )
    
    def __str__(self) -> str:
        """String representation of the configuration."""
        return (f"GAConfig(pop_size={self.population_size}, "
                f"generations={self.generations}, "
                f"categories={len(self.category_sizes)}, "
                f"crossover_rate={self.crossover_rate}, "
                f"mutation_rate={self.mutation_rate})")
    
    def __repr__(self) -> str:
        """Detailed string representation of the configuration."""
        return self.__str__() 