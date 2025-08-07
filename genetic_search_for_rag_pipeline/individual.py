"""
Individual module for genetic algorithm.

This module contains the Individual class that represents a single solution
in the genetic algorithm for component combination search.
"""

import random
from typing import List, Optional


class Individual:
    """
    Represents a single individual (solution) in the genetic algorithm.
    
    An individual is represented as a list of integers, where each integer
    is the index of the selected box from its corresponding category.
    
    Attributes:
        genes (List[int]): List of selected box indices for each category
        fitness (Optional[float]): Fitness score of this individual (0-100)
        category_sizes (List[int]): Number of boxes available in each category
    """
    
    def __init__(self, category_sizes: List[int], genes: Optional[List[int]] = None):
        """
        Initialize an individual.
        
        Args:
            category_sizes: List containing the number of boxes in each category
            genes: Optional list of gene values. If None, random genes are generated
        """
        self.category_sizes = category_sizes
        self.fitness: Optional[float] = None
        
        if genes is not None:
            self.genes = genes.copy()
            self._validate_genes()
        else:
            self.genes = self._generate_random_genes()
    
    def _generate_random_genes(self) -> List[int]:
        """
        Generate random genes for initialization.
        
        Returns:
            List of random gene values, one for each category
        """
        return [random.randint(0, size - 1) for size in self.category_sizes]
    
    def _validate_genes(self) -> None:
        """
        Validate that genes are within valid ranges for each category.
        
        Raises:
            ValueError: If genes are invalid
        """
        if len(self.genes) != len(self.category_sizes):
            raise ValueError(f"Number of genes ({len(self.genes)}) must match "
                           f"number of categories ({len(self.category_sizes)})")
        
        for i, (gene, size) in enumerate(zip(self.genes, self.category_sizes)):
            if not (0 <= gene < size):
                raise ValueError(f"Gene {i} value {gene} is out of range [0, {size-1}]")
    
    def mutate(self, mutation_rate: float) -> None:
        """
        Apply mutation to this individual.
        
        Args:
            mutation_rate: Probability of mutating each gene (0.0 to 1.0)
        """
        for i in range(len(self.genes)):
            if random.random() < mutation_rate:
                self.genes[i] = random.randint(0, self.category_sizes[i] - 1)
        
        # Reset fitness after mutation
        self.fitness = None
    
    def crossover(self, other: 'Individual', crossover_point: Optional[int] = None) -> 'Individual':
        """
        Perform single-point crossover with another individual.
        
        Args:
            other: Another individual to crossover with
            crossover_point: Point to split genes. If None, randomly chosen
            
        Returns:
            New individual created from crossover
        """
        if crossover_point is None:
            crossover_point = random.randint(1, len(self.genes) - 1)
        
        # Create new genes by combining parts from both parents
        new_genes = self.genes[:crossover_point] + other.genes[crossover_point:]
        
        return Individual(self.category_sizes, new_genes)
    
    def evaluate(self, evaluate_func) -> float:
        """
        Evaluate this individual using the provided evaluation function.
        
        Args:
            evaluate_func: Function that takes a candidate and returns a fitness score
            
        Returns:
            Fitness score (0-100)
        """
        if self.fitness is None:
            self.fitness = evaluate_func(self.genes)
        return self.fitness
    
    def copy(self) -> 'Individual':
        """
        Create a deep copy of this individual.
        
        Returns:
            New Individual instance with same genes and fitness
        """
        new_individual = Individual(self.category_sizes, self.genes)
        new_individual.fitness = self.fitness
        return new_individual
    
    def __str__(self) -> str:
        """String representation of the individual."""
        fitness_str = f"{self.fitness:.2f}" if self.fitness is not None else "N/A"
        return f"Individual(genes={self.genes}, fitness={fitness_str})"
    
    def __repr__(self) -> str:
        """Detailed string representation of the individual."""
        return self.__str__()
    
    def __lt__(self, other: 'Individual') -> bool:
        """Compare individuals by fitness for sorting (higher fitness is better)."""
        if self.fitness is None or other.fitness is None:
            return False
        return self.fitness < other.fitness
    
    def __eq__(self, other: 'Individual') -> bool:
        """Check if two individuals are equal based on their genes."""
        return self.genes == other.genes 