"""
RAG Pipeline Core Module

This module provides a clean, extensible RAG evaluation pipeline focused on:
- Testing multiple embedding models and LLM combinations
- Comprehensive retrieval and generation evaluation
- Easy extension with new RAG techniques

Main classes:
- RAGPipeline: Main orchestrator for RAG evaluation
- RAGConfig: Configuration for pipeline settings
- RAGEvaluationResult: Individual test case results
- RAGBenchmarkResult: Aggregated benchmark results
"""

from .models import (
    RAGConfig,
    RAGTestCase,
    RetrievalResult,
    GenerationResult,
    RAGMetrics,
    RAGEvaluationResult,
    RAGBenchmarkResult,
    RAGDocument
)

from .components import (
    RetrievalComponent,
    GenerationComponent,
    VectorStoreRetrieval,
    OllamaGeneration,
    ComponentFactory
)

from .evaluator import RAGEvaluator
from .dataset import RAGDataset
from .pipeline import RAGPipeline

__all__ = [
    # Core pipeline
    'RAGPipeline',
    
    # Configuration and data models
    'RAGConfig',
    'RAGTestCase',
    'RAGDocument',
    
    # Result models
    'RetrievalResult',
    'GenerationResult',
    'RAGMetrics',
    'RAGEvaluationResult',
    'RAGBenchmarkResult',
    
    # Components
    'RetrievalComponent',
    'GenerationComponent',
    'VectorStoreRetrieval',
    'OllamaGeneration',
    'ComponentFactory',
    
    # Supporting classes
    'RAGEvaluator',
    'RAGDataset'
] 