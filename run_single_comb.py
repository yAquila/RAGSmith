#!/usr/bin/env python3
"""
Run evaluation for a single RAG pipeline configuration.

This script sends an evaluation request to the RAG Evaluation API
for testing specific combinations of RAG techniques.

Usage:
    python run_single_comb.py [OPTIONS]

Examples:
    # Run with default configuration
    python run_single_comb.py

    # Run with custom generator
    python run_single_comb.py --generator "generator_gemma3:27b"

    # Run with hybrid retrieval and reranking
    python run_single_comb.py --retrieval "retrieval-hybrid_vector_keyword_cc" \
                              --passage-rerank "passage-rerank_ce_rerank_bge"

    # Run against a remote server
    python run_single_comb.py --host "192.168.1.100" --port 8060

    # List all available options
    python run_single_comb.py --list-options
"""

import argparse
import json
import sys
import requests
from typing import Dict, Any, Optional


# Available configuration options for each stage
AVAILABLE_OPTIONS = {
    "pre-embedding": [
        "pre-embedding_none",
        "pre-embedding_contextual_chunk_headers",
        "pre-embedding_hype",
        "pre-embedding_parent_document_retriever",
    ],
    "query-expansion": [
        "query-expansion_none",
        "query-expansion_simple_multi_query_cc_dbsf",
        "query-expansion_simple_multi_query_borda",
        "query-expansion_rag_fusion",
        "query-expansion_decomposition_cc",
        "query-expansion_hyde_cc",
        "query-expansion_step_back_prompting_cc",
        "query-expansion_graph_as_qe_cc",
        "query-expansion_refinement_clarification",
        "query-expansion_refinement_rephrasing",
    ],
    "retrieval": [
        "retrieval-vector_mxbai",
        "retrieval-keyword_bm25",
        "retrieval-graph_rag",
        "retrieval-hypergraph_rag",
        "retrieval-hybrid_vector_keyword_cc",
        "retrieval-hybrid_vector_graph_simply",
        "retrieval-hybrid_graph_hypergraph_simply",
        "retrieval-hybrid_vector_graph_hypergraph_simply",
        "retrieval-hybrid_vector_keyword_graph_simply",
        "retrieval-hybrid_vector_keyword_hypergraph_simply",
        "retrieval-hybrid_vector_keyword_graph_hypergraph_simply",
    ],
    "passage-rerank": [
        "passage-rerank_none",
        "passage-rerank_ce_rerank_bge",
        "passage-rerank_llm_rerank_gemma",
        "passage-rerank_cellm_parallel_rerank",
    ],
    "passage-filter": [
        "passage-filter_simple_threshold",
        "passage-filter_similarity_threshold",
    ],
    "passage-augment": [
        "passage-augment_none",
        "passage-augment_prev_next_augmenter",
        "passage-augment_relevant_segment_extractor",
    ],
    "passage-compress": [
        "passage-compress_none",
        "passage-compress_llm_summarize",
        "passage-compress_tree_summarize",
    ],
    "prompt-maker": [
        "prompt-maker_simple_listing",
        "prompt-maker_long_context_reorder_1",
        "prompt-maker_long_context_reorder_2",
    ],
    "generator": [
        "generator_gemma3:27b",
        "generator_alibayram/Qwen3-30B-A3B-Instruct-2507:latest",
        "generator_multi_llm_gemma3:27b-alibayram/Qwen3-30B-A3B-Instruct-2507:latest-Ensemble:alibayram/Qwen3-30B-A3B-Instruct-2507:latest",
    ],
    "post-generation": [
        "post-generation_none",
        "post-generation_reflection_revising",
    ],
}

# Default configuration (matches README example)
DEFAULT_CONFIG = {
    "pre-embedding": "pre-embedding_none",
    "query-expansion": "query-expansion_none",
    "retrieval": "retrieval-vector_mxbai",
    "passage-rerank": "passage-rerank_none",
    "passage-filter": "passage-filter_simple_threshold",
    "passage-augment": "passage-augment_none",
    "passage-compress": "passage-compress_none",
    "prompt-maker": "prompt-maker_simple_listing",
    "generator": "generator_alibayram/Qwen3-30B-A3B-Instruct-2507:latest",
    "post-generation": "post-generation_none",
}


