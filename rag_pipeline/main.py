#!/usr/bin/env python3
"""
RAG Pipeline - Clean evaluation pipeline for Retrieval-Augmented Generation

This refactored version provides:
- Clean separation between retrieval and generation components  
- Proper testing of all embedding model × LLM model combinations
- Extensible architecture for adding new RAG techniques
- Comprehensive evaluation metrics
- Efficient batch processing

Configuration can be loaded from gen_search_config.yml in the project root.
"""

import asyncio
import logging
import time
import sys
import os
from typing import List, Optional, Dict, Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

from rag_pipeline.core import ModularRAGPipeline, ModularRAGConfig
from rag_pipeline.util.misc.config_map import CONFIG_MAP

# Add parent directory to path for config_loader import
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# Global variable to store loaded YAML config
_yaml_config = None


def load_yaml_config():
    """Load configuration from gen_search_config.yml"""
    global _yaml_config
    if _yaml_config is not None:
        return _yaml_config
    
    try:
        from config_loader import load_config
        _yaml_config = load_config()
        logger.info("✅ Loaded configuration from gen_search_config.yml")
        logger.info(f"📁 Dataset path: {_yaml_config.dataset.path}")
        return _yaml_config
    except Exception as e:
        logger.warning(f"⚠️ Could not load YAML config: {e}. Using defaults.")
        return None

# FastAPI app
app = FastAPI(title="RAG Evaluation API", version="1.0.0")


class EvaluationRequest(BaseModel):
    evaluation_request: Dict[str, Any]

@app.post("/api/evaluate")
async def evaluate_endpoint(request: EvaluationRequest) -> Dict[str, Any]:
    """
    Accept GA evaluation_request with pipeline_config, run ModularRAG evaluation,
    and return {"evaluation": {"final_score": <0..1>}}.
    """
    payload = request.evaluation_request or {}
    pipeline_config = payload.get("pipeline_config", {})

    if not isinstance(pipeline_config, dict) or not pipeline_config:
        raise HTTPException(status_code=400, detail="evaluation_request.pipeline_config is required")

    logger.info("Received evaluation request with pipeline_config: %s", pipeline_config)

    config = parse_config(pipeline_config)

    try:
        logger.info("Starting Modular RAG evaluation for genetic algorithm...")
        start_time = time.time()

        # Run evaluation (uses all config combinations)
        results = await ModularRAGPipeline.run_evaluation({}, config)

        # Print results (can be improved for modular combos)
        # logger.info(f"Results: {results}")
        await save_markdown_results(results)
        
        # Extract overall score safely
        if hasattr(results, 'aggregated_metrics') and results.aggregated_metrics:
            if isinstance(results.aggregated_metrics, dict):
                if "overall_score" in results.aggregated_metrics:
                    final_score = float(results.aggregated_metrics["overall_score"])
                else:
                    # Get first combination's overall score
                    first_combo_metrics = next(iter(results.aggregated_metrics.values()))
                    final_score = float(first_combo_metrics.get("overall_score", 0.0))
            else:
                final_score = 0.0
        else:
            final_score = 0.0
            
        logger.info(f"Evaluation completed in {time.time() - start_time:.2f}s")
        
        
        # Clamp to [0, 1] range
        final_score = max(0.0, min(1.0, final_score))
        
        logger.info(f"Final score: {final_score}")
        return {"evaluation": {"final_score": final_score}}

    except Exception as e:
        logger.error(f"Evaluation failed: {e}")
        import traceback
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"RAG evaluation failed: {e}")

