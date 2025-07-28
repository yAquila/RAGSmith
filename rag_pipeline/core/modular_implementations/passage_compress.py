import logging
from typing import List, Dict, Any, TypedDict

from rag_pipeline.core.modular_framework import (
    PassageCompressComponent, Document, Query
)

logger = logging.getLogger(__name__)

class PassageCompressResult(TypedDict):
    documents: List[Document]
    embedding_token_count: float
    llm_input_token_count: float
    llm_output_token_count: float

class NonePassageCompress(PassageCompressComponent):
    """No passage compression - pass documents through unchanged"""
    
    async def compress_passages(self, documents: List[Document], query: Query) -> PassageCompressResult:
        """Pass documents through unchanged"""
        result = PassageCompressResult(
            documents=documents,
            embedding_token_count=0.0,
            llm_input_token_count=0.0,
            llm_output_token_count=0.0
        )
        return result


class TreeSummarize(PassageCompressComponent):
    """Compress passages using tree summarization"""
    
    async def compress_passages(self, documents: List[Document], query: Query) -> PassageCompressResult:
        """Compress documents using tree summarization"""
        # Placeholder implementation
        logger.warning("TreeSummarize not fully implemented yet")
        result = PassageCompressResult(
            documents=documents,
                embedding_token_count=0.0,
                llm_input_token_count=0.0,
                llm_output_token_count=0.0
            )
        return result

class LLMSummarize(PassageCompressComponent):
    """Compress passages using LLM"""
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

    async def compress_passages(self, documents: List[Document], query: Query) -> PassageCompressResult:
        """Compress documents using LLM"""
        compressed_documents = []
        total_prompt_tokens = 0
        total_eval_count = 0
        for doc in documents:
            default_prompt = """
You are an efficient Document Compressor. Your task is to read the document provided below and extract its key information.

### Instructions
1.  Identify and list the main facts, figures, names, and core concepts from the text.
2.  Present these points as a concise, factual list.
3.  Do not add any information, opinions, or interpretations not present in the original text.
4.  The output should be a dense, information-rich summary.

### Document to Compress
{document}

### Compressed Summary
            """
            prompt = self.config.get("prompt", default_prompt)
            response = self.client.get_ollama_response(self.config.get("model", "gemma3:4b"), prompt.format(document=doc.content))
            if isinstance(response, dict):
                total_prompt_tokens += float(response.get('prompt_tokens', len(prompt.split())))
                total_eval_count += float(response.get('eval_count', 0))
                compressed_documents.append(Document(
                    doc_id=doc.doc_id,
                    content=response.get('response', ''),
                    score=doc.score,
                    metadata=doc.metadata
                ))
            else:
                compressed_documents.append(doc)

        result = PassageCompressResult(
            documents=compressed_documents,
            embedding_token_count=0.0,
            llm_input_token_count=total_prompt_tokens,
            llm_output_token_count=total_eval_count
        )
        return result
