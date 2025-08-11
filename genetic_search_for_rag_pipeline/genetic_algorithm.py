"""
Main genetic algorithm module.

This module contains the GeneticAlgorithm class that orchestrates the entire
genetic algorithm process for component combination search.
"""

import random
import time
from typing import List, Dict, Any, Callable, Optional, Tuple
from dataclasses import dataclass
from individual import Individual
from population import Population
from config import GAConfig
from selection import SelectionMethod
from crossover import CrossoverMethod
from mutation import MutationMethod


@dataclass
class GenerationStatistics:
    """Statistics for a single generation."""
    generation: int
    best_fitness: float
    worst_fitness: float
    average_fitness: float
    diversity_score: float
    best_individual_genes: List[int]
    execution_time: float


class GeneticAlgorithm:
    """
    Main genetic algorithm class for component combination optimization.
    
    This class orchestrates the entire genetic algorithm process, including
    initialization, evolution, selection, crossover, mutation, and tracking
    of statistics and progress.
    
    Attributes:
        config: Configuration object containing all GA parameters
        population: Current population of individuals
        statistics: List of generation statistics
        best_ever_individual: Best individual found during evolution
        generations_without_improvement: Counter for convergence detection
        evaluate_func: External evaluation function
    """
    
    def __init__(self, config: GAConfig, evaluate_func: Callable[[List[int]], float]):
        """
        Initialize the genetic algorithm.
        
        Args:
            config: Configuration object with GA parameters
            evaluate_func: Function that evaluates a candidate and returns fitness (0-100)
        """
        self.config = config
        self.evaluate_func = evaluate_func
        
        # Set random seed if provided
        if config.random_seed is not None:
            random.seed(config.random_seed)
        
        # Initialize population
        self.population = Population(config.population_size, config.category_sizes)
        
        # Statistics tracking
        self.statistics: List[GenerationStatistics] = []
        self.best_ever_individual: Optional[Individual] = None
        self.generations_without_improvement = 0
        self.start_time: Optional[float] = None
        
        # Evolution tracking
        self.current_generation = 0
        self.converged = False
        self.target_reached = False
    
    def initialize_population(self) -> None:
        """Initialize and evaluate the population."""
        if self.config.verbose:
            print(f"Initializing population of {self.config.population_size} individuals...")
        
        # Evaluate all individuals in the population and track global best
        for individual in self.population.individuals:
            individual.evaluate(self.evaluate_func)
            
            # Track the best individual from initial population
            if individual.fitness is not None and (self.best_ever_individual is None or 
                                                 individual.fitness > self.best_ever_individual.fitness):
                self.best_ever_individual = individual.copy()
        
        if self.config.verbose:
            best_fitness = self.best_ever_individual.fitness if self.best_ever_individual else 0
            print(f"Initial population created. Best fitness: {best_fitness:.4f}")
    
    def select_parents(self, num_parents: int) -> List[Individual]:
        """
        Select parents for reproduction.
        
        Args:
            num_parents: Number of parents to select
            
        Returns:
            List of selected parent individuals
        """
        return self.config.selection_method.select(self.population, num_parents)
    
    def create_offspring(self, parents: List[Individual]) -> List[Individual]:
        """
        Create offspring through crossover and mutation.
        
        Args:
            parents: List of parent individuals
            
        Returns:
            List of offspring individuals
        """
        offspring = []
        
        # Create pairs of parents and perform crossover
        for i in range(0, len(parents) - 1, 2):
            parent1 = parents[i]
            parent2 = parents[i + 1] if i + 1 < len(parents) else parents[0]
            
            if random.random() < self.config.crossover_rate:
                # Perform crossover
                child1, child2 = self.config.crossover_method.crossover(parent1, parent2)
            else:
                # No crossover, copy parents
                child1, child2 = parent1.copy(), parent2.copy()
            
            # Apply mutation
            child1 = self.config.mutation_method.mutate(child1)
            child2 = self.config.mutation_method.mutate(child2)
            
            offspring.extend([child1, child2])
        
        return offspring
    
    def apply_elitism(self, new_population: List[Individual]) -> List[Individual]:
        """
        Apply elitism by preserving the best individuals.
        
        Args:
            new_population: List of new individuals
            
        Returns:
            Population with elitism applied
        """
        if self.config.elitism_count == 0:
            return new_population
        
        # Get the best individuals from current population
        elite_individuals = self.population.get_top_individuals(self.config.elitism_count)
        
        # Replace worst individuals in new population with elite individuals
        new_population.sort(key=lambda x: x.fitness if x.fitness is not None else -1, reverse=True)
        
        # Replace the worst individuals with elite ones
        final_population = new_population[:-self.config.elitism_count] + elite_individuals
        
        return final_population
    
    def evolve_generation(self) -> None:
        """Evolve one generation of the population."""
        generation_start_time = time.time()
        
        # Calculate number of offspring needed
        offspring_count = self.config.population_size - self.config.elitism_count
        
        # Select parents for reproduction
        parents = self.select_parents(offspring_count)
        
        # Create offspring through crossover and mutation
        offspring = self.create_offspring(parents)
        
        # Ensure we have the right number of offspring
        offspring = offspring[:offspring_count]
        
        # Evaluate offspring and track best individual from ALL evaluations
        for individual in offspring:
            individual.evaluate(self.evaluate_func)
            
            # Check if this individual is the best ever seen
            if individual.fitness is not None and (self.best_ever_individual is None or 
                                                 individual.fitness > self.best_ever_individual.fitness):
                self.best_ever_individual = individual.copy()
                self.generations_without_improvement = 0
                print(f"!!!NEW GLOBAL BEST!!! {self.best_ever_individual}")
        
        # Apply elitism
        if self.config.elitism_count > 0:
            new_individuals = self.apply_elitism(offspring)
        else:
            new_individuals = offspring
        
        # Create new population
        self.population = Population(self.config.population_size, self.config.category_sizes)
        self.population.individuals = new_individuals[:self.config.population_size]
        
        # Update best individual from current population (for logging)
        current_best = self.population.get_best_individual()
        print("!!!current_best_in_population!!!", current_best)
        
        # Also check if anyone in the current population is better (shouldn't happen, but safety check)
        if current_best and current_best.fitness is not None and (self.best_ever_individual is None or 
                           current_best.fitness > self.best_ever_individual.fitness):
            self.best_ever_individual = current_best.copy()
            self.generations_without_improvement = 0
        else:
            self.generations_without_improvement += 1
        
        print("!!!best_ever_individual!!!", self.best_ever_individual)
        
        # Record statistics
        if self.config.track_statistics and self.current_generation % self.config.statistics_interval == 0:
            stats = self._collect_generation_statistics(time.time() - generation_start_time)
            self.statistics.append(stats)
        
        # Update adaptive mutation rate if applicable
        from mutation import AdaptiveMutation
        if isinstance(self.config.mutation_method, AdaptiveMutation):
            best_fitness = self.best_ever_individual.fitness if self.best_ever_individual else 0
            diversity = self.population.get_diversity_score()
            self.config.mutation_method.update_mutation_rate(best_fitness, diversity)
    
    def _collect_generation_statistics(self, execution_time: float) -> GenerationStatistics:
        """
        Collect statistics for the current generation.
        
        Args:
            execution_time: Time taken for this generation
            
        Returns:
            GenerationStatistics object
        """
        best_individual = self.population.get_best_individual()
        worst_individual = self.population.get_worst_individual()
        avg_fitness = self.population.get_average_fitness()
        diversity = self.population.get_diversity_score()
        
        return GenerationStatistics(
            generation=self.current_generation,
            best_fitness=best_individual.fitness if best_individual else 0,
            worst_fitness=worst_individual.fitness if worst_individual else 0,
            average_fitness=avg_fitness if avg_fitness else 0,
            diversity_score=diversity,
            best_individual_genes=best_individual.genes.copy() if best_individual else [],
            execution_time=execution_time
        )
    
    def check_termination_criteria(self) -> bool:
        """
        Check if any termination criteria are met.
        
        Returns:
            True if algorithm should terminate, False otherwise
        """
        # Check generation limit
        if self.current_generation >= self.config.generations:
            return True
        
        # Check convergence (no improvement)
        if self.generations_without_improvement >= self.config.convergence_threshold:
            self.converged = True
            return True
        
        # Check target fitness
        if (self.config.target_fitness is not None and 
            self.best_ever_individual and 
            self.best_ever_individual.fitness >= self.config.target_fitness):
            self.target_reached = True
            return True
        
        return False
    
    def run(self) -> Dict[str, Any]:
        """
        Run the genetic algorithm.
        
        Returns:
            Dictionary containing results and statistics
        """
        self.start_time = time.time()
        
        if self.config.verbose:
            print(f"Starting genetic algorithm with configuration:")
            print(f"  Population size: {self.config.population_size}")
            print(f"  Generations: {self.config.generations}")
            print(f"  Categories: {len(self.config.category_sizes)}")
            print(f"  Total combinations: {self.config.get_total_combinations():,}")
            print("-" * 50)
        
        # Initialize population
        self.initialize_population()
        
        # Main evolution loop
        while not self.check_termination_criteria():
            self.current_generation += 1
            
            # Evolve one generation
            self.evolve_generation()
            
            # Print progress
            if self.config.verbose and self.current_generation % 10 == 0:
                best_fitness = self.best_ever_individual.fitness if self.best_ever_individual else 0
                diversity = self.population.get_diversity_score()
                print(f"Generation {self.current_generation:3d}: "
                      f"Best fitness = {best_fitness:6.4f}, "
                      f"Diversity = {diversity:.3f}, "
                      f"No improvement = {self.generations_without_improvement}")
        
        # Calculate total execution time
        total_time = time.time() - self.start_time
        
        # Final statistics collection
        if self.config.track_statistics:
            final_stats = self._collect_generation_statistics(0.0)
            self.statistics.append(final_stats)
        
        # Prepare results
        results = self._prepare_results(total_time)
        
        if self.config.verbose:
            self._print_final_results(results)
        
        return results
    
    def _prepare_results(self, total_time: float) -> Dict[str, Any]:
        """
        Prepare final results dictionary.
        
        Args:
            total_time: Total execution time
            
        Returns:
            Dictionary containing all results and statistics
        """
        best_individual = self.best_ever_individual
        
        final_stats = self.population.get_statistics()
        
        return {
            'best_combination': best_individual.genes if best_individual else None,
            'best_fitness': best_individual.fitness if best_individual else None,
            'generations_completed': self.current_generation,
            'total_time': total_time,
            'converged': self.converged,
            'target_reached': self.target_reached,
            'generations_without_improvement': self.generations_without_improvement,
            'final_population_stats': final_stats,
            'final_diversity': final_stats['diversity_score'],  # Add direct access to diversity
            'final_average_fitness': final_stats['average_fitness'],  # Add direct access to avg fitness
            'statistics': self.statistics,
            'config': self.config.to_dict()
        }
    
    def _print_final_results(self, results: Dict[str, Any]) -> None:
        """
        Print final results summary.
        
        Args:
            results: Results dictionary
        """
        print("-" * 50)
        print("GENETIC ALGORITHM COMPLETED")
        print("-" * 50)
        print(f"Best combination found: {results['best_combination']}")
        print(f"Best fitness: {results['best_fitness']:.4f}")
        print(f"Generations completed: {results['generations_completed']}")
        print(f"Total execution time: {results['total_time']:.2f} seconds")
        
        if results['converged']:
            print(f"Algorithm converged (no improvement for {self.config.convergence_threshold} generations)")
        elif results['target_reached']:
            print(f"Target fitness {self.config.target_fitness} reached!")
        else:
            print("Algorithm completed all generations")
        
        final_stats = results['final_population_stats']
        print(f"Final population diversity: {final_stats['diversity_score']:.3f}")
        print(f"Final average fitness: {final_stats['average_fitness']:.4f}")
    
    def get_best_solution(self) -> Tuple[List[int], float]:
        """
        Get the best solution found.
        
        Returns:
            Tuple of (best_combination, best_fitness)
        """
        if self.best_ever_individual:
            return self.best_ever_individual.genes.copy(), self.best_ever_individual.fitness
        else:
            return [], 0.0
    
    def get_statistics_summary(self) -> Dict[str, Any]:
        """
        Get a summary of evolution statistics.
        
        Returns:
            Dictionary containing statistics summary
        """
        if not self.statistics:
            return {}
        
        best_fitnesses = [stat.best_fitness for stat in self.statistics]
        avg_fitnesses = [stat.average_fitness for stat in self.statistics]
        diversities = [stat.diversity_score for stat in self.statistics]
        
        return {
            'total_generations': len(self.statistics),
            'fitness_improvement': best_fitnesses[-1] - best_fitnesses[0] if len(best_fitnesses) > 1 else 0,
            'max_fitness': max(best_fitnesses),
            'min_fitness': min(best_fitnesses),
            'average_diversity': sum(diversities) / len(diversities),
            'final_diversity': diversities[-1] if diversities else 0,
            'total_evaluations': self.current_generation * self.config.population_size
        } 