"""
RAG Pipeline Configuration Guide
===============================

This guide shows you TWO ways to configure and optimize your RAG pipeline:
1. Direct Genetic Algorithm usage (using our core classes)
2. Simplified pipeline approach (using run_optimization.py)

Choose the method that best fits your needs!
"""

from typing import Dict, List, Any, Callable
from run_optimization import run_rag_optimization
from config import GAConfig
from genetic_algorithm import GeneticAlgorithm
from population import Population
from individual import Individual
from selection import TournamentSelection, RouletteWheelSelection, EliteSelection
from crossover import SinglePointCrossover, UniformCrossover, MultiPointCrossover
from mutation import RandomMutation, AdaptiveMutation, CategoricalMutation
import random
import time

# ============================================================================
# STEP 1: DEFINE YOUR RAG COMPONENTS
# ============================================================================

def define_rag_components():
    """
    Define all the components available for your RAG pipeline.
    Each category represents a different aspect of your RAG system.
    """
    
    # 🎯 COMPREHENSIVE RAG COMPONENT OPTIONS
    your_rag_components = {
        
        # 📝 Text Preprocessing
        "text_preprocessor": [
            "basic_cleaning",           # Simple text cleanup
            "advanced_nlp",            # NLP-based preprocessing  
            "domain_specific",         # Custom domain processing
            "multilingual"             # Multi-language support
        ],
        
        # 🧠 Embedding Models
        "embedding_model": [
            "sentence_transformers",   # General-purpose embeddings
            "openai_ada002",          # OpenAI's embedding model
            "cohere_embed",           # Cohere embeddings
            "custom_bert",            # Fine-tuned BERT
            "e5_large"                # E5 embeddings
        ],
        
        # 🗄️ Vector Databases
        "vector_database": [
            "faiss",                  # Facebook AI Similarity Search
            "pinecone",               # Managed vector DB
            "weaviate",               # Open-source vector DB
            "chroma",                 # Simple vector store
            "qdrant"                  # High-performance vector DB
        ],
        
        # 🔍 Retrieval Strategies
        "retrieval_strategy": [
            "similarity_search",      # Basic cosine similarity
            "mmr",                   # Maximal Marginal Relevance
            "hybrid_search",         # Vector + keyword search
            "contextual_retrieval",  # Context-aware retrieval
            "multi_query"            # Multiple query variations
        ],
        
        # 📊 Ranking/Reranking
        "reranking_method": [
            "no_reranking",          # Use initial ranking
            "cross_encoder",         # Cross-encoder reranking
            "llm_reranking",         # LLM-based reranking
            "feature_based",         # Feature-based scoring
        ],
        
        # 🎭 Prompt Engineering
        "prompt_template": [
            "basic_qa",              # Simple Q&A format
            "chain_of_thought",      # CoT prompting
            "few_shot",              # Few-shot examples
            "structured_output",     # Structured response format
        ],
        
        # 🤖 Language Models
        "llm_model": [
            "gpt_3_5_turbo",         # OpenAI GPT-3.5
            "gpt_4",                 # OpenAI GPT-4
            "claude_3",              # Anthropic Claude
            "llama_2_70b",           # Meta LLaMA 2
            "gemini_pro"             # Google Gemini
        ],
        
        # ⚙️ Generation Parameters
        "generation_config": [
            "conservative",          # Low temperature, focused
            "balanced",              # Medium temperature
            "creative",              # High temperature, diverse
            "deterministic"          # Temperature = 0
        ],
        
        # 🔧 Chunk Processing
        "chunk_strategy": [
            "fixed_size",            # Fixed token chunks
            "semantic_chunking",     # Meaning-based chunks
            "sliding_window",        # Overlapping chunks
            "hierarchical"           # Multi-level chunking
        ],
        
        # 🎯 Response Processing
        "response_processing": [
            "direct_output",         # Raw LLM response
            "fact_checking",         # Verify against sources
            "citation_formatting",   # Add proper citations
            "confidence_scoring"     # Add confidence scores
        ]
    }
    
    return your_rag_components

# ============================================================================
# STEP 2: CREATE A DUMMY RAG EVALUATOR (for testing)
# ============================================================================

def create_dummy_rag_evaluator(components: Dict[str, List[str]]) -> Callable:
    """
    Create a dummy evaluator for testing purposes.
    In real usage, you'd connect to your actual RAG evaluation API.
    """
    
    # Define some "good" combinations for realistic scoring
    preferred_combinations = {
        ("embedding_model", "sentence_transformers"): 10,
        ("embedding_model", "openai_ada002"): 15,
        ("vector_database", "faiss"): 8,
        ("vector_database", "pinecone"): 12,
        ("retrieval_strategy", "hybrid_search"): 15,
        ("llm_model", "gpt_4"): 20,
        ("llm_model", "claude_3"): 18,
    }
    
    def dummy_evaluate(candidate: List[int]) -> float:
        """
        Dummy evaluation function that simulates RAG pipeline performance.
        
        Args:
            candidate: List of component indices [0, 2, 1, 4, ...]
            
        Returns:
            Simulated performance score (0-1)  # Was (0-100)
        """
        score = 0.5  # Base score (was 50.0)
        component_names = list(components.keys())
        
        # Add bonus points for "good" components
        for i, choice_index in enumerate(candidate):
            component_name = component_names[i]
            component_choice = components[component_name][choice_index]
            
            key = (component_name, component_choice)
            if key in preferred_combinations:
                score += preferred_combinations[key] * 0.01  # Convert to 0-1 scale
        
        # Add some randomness to simulate real evaluation variance
        score += random.uniform(-0.05, 0.05)  # Was (-5, 5)
        
        # Ensure score is within bounds
        score = max(0, min(1, score))  # Was min(100, score)
        
        # Simulate evaluation time
        time.sleep(0.01)
        
        return score
    
    return dummy_evaluate

