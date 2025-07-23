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
    RAGTestCase,
    RetrievalResult,
    GenerationResult,
    RAGMetrics,
    RAGEvaluationResult,
    RAGBenchmarkResult,
    RAGDocument
)

from .modular_pipeline import ModularRAGPipeline

from .modular_configs import ModularRAGConfig

from .evaluator import RAGEvaluator
from .dataset import RAGDataset

__all__ = [
    # Core pipeline
    'ModularRAGPipeline',
    # Configuration and data models
    'RAGTestCase',
    'RAGDocument',
    'ModularRAGConfig',
    
    # Result models
    'RetrievalResult',
    'GenerationResult',
    'RAGMetrics',
    'RAGEvaluationResult',
    'RAGBenchmarkResult',
    
    # Supporting classes
    'RAGEvaluator',
    'RAGDataset'
] 