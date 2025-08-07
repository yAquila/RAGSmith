"""
Mutation module for genetic algorithm.

This module contains various mutation methods designed specifically for 
categorical genetic algorithms where genes represent discrete category choices.
"""

import random
from abc import ABC, abstractmethod
from typing import List, Optional
from individual import Individual


class MutationMethod(ABC):
    """
    Abstract base class for mutation methods.
    
    All mutation methods should inherit from this class and implement
    the mutate method.
    """
    
    @abstractmethod
    def mutate(self, individual: Individual) -> Individual:
        """
        Apply mutation to an individual.
        
        Args:
            individual: Individual to mutate
            
        Returns:
            Mutated individual (may be a copy or modified in-place)
        """
        pass


class RandomMutation(MutationMethod):
    """
    Random mutation method for categorical variables.
    
    Randomly changes genes in an individual based on a mutation rate.
    Each gene has an independent probability of being mutated to a 
    different random category.
    """
    
    def __init__(self, mutation_rate: float = 0.1):
        """
        Initialize random mutation.
        
        Args:
            mutation_rate: Probability of mutating each gene (0.0 to 1.0)
        """
        if not (0.0 <= mutation_rate <= 1.0):
            raise ValueError("Mutation rate must be between 0.0 and 1.0")
        
        self.mutation_rate = mutation_rate
    
    def mutate(self, individual: Individual) -> Individual:
        """
        Apply random mutation to an individual.
        
        For categorical variables, this means randomly selecting a new 
        category from the available options for each mutated gene.
        
        Args:
            individual: Individual to mutate
            
        Returns:
            Mutated individual (copy of original)
        """
        mutated = individual.copy()
        
        for i in range(len(mutated.genes)):
            if random.random() < self.mutation_rate:
                # Randomly select a new category (different from current)
                current_value = mutated.genes[i]
                available_values = list(range(mutated.category_sizes[i]))
                
                # Remove current value to ensure we get a different one
                if len(available_values) > 1:
                    available_values.remove(current_value)
                    mutated.genes[i] = random.choice(available_values)
                # If only one option available, keep the same value
        
        # Reset fitness since individual has changed
        mutated.fitness = None
        
        return mutated
    
    def __str__(self) -> str:
        """String representation of random mutation."""
        return f"RandomMutation(mutation_rate={self.mutation_rate})"


class AdaptiveMutation(MutationMethod):
    """
    Adaptive mutation method for categorical variables.
    
    Adjusts mutation rate based on population diversity or fitness improvement.
    Higher diversity or recent improvements lead to lower mutation rates.
    """
    
    def __init__(self, base_mutation_rate: float = 0.1, 
                 min_mutation_rate: float = 0.01,
                 max_mutation_rate: float = 0.5):
        """
        Initialize adaptive mutation.
        
        Args:
            base_mutation_rate: Base mutation rate
            min_mutation_rate: Minimum allowed mutation rate
            max_mutation_rate: Maximum allowed mutation rate
        """
        if not (0.0 <= min_mutation_rate <= base_mutation_rate <= max_mutation_rate <= 1.0):
            raise ValueError("Invalid mutation rate parameters")
        
        self.base_mutation_rate = base_mutation_rate
        self.min_mutation_rate = min_mutation_rate
        self.max_mutation_rate = max_mutation_rate
        self.current_mutation_rate = base_mutation_rate
        
        # Tracking variables for adaptation
        self.generations_without_improvement = 0
        self.last_best_fitness = None
    
    def update_mutation_rate(self, current_best_fitness: float, 
                           population_diversity: float = 0.5) -> None:
        """
        Update mutation rate based on fitness improvement and diversity.
        
        Args:
            current_best_fitness: Best fitness in current generation
            population_diversity: Population diversity score (0.0 to 1.0)
        """
        # Check for fitness improvement
        if self.last_best_fitness is None:
            self.last_best_fitness = current_best_fitness
            self.generations_without_improvement = 0
        elif current_best_fitness <= self.last_best_fitness:
            self.generations_without_improvement += 1
        else:
            self.generations_without_improvement = 0
            self.last_best_fitness = current_best_fitness
        
        # Adapt mutation rate based on diversity and improvement
        diversity_factor = 1.0 - population_diversity  # Low diversity = high factor
        stagnation_factor = min(self.generations_without_improvement / 10.0, 1.0)
        
        # Increase mutation rate if low diversity or no improvement
        adaptation_factor = (diversity_factor + stagnation_factor) / 2.0
        
        target_rate = self.base_mutation_rate + (self.max_mutation_rate - self.base_mutation_rate) * adaptation_factor
        self.current_mutation_rate = max(self.min_mutation_rate, min(self.max_mutation_rate, target_rate))
    
    def mutate(self, individual: Individual) -> Individual:
        """
        Apply adaptive mutation to an individual.
        
        Args:
            individual: Individual to mutate
            
        Returns:
            Mutated individual (copy of original)
        """
        mutated = individual.copy()
        
        for i in range(len(mutated.genes)):
            if random.random() < self.current_mutation_rate:
                # Randomly select a new category (different from current)
                current_value = mutated.genes[i]
                available_values = list(range(mutated.category_sizes[i]))
                
                # Remove current value to ensure we get a different one
                if len(available_values) > 1:
                    available_values.remove(current_value)
                    mutated.genes[i] = random.choice(available_values)
        
        mutated.fitness = None
        return mutated
    
    def __str__(self) -> str:
        """String representation of adaptive mutation."""
        return (f"AdaptiveMutation(current_rate={self.current_mutation_rate:.3f}, "
                f"base={self.base_mutation_rate})")


