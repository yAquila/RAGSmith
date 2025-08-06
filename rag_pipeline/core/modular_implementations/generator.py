
import logging
from typing import Dict, Any, TypedDict

from rag_pipeline.core.modular_framework import (
    GeneratorComponent, Query
)

logger = logging.getLogger(__name__)

class GeneratorResult(TypedDict):
    text: str
    embedding_token_count: float
    llm_token_count: Dict[str, Dict[str, float]]  # {"model_name": {"in": float, "out": float}}


class LLMGenerator(GeneratorComponent):
    """✅ CURRENTLY IMPLEMENTED - LLM-based generation (Ollama/Gemini)"""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.client = None
        self._setup_client()
    
    def _setup_client(self):
        """Setup the appropriate LLM client"""
        provider = self.config.get("provider", "ollama")
        
        try:
            if provider.lower() == "ollama":
                from rag_pipeline.util.api.ollama_client import OllamaUtil
                self.client = OllamaUtil
            elif provider.lower() == "gemini":
                from rag_pipeline.util.api.gemini_client import GeminiUtil
                self.client = GeminiUtil
            else:
                raise ValueError(f"Unsupported provider: {provider}")
                
        except Exception as e:
            logger.error(f"Failed to setup {provider} client: {e}")
            raise
    
    async def generate(self, prompt: str, query: Query) -> GeneratorResult:
        """Generate answer using LLM. Returns (generated_text, prompt_tokens, eval_count)"""
        try:
            model = self.config.get("model", "gpt-3.5-turbo")
            if self.config.get("provider", "ollama").lower() == "ollama":
                response = self.client.get_ollama_response(model, prompt)
                if isinstance(response, dict):
                    result = GeneratorResult(
                        text=response.get('response', ''),
                        embedding_token_count=0.0,
                        llm_token_count={model: {"in": float(response.get('prompt_tokens', len(prompt.split()))), "out": float(response.get('eval_count', 0))}}
                    )
                    return result
                else:
                    result = GeneratorResult(
                        text=str(response),
                        embedding_token_count=0.0,
                        llm_token_count={model: {"in": float(len(prompt.split())), "out": float(len(str(response).split()))}}
                    )
                    return result
            else:  # gemini
                response = self.client.get_gemini_response(model, prompt)
                if isinstance(response, dict):
                    result = GeneratorResult(
                        text=response.get('response', ''),
                        embedding_token_count=0.0,
                        llm_token_count={model: {"in": float(len(prompt.split())), "out": float(len(response.get('response', '').split()))}}
                    )
                    return result
                else:
                    result = GeneratorResult(
                        text=str(response),
                        embedding_token_count=0.0,
                        llm_token_count={model: {"in": float(len(prompt.split())), "out": float(len(str(response).split()))}}
                    )
                    return result
        except Exception as e:
            logger.error(f"Generation failed: {e}")
            result = GeneratorResult(
                text="",
                embedding_token_count=0.0,
                llm_token_count={self.config.get("model", "gpt-3.5-turbo"): {"in": float(len(prompt.split())), "out": 0.0}}
            )
            return result

