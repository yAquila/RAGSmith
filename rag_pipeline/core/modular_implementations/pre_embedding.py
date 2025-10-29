import logging
from typing import List, TypedDict, Dict, Any, Optional
import re

from rag_pipeline.core.modular_framework import (
    PreEmbeddingComponent, Document
)

logger = logging.getLogger(__name__)

class PreEmbeddingResult(TypedDict):
    documents: List[Document]
    embedding_token_count: float
    llm_token_count: Dict[str, Dict[str, float]]  # {"model_name": {"in": float, "out": float}}

class NonePreEmbedding(PreEmbeddingComponent):
    """No pre-embedding processing - pass documents through unchanged"""
    
    async def process_documents(self, documents: List[Document]) -> PreEmbeddingResult:
        """Pass documents through unchanged"""
        result = PreEmbeddingResult(
            documents=documents,
            embedding_token_count=0.0,
            llm_token_count={}
        )
        return result

class ContextualChunkHeaders(PreEmbeddingComponent):
    """Add contextual headers to document chunks using LLM-based semantic analysis"""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.client = None
        self._setup_client()
    
    def _setup_client(self):
        """Setup the appropriate LLM client for header generation"""
        provider = self.config.get("header_provider", "ollama")
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
    
    def _generate_header_prompt(self, content: str) -> str:
        """Generate the prompt for header generation based on configuration strategy"""
        strategy = self.config.get("header_generation_strategy", "semantic")
        
        if strategy == "semantic":
            prompt_template = self.config.get("header_semantic_prompt", 
                "Generate a concise header (3-5 words) that captures the main topic of this document section.\n\nDocument content:\n{content}\n\nHeader:")
            return prompt_template.format(content=content)
        
        elif strategy == "query_aware":
            prompt_template = self.config.get("header_query_aware_prompt",
                "Generate a header that would help answer questions about this content.\n\nDocument content:\n{content}\n\nHeader:")
            return prompt_template.format(content=content)
        
        elif strategy == "structural":
            prompt_template = self.config.get("header_structural_prompt",
                "Extract or generate a section title for this content.\n\nDocument content:\n{content}\n\nTitle:")
            return prompt_template.format(content=content)
        
        else:
            # Default to semantic strategy
            logger.warning(f"Unknown header generation strategy: {strategy}. Defaulting to semantic.")
            prompt_template = self.config.get("header_semantic_prompt",
                "Generate a concise header (3-5 words) that captures the main topic of this document section.\n\nDocument content:\n{content}\n\nHeader:")
            return prompt_template.format(content=content)
    
    def _clean_header(self, header: str) -> str:
        """Clean and validate the generated header based on configuration"""
        if not header:
            return ""
        
        # Remove common prefixes and suffixes
        header = re.sub(r'^(Header|Title|Section):\s*', '', header, flags=re.IGNORECASE)
        header = header.strip()
        
        # Remove quotes if present
        header = re.sub(r'^["\']|["\']$', '', header)
        
        # Limit length based on configuration
        max_length = self.config.get("header_max_length", 50)
        if len(header) > max_length:
            header = header[:max_length].rsplit(' ', 1)[0]  # Cut at word boundary
        
        return header
    
    def _generate_header(self, content: str) -> Optional[str]:
        """Generate a header for the given content using configuration settings"""
        try:
            logger.info(f"ContextualChunkHeaders: Generating header for content: {content[:100]}...")
            
            prompt = self._generate_header_prompt(content)
            model = self.config.get("header_generation_model", "alibayram/Qwen3-30B-A3B-Instruct-2507:latest")
            provider = self.config.get("header_provider", "ollama")
            
            logger.info(f"ContextualChunkHeaders: Using model {model} with provider {provider}")
            logger.debug(f"ContextualChunkHeaders: Generated prompt: {prompt[:200]}...")
            
            if provider.lower() == "ollama":
                logger.info("ContextualChunkHeaders: Calling Ollama client...")
                response = self.client.get_ollama_response(model, prompt)
            elif provider.lower() == "gemini":
                logger.info("ContextualChunkHeaders: Calling Gemini client...")
                response = self.client.get_gemini_response(model, prompt)
            else:
                raise ValueError(f"Unsupported provider: {provider}")
            
            logger.info(f"ContextualChunkHeaders: Got response: {type(response)} - {str(response)[:200]}...")
            
            if response and isinstance(response, dict):
                header_text = response.get('response', '').strip()
                cleaned_header = self._clean_header(header_text)
                logger.info(f"ContextualChunkHeaders: Cleaned header: '{cleaned_header}'")
                return cleaned_header
            elif response and isinstance(response, str):
                cleaned_header = self._clean_header(response)
                logger.info(f"ContextualChunkHeaders: Cleaned header from string: '{cleaned_header}'")
                return cleaned_header
            else:
                logger.warning(f"ContextualChunkHeaders: Failed to generate header - invalid response type or empty response")
                return None
                
        except Exception as e:
            logger.error(f"ContextualChunkHeaders: Error generating header: {e}")
            import traceback
            logger.error(f"ContextualChunkHeaders: Full traceback: {traceback.format_exc()}")
            return None
    
    def _format_document_with_header(self, doc: Document, header: str) -> Document:
        """Format document with the generated header using configuration template"""
        if not header:
            return doc
        
        # Use the header template from configuration
        template = self.config.get("header_template", "Document Section: {title}\nContext: {context}\n\n")
        formatted_content = template.format(title=header, context=doc.content)
        
        # Create new metadata with header information
        new_metadata = {
            **doc.metadata,
            "original_content": doc.content,
            "generated_header": header,
            "technique": "contextual_chunk_headers",
            "header_generation_strategy": self.config.get("header_generation_strategy", "semantic"),
            "header_provider": self.config.get("header_provider", "ollama")
        }
        
        return Document(
            doc_id=doc.doc_id,
            content=formatted_content,
            metadata=new_metadata
        )
    
    async def process_documents(self, documents: List[Document]) -> PreEmbeddingResult:
        """Add contextual headers to documents using LLM-based generation"""
        logger.info(f"ContextualChunkHeaders: Processing {len(documents)} documents with contextual headers")
        
        documents_with_headers = []
        total_prompt_tokens = 0.0
        total_output_tokens = 0.0
        
        for i, doc in enumerate(documents):
            try:
                logger.info(f"ContextualChunkHeaders: Processing document {i+1}/{len(documents)}: {doc.doc_id}")
                
                # Generate header for the document
                header = self._generate_header(doc.content)
                logger.info(f"ContextualChunkHeaders: Generated header for {doc.doc_id}: '{header}'")
                
                # Format document with header
                formatted_doc = self._format_document_with_header(doc, header)
                documents_with_headers.append(formatted_doc)
                
                # Estimate token counts (will be updated with actual counts if available)
                if header:
                    total_prompt_tokens += len(doc.content.split()) + 20  # Rough estimate
                    total_output_tokens += len(header.split())
                
                logger.info(f"ContextualChunkHeaders: Successfully processed document {doc.doc_id}")
                
            except Exception as e:
                logger.error(f"ContextualChunkHeaders: Error processing document {doc.doc_id}: {e}")
                import traceback
                logger.error(f"ContextualChunkHeaders: Full traceback: {traceback.format_exc()}")
                # Fallback: use original document without header
                documents_with_headers.append(doc)
        
        logger.info(f"ContextualChunkHeaders: Successfully processed {len(documents_with_headers)} documents with headers")
        logger.info(f"ContextualChunkHeaders: Token counts - Input: {total_prompt_tokens}, Output: {total_output_tokens}")
        
        llm_token_count = {}
        model = self.config.get("header_generation_model", "alibayram/Qwen3-30B-A3B-Instruct-2507:latest")
        llm_token_count[model] = {"in": total_prompt_tokens, "out": total_output_tokens}
        result = PreEmbeddingResult(
            documents=documents_with_headers,
            embedding_token_count=0.0,  # Headers don't affect embedding tokens
            llm_token_count=llm_token_count
        )
        logger.info(f"ContextualChunkHeaders: Returning result with {len(result['documents'])} documents")
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
                response = self.client.get_ollama_response(self.config.get("hype_model", "alibayram/Qwen3-30B-A3B-Instruct-2507:latest"), prompt)
            elif self.config.get("provider", "ollama").lower() == "gemini":
                response = self.client.get_gemini_response(self.config.get("hype_model", "alibayram/Qwen3-30B-A3B-Instruct-2507:latest"), prompt)
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
        llm_token_count = {}
        model = self.config.get("hype_model", "alibayram/Qwen3-30B-A3B-Instruct-2507:latest")
        llm_token_count[model] = {"in": total_prompt_tokens, "out": total_eval_count}
        logger.info(f"Documents to embed[:2]: {documents_to_embed[:2]}")
        result = PreEmbeddingResult(
            documents=documents_to_embed,
            embedding_token_count=0.0,
            llm_token_count=llm_token_count
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
            llm_token_count={}
        )
        return result
