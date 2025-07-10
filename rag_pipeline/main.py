#!/usr/bin/env python3
"""
RAG Pipeline - Clean evaluation pipeline for Retrieval-Augmented Generation

This refactored version provides:
- Clean separation between retrieval and generation components  
- Proper testing of all embedding model × LLM model combinations
- Extensible architecture for adding new RAG techniques
- Comprehensive evaluation metrics
- Efficient batch processing
"""

import asyncio
import logging
import time
from typing import List, Optional

from core import RAGPipeline, RAGConfig

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def run_rag_evaluation():
    """Run RAG evaluation with multiple model combinations"""
    
    # Configuration for RAG evaluation
    config = RAGConfig(
        # Models to test
        embedding_models=[
            "nomic-embed-text", 
            "mxbai-embed-large"
        ],
        llm_models=[
            "llama3.2:1b",
            "gemma3:4b"
        ],
        eval_llm_model="gemma3:12b",  # Model used for LLM-based evaluation
        
        # Retrieval settings
        retrieval_k=10,
        retrieval_threshold=0.5,
        
        # Cross-encoder reranking settings (optional)
        rerank_model="BAAI/bge-reranker-v2-m3",  # Set to None to disable cross-encoder reranking
        rerank_top_k=5,  # Keep top 5 after cross-encoder reranking
        test_with_and_without_reranking=True,  # Test both with and without cross-encoder reranking
        rerank_cache_dir=None,  # Use default cache directory
        rerank_force_cpu=False,  # Use GPU if available
        
        # LLM reranking settings (optional)
        llm_rerank_model="gemma3:4b",  # Set to None to disable LLM reranking
        llm_rerank_top_k=5,  # Keep top 5 after LLM reranking
        test_with_and_without_llm_reranking=True,  # Test both with and without LLM reranking
        llm_rerank_max_tokens=2048,  # Max tokens for LLM reranking
        llm_rerank_temperature=0.1,  # Temperature for LLM reranking
        
        # Generation settings
        max_tokens=500,
        temperature=0.1,
        
        # Evaluation settings
        eval_batch_size=5,  # Process 5 test cases at a time
        max_test_cases=100,  
        
        # Dataset settings
        dataset_path=None, 
        
        # Parallel reranking settings
        enable_parallel_reranking=True,  # Enable parallel reranking
        rerank_ensemble_method="weighted",  # Use weighted ensemble
        ce_rerank_weight=0.7,  # Higher weight for cross-encoder
        llm_rerank_weight=0.3,  # Lower weight for LLM
    )
    
    # Create and run pipeline
    pipeline = RAGPipeline(config)
    
    try:
        logger.info("Starting RAG evaluation...")
        start_time = time.time()
        
        # Run evaluation
        results = await pipeline.run_evaluation()
        
        # Print detailed results
        pipeline.print_results_summary(results)
        
        # Save results to file (optional)
        await save_results(results)
        
        logger.info(f"Evaluation completed in {time.time() - start_time:.2f}s")
        return results
        
    except Exception as e:
        logger.error(f"Evaluation failed: {e}")
        import traceback
        logger.error(traceback.format_exc())
        raise

async def save_results(results, filename: Optional[str] = None):
    """Save evaluation results to JSON file"""
    import json
    from datetime import datetime
    
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"rag_evaluation_results_{timestamp}.json"
    
    try:
        # Convert results to dict for JSON serialization
        results_dict = results.model_dump()
        
        with open(filename, 'w') as f:
            json.dump(results_dict, f, indent=2, default=str)
        
        logger.info(f"Results saved to {filename}")
        
    except Exception as e:
        logger.warning(f"Failed to save results: {e}")

def run_super_quick_test():
    """Run a super quick test to verify pipeline works (30 seconds max)"""
    
    logger.info("Running super quick test...")
    
    config = RAGConfig(
        embedding_models=["nomic-embed-text"],  # Only 1 embedding model
        llm_models=["llama3.2:1b"],             # Only fastest LLM model
        eval_llm_model="llama3.2:1b",          # Use fastest model for evaluation
        retrieval_k=2,                         # Only 2 retrieved docs
        rerank_model=None,                     # Disable reranking for speed
        test_with_and_without_reranking=False, # Not applicable when rerank_model is None
        rerank_cache_dir=None,                 # Use default cache directory
        rerank_force_cpu=False,                # Use GPU if available
        eval_batch_size=1,                     # Process 1 at a time
        max_test_cases=1,                      # Only test 1 case
        
        # Parallel reranking settings
        enable_parallel_reranking=False,
        rerank_ensemble_method="weighted",
        ce_rerank_weight=0.7,
        llm_rerank_weight=0.3,
    )
    
    pipeline = RAGPipeline(config)
    return asyncio.run(pipeline.run_evaluation())

def run_quick_test():
    """Run a quick test with minimal models and test cases"""
    
    logger.info("Running quick test...")
    
    config = RAGConfig(
        embedding_models=["nomic-embed-text"],  # Only 1 embedding model
        llm_models=["llama3.2:1b"],             # Only 1 LLM model (fastest)
        eval_llm_model="llama3.2:1b",          # Use fastest model for evaluation
        retrieval_k=5,                         # Fewer retrieved docs
        rerank_model="BAAI/bge-reranker-v2-m3", # Enable cross-encoder reranking for testing
        test_with_and_without_reranking=True,  # Test both with and without cross-encoder reranking
        rerank_cache_dir=None,                 # Use default cache directory
        rerank_force_cpu=False,                # Use GPU if available
        llm_rerank_model="gemma3:4b",       # Enable LLM reranking for testing
        test_with_and_without_llm_reranking=True,  # Test both with and without LLM reranking
        eval_batch_size=1,                     # Smaller batches
        max_test_cases=2,                      # Only test first 2 cases
        
        # Parallel reranking settings
        enable_parallel_reranking=True,
        rerank_ensemble_method="weighted",
        ce_rerank_weight=0.7,
        llm_rerank_weight=0.3,
    )
    
    pipeline = RAGPipeline(config)
    return asyncio.run(pipeline.run_evaluation())

def main():
    """Main entry point"""
    
    import sys
    
    # Print usage if no arguments
    # if len(sys.argv) == 1:
    #     print("Usage:")
    #     print("  python main.py --super-quick  # Test 1 case, 1 model combo (~30s)")
    #     print("  python main.py --quick       # Test 2 cases, 1 model combo (~1-2min)")
    #     print("  python main.py --full        # Test all cases, all model combos (~10min)")
    #     return 0
    
    # Check command line arguments
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        
        if arg == "--super-quick":
            # Super quick test mode (30 seconds)
            try:
                results = run_super_quick_test()
                print(f"\n⚡ Super quick test completed successfully!")
                print(f"Best combination: {results.best_overall_combo}")
                print(f"Pipeline is working correctly!")
            except Exception as e:
                print(f"❌ Super quick test failed: {e}")
                return 1
                
        elif arg == "--quick":
            # Quick test mode (1-2 minutes)
            try:
                results = run_quick_test()
                print(f"\n✅ Quick test completed successfully!")
                print(f"Best combination: {results.best_overall_combo}")
            except Exception as e:
                print(f"❌ Quick test failed: {e}")
                return 1
                
        else:
            # Full evaluation mode (10+ minutes)
            try:
                results = asyncio.run(run_rag_evaluation())
                print(f"\n🎉 Full evaluation completed successfully!")
                print(f"Best overall combination: {results.best_overall_combo}")
            except Exception as e:
                print(f"❌ Evaluation failed: {e}")
                return 1
    return 0

if __name__ == "__main__":
    exit_code = main()