class CategoricalMutation(MutationMethod):
    """
    Advanced categorical mutation method.
    
    Specifically designed for categorical variables with different mutation strategies:
    - Random change to any other category
    - Weighted change based on category frequency
    - Multiple gene mutation with adjusted probabilities
    """
    
    def __init__(self, mutation_rate: float = 0.1, 
                 force_change: bool = True,
                 multi_gene_probability: float = 0.3):
        """
        Initialize categorical mutation.
        
        Args:
            mutation_rate: Base probability of mutation per gene
            force_change: If True, mutation always changes the value
            multi_gene_probability: Probability of mutating multiple genes at once
        """
        if not (0.0 <= mutation_rate <= 1.0):
            raise ValueError("Mutation rate must be between 0.0 and 1.0")
        if not (0.0 <= multi_gene_probability <= 1.0):
            raise ValueError("Multi-gene probability must be between 0.0 and 1.0")
        
        self.mutation_rate = mutation_rate
        self.force_change = force_change
        self.multi_gene_probability = multi_gene_probability
    
    def mutate(self, individual: Individual) -> Individual:
        """
        Apply categorical mutation to an individual.
        
        Args:
            individual: Individual to mutate
            
        Returns:
            Mutated individual (copy of original)
        """
        mutated = individual.copy()
        
        # Decide if we should perform multi-gene mutation
        if random.random() < self.multi_gene_probability and len(mutated.genes) > 1:
            # Multi-gene mutation: select 2-3 genes to mutate
            num_genes_to_mutate = min(random.randint(2, 3), len(mutated.genes))
            genes_to_mutate = random.sample(range(len(mutated.genes)), num_genes_to_mutate)
            
            for i in genes_to_mutate:
                self._mutate_gene(mutated, i)
        else:
            # Standard single-gene mutation
            for i in range(len(mutated.genes)):
                if random.random() < self.mutation_rate:
                    self._mutate_gene(mutated, i)
        
        mutated.fitness = None
        return mutated
    
    def _mutate_gene(self, individual: Individual, gene_index: int) -> None:
        """
        Mutate a single gene in the individual.
        
        Args:
            individual: Individual to mutate
            gene_index: Index of gene to mutate
        """
        current_value = individual.genes[gene_index]
        available_values = list(range(individual.category_sizes[gene_index]))
        
        if self.force_change and len(available_values) > 1:
            # Remove current value to ensure change
            available_values.remove(current_value)
            individual.genes[gene_index] = random.choice(available_values)
        elif not self.force_change:
            # Allow keeping the same value
            individual.genes[gene_index] = random.choice(available_values)
    
    def __str__(self) -> str:
        """String representation of categorical mutation."""
        return (f"CategoricalMutation(rate={self.mutation_rate}, "
                f"force_change={self.force_change}, "
                f"multi_gene={self.multi_gene_probability})")