def list_available_options():
    """Print all available configuration options."""
    print("\n" + "=" * 60)
    print("AVAILABLE CONFIGURATION OPTIONS")
    print("=" * 60)
    
    for stage, options in AVAILABLE_OPTIONS.items():
        print(f"\n{stage}:")
        for option in options:
            default_marker = " (default)" if option == DEFAULT_CONFIG[stage] else ""
            print(f"  - {option}{default_marker}")
    
    print("\n" + "=" * 60)


def validate_config(config: Dict[str, str]) -> bool:
    """Validate that all config values are valid options."""
    is_valid = True
    
    for stage, value in config.items():
        if stage not in AVAILABLE_OPTIONS:
            print(f"❌ Unknown stage: {stage}")
            is_valid = False
            continue
            
        if value not in AVAILABLE_OPTIONS[stage]:
            print(f"❌ Invalid option for {stage}: {value}")
            print(f"   Available options: {', '.join(AVAILABLE_OPTIONS[stage])}")
            is_valid = False
    
    return is_valid


def run_evaluation(
    config: Dict[str, str],
    host: str = "localhost",
    port: int = 8060,
    timeout: int = 600
) -> Optional[Dict[str, Any]]:
    """
    Send evaluation request to the RAG Evaluation API.
    
    Args:
        config: Pipeline configuration dictionary
        host: API host address
        port: API port number
        timeout: Request timeout in seconds
        
    Returns:
        Response dictionary or None if request failed
    """
    url = f"http://{host}:{port}/api/evaluate"
    
    payload = {
        "evaluation_request": {
            "pipeline_config": config
        }
    }
    
    print("\n" + "=" * 60)
    print("RAG PIPELINE EVALUATION")
    print("=" * 60)
    print(f"\n📡 API Endpoint: {url}")
    print("\n📋 Pipeline Configuration:")
    for stage, technique in config.items():
        print(f"   {stage}: {technique}")
    
    print("\n⏳ Running evaluation... (this may take a few minutes)")
    print("-" * 60)
    
    try:
        response = requests.post(
            url,
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=timeout
        )
        
        response.raise_for_status()
        result = response.json()
        
        print("\n✅ Evaluation completed successfully!")
        print("-" * 60)
        
        if "evaluation" in result:
            evaluation = result["evaluation"]
            final_score = evaluation.get("final_score", "N/A")
            
            print(f"\n🎯 FINAL SCORE: {final_score}")
            
            # Print additional metrics if available
            if "retrieval_metrics" in evaluation:
                print("\n📊 Retrieval Metrics:")
                for metric, value in evaluation["retrieval_metrics"].items():
                    print(f"   {metric}: {value}")
            
            if "generation_metrics" in evaluation:
                print("\n📊 Generation Metrics:")
                for metric, value in evaluation["generation_metrics"].items():
                    print(f"   {metric}: {value}")
        
        print("\n" + "=" * 60)
        print("Full Response:")
        print(json.dumps(result, indent=2))
        print("=" * 60)
        
        return result
        
    except requests.exceptions.ConnectionError:
        print(f"\n❌ Connection Error: Could not connect to {url}")
        print("   Make sure the RAG Evaluation API server is running.")
        print("   Start it with: docker-compose up -d rag_pipeline")
        return None
        
    except requests.exceptions.Timeout:
        print(f"\n❌ Timeout Error: Request timed out after {timeout} seconds.")
        print("   Try increasing the timeout with --timeout option.")
        return None
        
    except requests.exceptions.HTTPError as e:
        print(f"\n❌ HTTP Error: {e}")
        if response.text:
            print(f"   Response: {response.text}")
        return None
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Run evaluation for a single RAG pipeline configuration.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_single_comb.py
  python run_single_comb.py --generator "generator_gemma3:27b"
  python run_single_comb.py --retrieval "retrieval-hybrid_vector_keyword_cc"
  python run_single_comb.py --list-options
        """
    )
    
    # Server configuration
    parser.add_argument(
        "--host", 
        type=str, 
        default="localhost",
        help="API host address (default: localhost)"
    )
    parser.add_argument(
        "--port", 
        type=int, 
        default=8060,
        help="API port number (default: 8060)"
    )
    parser.add_argument(
        "--timeout", 
        type=int, 
        default=3600,
        help="Request timeout in seconds (default: 600)"
    )
    
    # Utility options
    parser.add_argument(
        "--list-options", 
        action="store_true",
        help="List all available configuration options and exit"
    )
    parser.add_argument(
        "--validate-only", 
        action="store_true",
        help="Only validate the configuration without running evaluation"
    )
    
    # Pipeline configuration stages
    parser.add_argument(
        "--pre-embedding", 
        type=str, 
        default=DEFAULT_CONFIG["pre-embedding"],
        help=f"Pre-embedding technique (default: {DEFAULT_CONFIG['pre-embedding']})"
    )
    parser.add_argument(
        "--query-expansion", 
        type=str, 
        default=DEFAULT_CONFIG["query-expansion"],
        help=f"Query expansion technique (default: {DEFAULT_CONFIG['query-expansion']})"
    )
    parser.add_argument(
        "--retrieval", 
        type=str, 
        default=DEFAULT_CONFIG["retrieval"],
        help=f"Retrieval technique (default: {DEFAULT_CONFIG['retrieval']})"
    )
    parser.add_argument(
        "--passage-rerank", 
        type=str, 
        default=DEFAULT_CONFIG["passage-rerank"],
        help=f"Passage reranking technique (default: {DEFAULT_CONFIG['passage-rerank']})"
    )
    parser.add_argument(
        "--passage-filter", 
        type=str, 
        default=DEFAULT_CONFIG["passage-filter"],
        help=f"Passage filtering technique (default: {DEFAULT_CONFIG['passage-filter']})"
    )
    parser.add_argument(
        "--passage-augment", 
        type=str, 
        default=DEFAULT_CONFIG["passage-augment"],
        help=f"Passage augmentation technique (default: {DEFAULT_CONFIG['passage-augment']})"
    )
    parser.add_argument(
        "--passage-compress", 
        type=str, 
        default=DEFAULT_CONFIG["passage-compress"],
        help=f"Passage compression technique (default: {DEFAULT_CONFIG['passage-compress']})"
    )
    parser.add_argument(
        "--prompt-maker", 
        type=str, 
        default=DEFAULT_CONFIG["prompt-maker"],
        help=f"Prompt maker technique (default: {DEFAULT_CONFIG['prompt-maker']})"
    )
    parser.add_argument(
        "--generator", 
        type=str, 
        default=DEFAULT_CONFIG["generator"],
        help=f"Generator model (default: {DEFAULT_CONFIG['generator']})"
    )
    parser.add_argument(
        "--post-generation", 
        type=str, 
        default=DEFAULT_CONFIG["post-generation"],
        help=f"Post-generation technique (default: {DEFAULT_CONFIG['post-generation']})"
    )
    
    args = parser.parse_args()
    
    # Handle --list-options
    if args.list_options:
        list_available_options()
        return 0
    
    # Build configuration from arguments
    config = {
        "pre-embedding": args.pre_embedding,
        "query-expansion": args.query_expansion,
        "retrieval": args.retrieval,
        "passage-rerank": args.passage_rerank,
        "passage-filter": args.passage_filter,
        "passage-augment": args.passage_augment,
        "passage-compress": args.passage_compress,
        "prompt-maker": args.prompt_maker,
        "generator": args.generator,
        "post-generation": args.post_generation,
    }
    
    # Validate configuration
    if not validate_config(config):
        print("\n❌ Configuration validation failed.")
        print("   Use --list-options to see available options.")
        return 1
    
    if args.validate_only:
        print("\n✅ Configuration is valid.")
        return 0
    
    # Run evaluation
    result = run_evaluation(
        config=config,
        host=args.host,
        port=args.port,
        timeout=args.timeout
    )
    
    if result is None:
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

