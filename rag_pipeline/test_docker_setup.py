#!/usr/bin/env python3
"""
Test script to verify Docker setup for GPU access and persistent caching
"""

import os
import logging
import time
import torch
from util.rerank.reranker import get_reranker

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def test_gpu_access():
    """Test GPU access in Docker container"""
    logger.info("=== Testing GPU Access ===")
    
    # Check PyTorch CUDA availability
    cuda_available = torch.cuda.is_available()
    logger.info(f"CUDA available: {cuda_available}")
    
    if cuda_available:
        gpu_count = torch.cuda.device_count()
        logger.info(f"GPU count: {gpu_count}")
        
        for i in range(gpu_count):
            gpu_name = torch.cuda.get_device_name(i)
            gpu_memory = torch.cuda.get_device_properties(i).total_memory / (1024**3)
            logger.info(f"GPU {i}: {gpu_name} ({gpu_memory:.1f}GB)")
    else:
        logger.warning("No GPU access detected in container")
    
    return cuda_available

def test_cache_persistence():
    """Test that cache directory is properly mounted and persistent"""
    logger.info("\n=== Testing Cache Persistence ===")
    
    cache_dir = "/root/.cache/rag_pipeline/reranker_models"
    logger.info(f"Cache directory: {cache_dir}")
    
    # Check if directory exists and is writable
    if os.path.exists(cache_dir):
        logger.info("✓ Cache directory exists")
        
        # Test write permissions
        test_file = os.path.join(cache_dir, "test_write.txt")
        try:
            with open(test_file, 'w') as f:
                f.write("test")
            os.remove(test_file)
            logger.info("✓ Cache directory is writable")
        except Exception as e:
            logger.error(f"✗ Cache directory not writable: {e}")
            return False
            
    else:
        logger.error("✗ Cache directory does not exist")
        return False
    
    # Check if it's a mounted volume
    with open('/proc/mounts', 'r') as f:
        mounts = f.read()
        if cache_dir in mounts:
            logger.info("✓ Cache directory appears to be mounted as volume")
        else:
            logger.warning("? Cache directory might not be mounted as volume")
    
    return True

def test_reranker_with_gpu():
    """Test reranker functionality with GPU and caching"""
    logger.info("\n=== Testing Reranker with GPU and Caching ===")
    
    # Test documents
    test_query = "What is machine learning?"
    test_documents = [
        {"content": "Machine learning is a subset of artificial intelligence.", "doc_id": "1"},
        {"content": "Deep learning uses neural networks.", "doc_id": "2"},
        {"content": "Natural language processing deals with text.", "doc_id": "3"},
    ]
    
    try:
        # Test reranker creation and GPU usage
        logger.info("Creating reranker instance...")
        start_time = time.time()
        
        reranker = get_reranker("BAAI/bge-reranker-v2-m3")
        ranked_docs = reranker.rerank_documents(test_query, test_documents, top_k=2)
        
        elapsed_time = time.time() - start_time
        logger.info(f"Reranking completed in {elapsed_time:.2f} seconds")
        logger.info(f"Top document: {ranked_docs[0]['content'][:50]}...")
        logger.info(f"Rerank score: {ranked_docs[0]['rerank_score']:.4f}")
        
        # Check what device the model is actually using
        if hasattr(reranker, 'model') and reranker.model:
            try:
                device = next(reranker.model.model.parameters()).device
                logger.info(f"Model device: {device}")
                
                if device.type == 'cuda':
                    logger.info("✓ Reranker is using GPU!")
                else:
                    logger.warning(f"Reranker is using {device.type} instead of GPU")
            except Exception as e:
                logger.warning(f"Could not determine model device: {e}")
        
        return True
        
    except Exception as e:
        logger.error(f"Reranker test failed: {e}")
        return False

def test_cache_effectiveness():
    """Test that caching actually improves performance"""
    logger.info("\n=== Testing Cache Effectiveness ===")
    
    test_query = "What is AI?"
    test_documents = [
        {"content": "Artificial intelligence is machine intelligence.", "doc_id": "1"},
        {"content": "Machine learning is a subset of AI.", "doc_id": "2"},
    ]
    
    # Clear any existing instance to force reload
    import util.rerank.reranker
    util.rerank.reranker._reranker_instance = None
    
    # First run (should load from cache if available, or download if not)
    logger.info("First reranker run...")
    start_time = time.time()
    reranker1 = get_reranker("BAAI/bge-reranker-v2-m3")
    ranked_docs1 = reranker1.rerank_documents(test_query, test_documents)
    first_time = time.time() - start_time
    
    # Second run (should reuse existing instance)
    logger.info("Second reranker run...")
    start_time = time.time()
    reranker2 = get_reranker("BAAI/bge-reranker-v2-m3")
    ranked_docs2 = reranker2.rerank_documents(test_query, test_documents)
    second_time = time.time() - start_time
    
    logger.info(f"First run: {first_time:.2f}s")
    logger.info(f"Second run: {second_time:.2f}s")
    
    if second_time < first_time:
        speedup = first_time / second_time
        logger.info(f"✓ Second run was {speedup:.2f}x faster (caching working)")
    else:
        logger.warning("Second run was not faster (caching might not be working)")
    
    # Check cache contents
    cache_dir = "/root/.cache/rag_pipeline/reranker_models"
    if os.path.exists(cache_dir):
        cached_items = os.listdir(cache_dir)
        logger.info(f"Cache contains: {cached_items}")
        
        # Calculate cache size
        total_size = 0
        for item in cached_items:
            item_path = os.path.join(cache_dir, item)
            if os.path.isdir(item_path):
                for root, dirs, files in os.walk(item_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        if os.path.exists(file_path):
                            total_size += os.path.getsize(file_path)
        
        logger.info(f"Total cache size: {total_size / (1024*1024):.1f} MB")

def main():
    """Run all Docker setup tests"""
    logger.info("🐳 Testing RAG Pipeline Docker Setup")
    logger.info("=" * 50)
    
    # Test GPU access
    gpu_available = test_gpu_access()
    
    # Test cache persistence  
    cache_working = test_cache_persistence()
    
    # Test reranker functionality
    reranker_working = test_reranker_with_gpu()
    
    # Test cache effectiveness
    test_cache_effectiveness()
    
    # Summary
    logger.info("\n" + "=" * 50)
    logger.info("🏁 DOCKER SETUP TEST SUMMARY")
    logger.info("=" * 50)
    logger.info(f"GPU Access: {'✓ PASS' if gpu_available else '✗ FAIL'}")
    logger.info(f"Cache Persistence: {'✓ PASS' if cache_working else '✗ FAIL'}")
    logger.info(f"Reranker Functionality: {'✓ PASS' if reranker_working else '✗ FAIL'}")
    
    if gpu_available and cache_working and reranker_working:
        logger.info("🎉 All tests passed! Docker setup is working correctly.")
        return 0
    else:
        logger.error("❌ Some tests failed. Check the setup.")
        return 1

if __name__ == "__main__":
    exit(main()) 