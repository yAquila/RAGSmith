"""
Selection module for genetic algorithm.

This module contains various selection methods used in genetic algorithms
including tournament selection and roulette wheel selection.
"""

import random
from abc import ABC, abstractmethod
from typing import List, Optional
from individual import Individual
from population import Population


class SelectionMethod(ABC):
    """
    Abstract base class for selection methods.
    
    All selection methods should inherit from this class and implement
    the select method.
    """
    
    @abstractmethod
    def select(self, population: Population, num_parents: int) -> List[Individual]:
        """
        Select individuals from the population for reproduction.
        
        Args:
            population: Population to select from
            num_parents: Number of individuals to select
            
        Returns:
            List of selected individuals
        """
        pass


class TournamentSelection(SelectionMethod):
    """
    Tournament selection method.
    
    Selects individuals by running tournaments between randomly chosen
    individuals and selecting the winner (highest fitness) of each tournament.
    
    Attributes:
        tournament_size (int): Number of individuals in each tournament
    """
    
    def __init__(self, tournament_size: int = 3):
        """
        Initialize tournament selection.
        
        Args:
            tournament_size: Number of individuals competing in each tournament
        """
        if tournament_size < 2:
            raise ValueError("Tournament size must be at least 2")
        
        self.tournament_size = tournament_size
    
    def select(self, population: Population, num_parents: int) -> List[Individual]:
        """
        Select individuals using tournament selection.
        
        Args:
            population: Population to select from
            num_parents: Number of individuals to select
            
        Returns:
            List of selected individuals
            
        Raises:
            ValueError: If population is too small for tournament size
        """
        if len(population) < self.tournament_size:
            raise ValueError(f"Population size ({len(population)}) must be at least "
                           f"tournament size ({self.tournament_size})")
        
        # Filter out individuals without fitness scores
        evaluated_individuals = [ind for ind in population if ind.fitness is not None]
        if len(evaluated_individuals) < self.tournament_size:
            raise ValueError(f"Not enough evaluated individuals ({len(evaluated_individuals)}) "
                           f"for tournament size ({self.tournament_size})")
        
        selected = []
        for _ in range(num_parents):
            # Select random individuals for tournament
            tournament_contestants = random.sample(evaluated_individuals, self.tournament_size)
            
            # Select the best individual from the tournament
            winner = max(tournament_contestants, key=lambda x: x.fitness)
            selected.append(winner.copy())  # Return a copy to avoid modifying original
        
        return selected
    
    def __str__(self) -> str:
        """String representation of tournament selection."""
        return f"TournamentSelection(tournament_size={self.tournament_size})"


class RouletteWheelSelection(SelectionMethod):
    """
    Roulette wheel selection method.
    
    Selects individuals with probability proportional to their fitness.
    Individuals with higher fitness have a higher chance of being selected.
    
    Note: This implementation handles negative fitness values by shifting
    all fitness values to be positive.
    """
    
    def __init__(self):
        """Initialize roulette wheel selection."""
        pass
    
    def select(self, population: Population, num_parents: int) -> List[Individual]:
        """
        Select individuals using roulette wheel selection.
        
        Args:
            population: Population to select from
            num_parents: Number of individuals to select
            
        Returns:
            List of selected individuals
            
        Raises:
            ValueError: If no individuals have been evaluated
        """
        # Filter out individuals without fitness scores
        evaluated_individuals = [ind for ind in population if ind.fitness is not None]
        if not evaluated_individuals:
            raise ValueError("No evaluated individuals in population")
        
        # Handle negative fitness values by shifting to positive values
        min_fitness = min(ind.fitness for ind in evaluated_individuals)
        if min_fitness < 0:
            shifted_fitness = [ind.fitness - min_fitness + 1 for ind in evaluated_individuals]
        else:
            shifted_fitness = [ind.fitness for ind in evaluated_individuals]
        
        # Calculate total fitness for probability computation
        total_fitness = sum(shifted_fitness)
        
        if total_fitness == 0:
            # If all fitness values are zero, use uniform selection
            return [random.choice(evaluated_individuals).copy() for _ in range(num_parents)]
        
        # Calculate selection probabilities
        probabilities = [fitness / total_fitness for fitness in shifted_fitness]
        
        # Select individuals using weighted random selection
        selected = []
        for _ in range(num_parents):
            selected_individual = self._weighted_random_choice(evaluated_individuals, probabilities)
            selected.append(selected_individual.copy())
        
        return selected
    
    def _weighted_random_choice(self, individuals: List[Individual], 
                               probabilities: List[float]) -> Individual:
        """
        Select an individual using weighted random selection.
        
        Args:
            individuals: List of individuals to choose from
            probabilities: List of selection probabilities
            
        Returns:
            Selected individual
        """
        # Generate random number between 0 and 1
        r = random.random()
        
        # Find the individual corresponding to this probability
        cumulative_prob = 0.0
        for individual, prob in zip(individuals, probabilities):
            cumulative_prob += prob
            if r <= cumulative_prob:
                return individual
        
        # Fallback (should not happen with proper probabilities)
        return individuals[-1]
    
    def __str__(self) -> str:
        """String representation of roulette wheel selection."""
        return "RouletteWheelSelection()"


