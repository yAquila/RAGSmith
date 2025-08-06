
import logging
from typing import List, TypedDict, Dict

from rag_pipeline.core.modular_framework import (
    PromptMakerComponent, Document, Query
)

logger = logging.getLogger(__name__)

class PromptMakerResult(TypedDict):
    text: str
    embedding_token_count: float
    llm_token_count: Dict[str, Dict[str, float]]  # {"model_name": {"in": float, "out": float}}

class SimpleListingPromptMaker(PromptMakerComponent):
    """✅ CURRENTLY IMPLEMENTED - Simple listing of documents in prompt"""
    
    async def make_prompt(self, query: Query, documents: List[Document]) -> PromptMakerResult:
        """Create a simple prompt by listing documents"""
        template = self.config.get("template", "Context:\n{context}\n\nQuestion: {query}\n\nAnswer:")
        separator = self.config.get("separator", "\n\n")
        include_doc_numbers = self.config.get("include_doc_numbers", True)
        include_scores = self.config.get("include_scores", False)
        
        # Format context from documents
        context_parts = []
        for i, doc in enumerate(documents, 1):
            content = doc.content.strip()
            if content:
                if include_doc_numbers:
                    if include_scores and doc.score is not None:
                        context_parts.append(f"Document {i} (Score: {doc.score:.3f}):\n{content}")
                    else:
                        context_parts.append(f"Document {i}:\n{content}")
                else:
                    context_parts.append(content)
        
        context = separator.join(context_parts)
        
        # Format final prompt
        prompt = template.format(context=context, query=query.processed_text)
        result = PromptMakerResult(
            text=prompt,
            embedding_token_count=0.0,
            llm_token_count={}
        )
        return result

class LongContextReorder(PromptMakerComponent): # Top n passages are reinforced by putting them at the end

    async def make_prompt(self, query: Query, documents: List[Document]) -> PromptMakerResult:
        """Reorder documents to put long context passages first"""
        template = self.config.get("template", "Context:\n{context}\n\nQuestion: {query}\n\nAnswer:")
        separator = self.config.get("separator", "\n\n")
        include_doc_numbers = self.config.get("include_doc_numbers", True)
        include_scores = self.config.get("include_scores", False)
        reinforce_top_n_passages = self.config.get("reinforce_top_n_passages", 1)
        
        # Format context from documents
        context_parts = []
        for i, doc in enumerate(documents):
            content = doc.content.strip()
            if content:
                if include_doc_numbers:
                    if include_scores and doc.score is not None:
                        context_parts.append(f"Document {i} (Score: {doc.score:.3f}):\n{content}")
                    else:
                        context_parts.append(f"Document {i}:\n{content}")
                else:
                    context_parts.append(content)
        if len(context_parts) > reinforce_top_n_passages:
            for i in range(reinforce_top_n_passages-1, -1, -1):
                context_parts.append(context_parts[i]) # Reinforce top n passages by putting them at the end
        context = separator.join(context_parts)
        
        # Format final prompt
        prompt = template.format(context=context, query=query.processed_text)
        result = PromptMakerResult(
            text=prompt,
            embedding_token_count=0.0,
            llm_token_count={}
        )
        return result

