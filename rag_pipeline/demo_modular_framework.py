#!/usr/bin/env python3
"""
Demo: Advanced RAG Modular Framework

This script demonstrates the new modular RAG framework by running
different configurations and comparing their performance.

Usage:
    python demo_modular_framework.py --config basic
    python demo_modular_framework.py --config advanced
    python demo_modular_framework.py --config all
"""

import asyncio
import argparse
import time
from typing import Dict, Any

from core.modular_pipeline import ModularRAGPipeline
from configs.basic_modular_config import get_basic_config, get_gemma_config, get_no_rerank_config
from configs.advanced_modular_config import get_advanced_config, get_research_config, get_fast_config


async def demo_basic_framework():
    """Demonstrate basic framework functionality"""
    
    print("🚀 Advanced RAG Modular Framework Demo")
    print("=" * 60)
    
    # Test queries
    test_queries = [
        "What is machine learning?",
        "How do neural networks work?",
        "What are the applications of AI in healthcare?"
    ]
    
    # Basic configuration
    config = get_basic_config()
    pipeline = ModularRAGPipeline(config)
    
    # Validate configuration
    print("🔧 Validating pipeline configuration...")
    validation = pipeline.validate_configuration()
    
    if not validation["valid"]:
        print("❌ Configuration validation failed:")
        for error in validation["errors"]:
            print(f"   • {error}")
        return
    
    if validation["warnings"]:
        print("⚠️ Configuration warnings:")
        for warning in validation["warnings"]:
            print(f"   • {warning}")
    
    print("✅ Configuration is valid!")
    
    # Show pipeline info
    info = pipeline.get_pipeline_info()
    print(f"\n📊 Pipeline: {info['pipeline_name']}")
    print("🔧 Enabled components:")
    for category, component in info["enabled_components"].items():
        print(f"   • {category}: {component}")
    
    # Run test queries
    print(f"\n🧪 Testing with {len(test_queries)} queries...")
    
    total_time = 0
    for i, query in enumerate(test_queries, 1):
        print(f"\n--- Query {i}/{len(test_queries)} ---")
        print(f"❓ Query: {query}")
        
        start_time = time.time()
        result = await pipeline.execute_pipeline(query)
        elapsed_time = time.time() - start_time
        total_time += elapsed_time
        
        print(f"⏱️ Execution time: {elapsed_time:.3f}s")
        print(f"🔍 Retrieved documents: {len(result.retrieved_documents)}")
        print(f"📄 Final documents: {len(result.final_documents)}")
        print(f"📝 Answer: {result.final_answer[:200]}...")
        
        # Show timing breakdown
        if result.retrieval_time > 0:
            print(f"   📊 Retrieval: {result.retrieval_time:.3f}s")
        if result.passage_rerank_time > 0:
            print(f"   🔄 Reranking: {result.passage_rerank_time:.3f}s")
        if result.prompt_maker_time > 0:
            print(f"   📝 Prompt: {result.prompt_maker_time:.3f}s")
        if result.generation_time > 0:
            print(f"   🤖 Generation: {result.generation_time:.3f}s")
    
    print(f"\n✅ Demo completed! Total time: {total_time:.3f}s")
    print(f"⏱️ Average time per query: {total_time/len(test_queries):.3f}s")