def parse_config(config_dict: Dict[str, str] = None):
    """
    Parse the config file and return a ModularRAGConfig object.
    
    Configuration values are loaded from gen_search_config.yml when available.
    """
    # Load YAML config for dataset path and evaluation weights
    yaml_config = load_yaml_config()
    
    # Get dataset path from YAML config or use default
    dataset_path = None
    if yaml_config is not None:
        dataset_path = yaml_config.dataset.path
        logger.info(f"📁 Using dataset path from YAML config: {dataset_path}")
    
    # Get evaluation weights from YAML config or use defaults
    if yaml_config is not None:
        retrieval_weights = yaml_config.evaluation.retrieval_weights
        generation_weights = yaml_config.evaluation.generation_weights
        overall_weights = yaml_config.evaluation.overall_weights
        llm_eval_model = yaml_config.evaluation.llm_eval_model
    else:
        retrieval_weights = {
            'recall_at_k': 0.25,
            'map_score': 0.25,
            'ndcg_at_k': 0.25,
            'mrr': 0.25
        }
        generation_weights = {
            'llm_score': 0.5,
            'semantic_similarity': 0.5
        }
        overall_weights = {
            'retrieval': 0.5,
            'generation': 0.5
        }
        llm_eval_model = 'gpt-oss:120B'
    
    config = ModularRAGConfig(
        run_name="retrieval - alibayram/Qwen3-30B-A3B-Instruct-2507:latest",
        save_eval_cases=False,
        enable_logging=True,
        log_level="INFO",
        enable_timing=True,

        pre_embedding=[CONFIG_MAP["pre-embedding"][config_dict["pre-embedding"]]],
        query_expansion=[CONFIG_MAP["query-expansion"][config_dict["query-expansion"]]],
        retrieval=[CONFIG_MAP["retrieval"][config_dict["retrieval"]]],
        passage_rerank=[CONFIG_MAP["passage-rerank"][config_dict["passage-rerank"]]],
        passage_filter=[CONFIG_MAP["passage-filter"][config_dict["passage-filter"]]],
        passage_augment=[CONFIG_MAP["passage-augment"][config_dict["passage-augment"]]],
        passage_compress=[CONFIG_MAP["passage-compress"][config_dict["passage-compress"]]],
        prompt_maker=[CONFIG_MAP["prompt-maker"][config_dict["prompt-maker"]]],
        generator=[CONFIG_MAP["generator"][config_dict["generator"]]],
        post_generation=[CONFIG_MAP["post-generation"][config_dict["post-generation"]]],


        # Dataset/global settings (from YAML config)
        dataset_path=dataset_path,
        qdrant_collection_hash=None,
        max_test_cases=100,
        test_case_offset=0,
        eval_batch_size=1,
        parallel_execution=True,
        max_workers=4,
        cache_enabled=True,


        # Evaluation settings (from YAML config)
        retrieval_weights=retrieval_weights,
        generation_weights=generation_weights,
        overall_weights=overall_weights,
        llm_eval_model=llm_eval_model
    )
    return config

