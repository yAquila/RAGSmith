#!/usr/bin/env python3
"""
Configuration Loader for RAGSmith

This module provides utilities for loading and parsing the gen_search_config.yml file.
It can be used by both the RAG pipeline and the genetic search modules.
"""

import os
import yaml
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class DatasetConfig:
    """Dataset configuration."""
    path: str = "rag_pipeline/default_datasets/military_10"


@dataclass
class APIConfig:
    """API configuration."""
    host: str = "localhost"
    port: int = 8060
    timeout: int = 3600


@dataclass
class SelectionConfig:
    """Selection method configuration."""
    method: str = "tournament"
    tournament_size: int = 3
    selection_pressure: float = 2.0


@dataclass
class CrossoverConfig:
    """Crossover method configuration."""
    method: str = "single_point"
    num_points: int = 2
    probability: float = 0.5
    num_segments: int = 3


@dataclass
class MutationConfig:
    """Mutation method configuration."""
    method: str = "random"
    base_mutation_rate: float = 0.1
    min_mutation_rate: float = 0.01
    max_mutation_rate: float = 0.5
    force_change: bool = True
    multi_gene_probability: float = 0.3


@dataclass
class GeneticAlgorithmConfig:
    """Genetic algorithm configuration."""
    population_size: int = 50
    generations: int = 100
    crossover_rate: float = 0.8
    mutation_rate: float = 0.1
    elitism_count: int = 2
    selection: SelectionConfig = field(default_factory=SelectionConfig)
    crossover: CrossoverConfig = field(default_factory=CrossoverConfig)
    mutation: MutationConfig = field(default_factory=MutationConfig)
    convergence_threshold: int = 20
    target_fitness: Optional[float] = None
    random_seed: Optional[int] = None
    verbose: bool = True
    track_statistics: bool = True
    statistics_interval: int = 1


@dataclass
class SearchSpace:
    """Search space configuration (available technique options)."""
    pre_embedding: List[str] = field(default_factory=list)
    query_expansion: List[str] = field(default_factory=list)
    retrieval: List[str] = field(default_factory=list)
    passage_rerank: List[str] = field(default_factory=list)
    passage_filter: List[str] = field(default_factory=list)
    passage_augment: List[str] = field(default_factory=list)
    passage_compress: List[str] = field(default_factory=list)
    prompt_maker: List[str] = field(default_factory=list)
    generator: List[str] = field(default_factory=list)
    post_generation: List[str] = field(default_factory=list)


@dataclass
class EvaluationWeights:
    """Evaluation weights configuration."""
    retrieval_weights: Dict[str, float] = field(default_factory=lambda: {
        'recall_at_k': 0.25,
        'map_score': 0.25,
        'ndcg_at_k': 0.25,
        'mrr': 0.25
    })
    generation_weights: Dict[str, float] = field(default_factory=lambda: {
        'llm_score': 0.5,
        'semantic_similarity': 0.5
    })
    overall_weights: Dict[str, float] = field(default_factory=lambda: {
        'retrieval': 0.5,
        'generation': 0.5
    })
    llm_eval_model: str = "gpt-oss:120B"


@dataclass
class OutputConfig:
    """Output configuration."""
    save_best_configs: bool = True
    best_configs_file: str = "best_rag_configs.json"
    save_evolution_history: bool = True
    evolution_history_file: str = "evolution_history.json"
    log_level: str = "INFO"


@dataclass
class RAGSmithConfig:
    """Complete RAGSmith configuration."""
    dataset: DatasetConfig = field(default_factory=DatasetConfig)
    api: APIConfig = field(default_factory=APIConfig)
    genetic_algorithm: GeneticAlgorithmConfig = field(default_factory=GeneticAlgorithmConfig)
    search_space: SearchSpace = field(default_factory=SearchSpace)
    evaluation: EvaluationWeights = field(default_factory=EvaluationWeights)
    output: OutputConfig = field(default_factory=OutputConfig)


