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
            #"nomic-embed-text", 
            "mxbai-embed-large"
        ],
        llm_models=[
            "gemini-2.0-flash",
            "gemma3:4b"
        ],
        eval_llm_model="gemini-2.0-flash",  # Model used for LLM-based evaluation
        
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
        # llm_rerank_model="gemma3:4b",  # Set to None to disable LLM reranking
        # llm_rerank_top_k=5,  # Keep top 5 after LLM reranking
        # test_with_and_without_llm_reranking=True,  # Test both with and without LLM reranking
        # llm_rerank_max_tokens=2048,  # Max tokens for LLM reranking
        # llm_rerank_temperature=0.1,  # Temperature for LLM reranking
        
        # Generation settings
        max_tokens=500,
        temperature=0.1,
        
        # Evaluation settings
        eval_batch_size=5,  # Process 5 test cases at a time
        max_test_cases=5,  
        
        # Dataset settings
        dataset_path=None, 
        
        # Parallel reranking settings
        # enable_parallel_reranking=True,  # Enable parallel reranking
        # rerank_ensemble_method="weighted",  # Use weighted ensemble
        # ce_rerank_weight=0.7,  # Higher weight for cross-encoder
        # llm_rerank_weight=0.3,  # Lower weight for LLM
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
        
        # Save results to markdown file
        await save_markdown_results(results)
        
        logger.info(f"Evaluation completed in {time.time() - start_time:.2f}s")
        return results
        
    except Exception as e:
        logger.error(f"Evaluation failed: {e}")
        import traceback
        logger.error(traceback.format_exc())
        raise

async def save_markdown_results(results, filename: Optional[str] = None):
    """Save evaluation results to Markdown file"""
    from datetime import datetime
    
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"rag_evaluation_results_{timestamp}.md"
    
    try:
        markdown_content = generate_markdown_report(results)
        
        with open(filename, 'w') as f:
            f.write(markdown_content)
        
        logger.info(f"Results saved to {filename}")
        
    except Exception as e:
        logger.warning(f"Failed to save results: {e}")


def generate_markdown_report(results) -> str:
    """Generate markdown report from RAGBenchmarkResult"""
    from datetime import datetime
    
    # Header
    markdown = """# RAG EVALUATION RESULTS

"""
    
    # Basic info
    total_test_cases = results.total_test_cases
    successful_cases = results.successful_cases
    total_results = len(results.individual_results)
    total_runtime = results.total_runtime
    
    markdown += f"**Dataset:** {total_test_cases} test cases  \n"
    markdown += f"**Success rate:** {successful_cases}/{total_results} ({successful_cases/total_results*100:.1f}%)  \n"
    markdown += f"**Total runtime:** {total_runtime:.2f}s\n\n"
    
    # Model combinations
    aggregated_metrics = results.aggregated_metrics
    markdown += f"**Model combinations tested:** {len(aggregated_metrics)}\n"
    markdown += _format_model_combinations_list(aggregated_metrics)
    markdown += "\n\n"
    
    # Best performing combinations
    markdown += "## 🏆 BEST PERFORMING COMBINATIONS:\n\n"
    best_retrieval = results.best_retrieval_combo or 'N/A'
    best_generation = results.best_generation_combo or 'N/A'
    best_overall = results.best_overall_combo or 'N/A'
    
    markdown += f"**Retrieval:** {best_retrieval}  \n"
    markdown += f"**Generation:** {best_generation}  \n"
    markdown += f"**Overall:** {best_overall}\n\n"
    
    # Detailed metrics
    markdown += "## 📊 DETAILED METRICS BY COMBINATION:\n"
    markdown += _format_detailed_metrics(aggregated_metrics)
    markdown += "\n\n"
    
    # Timing breakdown
    total_retr_pred_time = results.total_retrieval_prediction_time
    total_gen_pred_time = results.total_generation_prediction_time
    total_retr_eval_time = results.total_retrieval_evaluation_time
    total_gen_eval_time = results.total_generation_evaluation_time
    
    total_prediction_time = total_retr_pred_time + total_gen_pred_time
    total_evaluation_time = total_retr_eval_time + total_gen_eval_time
    
    markdown += "## ⏱️ TIMING BREAKDOWN:\n\n"
    markdown += "**Prediction Times:**\n"
    markdown += f"  - Retrieval: {total_retr_pred_time:.2f}s\n"
    markdown += f"  - Generation: {total_gen_pred_time:.2f}s\n"
    markdown += f"  - Total Prediction: {total_prediction_time:.2f}s\n\n"
    
    markdown += "**Evaluation Times:**\n"
    markdown += f"  - Retrieval: {total_retr_eval_time:.2f}s\n"
    markdown += f"  - Generation: {total_gen_eval_time:.2f}s\n"
    markdown += f"  - Total Evaluation: {total_evaluation_time:.2f}s\n\n"
    
    markdown += f"**Pipeline Total:** {total_runtime:.2f}s\n\n"
    
    # Footer
    markdown += "---\n\n"
    markdown += f"*Report generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n"
    
    return markdown