class RankSelection(SelectionMethod):
    """
    Rank-based selection method.
    
    Selects individuals based on their rank in the population rather than
    their raw fitness values. This helps avoid premature convergence when
    fitness values have large differences.
    """
    
    def __init__(self, selection_pressure: float = 2.0):
        """
        Initialize rank selection.
        
        Args:
            selection_pressure: Controls selection intensity (1.0-2.0)
        """
        if not (1.0 <= selection_pressure <= 2.0):
            raise ValueError("Selection pressure must be between 1.0 and 2.0")
        
        self.selection_pressure = selection_pressure
    
    def select(self, population: Population, num_parents: int) -> List[Individual]:
        """
        Select individuals using rank-based selection.
        
        Args:
            population: Population to select from
            num_parents: Number of individuals to select
            
        Returns:
            List of selected individuals
        """
        # Filter out individuals without fitness scores
        evaluated_individuals = [ind for ind in population if ind.fitness is not None]
        if not evaluated_individuals:
            raise ValueError("No evaluated individuals in population")
        
        # Sort individuals by fitness (ascending order for rank calculation)
        sorted_individuals = sorted(evaluated_individuals, key=lambda x: x.fitness)
        
        # Calculate rank-based probabilities
        n = len(sorted_individuals)
        probabilities = []
        
        for rank in range(n):  # rank 0 is worst, rank n-1 is best
            prob = (2 - self.selection_pressure + 2 * self.selection_pressure * rank / (n - 1)) / n
            probabilities.append(prob)
        
        # Select individuals using weighted random selection
        selected = []
        for _ in range(num_parents):
            r = random.random()
            cumulative_prob = 0.0
            
            for individual, prob in zip(sorted_individuals, probabilities):
                cumulative_prob += prob
                if r <= cumulative_prob:
                    selected.append(individual.copy())
                    break
            else:
                # Fallback
                selected.append(sorted_individuals[-1].copy())
        
        return selected
    
    def __str__(self) -> str:
        """String representation of rank selection."""
        return f"RankSelection(selection_pressure={self.selection_pressure})"


class EliteSelection(SelectionMethod):
    """
    Elite selection method.
    
    Simply selects the best individuals from the population.
    This is often used in combination with other selection methods.
    """
    
    def __init__(self):
        """Initialize elite selection."""
        pass
    
    def select(self, population: Population, num_parents: int) -> List[Individual]:
        """
        Select the best individuals from the population.
        
        Args:
            population: Population to select from
            num_parents: Number of individuals to select
            
        Returns:
            List of best individuals
        """
        top_individuals = population.get_top_individuals(num_parents)
        return [ind.copy() for ind in top_individuals]
    
    def __str__(self) -> str:
        """String representation of elite selection."""
        return "EliteSelection()" 