#!/usr/bin/env python3
"""
Test script for Gemini integration.

This script tests the Gemini client implementation to ensure it works
similarly to the Ollama client and can be used as a drop-in replacement.
"""

import os
import sys
import asyncio
import logging
from typing import Dict, Any

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from util.api.gemini_client import GeminiUtil
from util.api.ollama_client import OllamaUtil
from core.components import GeminiGeneration, OllamaGeneration
from core.config import RAGConfig

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_gemini_client():
    """Test the Gemini client directly"""
    print("=== Testing Gemini Client ===")
    
    # Check if API key is set
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ GEMINI_API_KEY environment variable not set")
        print("Please set it with: export GEMINI_API_KEY='your-api-key'")
        return False
    
    print(f"✅ GEMINI_API_KEY found: {api_key[:10]}...")
    
    # Test simple prompt
    test_prompt = "What is the capital of France? Please provide a brief answer."
    test_model = "gemini-1.5-flash"
    
    print(f"Testing with model: {test_model}")
    print(f"Prompt: {test_prompt}")
    
    try:
        response = GeminiUtil.get_gemini_response(test_model, test_prompt)
        
        if response:
            print("✅ Gemini client test successful!")
            print(f"Response: {response.get('response', 'No response')}")
            print(f"Tokens per second: {response.get('tps', 'N/A')}")
            print(f"Estimated tokens: {response.get('eval_count', 'N/A')}")
            return True
        else:
            print("❌ Gemini client returned None")
            return False
            
    except Exception as e:
        print(f"❌ Gemini client test failed: {e}")
        return False

def test_gemini_generation_component():
    """Test the Gemini generation component"""
    print("\n=== Testing Gemini Generation Component ===")
    
    # Create a simple config
    config = RAGConfig()
    
    try:
        # Create Gemini generation component
        gemini_gen = GeminiGeneration("gemini-1.5-flash", config)
        print("✅ Gemini generation component created successfully")
        
        # Test generation
        test_query = "What is machine learning?"
        test_context = "Machine learning is a subset of artificial intelligence that enables computers to learn and make decisions from data without being explicitly programmed."
        
        print(f"Testing generation with query: {test_query}")
        print(f"Context: {test_context}")
        
        # Run async test
        async def run_test():
            result = await gemini_gen.generate(test_query, test_context, "test-embedding")
            
            if result.generated_answer:
                print("✅ Gemini generation test successful!")
                print(f"Generated answer: {result.generated_answer}")
                print(f"Generation time: {result.generation_time:.2f}s")
                print(f"Tokens per second: {result.tokens_per_second}")
                return True
            else:
                print("❌ Gemini generation returned empty answer")
                return False
        
        # Run the async test
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        success = loop.run_until_complete(run_test())
        loop.close()
        
        return success
        
    except Exception as e:
        print(f"❌ Gemini generation component test failed: {e}")
        return False

def test_component_factory():
    """Test the component factory with Gemini"""
    print("\n=== Testing Component Factory with Gemini ===")
    
    config = RAGConfig()
    
    try:
        from core.components import ComponentFactory
        
        # Test creating Gemini generation component
        gemini_component = ComponentFactory.create_generation_component(
            "gemini-1.5-flash", config, "gemini"
        )
        
        print("✅ Component factory created Gemini component successfully")
        print(f"Component type: {type(gemini_component).__name__}")
        
        return True
        
    except Exception as e:
        print(f"❌ Component factory test failed: {e}")
        return False

def compare_interfaces():
    """Compare the interfaces of Ollama and Gemini clients"""
    print("\n=== Comparing Ollama and Gemini Interfaces ===")
    
    # Test that both clients have the same interface
    ollama_methods = [method for method in dir(OllamaUtil) if not method.startswith('_')]
    gemini_methods = [method for method in dir(GeminiUtil) if not method.startswith('_')]
    
    print(f"OllamaUtil methods: {ollama_methods}")
    print(f"GeminiUtil methods: {gemini_methods}")
    
    # Check if key methods exist in both
    key_methods = ['get_ollama_response', 'get_gemini_response']
    
    for method in key_methods:
        if hasattr(OllamaUtil, 'get_ollama_response') and hasattr(GeminiUtil, 'get_gemini_response'):
            print(f"✅ Both clients have equivalent response methods")
            break
    else:
        print("❌ Clients don't have equivalent response methods")
        return False
    
    return True

def main():
    """Run all tests"""
    print("🚀 Starting Gemini Integration Tests\n")
    
    tests = [
        ("Gemini Client", test_gemini_client),
        ("Gemini Generation Component", test_gemini_generation_component),
        ("Component Factory", test_component_factory),
        ("Interface Comparison", compare_interfaces),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} test crashed: {e}")
            results.append((test_name, False))
    
    # Print summary
    print("\n" + "="*50)
    print("📊 TEST SUMMARY")
    print("="*50)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Gemini integration is working correctly.")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 