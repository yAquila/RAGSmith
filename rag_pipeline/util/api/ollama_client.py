"""
Ollama API client utilities.

Provides utilities for:
- Connecting to Ollama server
- Making API requests
- Session management and connection pooling
"""

import json
import os
import requests
import logging

logger = logging.getLogger(__name__)

class OllamaUtil:
    """Utility class for communicating with Ollama API"""
    
    _session = None  # Class-level session for connection pooling
    
    def __init__(self):
        pass
    
    @classmethod
    def get_session(cls):
        """Get or create a reusable session for connection pooling"""
        if cls._session is None:
            cls._session = requests.Session()
            # Configure session for better performance
            adapter = requests.adapters.HTTPAdapter(
                pool_connections=10,
                pool_maxsize=20,
                max_retries=3
            )
            cls._session.mount('http://', adapter)
            cls._session.mount('https://', adapter)
        return cls._session
    
    def connect_to_ollama(self):
        """Connect to Ollama server (placeholder for compatibility)"""
        pass

    def disconnect_ollama(self):
        """Disconnect from Ollama server (placeholder for compatibility)"""
        pass

    @staticmethod
    def get_ollama_response(model, prompt, is_eval=False, system_prompt="ANSWER ONLY THE QUESTION YOU ARE ASKED AS CONCISE AS POSSIBLE."):
        """
        Get response from Ollama model.
        Returns a dict with keys: response, prompt_tokens, eval_count, tps
        """
        payload = {
            "model": model,
            "prompt": prompt,
            "verbose": True,
            "system": system_prompt,
            #"think":"low",
            "stream": False  # Set to False for a single response
        }
        # Use environment variable or fallback to default
        if is_eval:
            ollama_api_url = os.getenv("OLLAMA_API_URL2", "http://rag-pipeline-ollama-gpu-2:11434/api")
            payload["think"] = "low"
        else :
            ollama_api_url = os.getenv("OLLAMA_API_URL", "http://rag-pipeline-ollama-gpu:11434/api")
        url = f"{ollama_api_url}/generate"
        
        
        headers = {'Content-Type': 'application/json'}

        try:
            # Use session for connection pooling
            session = OllamaUtil.get_session()
            response = session.post(url, data=json.dumps(payload), headers=headers, timeout=900)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
            data = response.json()
            
            # Calculate TPS with error handling
            tps = None
            prompt_tokens = data.get("prompt_eval_count")
            eval_count = data.get("eval_count")
            eval_duration = data.get("eval_duration")
            
            logger.info(f"eval_count: {eval_count}, eval_duration: {eval_duration}")
            
            if eval_count is not None and eval_duration is not None and eval_duration > 0:
                # Convert nanoseconds to seconds and calculate TPS
                duration_seconds = eval_duration / 1_000_000_000
                tps = eval_count / duration_seconds
                logger.debug(f"Model: {model}, Prompt: {prompt[:50]}...,\n Calculated TPS: {tps:.2f} tokens/second")
            else:
                logger.warning(f"Cannot calculate TPS - eval_count: {eval_count}, eval_duration: {eval_duration}")
            
            response_text = data.get("response")
            if is_eval: logger.info(f"Response text: {response_text}")
            # Remove <think>...</think> sections from the response, if present
            import re
            if response_text:
                # Remove all occurrences of <think>...</think> (non-greedy, multiline)
                response_text = re.sub(r"<think>.*?</think>", "", response_text, flags=re.DOTALL)
                # Optionally, strip leading/trailing whitespace
                response_text = response_text.strip()
            # Fallback: estimate tokens if not present
            if prompt_tokens is None:
                prompt_tokens = len(prompt.split())
            if eval_count is None and response_text:
                eval_count = len(response_text.split())
            return {
                "response": response_text,
                "prompt_tokens": prompt_tokens,
                "eval_count": eval_count,
                "tps": tps
            }
        except requests.exceptions.RequestException as e:
            logger.error(f"Error connecting to Ollama server: {e}")
            logger.error(f"Please ensure Ollama is running and the model: {model} is pulled.")
            return None 
        except Exception as e:
            logger.error(f"Error getting Ollama response: {e}")
            return None