# ============================================================================
# APPROACH 1: DIRECT GENETIC ALGORITHM USAGE
# ============================================================================

def direct_genetic_algorithm_example():
    """
    🔧 APPROACH 1: Direct GA Usage
    
    Use this when you want FULL CONTROL over every aspect of the genetic algorithm.
    Perfect for research, custom modifications, or when you need specific GA operators.
    """
    
    print("🔧 APPROACH 1: Direct Genetic Algorithm Usage")
    print("=" * 60)
    
    # Step 1: Define components and create evaluator
    components = define_rag_components()
    evaluate_function = create_dummy_rag_evaluator(components)
    
    # Step 2: Calculate category sizes
    category_sizes = [len(options) for options in components.values()]
    print(f"📊 Categories: {len(category_sizes)}")
    print(f"📊 Category sizes: {category_sizes}")
    
    # Step 3: Configure the Genetic Algorithm
    config = GAConfig(
        population_size=30,
        generations=50,
        crossover_rate=0.8,
        mutation_rate=0.1,
        elitism_count=3,
        selection_method=TournamentSelection(tournament_size=3),
        crossover_method=UniformCrossover(probability=0.5),
        mutation_method=AdaptiveMutation(),
        convergence_threshold=15,
        target_fitness=0.9,  # Was 90.0
        verbose=True,
        track_statistics=True
    )
    
    # Step 4: Create and run the Genetic Algorithm
    print("\n🚀 Creating Genetic Algorithm...")
    ga = GeneticAlgorithm(
        config=config,
        category_sizes=category_sizes,
        evaluate_function=evaluate_function
    )
    
    print("🔄 Running optimization...")
    results = ga.run()
    
    # Step 5: Analyze results
    print("\n🎉 Direct GA Results:")
    print("=" * 40)
    print(f"🏆 Best Fitness: {results['best_fitness']:.4f}")
    print(f"⏱️  Total Time: {results['total_time']:.2f} seconds")
    print(f"🔄 Generations: {results['generations_completed']}")
    print(f"📈 Converged: {results['converged']}")
    print(f"📊 Final Diversity: {results['final_diversity']:.3f}")
    
    # Decode the best configuration
    best_config = decode_rag_configuration(results['best_combination'], components)
    print(f"\n🎯 Best RAG Configuration:")
    for component, choice in best_config.items():
        print(f"   📌 {component}: {choice}")
    
    return results

# ============================================================================
# APPROACH 2: SIMPLIFIED PIPELINE APPROACH  
# ============================================================================

def simplified_pipeline_example():
    """
    🚀 APPROACH 2: Simplified Pipeline
    
    Use this for QUICK AND EASY optimization when you don't need to customize
    the genetic algorithm details. Perfect for production use and standard RAG optimization.
    """
    
    print("\n🚀 APPROACH 2: Simplified Pipeline Approach")
    print("=" * 60)
    
    # Step 1: Define components
    components = define_rag_components()
    
    # Step 2: Use the simplified pipeline (this would normally call your RAG API)
    print("🔍 Running simplified optimization pipeline...")
    
    # For demonstration, we'll modify run_rag_optimization to use our dummy evaluator
    # In real usage, you'd just provide your API endpoint
    
    results = run_rag_optimization(
        api_endpoint="http://dummy-endpoint.com/evaluate",  # This gets ignored in our demo
        component_options=components,
        population_size=30,
        generations=50,
        crossover_rate=0.8,
        mutation_rate=0.1,
        verbose=True,
        evaluation_function=create_dummy_rag_evaluator(components)  # Demo only
    )
    
    # Step 3: Analyze results
    print("\n🎉 Pipeline Results:")
    print("=" * 40)
    print(f"🏆 Best Performance: {results['best_fitness']:.4f}")
    print(f"⏱️  Total Time: {results['total_time']:.2f} seconds")
    print(f"🔄 Generations: {results['generations_completed']}")
    print(f"📈 Converged: {results['converged']}")
    
    # Decode the best configuration
    best_config = decode_rag_configuration(results['best_combination'], components)
    print(f"\n🎯 Best RAG Configuration:")
    for component, choice in best_config.items():
        print(f"   📌 {component}: {choice}")
    
    return results

# ============================================================================
# STEP 3: ADVANCED GA CONFIGURATIONS
# ============================================================================

