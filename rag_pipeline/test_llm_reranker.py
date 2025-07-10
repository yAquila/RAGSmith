#!/usr/bin/env python3
"""
Test script for LLM-based reranking functionality

This script tests the LLM reranker independently to ensure it works correctly
before integrating with the full RAG pipeline.
"""

import asyncio
import logging
import time
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def test_llm_reranker():
    """Test LLM reranker with sample documents"""
    
    print("🧪 Testing LLM Reranker")
    print("=" * 50)
    
    # Sample query and documents for testing
    query = "What is machine learning?"
    
    sample_docs = [
        {
            "doc_id": "doc1",
            "content": "Machine learning is a subset of artificial intelligence that enables computers to learn and improve from experience without being explicitly programmed.",
            "score": 0.85
        },
        {
            "doc_id": "doc2", 
            "content": "The weather today is sunny with a temperature of 75 degrees Fahrenheit.",
            "score": 0.20
        },
        {
            "doc_id": "doc3",
            "content": "Deep learning is a subset of machine learning that uses neural networks with multiple layers to model and understand complex patterns.",
            "score": 0.78
        },
        {
            "doc_id": "doc4",
            "content": "Python is a high-level programming language known for its simplicity and readability.",
            "score": 0.45
        },
        {
            "doc_id": "doc5",
            "content": "Supervised learning is a type of machine learning where the algorithm learns from labeled training data.",
            "score": 0.82
        }
    ]
    
    print(f"📝 Query: {query}")
    print(f"📄 Documents to rerank: {len(sample_docs)}")
    print()
    
    # Print original ranking
    print("📊 Original ranking (by vector similarity score):")
    for i, doc in enumerate(sample_docs, 1):
        print(f"  {i}. {doc['doc_id']} (score: {doc['score']:.2f})")
        print(f"     {doc['content'][:80]}...")
    print()
    
    try:
        # Test LLM reranker
        from util.rerank.llm_reranker import get_llm_reranker
        
        print("🤖 Initializing LLM reranker...")
        llm_reranker = get_llm_reranker(
            model_name='llama3.2:1b',
            max_tokens=2048,
            temperature=0.1
        )
        
        print(f"✅ LLM reranker initialized with model: {llm_reranker.model_name}")
        print()
        
        # Test reranking
        print("🔄 Applying LLM reranking...")
        start_time = time.time()
        
        reranked_docs = llm_reranker.rerank_documents(
            query=query,
            documents=sample_docs,
            top_k=3  # Keep top 3
        )
        
        rerank_time = time.time() - start_time
        print(f"⏱️  LLM reranking completed in {rerank_time:.2f}s")
        print()
        
        # Print reranked results
        print("🎯 LLM reranked results (top 3):")
        for i, doc in enumerate(reranked_docs, 1):
            llm_score = doc.get('llm_rerank_score', 0.0)
            original_score = doc.get('score', 0.0)
            print(f"  {i}. {doc['doc_id']} (LLM score: {llm_score:.2f}, original: {original_score:.2f})")
            print(f"     {doc['content'][:80]}...")
        print()
        
        # Test with different parameters
        print("🔧 Testing with different parameters...")
        reranker_fast = get_llm_reranker(
            model_name='llama3.2:1b',
            max_tokens=1024,
            temperature=0.0  # More deterministic
        )
        
        start_time = time.time()
        reranked_docs_fast = reranker_fast.rerank_documents(
            query=query,
            documents=sample_docs[:3],  # Test with fewer docs
            top_k=None  # Return all
        )
        fast_time = time.time() - start_time
        
        print(f"⚡ Fast reranking (3 docs) completed in {fast_time:.2f}s")
        for i, doc in enumerate(reranked_docs_fast, 1):
            llm_score = doc.get('llm_rerank_score', 0.0)
            print(f"  {i}. {doc['doc_id']} (LLM score: {llm_score:.2f})")
        print()
        
        # Test edge cases
        print("🔍 Testing edge cases...")
        
        # Test with single document
        single_doc_result = llm_reranker.rerank_documents(
            query=query,
            documents=[sample_docs[0]],
            top_k=None
        )
        print(f"✅ Single document test: {single_doc_result[0]['llm_rerank_score']:.2f}")
        
        # Test with empty documents
        empty_result = llm_reranker.rerank_documents(
            query=query,
            documents=[],
            top_k=None
        )
        print(f"✅ Empty documents test: {len(empty_result)} results")
        
        print()
        print("🎉 All LLM reranker tests passed!")
        
        # Performance comparison
        print("\n📈 Performance Analysis:")
        print(f"  • LLM reranking time: {rerank_time:.2f}s for {len(sample_docs)} docs")
        print(f"  • Fast reranking time: {fast_time:.2f}s for 3 docs")
        print(f"  • Average time per document: {rerank_time/len(sample_docs):.3f}s")
        
    except Exception as e:
        print(f"❌ LLM reranker test failed: {e}")
        logger.error(f"LLM reranker test failed: {e}", exc_info=True)
        return False
    
    return True

