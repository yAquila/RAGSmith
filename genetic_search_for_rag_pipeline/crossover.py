"""
Crossover module for genetic algorithm.

This module contains various crossover methods used in genetic algorithms
including single-point, multi-point, and uniform crossover.
"""

import random
from abc import ABC, abstractmethod
from typing import List, Tuple, Optional
from individual import Individual


class CrossoverMethod(ABC):
    """
    Abstract base class for crossover methods.
    
    All crossover methods should inherit from this class and implement
    the crossover method.
    """
    
    @abstractmethod
    def crossover(self, parent1: Individual, parent2: Individual) -> Tuple[Individual, Individual]:
        """
        Perform crossover between two parent individuals.
        
        Args:
            parent1: First parent individual
            parent2: Second parent individual
            
        Returns:
            Tuple of two offspring individuals
        """
        pass


class SinglePointCrossover(CrossoverMethod):
    """
    Single-point crossover method.
    
    Selects a random crossover point and exchanges genetic material
    between parents at that point to create two offspring.
    """
    
    def __init__(self):
        """Initialize single-point crossover."""
        pass
    
    def crossover(self, parent1: Individual, parent2: Individual) -> Tuple[Individual, Individual]:
        """
        Perform single-point crossover between two parents.
        
        Args:
            parent1: First parent individual
            parent2: Second parent individual
            
        Returns:
            Tuple of two offspring individuals
            
        Raises:
            ValueError: If parents have different gene lengths
        """
        if len(parent1.genes) != len(parent2.genes):
            raise ValueError("Parents must have the same number of genes")
        
        if len(parent1.category_sizes) != len(parent2.category_sizes):
            raise ValueError("Parents must have the same category sizes")
        
        gene_length = len(parent1.genes)
        
        # Handle edge case of single gene
        if gene_length <= 1:
            return parent1.copy(), parent2.copy()
        
        # Select random crossover point (between 1 and gene_length-1)
        crossover_point = random.randint(1, gene_length - 1)
        
        # Create offspring by combining genes
        offspring1_genes = parent1.genes[:crossover_point] + parent2.genes[crossover_point:]
        offspring2_genes = parent2.genes[:crossover_point] + parent1.genes[crossover_point:]
        
        # Create offspring individuals
        offspring1 = Individual(parent1.category_sizes, offspring1_genes)
        offspring2 = Individual(parent1.category_sizes, offspring2_genes)
        
        return offspring1, offspring2
    
    def __str__(self) -> str:
        """String representation of single-point crossover."""
        return "SinglePointCrossover()"


class MultiPointCrossover(CrossoverMethod):
    """
    Multi-point crossover method.
    
    Selects multiple random crossover points and alternates between
    parents when creating offspring.
    """
    
    def __init__(self, num_points: int = 2):
        """
        Initialize multi-point crossover.
        
        Args:
            num_points: Number of crossover points
        """
        if num_points < 1:
            raise ValueError("Number of crossover points must be at least 1")
        
        self.num_points = num_points
    
    def crossover(self, parent1: Individual, parent2: Individual) -> Tuple[Individual, Individual]:
        """
        Perform multi-point crossover between two parents.
        
        Args:
            parent1: First parent individual
            parent2: Second parent individual
            
        Returns:
            Tuple of two offspring individuals
        """
        if len(parent1.genes) != len(parent2.genes):
            raise ValueError("Parents must have the same number of genes")
        
        gene_length = len(parent1.genes)
        
        # Handle edge cases
        if gene_length <= 1 or self.num_points >= gene_length:
            return parent1.copy(), parent2.copy()
        
        # Select random crossover points
        crossover_points = sorted(random.sample(range(1, gene_length), 
                                               min(self.num_points, gene_length - 1)))
        
        # Add boundaries
        points = [0] + crossover_points + [gene_length]
        
        # Create offspring by alternating between parents
        offspring1_genes = []
        offspring2_genes = []
        
        for i in range(len(points) - 1):
            start, end = points[i], points[i + 1]
            
            if i % 2 == 0:  # Even segments: use original parent order
                offspring1_genes.extend(parent1.genes[start:end])
                offspring2_genes.extend(parent2.genes[start:end])
            else:  # Odd segments: swap parent order
                offspring1_genes.extend(parent2.genes[start:end])
                offspring2_genes.extend(parent1.genes[start:end])
        
        # Create offspring individuals
        offspring1 = Individual(parent1.category_sizes, offspring1_genes)
        offspring2 = Individual(parent1.category_sizes, offspring2_genes)
        
        return offspring1, offspring2
    
    def __str__(self) -> str:
        """String representation of multi-point crossover."""
        return f"MultiPointCrossover(num_points={self.num_points})"


