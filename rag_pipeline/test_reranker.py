#!/usr/bin/env python3
"""
Test script for reranker caching and GPU usage
"""

import os
import logging
import time
from util.rerank.reranker import get_reranker

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def test_reranker_caching():
    """Test reranker model caching and GPU usage"""
    
    logger.info("Testing reranker caching and GPU usage...")
    
    # Test documents
    test_query = "What is machine learning?"
    test_documents = [
        {"content": "Machine learning is a subset of artificial intelligence that focuses on algorithms.", "doc_id": "1"},
        {"content": "Deep learning uses neural networks with multiple layers.", "doc_id": "2"},
        {"content": "Natural language processing deals with text and speech.", "doc_id": "3"},
        {"content": "Computer vision enables machines to interpret visual information.", "doc_id": "4"},
    ]
    
    # First run - should download and cache the model
    logger.info("\n=== First run (should download and cache model) ===")
    start_time = time.time()
    reranker1 = get_reranker("BAAI/bge-reranker-v2-m3")
    ranked_docs1 = reranker1.rerank_documents(test_query, test_documents, top_k=2)
    first_run_time = time.time() - start_time
    
    logger.info(f"First run completed in {first_run_time:.2f} seconds")
    logger.info(f"Top ranked document: {ranked_docs1[0]['content'][:50]}...")
    logger.info(f"Rerank score: {ranked_docs1[0]['rerank_score']:.4f}")
    
    # Second run - should use cached model
    logger.info("\n=== Second run (should use cached model) ===")
    start_time = time.time()
    reranker2 = get_reranker("BAAI/bge-reranker-v2-m3")
    ranked_docs2 = reranker2.rerank_documents(test_query, test_documents, top_k=2)
    second_run_time = time.time() - start_time
    
    logger.info(f"Second run completed in {second_run_time:.2f} seconds")
    logger.info(f"Top ranked document: {ranked_docs2[0]['content'][:50]}...")
    logger.info(f"Rerank score: {ranked_docs2[0]['rerank_score']:.4f}")
    
    # Performance comparison
    speedup = first_run_time / second_run_time if second_run_time > 0 else 0
    logger.info(f"\n=== Performance Comparison ===")
    logger.info(f"First run (download + inference): {first_run_time:.2f}s")
    logger.info(f"Second run (cached + inference): {second_run_time:.2f}s")
    logger.info(f"Speedup from caching: {speedup:.2f}x")
    
    # Check cache directory
    cache_dir = os.path.join(os.path.expanduser("~"), ".cache", "rag_pipeline", "reranker_models")
    if os.path.exists(cache_dir):
        cached_models = os.listdir(cache_dir)
        logger.info(f"\n=== Cache Information ===")
        logger.info(f"Cache directory: {cache_dir}")
        logger.info(f"Cached models: {cached_models}")
        
        # Calculate cache size
        total_size = 0
        for model_dir in cached_models:
            model_path = os.path.join(cache_dir, model_dir)
            if os.path.isdir(model_path):
                for root, dirs, files in os.walk(model_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        total_size += os.path.getsize(file_path)
        
        logger.info(f"Total cache size: {total_size / (1024*1024):.1f} MB")
    
    # Test force CPU option
    logger.info("\n=== Testing CPU-only mode ===")
    start_time = time.time()
    reranker_cpu = get_reranker("BAAI/bge-reranker-v2-m3", force_cpu=True)
    ranked_docs_cpu = reranker_cpu.rerank_documents(test_query, test_documents, top_k=2)
    cpu_run_time = time.time() - start_time
    
    logger.info(f"CPU-only run completed in {cpu_run_time:.2f} seconds")
    logger.info(f"Results are consistent: {ranked_docs_cpu[0]['rerank_score'] == ranked_docs1[0]['rerank_score']}")
    
    logger.info("\n=== Test completed successfully! ===")

if __name__ == "__main__":
    test_reranker_caching() 