async def test_combination_scenario():
    """Test scenario with both cross-encoder and LLM reranking"""
    
    print("\n🔀 Testing Combined Reranking Scenario")
    print("=" * 50)
    
    query = "What are the benefits of renewable energy?"
    
    sample_docs = [
        {
            "doc_id": "doc1",
            "content": "Solar energy is a renewable source that reduces carbon emissions and provides clean electricity.",
            "score": 0.75
        },
        {
            "doc_id": "doc2",
            "content": "The stock market reached new highs yesterday with technology shares leading the gains.",
            "score": 0.30
        },
        {
            "doc_id": "doc3",
            "content": "Wind power is sustainable and helps reduce dependence on fossil fuels while creating jobs.",
            "score": 0.82
        },
        {
            "doc_id": "doc4",
            "content": "Renewable energy sources like hydro, solar, and wind are environmentally friendly and sustainable.",
            "score": 0.88
        }
    ]
    
    print(f"📝 Query: {query}")
    print(f"📄 Documents: {len(sample_docs)}")
    print()
    
    try:
        # Step 1: Apply cross-encoder reranking
        print("🔄 Step 1: Cross-encoder reranking...")
        from util.rerank.reranker import get_reranker
        
        ce_reranker = get_reranker('BAAI/bge-reranker-v2-m3', force_cpu=True)
        ce_reranked = ce_reranker.rerank_documents(query, sample_docs, top_k=3)
        
        print("Cross-encoder results:")
        for i, doc in enumerate(ce_reranked, 1):
            ce_score = doc.get('rerank_score', 0.0)
            print(f"  {i}. {doc['doc_id']} (CE score: {ce_score:.3f})")
        print()
        
        # Step 2: Apply LLM reranking on cross-encoder results
        print("🔄 Step 2: LLM reranking on CE results...")
        from util.rerank.llm_reranker import get_llm_reranker
        
        llm_reranker = get_llm_reranker('llama3.2:1b')
        final_reranked = llm_reranker.rerank_documents(query, ce_reranked, top_k=2)
        
        print("Final combined results:")
        for i, doc in enumerate(final_reranked, 1):
            ce_score = doc.get('rerank_score', 0.0)
            llm_score = doc.get('llm_rerank_score', 0.0)
            original_score = doc.get('score', 0.0)
            print(f"  {i}. {doc['doc_id']}")
            print(f"     Original: {original_score:.3f} | CE: {ce_score:.3f} | LLM: {llm_score:.3f}")
        print()
        
        print("✅ Combined reranking test successful!")
        
    except Exception as e:
        print(f"❌ Combined reranking test failed: {e}")
        logger.error(f"Combined reranking test failed: {e}", exc_info=True)
        return False
    
    return True

async def main():
    """Run all LLM reranker tests"""
    
    print("🚀 Starting LLM Reranker Tests")
    print("=" * 60)
    
    try:
        # Test basic LLM reranking
        test1_success = await test_llm_reranker()
        
        # Test combination scenario
        test2_success = await test_combination_scenario()
        
        print("\n" + "=" * 60)
        if test1_success and test2_success:
            print("🎉 ALL TESTS PASSED! LLM reranker is ready for integration.")
        else:
            print("❌ Some tests failed. Please check the logs.")
        print("=" * 60)
        
    except Exception as e:
        print(f"❌ Test execution failed: {e}")
        logger.error(f"Test execution failed: {e}", exc_info=True)

if __name__ == "__main__":
    asyncio.run(main()) 