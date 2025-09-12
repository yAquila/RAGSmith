"""
Gemini API client utilities.

Provides utilities for:
- Connecting to Gemini API
- Making API requests
- Session management and connection pooling
"""

import json
import os
import logging
import time
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

class GeminiUtil:
    """Utility class for communicating with Gemini API"""
    
    _client = None  # Class-level client for connection pooling
    
    def __init__(self):
        pass
    
    @classmethod
    def get_client(cls):
        """Get or create a reusable client for connection pooling"""
        if cls._client is None:
            try:
                import google.generativeai as genai
                
                # Get API key from environment variable
                api_key = os.getenv("GEMINI_API_KEY")
                if not api_key:
                    raise ValueError("GEMINI_API_KEY environment variable is required")
                
                # Configure the API
                genai.configure(api_key=api_key)
                cls._client = genai
                logger.info("Gemini client initialized successfully")
                
            except ImportError:
                raise ImportError("google-generativeai package is required. Install with: pip install google-generativeai")
            except Exception as e:
                logger.error(f"Failed to initialize Gemini client: {e}")
                raise
                
        return cls._client
    
    def connect_to_gemini(self):
        """Connect to Gemini API (placeholder for compatibility)"""
        pass

    def disconnect_gemini(self):
        """Disconnect from Gemini API (placeholder for compatibility)"""
        pass

    @staticmethod
    def get_gemini_response(model: str, prompt: str) -> Optional[Dict[str, Any]]:
        """
        Get response from Gemini model.
        
        Args:
            model: Name of the model to use (e.g., 'gemini-1.5-pro', 'gemini-2.0-flash-exp')
            prompt: Input prompt for the model
            
        Returns:
            Dict containing response text and metrics, or None if error occurred
        """
        try:
            logger.info("Gemini CALISIYOR!!!")
            client = GeminiUtil.get_client()
            
            # Map common model names to Gemini model names
            model_mapping = {
                'gemini3:4b': 'gemini-1.5-flash',
                'gemini3:2b': 'gemini-1.5-flash',
                'gemini-1.5-pro': 'gemini-1.5-pro',
                'gemini-1.5-flash': 'gemini-1.5-flash',
                'gemini-2.0-flash-exp': 'gemini-2.0-flash-exp',
                'gemini-2.0-pro': 'gemini-2.0-pro'
            }
            
            # Use mapped model name or the original name
            gemini_model_name = model_mapping.get(model, model)
            
            # Create the model instance
            genai_model = client.GenerativeModel(gemini_model_name)
            
            # Configure generation parameters
            generation_config = {
                'temperature': 0.1,  # Low temperature for more focused responses
                'top_p': 0.8,
                'top_k': 40,
                'max_output_tokens': 2048,
            }
            
            # Start timing
            start_time = time.time()
            
            # Generate response
            response = genai_model.generate_content(
                prompt,
                generation_config=generation_config
            )
            
            # Calculate timing
            generation_time = time.time() - start_time
            
            # Extract response text
            response_text = response.text if response.text else ""
            
            # Calculate approximate tokens (rough estimation)
            # Gemini doesn't provide exact token counts in the response
            # We'll estimate based on character count (roughly 4 chars per token)
            estimated_tokens = len(response_text) // 4
            
            # Calculate tokens per second
            tokens_per_second = estimated_tokens / generation_time if generation_time > 0 else 0
            
            # Remove <think>...</think> sections from the response, if present
            import re
            if response_text:
                # Remove all occurrences of <think>...</think> (non-greedy, multiline)
                response_text = re.sub(r"<think>.*?</think>", "", response_text, flags=re.DOTALL)
                # Optionally, strip leading/trailing whitespace
                response_text = response_text.strip()
            
            result = {
                "response": response_text,
                "tps": tokens_per_second,
                "eval_count": estimated_tokens,  # Using estimated token count
                "eval_duration": int(generation_time * 1_000_000_000),  # Convert to nanoseconds for compatibility
                "generation_time": generation_time
            }
            
            logger.debug(f"Model: {model}, Prompt: {prompt[:50]}..., Calculated TPS: {tokens_per_second:.2f} tokens/second")
            
            return result
            
        except Exception as e:
            logger.error(f"Error getting Gemini response: {e}")
            logger.error("Please ensure GEMINI_API_KEY is set and the model name is valid.")
            return None

    @staticmethod
    def list_available_models() -> list:
        """
        List available Gemini models.
        
        Returns:
            List of available model names
        """
        try:
            logger.info("GEMINI CALISTI -1 : ")
            client = GeminiUtil.get_client()
            models = client.list_models()
            
            # Filter for text generation models
            text_models = []
            for model in models:
                if 'gemini' in model.name.lower():
                    text_models.append(model.name)
            
            return text_models
            
        except Exception as e:
            logger.error(f"Error listing models: {e}")
            return [] 