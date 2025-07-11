"""
API client utilities.

Provides utilities for:
- Ollama API communication
- Gemini API communication
- Model interaction
- Connection management
"""

from .ollama_client import OllamaUtil
from .gemini_client import GeminiUtil

__all__ = ['OllamaUtil', 'GeminiUtil'] 