class SwapMutation(MutationMethod):
    """
    Swap mutation method for categorical variables.
    
    UPDATED: This is now a "category redistribution" mutation.
    Instead of swapping gene positions (which doesn't make sense for categorical data),
    this randomly redistributes categories among multiple genes.
    """
    
    def __init__(self, mutation_rate: float = 0.1):
        """
        Initialize swap mutation.
        
        Args:
            mutation_rate: Probability of performing category redistribution
        """
        if not (0.0 <= mutation_rate <= 1.0):
            raise ValueError("Mutation rate must be between 0.0 and 1.0")
        
        self.mutation_rate = mutation_rate
    
    def mutate(self, individual: Individual) -> Individual:
        """
        Apply category redistribution mutation.
        
        This selects 2-3 genes and gives them new random categories,
        providing a more exploratory mutation than single-gene changes.
        
        Args:
            individual: Individual to mutate
            
        Returns:
            Mutated individual (copy of original)
        """
        mutated = individual.copy()
        
        if len(mutated.genes) < 2:
            return mutated
        
        if random.random() < self.mutation_rate:
            # Select 2-3 genes for redistribution
            num_genes = min(random.randint(2, 3), len(mutated.genes))
            selected_genes = random.sample(range(len(mutated.genes)), num_genes)
            
            # Give each selected gene a new random category
            for gene_idx in selected_genes:
                current_value = mutated.genes[gene_idx]
                available_values = list(range(mutated.category_sizes[gene_idx]))
                
                # Remove current value to ensure change
                if len(available_values) > 1:
                    available_values.remove(current_value)
                    mutated.genes[gene_idx] = random.choice(available_values)
        
        mutated.fitness = None
        return mutated
    
    def __str__(self) -> str:
        """String representation of category redistribution mutation."""
        return f"SwapMutation(mutation_rate={self.mutation_rate})"


class InversionMutation(MutationMethod):
    """
    Inversion mutation method adapted for categorical variables.
    
    UPDATED: This is now a "segment randomization" mutation.
    Instead of reversing gene order (which doesn't make sense for categorical data),
    this randomizes all categories within a selected segment.
    """
    
    def __init__(self, mutation_rate: float = 0.1):
        """
        Initialize segment randomization mutation.
        
        Args:
            mutation_rate: Probability of performing segment randomization
        """
        if not (0.0 <= mutation_rate <= 1.0):
            raise ValueError("Mutation rate must be between 0.0 and 1.0")
        
        self.mutation_rate = mutation_rate
    
    def mutate(self, individual: Individual) -> Individual:
        """
        Apply segment randomization mutation.
        
        This selects a random segment of genes and assigns new 
        random categories to all genes in that segment.
        
        Args:
            individual: Individual to mutate
            
        Returns:
            Mutated individual (copy of original)
        """
        mutated = individual.copy()
        
        if len(mutated.genes) < 2:
            return mutated
        
        if random.random() < self.mutation_rate:
            # Select random segment
            segment_length = random.randint(2, min(4, len(mutated.genes)))
            start_pos = random.randint(0, len(mutated.genes) - segment_length)
            end_pos = start_pos + segment_length
            
            # Randomize all genes in the segment
            for i in range(start_pos, end_pos):
                current_value = mutated.genes[i]
                available_values = list(range(mutated.category_sizes[i]))
                
                # Remove current value to ensure change
                if len(available_values) > 1:
                    available_values.remove(current_value)
                    mutated.genes[i] = random.choice(available_values)
        
        mutated.fitness = None
        return mutated
    
    def __str__(self) -> str:
        """String representation of segment randomization mutation."""
        return f"InversionMutation(mutation_rate={self.mutation_rate})"


class CompositeMutation(MutationMethod):
    """
    Composite mutation method.
    
    Combines multiple mutation methods and applies them with specified probabilities.
    This allows for more diverse mutation strategies.
    """
    
    def __init__(self, mutation_methods: List[tuple]):
        """
        Initialize composite mutation.
        
        Args:
            mutation_methods: List of tuples (method, probability)
        """
        if not mutation_methods:
            raise ValueError("At least one mutation method must be provided")
        
        total_prob = sum(prob for _, prob in mutation_methods)
        if abs(total_prob - 1.0) > 1e-6:
            raise ValueError(f"Probabilities must sum to 1.0, got {total_prob}")
        
        self.mutation_methods = mutation_methods
    
    def mutate(self, individual: Individual) -> Individual:
        """
        Apply composite mutation to an individual.
        
        Args:
            individual: Individual to mutate
            
        Returns:
            Mutated individual (copy of original)
        """
        # Select mutation method based on probabilities
        r = random.random()
        cumulative_prob = 0.0
        
        for method, prob in self.mutation_methods:
            cumulative_prob += prob
            if r <= cumulative_prob:
                return method.mutate(individual)
        
        # Fallback to last method
        return self.mutation_methods[-1][0].mutate(individual)
    
    def __str__(self) -> str:
        """String representation of composite mutation."""
        methods_str = ", ".join(f"{method}({prob:.2f})" 
                               for method, prob in self.mutation_methods)
        return f"CompositeMutation([{methods_str}])" 