import logging
from typing import List, TypedDict, Dict, Any

from rag_pipeline.core.modular_framework import (
    PreEmbeddingComponent, Document
)

logger = logging.getLogger(__name__)

class PreEmbeddingResult(TypedDict):
    documents: List[Document]
    embedding_token_count: float
    llm_input_token_count: float
    llm_output_token_count: float

class NonePreEmbedding(PreEmbeddingComponent):
    """No pre-embedding processing - pass documents through unchanged"""
    
    async def process_documents(self, documents: List[Document]) -> PreEmbeddingResult:
        """Pass documents through unchanged"""
        result = PreEmbeddingResult(
            documents=documents,
            embedding_token_count=0.0,
            llm_input_token_count=0.0,
            llm_output_token_count=0.0
        )
        return result

class ContextualChunkHeaders(PreEmbeddingComponent):
    """Add contextual headers to document chunks"""
    
    async def process_documents(self, documents: List[Document]) -> PreEmbeddingResult:
        """Add contextual headers to documents"""
        logger.warning("ContextualChunkHeaders not fully implemented yet")
        result = PreEmbeddingResult(
            documents=documents,
            embedding_token_count=0.0,
            llm_input_token_count=0.0,
            llm_output_token_count=0.0
        )
        return result
    
class HyPE(PreEmbeddingComponent):
    """Use HyPE to embed documents"""

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


    async def process_documents(self, documents: List[Document]) -> PreEmbeddingResult:
        """Use HyPE to embed documents"""

        documents_to_embed = []
        total_prompt_tokens = 0
        total_eval_count = 0
        for doc in documents:
            prompt = self.config.get("hype_prompt", "").format(num_hype_questions=self.config.get("num_hype_questions", 3), document=doc.content)
            if self.config.get("provider", "ollama").lower() == "ollama":
                response = self.client.get_ollama_response(self.config.get("hype_model", "gemma3:4b"), prompt)
            elif self.config.get("provider", "ollama").lower() == "gemini":
                response = self.client.get_gemini_response(self.config.get("hype_model", "gemma3:4b"), prompt)
            else:
                raise ValueError(f"Unsupported provider: {self.config.get('provider', 'ollama')}")
            logger.info(f"HyPE response: {response}")
            if isinstance(response, dict):
                hype_questions = response.get('response', '').split("\n")
                total_prompt_tokens += float(response.get('prompt_tokens', len(prompt.split())))
                total_eval_count += float(response.get('eval_count', 0))
            else:
                hype_questions = response.split("\n")

            hype_questions = [line.strip() for line in hype_questions if line.strip()]
            for i, hype_question in enumerate(hype_questions):
                new_metadata = {
                    **doc.metadata,
                    "original_content": doc.content,
                    "original_doc_id": doc.doc_id,
                    "hype_doc_id": f"{doc.doc_id}___{i}",
                }
                documents_to_embed.append(Document(
                    doc_id=f"{doc.doc_id}___{i}",
                    content=hype_question,
                    metadata=new_metadata
                ))
        logger.info(f"Documents to embed[:2]: {documents_to_embed[:2]}")
        result = PreEmbeddingResult(
            documents=documents_to_embed,
            embedding_token_count=0.0,
            llm_input_token_count=total_prompt_tokens,
            llm_output_token_count=total_eval_count
        )
        return result

class ParentDocumentRetriever(PreEmbeddingComponent):

    async def process_documents(self, documents: List[Document]) -> PreEmbeddingResult:
        """Retrieve parent documents"""

        documents_to_embed = []
        for doc in documents:
            from langchain.text_splitter import RecursiveCharacterTextSplitter
            split_docs = RecursiveCharacterTextSplitter(
                chunk_size=self.config.get("pdr_chunk_size", 100),
                chunk_overlap=self.config.get("pdr_chunk_overlap", 20),
            ).split_text(doc.content)
            for i, split_doc in enumerate(split_docs):
                documents_to_embed.append(Document(
                    doc_id=f"{doc.doc_id}___{i}",
                    content=split_doc,
                    metadata={
                        **doc.metadata,
                        "original_content": doc.content,
                        "original_doc_id": doc.doc_id,
                        "pdr_doc_id": f"{doc.doc_id}___{i}",
                        "technique": "parent_document_retriever"
                    }
                ))

        result = PreEmbeddingResult(
            documents=documents_to_embed,
            embedding_token_count=0.0,
            llm_input_token_count=0.0,
            llm_output_token_count=0.0
        )
        return result