def _format_model_combinations_list(aggregated_metrics) -> str:
    """Format the list of model combinations tested."""
    lines = []
    for combo in aggregated_metrics.keys():
        # Parse combination key that may include multiple rerank models (using || delimiter)
        combo_parts = combo.split('||')
        if len(combo_parts) == 2:
            # Format: embedding_model||llm_model (no reranking)
            emb_model, llm_model = combo_parts
            lines.append(f"  • {emb_model} + {llm_model}")
        elif len(combo_parts) == 3:
            # Format: embedding_model||rerank_model||llm_model (single reranking)
            emb_model, rerank_model, llm_model = combo_parts
            lines.append(f"  • {emb_model} + {rerank_model} + {llm_model}")
        elif len(combo_parts) == 4:
            # Format: embedding_model||ce_rerank||llm_rerank||llm_model (dual reranking)
            emb_model, ce_rerank, llm_rerank, llm_model = combo_parts
            lines.append(f"  • {emb_model} + {ce_rerank} + {llm_rerank} + {llm_model}")
        else:
            # Fallback for unexpected format
            lines.append(f"  • {combo.replace('||', ' + ')}")
    
    return "\n".join(lines)


def _format_detailed_metrics(aggregated_metrics) -> str:
    """Format detailed metrics for each combination."""
    lines = []
    
    for combo, metrics in aggregated_metrics.items():
        # Parse combination key for display
        combo_parts = combo.split('||')
        if len(combo_parts) == 2:
            # Format: embedding_model||llm_model (no reranking)
            emb_model, llm_model = combo_parts
            combo_display = f"{emb_model} + {llm_model}"
        elif len(combo_parts) == 3:
            # Format: embedding_model||rerank_model||llm_model (single reranking)
            emb_model, rerank_model, llm_model = combo_parts
            combo_display = f"{emb_model} + {rerank_model} + {llm_model}"
        elif len(combo_parts) == 4:
            # Format: embedding_model||ce_rerank||llm_rerank||llm_model (dual reranking)
            emb_model, ce_rerank, llm_rerank, llm_model = combo_parts
            combo_display = f"{emb_model} + {ce_rerank} + {llm_rerank} + {llm_model}"
        else:
            # Fallback for unexpected format
            combo_display = combo.replace('||', ' + ')
        
        lines.append(f"\n**{combo_display}:**")
        
        # Retrieval metrics
        eval_k = metrics.get('eval_k', 10)
        recall = metrics.get('recall_at_k', 0.0)
        map_score = metrics.get('map_score', 0.0)
        ndcg = metrics.get('ndcg_at_k', 0.0)
        mrr = metrics.get('mrr', 0.0)
        lines.append(f"  Retrieval: R@{eval_k}={recall:.3f}, mAP={map_score:.3f}, nDCG@{eval_k}={ndcg:.3f}, MRR={mrr:.3f}")
        
        # Reranking info
        if metrics.get('reranked', False):
            rerank_model = metrics.get('rerank_model', 'N/A')
            rerank_time = metrics.get('rerank_time', 0.0)
            lines.append(f"  Cross-encoder Reranking: Model={rerank_model}, Avg Time={rerank_time:.3f}s")
        
        if metrics.get('llm_reranked', False):
            llm_rerank_model = metrics.get('llm_rerank_model', 'N/A')
            llm_rerank_time = metrics.get('llm_rerank_time', 0.0)
            lines.append(f"  LLM Reranking: Model={llm_rerank_model}, Avg Time={llm_rerank_time:.3f}s")
        
        # Generation metrics
        llm_score = metrics.get('llm_score', 0.0)
        semantic_sim = metrics.get('semantic_similarity', 0.0)
        lines.append(f"  Generation: LLM={llm_score:.3f}, Semantic={semantic_sim:.3f}")
        
        # Component and overall scores
        retrieval_score = metrics.get('retrieval_score', 0.0)
        generation_score = metrics.get('generation_score', 0.0)
        overall_score = metrics.get('overall_score', 0.0)
        lines.append(f"  Component Scores: Retrieval={retrieval_score:.3f}, Generation={generation_score:.3f}")
        lines.append(f"  Overall Score: {overall_score:.3f}")
        
        # Success rate
        success_rate = metrics.get('success_rate', 0.0)
        lines.append(f"  Success Rate: {success_rate:.1%}")
        
        # Timing info
        retr_pred_time = metrics.get('retrieval_prediction_time', 0.0)
        gen_pred_time = metrics.get('generation_prediction_time', 0.0)
        lines.append(f"  Avg Prediction Times: Retrieval={retr_pred_time:.3f}s, Generation={gen_pred_time:.3f}s")
        
        # Rerank timing
        if metrics.get('reranked', False) or metrics.get('llm_reranked', False):
            rerank_time_str = ""
            if metrics.get('reranked', False):
                rerank_time_str += f"CE: {metrics.get('rerank_time', 0.0):.3f}s"
            if metrics.get('llm_reranked', False):
                if rerank_time_str:
                    rerank_time_str += ", "
                rerank_time_str += f"LLM: {metrics.get('llm_rerank_time', 0.0):.3f}s"
            lines.append(f"  Avg Rerank Times: {rerank_time_str}")
        
        # Evaluation timing
        retr_eval_time = metrics.get('retrieval_evaluation_time', 0.0)
        gen_eval_time = metrics.get('generation_evaluation_time', 0.0)
        lines.append(f"  Avg Evaluation Times: Retrieval={retr_eval_time:.3f}s, Generation={gen_eval_time:.3f}s")
    
    return "\n".join(lines)

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
    time.sleep(1000000)
    return 0

if __name__ == "__main__":
    exit_code = main()