"""
Population module for genetic algorithm.

This module contains the Population class that manages a group of individuals
and provides methods for population-level operations.
"""

import random
from typing import List, Callable, Optional
from individual import Individual


class Population:
    """
    Represents a population of individuals in the genetic algorithm.
    
    The population manages a collection of individuals and provides methods
    for initialization, evaluation, and accessing population statistics.
    
    Attributes:
        individuals (List[Individual]): List of individuals in the population
        category_sizes (List[int]): Number of boxes available in each category
        size (int): Number of individuals in the population
    """
    
    def __init__(self, size: int, category_sizes: List[int]):
        """
        Initialize a population with random individuals.
        
        Args:
            size: Number of individuals in the population
            category_sizes: List containing the number of boxes in each category
        """
        self.size = size
        self.category_sizes = category_sizes
        self.individuals: List[Individual] = []
        
        # Generate random individuals
        for _ in range(size):
            individual = Individual(category_sizes)
            self.individuals.append(individual)
    
    def evaluate_all(self, evaluate_func: Callable) -> None:
        """
        Evaluate all individuals in the population using the provided function.
        
        Args:
            evaluate_func: Function that takes a candidate and returns a fitness score
        """
        for individual in self.individuals:
            individual.evaluate(evaluate_func)
    
    def get_best_individual(self) -> Optional[Individual]:
        """
        Get the individual with the highest fitness score.
        
        Returns:
            Individual with highest fitness, or None if population is empty
        """
        if not self.individuals:
            return None
        
        evaluated_individuals = [ind for ind in self.individuals if ind.fitness is not None]
        if not evaluated_individuals:
            return None
        
        return max(evaluated_individuals, key=lambda x: x.fitness)
    
    def get_worst_individual(self) -> Optional[Individual]:
        """
        Get the individual with the lowest fitness score.
        
        Returns:
            Individual with lowest fitness, or None if population is empty
        """
        if not self.individuals:
            return None
        
        evaluated_individuals = [ind for ind in self.individuals if ind.fitness is not None]
        if not evaluated_individuals:
            return None
        
        return min(evaluated_individuals, key=lambda x: x.fitness)
    
    def get_average_fitness(self) -> Optional[float]:
        """
        Calculate the average fitness of the population.
        
        Returns:
            Average fitness score, or None if no individuals are evaluated
        """
        evaluated_individuals = [ind for ind in self.individuals if ind.fitness is not None]
        if not evaluated_individuals:
            return None
        
        total_fitness = sum(ind.fitness for ind in evaluated_individuals)
        return total_fitness / len(evaluated_individuals)
    
    def sort_by_fitness(self, descending: bool = True) -> None:
        """
        Sort individuals by fitness score.
        
        Args:
            descending: If True, sort from highest to lowest fitness
        """
        # Filter out individuals without fitness scores
        evaluated_individuals = [ind for ind in self.individuals if ind.fitness is not None]
        unevaluated_individuals = [ind for ind in self.individuals if ind.fitness is None]
        
        # Sort evaluated individuals
        evaluated_individuals.sort(key=lambda x: x.fitness, reverse=descending)
        
        # Combine sorted evaluated individuals with unevaluated ones at the end
        self.individuals = evaluated_individuals + unevaluated_individuals
    
    def get_top_individuals(self, n: int) -> List[Individual]:
        """
        Get the top n individuals by fitness.
        
        Args:
            n: Number of top individuals to return
            
        Returns:
            List of top n individuals
        """
        self.sort_by_fitness(descending=True)
        return self.individuals[:min(n, len(self.individuals))]
    
    def replace_individual(self, index: int, new_individual: Individual) -> None:
        """
        Replace an individual at the specified index.
        
        Args:
            index: Index of individual to replace
            new_individual: New individual to insert
            
        Raises:
            IndexError: If index is out of range
        """
        if not (0 <= index < len(self.individuals)):
            raise IndexError(f"Index {index} is out of range for population of size {len(self.individuals)}")
        
        self.individuals[index] = new_individual
    
    def add_individual(self, individual: Individual) -> None:
        """
        Add a new individual to the population.
        
        Args:
            individual: Individual to add to the population
        """
        self.individuals.append(individual)
    
    def remove_worst_individuals(self, n: int) -> None:
        """
        Remove the n worst individuals from the population.
        
        Args:
            n: Number of worst individuals to remove
        """
        self.sort_by_fitness(descending=True)
        # Keep only the best individuals
        self.individuals = self.individuals[:max(0, len(self.individuals) - n)]
    
    def get_diversity_score(self) -> float:
        """
        Calculate a simple diversity score based on unique gene combinations.
        
        Returns:
            Diversity score between 0.0 and 1.0
        """
        if not self.individuals:
            return 0.0
        
        unique_genomes = set(tuple(ind.genes) for ind in self.individuals)
        return len(unique_genomes) / len(self.individuals)
    
    def get_statistics(self) -> dict:
        """
        Get comprehensive population statistics.
        
        Returns:
            Dictionary containing population statistics
        """
        best = self.get_best_individual()
        worst = self.get_worst_individual()
        avg_fitness = self.get_average_fitness()
        diversity = self.get_diversity_score()
        
        return {
            'size': len(self.individuals),
            'best_fitness': best.fitness if best else None,
            'worst_fitness': worst.fitness if worst else None,
            'average_fitness': avg_fitness,
            'diversity_score': diversity,
            'evaluated_count': len([ind for ind in self.individuals if ind.fitness is not None])
        }
    
    def __len__(self) -> int:
        """Return the number of individuals in the population."""
        return len(self.individuals)
    
    def __iter__(self):
        """Make the population iterable."""
        return iter(self.individuals)
    
    def __getitem__(self, index: int) -> Individual:
        """Allow indexing into the population."""
        return self.individuals[index]
    
    def __str__(self) -> str:
        """String representation of the population."""
        stats = self.get_statistics()
        return (f"Population(size={stats['size']}, "
                f"best_fitness={stats['best_fitness']:.4f if stats['best_fitness'] else 'N/A'}, "
                f"avg_fitness={stats['average_fitness']:.4f if stats['average_fitness'] else 'N/A'})")
    
    def __repr__(self) -> str:
        """Detailed string representation of the population."""
        return self.__str__() 