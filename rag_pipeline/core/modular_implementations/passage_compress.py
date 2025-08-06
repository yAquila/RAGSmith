import logging
from typing import List, Dict, Any, TypedDict, Tuple

from rag_pipeline.core.modular_framework import (
    PassageCompressComponent, Document, Query
)

logger = logging.getLogger(__name__)

class PassageCompressResult(TypedDict):
    documents: List[Document]
    embedding_token_count: float
    llm_token_count: Dict[str, Dict[str, float]]  # {"model_name": {"in": float, "out": float}}

class NonePassageCompress(PassageCompressComponent):
    """No passage compression - pass documents through unchanged"""
    
    async def compress_passages(self, documents: List[Document], query: Query) -> PassageCompressResult:
        """Pass documents through unchanged"""
        result = PassageCompressResult(
            documents=documents,
            embedding_token_count=0.0,
            llm_token_count={}
        )
        return result


class TreeSummarize(PassageCompressComponent):
    """Compress passages using tree summarization"""
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
    

    def summarize_chunk(self, text: str) -> Tuple[str, int, int]:
        prompt = (
            "Write a summary of the following. Try to use only the information provided. Try to include as many key details as possible.\n"
            "{context_str}\n"
            'SUMMARY:\n'
        )

        response = self.client.get_ollama_response(self.config.get("tree_summarize_model", "gemma3:4b"), prompt.format(context_str=text))
        if isinstance(response, dict):
            return response.get('response', '').strip(), response.get('prompt_tokens', 0), response.get('eval_count', 0)
        else:
            return response.strip(), 0, 0

    async def compress_passages(self, documents: List[Document], query: Query) -> PassageCompressResult:
        """
        Recursively summarize the content of the provided documents using a tree summarization approach.
        Each document's content is treated as a chunk. Summarization is performed in groups of max_fan_in.
        """
        # Extract text chunks from documents
        text_chunks = [doc.content for doc in documents]
        doc_metadatas = [doc.metadata for doc in documents]

        current_level = text_chunks
        current_metadatas = doc_metadatas

        llm_token_count = {}
        model = self.config.get("llm_summarize_model", "gemma3:4b")
        total_prompt_tokens = 0.0
        total_eval_count = 0.0

        # Helper to estimate token count (very rough)
        def estimate_tokens(text):
            return len(text.split()) / 0.75  # crude: 0.75 words/token

        while len(current_level) > 1:
            next_level = []
            next_metadatas = []
            for i in range(0, len(current_level), self.config.get("max_fan_in", 3)):
                group = current_level[i:i+self.config.get("max_fan_in", 3)]
                group_metadata = current_metadatas[i:i+self.config.get("max_fan_in", 3)]
                combined = "\n\n".join(group)
                summary, prompt_tokens, eval_count = self.summarize_chunk(combined)
                total_prompt_tokens += prompt_tokens if prompt_tokens > 0 else estimate_tokens(combined)
                total_eval_count += eval_count if eval_count > 0 else estimate_tokens(summary)
                next_level.append(summary)
                next_metadatas.append(group_metadata[0] if group_metadata else {})
            current_level = next_level
            current_metadatas = next_metadatas

        # Final summarized document
        summarized_content = current_level[0] if current_level else ""
        summarized_metadata = current_metadatas[0] if current_metadatas else {}

        summarized_doc = Document(
            doc_id=documents[0].doc_id,
            content=summarized_content,
            metadata=summarized_metadata
        )

        llm_token_count[model] = {"in": total_prompt_tokens, "out": total_eval_count}
        result = PassageCompressResult(
            documents=[summarized_doc],
            embedding_token_count=estimate_tokens(summarized_content),
            llm_token_count=llm_token_count
        )
        return result

class LLMSummarizeEachChunk(PassageCompressComponent):
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
        llm_token_count = {}
        model = self.config.get("llm_summarize_model", "gemma3:4b")
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
            response = self.client.get_ollama_response(model, prompt.format(document=doc.content))
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

        llm_token_count[model] = {"in": total_prompt_tokens, "out": total_eval_count}
        result = PassageCompressResult(
            documents=compressed_documents,
            embedding_token_count=0.0,
            llm_token_count=llm_token_count
        )
        return result

class LLMLinguaCompress(PassageCompressComponent):
    """Compress passages using LLMLingua"""
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.llm_lingua = None
        self._setup_client()

    def _setup_client(self):
        """Setup the appropriate LLM client"""
        from llmlingua import PromptCompressor
        self.llm_lingua = PromptCompressor(model_name=self.config.get("llm_lingua_model", "microsoft/llmlingua-2-xlm-roberta-large-meetingbank"), use_llmlingua2=True)

    
    async def compress_passages(self, documents: List[Document], query: Query) -> PassageCompressResult:
        """Compress passages using LLMLingua"""

        contents = [doc.content for doc in documents]
        result = self.llm_lingua.compress_prompt(context=contents, question=query.processed_text, rate=self.config.get("llm_lingua_compression_rate", 0.33))
        logger.info(f"LLMLinguaCompress compression rate: {result['rate']}")
        compressed_docs = []
        for i, compressed_prompt in enumerate(result['compressed_prompt_list']):
            compressed_docs.append(Document(
                doc_id=documents[i].doc_id,
                content=compressed_prompt,
                score=documents[i].score,
                metadata=documents[i].metadata
            ))
        llm_input_token_count = result['origin_tokens']
        llm_output_token_count = result['compressed_tokens']
        llm_token_count = {}
        model = self.config.get("llm_lingua_model", "microsoft/llmlingua-2-xlm-roberta-large-meetingbank")
        llm_token_count[model] = {"in": llm_input_token_count, "out": llm_output_token_count}
        return PassageCompressResult(
            documents=compressed_docs,
            embedding_token_count=0.0,
            llm_token_count=llm_token_count
        )