class MultiLLMGenerator(GeneratorComponent):
    """Generate answer using multiple LLMs"""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.clients = {}
        self._setup_client()
    
    def _setup_client(self):
        """Setup the appropriate LLM client"""
        models = self.config.get("models", ["llama3.2:1b", "gemma3:4b"])
        ensemble_llm_model = self.config.get("ensemble_llm_model", "gemma3:4b")
        if ensemble_llm_model.lower().startswith("gemini"):
            from rag_pipeline.util.api.gemini_client import GeminiUtil
            self.clients[ensemble_llm_model] = GeminiUtil
        else:
            from rag_pipeline.util.api.ollama_client import OllamaUtil
            self.clients[ensemble_llm_model] = OllamaUtil

        for model in models:
            if model.lower().startswith("gemini"):
                from rag_pipeline.util.api.gemini_client import GeminiUtil
                self.clients[model] = GeminiUtil
            else:
                from rag_pipeline.util.api.ollama_client import OllamaUtil
                self.clients[model] = OllamaUtil

    async def generate(self, prompt: str, query: Query) -> GeneratorResult:
        """
        Generate answers using multiple LLMs. 
        Returns a list of tuples: (generated_text, prompt_tokens, eval_count, model_name)
        """
        models = self.config.get("models", ["llama3.2:1b", "gemma3:4b"])
        results = []
        llm_token_count = {}
        for model in models:
            try:
                client = self.clients.get(model)
                if client is None:
                    logger.error(f"No client found for model: {model}")
                    llm_token_count[model] = {"in": float(len(prompt.split())), "out": 0.0}
                    results.append(("", 0.0, float(len(prompt.split())), 0.0, model))
                    continue

                if model.lower().startswith("gemini"):
                    response = client.get_gemini_response(model, prompt)
                    if isinstance(response, dict):
                        generated_text = response.get('response', '')
                        prompt_tokens = float(len(prompt.split()))
                        eval_count = float(len(generated_text.split()))
                        llm_token_count[model] = {"in": prompt_tokens, "out": eval_count}
                        results.append((generated_text, 0.0, prompt_tokens, eval_count, model))
                    else:
                        llm_token_count[model] = {"in": float(len(prompt.split())), "out": 0.0}
                        results.append((str(response), 0.0, float(len(prompt.split())), 0.0, model))
                else:  # ollama
                    response = client.get_ollama_response(model, prompt)
                    if isinstance(response, dict):
                        generated_text = response.get('response', '')
                        prompt_tokens = float(response.get('prompt_tokens', len(prompt.split())))
                        eval_count = float(response.get('eval_count', len(generated_text.split())))
                        llm_token_count[model] = {"in": prompt_tokens, "out": eval_count}
                        results.append((generated_text, 0.0, prompt_tokens, eval_count, model))
                    else:
                        llm_token_count[model] = {"in": float(len(prompt.split())), "out": 0.0}
                        results.append((str(response), 0.0, float(len(prompt.split())), 0.0, model))
            except Exception as e:
                logger.error(f"Generation failed for model {model}: {e}")
                llm_token_count[model] = {"in": float(len(prompt.split())), "out": 0.0}
                results.append(("", 0.0, float(len(prompt.split())), 0.0, model))



        original_prompt_with_context = prompt
        total_prompt_tokens = sum([result[2] for result in results])
        total_eval_count = sum([result[3] for result in results])
        logger.info(f"Total prompt tokens: {total_prompt_tokens}")
        logger.info(f"Total eval count: {total_eval_count}")
        ensemble_prompt = """
You are a response synthesizer. Your task is to create one high-quality final answer from several different drafts.

**[THE ORIGINAL PROMPT]**
---
{original_prompt_with_context}
---

**[DRAFT RESPONSES TO COMBINE]**
---
"""

        for draft_response in results:
            ensemble_prompt += f"**Response from {draft_response[4]}:**\n{draft_response[0]}\n\n"

        ensemble_prompt += """      
---


**[YOUR TASK]**
1.  Read the **[THE ORIGINAL PROMPT]** to understand the user's goal.
2.  Review each **[DRAFT RESPONSE]**.
3.  Identify the best and most correct parts from all drafts.
4.  Combine these best parts into a single, clear, and helpful answer.
5.  Remove any repeated information.
6.  Your output must ONLY be the final, combined answer. Do not add any explanation of your process.

**[FINAL ANSWER]**

"""
        ensemble_prompt = ensemble_prompt.format(original_prompt_with_context=original_prompt_with_context)
        ensemble_llm_client = self.clients[self.config.get("ensemble_llm_model", "gemma3:4b")]
        if self.config.get("ensemble_llm_model", "gemma3:4b").lower().startswith("gemini"):
            ensemble_llm_response = ensemble_llm_client.get_gemini_response(self.config.get("ensemble_llm_model", "gemma3:4b"), ensemble_prompt)
        else:
            ensemble_llm_response = ensemble_llm_client.get_ollama_response(self.config.get("ensemble_llm_model", "gemma3:4b"), ensemble_prompt)
        logger.debug(f"Ensemble LLM prompt: {ensemble_prompt}")
        logger.debug(f"Ensemble LLM response: {ensemble_llm_response}")
        ensemble_model = self.config.get("ensemble_llm_model", "gemma3:4b")
        if isinstance(ensemble_llm_response, dict):
            ensemble_llm_generated_text = ensemble_llm_response.get('response', '')
            ensemble_llm_prompt_tokens = float(ensemble_llm_response.get('prompt_tokens', len(ensemble_prompt.split())))
            ensemble_llm_eval_count = float(ensemble_llm_response.get('eval_count', len(ensemble_llm_generated_text.split())))
            logger.info(f"Ensemble LLM prompt tokens: {ensemble_llm_prompt_tokens}")
            logger.info(f"Ensemble LLM eval count: {ensemble_llm_eval_count}")
            llm_token_count[ensemble_model] = {"in": ensemble_llm_prompt_tokens, "out": ensemble_llm_eval_count}
            result = GeneratorResult(
                text=ensemble_llm_generated_text,
                embedding_token_count=0.0,
                llm_token_count=llm_token_count
            )
            return result
        else:
            llm_token_count[ensemble_model] = {"in": len(ensemble_prompt.split()), "out": len(str(ensemble_llm_response).split())}
            result = GeneratorResult(
                text=str(ensemble_llm_response),
                embedding_token_count=0.0,
                llm_token_count=llm_token_count
            )
            return result