async def demo_configuration_comparison():
    """Compare different configurations"""
    
    print("🔬 Configuration Comparison Demo")
    print("=" * 60)
    
    # Different configurations to test
    configs = {
        "Basic": get_basic_config(),
        "Basic (No Rerank)": get_no_rerank_config(),
        "Basic (Gemma)": get_gemma_config(),
        "Advanced": get_advanced_config(),
        "Fast": get_fast_config(),
    }
    
    test_query = "What are the main types of machine learning algorithms?"
    
    results = {}
    
    for name, config in configs.items():
        print(f"\n🧪 Testing: {name}")
        print("-" * 40)
        
        try:
            # Create pipeline
            pipeline = ModularRAGPipeline(config)
            
            # Validate
            validation = pipeline.validate_configuration()
            if not validation["valid"]:
                print(f"❌ Invalid configuration: {validation['errors']}")
                continue
            
            # Get info
            info = pipeline.get_pipeline_info()
            components = list(info["enabled_components"].keys())
            print(f"🔧 Components: {', '.join(components)}")
            
            # Execute
            start_time = time.time()
            result = await pipeline.execute_pipeline(test_query)
            total_time = time.time() - start_time
            
            # Store results
            results[name] = {
                "time": total_time,
                "components": len(components),
                "retrieved_docs": len(result.retrieved_documents),
                "final_docs": len(result.final_documents),
                "answer_length": len(result.final_answer),
                "answer": result.final_answer[:100] + "..."
            }
            
            print(f"⏱️ Time: {total_time:.3f}s")
            print(f"📊 Docs: {len(result.retrieved_documents)} → {len(result.final_documents)}")
            print(f"📝 Answer ({len(result.final_answer)} chars): {result.final_answer[:100]}...")
            
        except Exception as e:
            print(f"❌ Error: {e}")
            results[name] = {"error": str(e)}
    
    # Summary comparison
    print(f"\n📊 COMPARISON SUMMARY")
    print("=" * 60)
    print(f"{'Configuration':<20} {'Time (s)':<10} {'Components':<12} {'Final Docs':<12} {'Answer Length'}")
    print("-" * 70)
    
    for name, data in results.items():
        if "error" in data:
            print(f"{name:<20} {'ERROR':<10} {'-':<12} {'-':<12} {'-'}")
        else:
            print(f"{name:<20} {data['time']:<10.3f} {data['components']:<12} {data['final_docs']:<12} {data['answer_length']}")
    
    # Find fastest and most comprehensive
    valid_results = {k: v for k, v in results.items() if "error" not in v}
    if valid_results:
        fastest = min(valid_results.items(), key=lambda x: x[1]["time"])
        most_docs = max(valid_results.items(), key=lambda x: x[1]["final_docs"])
        longest_answer = max(valid_results.items(), key=lambda x: x[1]["answer_length"])
        
        print(f"\n🏆 WINNERS:")
        print(f"⚡ Fastest: {fastest[0]} ({fastest[1]['time']:.3f}s)")
        print(f"📚 Most comprehensive: {most_docs[0]} ({most_docs[1]['final_docs']} docs)")
        print(f"📝 Most detailed: {longest_answer[0]} ({longest_answer[1]['answer_length']} chars)")


async def demo_technique_showcase():
    """Showcase individual techniques"""
    
    print("🎯 Technique Showcase Demo")
    print("=" * 60)
    
    from core.modular_configs import ModularRAGConfig, RetrievalConfig, PassageRerankConfig, PassageFilterConfig, PromptMakerConfig, GeneratorConfig
    
    # Show impact of different techniques
    test_query = "Explain deep learning"
    
    # Base configuration
    base_config = ModularRAGConfig(
        retrieval=RetrievalConfig(
            enabled=True,
            techniques=["simple_vector_rag"],
            top_k=10
        ),
        prompt_maker=PromptMakerConfig(
            enabled=True,
            technique="simple_listing"
        ),
        generator=GeneratorConfig(
            enabled=True,
            model="gemini-2.0-flash",
            provider="gemini"
        )
    )
    
    # Test configurations
    test_configs = {
        "No Reranking": base_config,
        "With Cross-Encoder": ModularRAGConfig(
            **base_config.dict(),
            passage_rerank=PassageRerankConfig(
                enabled=True,
                techniques=["cross_encoder"]
            )
        ),
        "With Filtering": ModularRAGConfig(
            **base_config.dict(),
            passage_filter=PassageFilterConfig(
                enabled=True,
                techniques=["similarity_threshold"],
                similarity_threshold=0.7
            )
        )
    }
    
    for name, config in test_configs.items():
        print(f"\n🔬 Testing: {name}")
        print("-" * 30)
        
        try:
            pipeline = ModularRAGPipeline(config)
            result = await pipeline.execute_pipeline(test_query)
            
            print(f"📊 Retrieved: {len(result.retrieved_documents)} docs")
            print(f"📄 Final: {len(result.final_documents)} docs")
            print(f"⏱️ Time: {result.total_time:.3f}s")
            print(f"🔧 Components: {list(result.components_used.keys())}")
            
        except Exception as e:
            print(f"❌ Error: {e}")


def main():
    """Main demo function"""
    
    parser = argparse.ArgumentParser(description="Advanced RAG Modular Framework Demo")
    parser.add_argument(
        "--config", 
        choices=["basic", "advanced", "comparison", "techniques", "all"],
        default="basic",
        help="Which demo to run"
    )
    
    args = parser.parse_args()
    
    if args.config == "basic":
        asyncio.run(demo_basic_framework())
    elif args.config == "advanced":
        asyncio.run(demo_configuration_comparison())
    elif args.config == "comparison":
        asyncio.run(demo_configuration_comparison())
    elif args.config == "techniques":
        asyncio.run(demo_technique_showcase())
    elif args.config == "all":
        print("🚀 Running all demos...\n")
        asyncio.run(demo_basic_framework())
        print("\n" + "="*80 + "\n")
        asyncio.run(demo_configuration_comparison())
        print("\n" + "="*80 + "\n")
        asyncio.run(demo_technique_showcase())


if __name__ == "__main__":
    main() 