class UniformCrossover(CrossoverMethod):
    """
    Uniform crossover method.
    
    For each gene position, randomly selects which parent to inherit from
    based on a probability.
    """
    
    def __init__(self, probability: float = 0.5):
        """
        Initialize uniform crossover.
        
        Args:
            probability: Probability of inheriting from first parent (0.0 to 1.0)
        """
        if not (0.0 <= probability <= 1.0):
            raise ValueError("Probability must be between 0.0 and 1.0")
        
        self.probability = probability
    
    def crossover(self, parent1: Individual, parent2: Individual) -> Tuple[Individual, Individual]:
        """
        Perform uniform crossover between two parents.
        
        Args:
            parent1: First parent individual
            parent2: Second parent individual
            
        Returns:
            Tuple of two offspring individuals
        """
        if len(parent1.genes) != len(parent2.genes):
            raise ValueError("Parents must have the same number of genes")
        
        gene_length = len(parent1.genes)
        
        offspring1_genes = []
        offspring2_genes = []
        
        # For each gene position, randomly choose which parent to inherit from
        for i in range(gene_length):
            if random.random() < self.probability:
                # Inherit from first parent for offspring1, second parent for offspring2
                offspring1_genes.append(parent1.genes[i])
                offspring2_genes.append(parent2.genes[i])
            else:
                # Inherit from second parent for offspring1, first parent for offspring2
                offspring1_genes.append(parent2.genes[i])
                offspring2_genes.append(parent1.genes[i])
        
        # Create offspring individuals
        offspring1 = Individual(parent1.category_sizes, offspring1_genes)
        offspring2 = Individual(parent1.category_sizes, offspring2_genes)
        
        return offspring1, offspring2
    
    def __str__(self) -> str:
        """String representation of uniform crossover."""
        return f"UniformCrossover(probability={self.probability})"


class OrderCrossover(CrossoverMethod):
    """
    Order crossover method (OX).
    
    Designed for problems where gene order matters and duplicates should be avoided.
    For our box selection problem, this maintains valid selections while
    preserving partial order from parents.
    """
    
    def __init__(self):
        """Initialize order crossover."""
        pass
    
    def crossover(self, parent1: Individual, parent2: Individual) -> Tuple[Individual, Individual]:
        """
        Perform order crossover between two parents.
        
        Note: For our box selection problem, this is equivalent to single-point
        crossover since each gene is independent and represents a category selection.
        
        Args:
            parent1: First parent individual
            parent2: Second parent individual
            
        Returns:
            Tuple of two offspring individuals
        """
        # For our specific problem (box selection), order crossover
        # doesn't provide additional benefits over single-point crossover
        # since each gene position represents an independent category choice
        
        # We'll implement it as a variant that preserves some ordering
        if len(parent1.genes) != len(parent2.genes):
            raise ValueError("Parents must have the same number of genes")
        
        gene_length = len(parent1.genes)
        
        if gene_length <= 2:
            return parent1.copy(), parent2.copy()
        
        # Select two crossover points
        point1 = random.randint(0, gene_length - 2)
        point2 = random.randint(point1 + 1, gene_length - 1)
        
        # Create offspring
        offspring1_genes = parent1.genes.copy()
        offspring2_genes = parent2.genes.copy()
        
        # Swap the segment between crossover points
        offspring1_genes[point1:point2] = parent2.genes[point1:point2]
        offspring2_genes[point1:point2] = parent1.genes[point1:point2]
        
        # Create offspring individuals
        offspring1 = Individual(parent1.category_sizes, offspring1_genes)
        offspring2 = Individual(parent1.category_sizes, offspring2_genes)
        
        return offspring1, offspring2
    
    def __str__(self) -> str:
        """String representation of order crossover."""
        return "OrderCrossover()"


class SegmentCrossover(CrossoverMethod):
    """
    Segment crossover method.
    
    Divides genes into segments and exchanges complete segments between parents.
    This can be useful when certain gene combinations work well together.
    """
    
    def __init__(self, num_segments: int = 3):
        """
        Initialize segment crossover.
        
        Args:
            num_segments: Number of segments to divide genes into
        """
        if num_segments < 2:
            raise ValueError("Number of segments must be at least 2")
        
        self.num_segments = num_segments
    
    def crossover(self, parent1: Individual, parent2: Individual) -> Tuple[Individual, Individual]:
        """
        Perform segment crossover between two parents.
        
        Args:
            parent1: First parent individual
            parent2: Second parent individual
            
        Returns:
            Tuple of two offspring individuals
        """
        if len(parent1.genes) != len(parent2.genes):
            raise ValueError("Parents must have the same number of genes")
        
        gene_length = len(parent1.genes)
        
        if gene_length < self.num_segments:
            # Fall back to single-point crossover if not enough genes
            single_point = SinglePointCrossover()
            return single_point.crossover(parent1, parent2)
        
        # Calculate segment boundaries
        segment_size = gene_length // self.num_segments
        remainder = gene_length % self.num_segments
        
        segments = []
        start = 0
        for i in range(self.num_segments):
            # Distribute remainder among first segments
            size = segment_size + (1 if i < remainder else 0)
            segments.append((start, start + size))
            start += size
        
        # Create offspring by randomly selecting segments from parents
        offspring1_genes = []
        offspring2_genes = []
        
        for start, end in segments:
            if random.random() < 0.5:
                # Take segment from original parent
                offspring1_genes.extend(parent1.genes[start:end])
                offspring2_genes.extend(parent2.genes[start:end])
            else:
                # Take segment from other parent
                offspring1_genes.extend(parent2.genes[start:end])
                offspring2_genes.extend(parent1.genes[start:end])
        
        # Create offspring individuals
        offspring1 = Individual(parent1.category_sizes, offspring1_genes)
        offspring2 = Individual(parent1.category_sizes, offspring2_genes)
        
        return offspring1, offspring2
    
    def __str__(self) -> str:
        """String representation of segment crossover."""
        return f"SegmentCrossover(num_segments={self.num_segments})" 