def create_advanced_configurations():
    """
    Examples of different GA configurations for different scenarios.
    """
    
    configs = {}
    
    # 🚀 FAST EXPLORATION (for quick testing)
    configs["fast_exploration"] = GAConfig(
        population_size=20,
        generations=25,
        crossover_rate=0.9,           # High crossover for rapid mixing
        mutation_rate=0.2,            # High mutation for exploration
        elitism_count=2,
        selection_method=TournamentSelection(tournament_size=3),
        crossover_method=UniformCrossover(probability=0.5),
        mutation_method=AdaptiveMutation(),
        convergence_threshold=10
    )
    
    # 🎯 PRECISE OPTIMIZATION (for final tuning)
    configs["precise_optimization"] = GAConfig(
        population_size=100,
        generations=200,
        crossover_rate=0.7,           # Lower crossover for stability
        mutation_rate=0.05,           # Low mutation for fine-tuning
        elitism_count=10,             # Keep more elite solutions
        selection_method=EliteSelection(),
        crossover_method=SinglePointCrossover(),
        mutation_method=CategoricalMutation(mutation_rate=0.05, force_change=True),
        convergence_threshold=30
    )
    
    # 🌐 DIVERSE SEARCH (for exploring many options)
    configs["diverse_search"] = GAConfig(
        population_size=60,
        generations=100,
        crossover_rate=0.6,
        mutation_rate=0.15,
        elitism_count=5,
        selection_method=RouletteWheelSelection(),
        crossover_method=MultiPointCrossover(num_points=3),
        mutation_method=RandomMutation(mutation_rate=0.15),
        convergence_threshold=25
    )
    
    return configs

def demonstrate_advanced_configurations():
    """
    Show how to use different GA configurations for different optimization goals.
    """
    
    print("\n⚙️  ADVANCED CONFIGURATIONS DEMO")
    print("=" * 60)
    
    components = define_rag_components()
    evaluate_function = create_dummy_rag_evaluator(components)
    category_sizes = [len(options) for options in components.values()]
    
    configs = create_advanced_configurations()
    
    for config_name, config in configs.items():
        print(f"\n🔧 Testing {config_name}...")
        
        ga = GeneticAlgorithm(
            config=config,
            category_sizes=category_sizes,
            evaluate_function=evaluate_function
        )
        
        results = ga.run()
        
        print(f"   🏆 Best: {results['best_fitness']:.4f}")
        print(f"   ⏱️  Time: {results['total_time']:.1f}s")
        print(f"   🔄 Gens: {results['generations_completed']}")

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def decode_rag_configuration(combination: List[int], components: Dict[str, List[str]]) -> Dict[str, str]:
    """
    Convert genetic algorithm result back to readable RAG configuration.
    
    Args:
        combination: List of integers from GA (e.g., [2, 1, 4, 0, 3])
        components: Dictionary of component options
        
    Returns:
        Human-readable configuration
    """
    config = {}
    component_names = list(components.keys())
    
    for i, choice_index in enumerate(combination):
        component_name = component_names[i]
        component_options = components[component_name]
        chosen_option = component_options[choice_index]
        config[component_name] = chosen_option
    
    return config

# ============================================================================
# WHEN TO USE WHICH APPROACH
# ============================================================================

def explain_approaches():
    """
    Explain when to use each approach.
    """
    
    print("\n❓ WHEN TO USE WHICH APPROACH")
    print("=" * 60)
    
    print("\n🔧 Use DIRECT GENETIC ALGORITHM when:")
    print("   ✅ You need custom genetic operators")
    print("   ✅ You want to modify selection/crossover/mutation")
    print("   ✅ You're doing research or experiments")
    print("   ✅ You need access to population statistics")
    print("   ✅ You want to implement custom stopping criteria")
    print("   ✅ You need fine-grained control over the algorithm")
    
    print("\n🚀 Use SIMPLIFIED PIPELINE when:")
    print("   ✅ You just want to optimize your RAG pipeline")
    print("   ✅ You have a working RAG evaluation API")
    print("   ✅ You don't need to customize GA internals")
    print("   ✅ You want quick, production-ready optimization")
    print("   ✅ You're integrating with external systems")
    print("   ✅ You prefer simple function calls")

# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    
    print("🧬 RAG Pipeline Genetic Algorithm Configuration Guide")
    print("=" * 60)
    
    # Show available components
    components = define_rag_components()
    print(f"\n📋 Available RAG Components:")
    for category, options in components.items():
        print(f"   📂 {category}: {len(options)} options")
    
    # Explain the two approaches
    explain_approaches()
    
    # Demonstrate both approaches
    print(f"\n🎯 RUNNING DEMONSTRATIONS...")
    print("=" * 60)
    
    # Approach 1: Direct GA usage
    direct_results = direct_genetic_algorithm_example()
    
    # Approach 2: Simplified pipeline
    # pipeline_results = simplified_pipeline_example()  # Uncomment to run
    
    # Advanced configurations demo
    # demonstrate_advanced_configurations()  # Uncomment to run
    
    print(f"\n✅ Guide completed! Choose the approach that fits your needs.")
    print(f"📖 Read the function comments for detailed guidance!") 