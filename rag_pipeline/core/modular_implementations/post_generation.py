import logging
from typing import TypedDict, Dict, Any

from rag_pipeline.core.modular_framework import (
    PostGenerationComponent, Query, Context
)

logger = logging.getLogger(__name__)

class PostGenerationResult(TypedDict):
    text: str
    embedding_token_count: float
    llm_token_count: Dict[str, Dict[str, float]]  # {"model_name": {"in": float, "out": float}}

class NonePostGeneration(PostGenerationComponent):
    """No post-generation processing - return answer unchanged"""
    
    async def post_process(self, generated_answer: str, query: Query, context: Context) -> PostGenerationResult:
        """Return answer unchanged"""
        result = PostGenerationResult(
            text=generated_answer,
            embedding_token_count=0.0,
            llm_token_count={}
        )
        return result


class ReflectionRevising(PostGenerationComponent):
    """Refine answer using reflection and revising"""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.client = None
        self._setup_client()
    
    def _setup_client(self):
        """Setup the appropriate LLM client"""
        provider = self.config.get("provider", "ollama")
        if provider.lower() == "ollama":
            from rag_pipeline.util.api.ollama_client import OllamaUtil
            self.client = OllamaUtil
        elif provider.lower() == "gemini":
            from rag_pipeline.util.api.gemini_client import GeminiUtil
            self.client = GeminiUtil
        else:
            raise ValueError(f"Unsupported provider: {provider}")
    
    def _get_reflection_response(self, query_text: str, current_answer: str) -> tuple[str, int, int]:
        """Get reflection evaluation from LLM"""
        reflection_prompt = f"""
        Evaluate the following question and answer pair:

        Question: {query_text}
        
        Answer: {current_answer}
        
        Please evaluate the answer based on these criteria:
        1. Completeness: Does it fully address all aspects of the question?
        2. Accuracy: Is the information correct and well-supported by sources?
        3. Clarity: Is the reasoning process clear and well-structured?
        4. Source Attribution: Are all sources properly cited?
        
        Provide your evaluation in this format:
        Completeness: [Score 1-5]
        Accuracy: [Score 1-5]
        Clarity: [Score 1-5]
        Source Attribution: [Score 1-5]
        Overall Assessment: [Pass/Fail]
        Improvement Suggestions: [List specific areas for improvement]
        """

        response = self.client.get_ollama_response(
            self.config.get("reflection_revising_model", "alibayram/Qwen3-30B-A3B-Instruct-2507:latest"), 
            reflection_prompt
        )
        
        if isinstance(response, dict):
            return response.get('response', '').strip(), response.get('prompt_tokens', 0), response.get('eval_count', 0)
        else:
            return response.strip(), 0, 0
    
    def _get_improved_answer(self, query_text: str, current_answer: str, reflection_feedback: str) -> tuple[str, int, int]:
        """Get improved answer based on reflection feedback"""
        enhanced_prompt = f"""
        Previous Answer: {current_answer}
        
        Evaluation Feedback: {reflection_feedback}
        
        Please provide an improved answer addressing the feedback above.
        """

        response = self.client.get_ollama_response(
            self.config.get("reflection_revising_model", "alibayram/Qwen3-30B-A3B-Instruct-2507:latest"), 
            enhanced_prompt
        )
        
        if isinstance(response, dict):
            return response.get('response', '').strip(), response.get('prompt_tokens', 0), response.get('eval_count', 0)
        else:
            return response.strip(), 0, 0
    
    async def post_process(self, generated_answer: str, query: Query, context: Context) -> PostGenerationResult:
        """Post-process answer using reflection and revising"""
        current_answer = generated_answer
        max_retries = self.config.get("max_revisions", 2)
        retry_count = 0
        
        total_prompt_tokens = 0.0
        total_eval_count = 0.0
        
        while retry_count < max_retries:
            # Get reflection evaluation
            reflection, prompt_tokens, eval_count = self._get_reflection_response(
                query.processed_text, current_answer
            )
            logger.debug(f"Reflection: {reflection}")
            total_prompt_tokens += prompt_tokens if prompt_tokens > 0 else 0
            total_eval_count += eval_count if eval_count > 0 else 0
            
            # Check if the answer needs improvement
            if "Overall Assessment: Fail" in reflection:
                retry_count += 1
                if retry_count < max_retries:
                    # Get improved answer based on reflection feedback
                    improved_answer, imp_prompt_tokens, imp_eval_count = self._get_improved_answer(
                        query.processed_text, current_answer, reflection
                    )
                    logger.debug(f"Improved Answer: {improved_answer}")
                    total_prompt_tokens += imp_prompt_tokens if imp_prompt_tokens > 0 else 0
                    total_eval_count += imp_eval_count if imp_eval_count > 0 else 0
                    current_answer = improved_answer
                else:
                    # Max retries reached, keep the last answer
                    break
            else:
                # Answer passed evaluation, no need for further improvement
                break
        
        llm_token_count = {}
        model = self.config.get("reflection_revising_model", "alibayram/Qwen3-30B-A3B-Instruct-2507:latest")
        llm_token_count[model] = {"in": total_prompt_tokens, "out": total_eval_count}
        result = PostGenerationResult(
            text=current_answer,
            embedding_token_count=0.0,
            llm_token_count=llm_token_count
        )
        return result