async def run_rag_evaluation():
    """Run RAG evaluation with multiple model combinations"""
    
    # Configuration for Modular RAG evaluation
    from rag_pipeline.core.modular_configs import ModularRAGConfig, PreEmbeddingConfig, RetrievalConfig, GeneratorConfig, PassageRerankConfig, PassageFilterConfig, PassageCompressConfig, PromptMakerConfig, QueryExpansionConfig, PassageAugmentConfig, PostGenerationConfig
    from rag_pipeline.core.modular_pipeline import ModularRAGPipeline
    
    config_dict = {
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

    # Example ModularRAGConfig with multiple generator configs
    config = parse_config(config_dict)
    
    try:
        logger.info("Starting Modular RAG evaluation...")
        start_time = time.time()

        # Run evaluation (uses all config combinations)
        results = await ModularRAGPipeline.run_evaluation({}, config)

        # Print results (can be improved for modular combos)
        # logger.info(f"Results: {results}")
        await save_markdown_results(results)

        logger.info(f"Evaluation completed in {time.time() - start_time:.2f}s")
        return results

    except Exception as e:
        logger.error(f"Evaluation failed: {e}")
        print(e.traceback)
        import traceback
        logger.error(traceback.format_exc())
        raise

async def save_markdown_results(results, filename: str = None):
    """Save evaluation results to Markdown file using generate_markdown_report method."""
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
    
    # Token count breakdown
    markdown += "## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):\n\n"
    for combo, metrics in aggregated_metrics.items():
        markdown += f"**{combo}:**\n"
        # Handle embedding token counts
        embedding_counts = metrics.get("embedding_token_counts", {})
        if embedding_counts:
            markdown += f"  - Embedding Tokens:\n"
            for comp, val in embedding_counts.items():
                markdown += f"    - {comp}: {val:.1f}\n"
        
        # Handle LLM token counts
        llm_counts = metrics.get("llm_token_counts", {})
        if llm_counts:
            markdown += f"  - LLM Tokens:\n"
            for comp, model_counts in llm_counts.items():
                markdown += f"    - {comp}:\n"
                for model, counts in model_counts.items():
                    in_tokens = counts.get('in', 0.0)
                    out_tokens = counts.get('out', 0.0)
                    markdown += f"      - {model}: {in_tokens:.1f} in, {out_tokens:.1f} out\n"
    markdown += "\n"
    
    # Timing breakdown
    # Sum per-component times across all individual_results
    timing_keys_ordered = [
        ('pre_embedding_time', 'Pre-embedding'),
        ('query_expansion_time', 'Query Expansion'),
        ('retrieval_time', 'Retrieval'),
        ('passage_augment_time', 'Passage Augment'),
        ('passage_rerank_time', 'Passage Rerank'),
        ('passage_filter_time', 'Passage Filter'),
        ('passage_compress_time', 'Passage Compress'),
        ('prompt_maker_time', 'Prompt Maker'),
        ('generation_time', 'Generation'),
        ('post_generation_time', 'Post-generation'),
    ]
    markdown += "## ⏱️ TIMING BREAKDOWN:\n\n"
    markdown += "**Prediction Times:**\n"
    # Evaluation times
    total_retr_eval_time = sum(getattr(r, 'retrieval_eval_time', 0.0) for r in results.individual_results)
    total_gen_eval_time = sum(getattr(r, 'generation_eval_time', 0.0) for r in results.individual_results)
    total_evaluation_time = total_retr_eval_time + total_gen_eval_time
    
    sum_times = {}
    for key, _ in timing_keys_ordered:
        vals = [metrics.get(key, 0.0) for metrics in aggregated_metrics.values() if metrics.get(key, 0.0) > 0]
        if vals:
            sum_times[key] = sum(vals)

    for key, pretty in timing_keys_ordered:
        if key in sum_times:
            markdown += f"- {pretty}: {sum_times[key]:.3f}s\n"
    markdown += f"- Total Prediction Time: {sum(sum_times.values()):.3f}s\n"
    markdown += "\n"
    
    
    markdown += "**Evaluation Times:**\n"
    markdown += f"  - Retrieval: {total_retr_eval_time:.2f}s\n"
    markdown += f"  - Generation: {total_gen_eval_time:.2f}s\n"
    markdown += f"  - Total Evaluation: {total_evaluation_time:.2f}s\n\n"
    markdown += f"**Pipeline Total:** {total_runtime:.2f}s\n\n"

    # Canonical timing keys and pretty names from modular_pipeline.py
    timing_keys_ordered = [
        ('pre_embedding_time', 'Pre-embedding'),
        ('query_expansion_time', 'Query Expansion'),
        ('retrieval_time', 'Retrieval'),
        ('passage_augment_time', 'Passage Augment'),
        ('passage_rerank_time', 'Passage Rerank'),
        ('passage_filter_time', 'Passage Filter'),
        ('passage_compress_time', 'Passage Compress'),
        ('prompt_maker_time', 'Prompt Maker'),
        ('generation_time', 'Generation'),
        ('post_generation_time', 'Post-generation'),
    ]

    # Compute averages for each timing key
    
    # Footer
    markdown += "---\n\n"
    markdown += f"*Report generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n"
    
    return markdown


def _format_model_combinations_list(aggregated_metrics) -> str:
    """Format the list of model combinations tested."""
    return "\n".join(["  • " + combo for combo in aggregated_metrics.keys()])


def _format_detailed_metrics(aggregated_metrics) -> str:
    """Format detailed metrics for each combination."""
    lines = []
    
    for combo, metrics in aggregated_metrics.items():
    
        lines.append(f"\n**{combo}:**")
        
        # Retrieval metrics
        eval_k = metrics.get('eval_k', 10)
        recall = metrics.get('recall_at_k', 0.0)
        map_score = metrics.get('map_score', 0.0)
        ndcg = metrics.get('ndcg_at_k', 0.0)
        mrr = metrics.get('mrr', 0.0)
        lines.append(f"  Retrieval: R@{eval_k}={recall:.3f}, mAP={map_score:.3f}, nDCG@{eval_k}={ndcg:.3f}, MRR={mrr:.3f}")
        
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
        pre_embedding_time = metrics.get('pre_embedding_time', 0.0)
        query_expansion_time = metrics.get('query_expansion_time', 0.0)
        retrieval_time = metrics.get('retrieval_time', 0.0)
        passage_augment_time = metrics.get('passage_augment_time', 0.0)
        passage_rerank_time = metrics.get('passage_rerank_time', 0.0)
        passage_filter_time = metrics.get('passage_filter_time', 0.0)
        passage_compress_time = metrics.get('passage_compress_time', 0.0)
        prompt_maker_time = metrics.get('prompt_maker_time', 0.0)
        generation_time = metrics.get('generation_time', 0.0)
        post_generation_time = metrics.get('post_generation_time', 0.0)
        
        # Only show prediction times for components with time > 0
        pred_times = [
            ("Pre-embedding", pre_embedding_time),
            ("Query Expansion", query_expansion_time),
            ("Retrieval", retrieval_time),
            ("Passage Augment", passage_augment_time),
            ("Passage Rerank", passage_rerank_time),
            ("Passage Filter", passage_filter_time),
            ("Passage Compress", passage_compress_time),
            ("Prompt Maker", prompt_maker_time),
            ("Generation", generation_time),
            ("Post-generation", post_generation_time),
        ]
        shown_pred_times = [f"{name}={val:.3f}s" for name, val in pred_times if val > 0]
        if shown_pred_times:
            lines.append(f"  Avg Prediction Times: {', '.join(shown_pred_times)}")
        total_pred_time = sum(val for _, val in pred_times)
        if total_pred_time > 0:
            lines.append(f"  Total Prediction Time: {total_pred_time:.3f}s")
        # Token counts per component
        embedding_counts = metrics.get("embedding_token_counts", {})
        if embedding_counts:
            lines.append(f"  Embedding Tokens: {sum(embedding_counts.values()):.1f}")
        
        llm_counts = metrics.get("llm_token_counts", {})
        if llm_counts:
            total_llm_in = 0
            total_llm_out = 0
            for comp, model_counts in llm_counts.items():
                for model, counts in model_counts.items():
                    total_llm_in += counts.get('in', 0.0)
                    total_llm_out += counts.get('out', 0.0)
            lines.append(f"  LLM Tokens: {total_llm_in:.1f} in, {total_llm_out:.1f} out")
        # Evaluation timing
        retr_eval_time = metrics.get('retrieval_evaluation_time', 0.0)
        gen_eval_time = metrics.get('generation_evaluation_time', 0.0)
        lines.append(f"  Avg Evaluation Times: Retrieval={retr_eval_time:.3f}s, Generation={gen_eval_time:.3f}s")
    
    return "\n".join(lines)


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
        
        # Get port from YAML config or use default
        yaml_config = load_yaml_config()
        port = 8060  # Default port
        if yaml_config is not None:
            port = yaml_config.api.port
        
        # if arg == "--server":
            # Start FastAPI server for genetic algorithm evaluation
        logger.info(f"Starting RAG Evaluation API server on port {port}...")
        uvicorn.run(
            "rag_pipeline.main:app",
            host="0.0.0.0",
            port=port,
            reload=False,
            log_level="info"
        )
            # return 0
            
        # elif arg == "--super-quick":
        #     # Super quick test mode (30 seconds)
        #     try:
        #         results = run_super_quick_test()
        #         print(f"\n⚡ Super quick test completed successfully!")
        #         print(f"Best combination: {results.best_overall_combo}")
        #         print(f"Pipeline is working correctly!")
        #     except Exception as e:
        #         print(f"❌ Super quick test failed: {e}")
        #         return 1
                
        # elif arg == "--quick":
        #     # Quick test mode (1-2 minutes)
        #     try:
        #         results = run_quick_test()
        #         print(f"\n✅ Quick test completed successfully!")
        #         print(f"Best combination: {results.best_overall_combo}")
        #     except Exception as e:
        #         print(f"❌ Quick test failed: {e}")
        #         return 1
        # elif arg == "--basic-modular":
        #     # Basic modular test mode (1-2 minutes)
        #     try:
        #         results = asyncio.run(demo_basic_framework())
        #         print(f"\n✅ Basic modular test completed successfully!")
        #         print(f"Best combination: {results.best_overall_combo}")
        #     except Exception as e:
        #         print(f"❌ Basic modular test failed: {e}")
        #         return 1
        # elif arg == "--full":
        #     # Full evaluation mode (10+ minutes)
        #     try:
        #         results = asyncio.run(run_rag_evaluation())
        #         print(f"\n🎉 Full evaluation completed successfully!")
        #         print(f"Best overall combination: {results.best_overall_combo}")
        #     except Exception as e:
        #         print(f"❌ Evaluation failed: {e}")
        #         return 1
        # else:
        #     try:
        #         results = asyncio.run(demo_basic_framework())
        #         print(f"\n✅ Basic modular test completed successfully!")
        #         print(f"Best combination: {results.best_overall_combo}")
        #     except Exception as e:
        #         print(f"❌ Basic modular test failed: {e}")
        #         return 1
    time.sleep(1000000)
    return 0

if __name__ == "__main__":
    exit_code = main()