def find_config_file(config_path: Optional[str] = None) -> str:
    """
    Find the configuration file path.
    
    Args:
        config_path: Optional explicit path to config file
        
    Returns:
        Path to the configuration file
        
    Raises:
        FileNotFoundError: If config file cannot be found
    """
    if config_path and os.path.exists(config_path):
        return config_path
    
    # Search in common locations
    search_paths = [
        "gen_search_config.yml",
        "../gen_search_config.yml",
        "../../gen_search_config.yml",
        os.path.join(os.path.dirname(__file__), "gen_search_config.yml"),
        os.path.join(os.path.dirname(__file__), "..", "gen_search_config.yml"),
    ]
    
    # Also check environment variable
    env_path = os.environ.get("RAGSMITH_CONFIG")
    if env_path:
        search_paths.insert(0, env_path)
    
    for path in search_paths:
        if os.path.exists(path):
            return os.path.abspath(path)
    
    raise FileNotFoundError(
        f"Could not find gen_search_config.yml. Searched: {search_paths}"
    )


def load_yaml_config(config_path: Optional[str] = None) -> Dict[str, Any]:
    """
    Load raw YAML configuration from file.
    
    Args:
        config_path: Optional path to config file
        
    Returns:
        Raw dictionary from YAML file
    """
    path = find_config_file(config_path)
    
    with open(path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    return config


def load_config(config_path: Optional[str] = None) -> RAGSmithConfig:
    """
    Load and parse the complete RAGSmith configuration.
    
    Args:
        config_path: Optional path to config file
        
    Returns:
        RAGSmithConfig object with all settings
    """
    raw_config = load_yaml_config(config_path)
    
    # Parse dataset config
    dataset_raw = raw_config.get('dataset', {})
    dataset = DatasetConfig(
        path=dataset_raw.get('path', 'rag_pipeline/default_datasets/military_10')
    )
    
    # Parse API config
    api_raw = raw_config.get('api', {})
    api = APIConfig(
        host=api_raw.get('host', 'localhost'),
        port=api_raw.get('port', 8060),
        timeout=api_raw.get('timeout', 3600)
    )
    
    # Parse genetic algorithm config
    ga_raw = raw_config.get('genetic_algorithm', {})
    
    selection_raw = ga_raw.get('selection', {})
    selection = SelectionConfig(
        method=selection_raw.get('method', 'tournament'),
        tournament_size=selection_raw.get('tournament_size', 3),
        selection_pressure=selection_raw.get('selection_pressure', 2.0)
    )
    
    crossover_raw = ga_raw.get('crossover', {})
    crossover = CrossoverConfig(
        method=crossover_raw.get('method', 'single_point'),
        num_points=crossover_raw.get('num_points', 2),
        probability=crossover_raw.get('probability', 0.5),
        num_segments=crossover_raw.get('num_segments', 3)
    )
    
    mutation_raw = ga_raw.get('mutation', {})
    mutation = MutationConfig(
        method=mutation_raw.get('method', 'random'),
        base_mutation_rate=mutation_raw.get('base_mutation_rate', 0.1),
        min_mutation_rate=mutation_raw.get('min_mutation_rate', 0.01),
        max_mutation_rate=mutation_raw.get('max_mutation_rate', 0.5),
        force_change=mutation_raw.get('force_change', True),
        multi_gene_probability=mutation_raw.get('multi_gene_probability', 0.3)
    )
    
    genetic_algorithm = GeneticAlgorithmConfig(
        population_size=ga_raw.get('population_size', 50),
        generations=ga_raw.get('generations', 100),
        crossover_rate=ga_raw.get('crossover_rate', 0.8),
        mutation_rate=ga_raw.get('mutation_rate', 0.1),
        elitism_count=ga_raw.get('elitism_count', 2),
        selection=selection,
        crossover=crossover,
        mutation=mutation,
        convergence_threshold=ga_raw.get('convergence_threshold', 20),
        target_fitness=ga_raw.get('target_fitness'),
        random_seed=ga_raw.get('random_seed'),
        verbose=ga_raw.get('verbose', True),
        track_statistics=ga_raw.get('track_statistics', True),
        statistics_interval=ga_raw.get('statistics_interval', 1)
    )
    
    # Parse search space
    ss_raw = raw_config.get('search_space', {})
    search_space = SearchSpace(
        pre_embedding=ss_raw.get('pre-embedding', []),
        query_expansion=ss_raw.get('query-expansion', []),
        retrieval=ss_raw.get('retrieval', []),
        passage_rerank=ss_raw.get('passage-rerank', []),
        passage_filter=ss_raw.get('passage-filter', []),
        passage_augment=ss_raw.get('passage-augment', []),
        passage_compress=ss_raw.get('passage-compress', []),
        prompt_maker=ss_raw.get('prompt-maker', []),
        generator=ss_raw.get('generator', []),
        post_generation=ss_raw.get('post-generation', [])
    )
    
    # Parse evaluation weights
    eval_raw = raw_config.get('evaluation', {})
    evaluation = EvaluationWeights(
        retrieval_weights=eval_raw.get('retrieval_weights', {}),
        generation_weights=eval_raw.get('generation_weights', {}),
        overall_weights=eval_raw.get('overall_weights', {}),
        llm_eval_model=eval_raw.get('llm_eval_model', 'gpt-oss:120B')
    )
    
    # Parse output config
    output_raw = raw_config.get('output', {})
    output = OutputConfig(
        save_best_configs=output_raw.get('save_best_configs', True),
        best_configs_file=output_raw.get('best_configs_file', 'best_rag_configs.json'),
        save_evolution_history=output_raw.get('save_evolution_history', True),
        evolution_history_file=output_raw.get('evolution_history_file', 'evolution_history.json'),
        log_level=output_raw.get('log_level', 'INFO')
    )
    
    return RAGSmithConfig(
        dataset=dataset,
        api=api,
        genetic_algorithm=genetic_algorithm,
        search_space=search_space,
        evaluation=evaluation,
        output=output
    )


def get_search_space_as_component_options(config: RAGSmithConfig) -> Dict[str, List[str]]:
    """
    Convert SearchSpace to component_options format used by RAGPipelineEvaluator.
    
    Args:
        config: RAGSmithConfig object
        
    Returns:
        Dictionary mapping component category names to lists of options
    """
    return {
        "pre-embedding": config.search_space.pre_embedding,
        "query-expansion": config.search_space.query_expansion,
        "retrieval": config.search_space.retrieval,
        "passage-rerank": config.search_space.passage_rerank,
        "passage-filter": config.search_space.passage_filter,
        "passage-augment": config.search_space.passage_augment,
        "passage-compress": config.search_space.passage_compress,
        "prompt-maker": config.search_space.prompt_maker,
        "generator": config.search_space.generator,
        "post-generation": config.search_space.post_generation,
    }


def get_api_endpoint(config: RAGSmithConfig) -> str:
    """
    Get the full API endpoint URL.
    
    Args:
        config: RAGSmithConfig object
        
    Returns:
        Full API endpoint URL
    """
    return f"http://{config.api.host}:{config.api.port}/api/evaluate"


def get_category_sizes(config: RAGSmithConfig) -> List[int]:
    """
    Get category sizes for genetic algorithm.
    
    Args:
        config: RAGSmithConfig object
        
    Returns:
        List of category sizes (number of options in each category)
    """
    component_options = get_search_space_as_component_options(config)
    return [len(options) for options in component_options.values()]


# Convenience function for quick access
_cached_config: Optional[RAGSmithConfig] = None


def get_config(config_path: Optional[str] = None, reload: bool = False) -> RAGSmithConfig:
    """
    Get the RAGSmith configuration, with caching.
    
    Args:
        config_path: Optional path to config file
        reload: Force reload of config even if cached
        
    Returns:
        RAGSmithConfig object
    """
    global _cached_config
    
    if _cached_config is None or reload:
        _cached_config = load_config(config_path)
    
    return _cached_config


if __name__ == "__main__":
    # Test loading the config
    try:
        config = load_config()
        print("✅ Configuration loaded successfully!")
        print(f"\n📁 Dataset: {config.dataset.path}")
        print(f"🌐 API: {get_api_endpoint(config)}")
        print(f"\n🧬 Genetic Algorithm:")
        print(f"   Population: {config.genetic_algorithm.population_size}")
        print(f"   Generations: {config.genetic_algorithm.generations}")
        print(f"   Crossover Rate: {config.genetic_algorithm.crossover_rate}")
        print(f"   Mutation Rate: {config.genetic_algorithm.mutation_rate}")
        
        print(f"\n🔍 Search Space:")
        component_options = get_search_space_as_component_options(config)
        for category, options in component_options.items():
            print(f"   {category}: {len(options)} options")
        
        print(f"\n📊 Total combinations: {eval('*'.join(map(str, get_category_sizes(config))))}")
        
    except Exception as e:
        print(f"❌ Error loading config: {e}")

