
import logging
from typing import List, Dict, Any, TypedDict
from rag_pipeline.core.modular_framework import (
    QueryExpansionComponent, Query
)
from rag_pipeline.core.modular_implementations.retrieval import GraphRAG

logger = logging.getLogger(__name__)


class QueryExpansionResult(TypedDict):
    query: Query
    embedding_token_count: float
    llm_token_count: Dict[str, Dict[str, float]]  # {"model_name": {"in": float, "out": float}}

class NoneQueryExpansion(QueryExpansionComponent):
    """No query expansion - return original query"""
    
    async def expand_query(self, query: str) -> QueryExpansionResult:
        """Return original query unchanged"""
        result = QueryExpansionResult(
            query=Query(
                original_text=query,
                processed_text=query,
                expanded_queries=None,
                metadata={}
            ),
            embedding_token_count=0.0,
            llm_token_count={}
        )
        return result


class SimpleMultiQuery(QueryExpansionComponent):
    """Generate multiple variations of the query"""
    
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

    async def expand_query(self, query: str) -> QueryExpansionResult:
        """Compress documents using LLM"""
        expanded_queries = []
        llm_token_count = {}
        num_expanded_queries = self.config.get("num_expanded_queries", 3)
        model = self.config.get("model", "alibayram/Qwen3-30B-A3B-Instruct-2507:latest")
        
        prompt = self.config.get("prompt", "")
        response = self.client.get_ollama_response(model, prompt.format(query=query, num_expanded_queries=num_expanded_queries))
        if isinstance(response, dict):
            prompt_tokens = float(response.get('prompt_tokens', len(prompt.split())))
            output_tokens = float(response.get('eval_count', 0))
            llm_token_count[model] = {"in": prompt_tokens, "out": output_tokens}
            for exp_query in response.get('response', '').split('\n'):
                if exp_query.strip() != '':
                    if exp_query and exp_query[0].isdigit():
                        exp_query = exp_query[exp_query.find('.') + 1:].strip()
                    else:
                        exp_query = exp_query.strip()
                    expanded_queries.append(Query(
                        original_text=exp_query,
                        processed_text=exp_query,
                        expanded_queries=None,
                        metadata={}
                    ))
        else:
            expanded_queries.append(Query(
                original_text=response.get('response', ''),
                processed_text=response.get('response', ''),
                expanded_queries=None,
                metadata={}
            ))
        logger.debug(f"Expanded queries: {expanded_queries}")
        expanded_queries.append(Query(
            original_text=query,
            processed_text=query,
            expanded_queries=None,
            metadata={}
        ))
        result = QueryExpansionResult(
            query=Query(
                original_text=query,
                processed_text=query,
                expanded_queries=expanded_queries,
                metadata={"technique": self.config.get("technique", "simple_multi_query")}
            ),
            embedding_token_count=0.0,
            llm_token_count=llm_token_count
        )
        return result

class Decomposition(SimpleMultiQuery):
    """Decompose a query into multiple, more specific queries"""
    
    def __init__(self, config: Dict[str, Any]):
        config["prompt"] = config.get("decomposition_prompt", "")
        super().__init__(config)

    async def expand_query(self, query: str) -> QueryExpansionResult:
        """Decompose a query into multiple, more specific queries"""
        return await super().expand_query(query)
            
class RAGFusion(SimpleMultiQuery):
    """Combine multiple queries into a single query"""


    def __init__(self, config: Dict[str, Any]):
        config["combination_method"] = "reciprocal_rank_fusion"

        super().__init__(config)
    
    async def expand_query(self, query: str) -> QueryExpansionResult:
        """Combine multiple queries into a single query"""
        return await super().expand_query(query)

class HyDE(SimpleMultiQuery):
    """Combine multiple queries into a single query"""
    
    def __init__(self, config: Dict[str, Any]):
        config["prompt"] = config.get("hyde_prompt", "")
        super().__init__(config)
    def _parse_documents_from_response(self, response_text: str) -> List[str]:
        """
        Parse documents from response text that follows the format:
        Document 1:
        [content]
        Document 2:
        [content]
        ...
        """
        documents = []
        lines = response_text.strip().split('\n')
        current_document = []
        in_document = False
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Check if this line starts a new document
            if line.lower().startswith('document ') and ':' in line:
                # Save previous document if we have one
                if current_document and in_document:
                    documents.append('\n'.join(current_document).strip())
                    current_document = []
                in_document = True
                # Skip the "Document X:" line
                continue
            
            # If we're in a document, add the line
            if in_document:
                current_document.append(line)
        
        # Don't forget the last document
        if current_document and in_document:
            documents.append('\n'.join(current_document).strip())
        
        return documents

    async def expand_query(self, query: str) -> QueryExpansionResult:
        """Generate documents using HyDE (Hypothetical Document Embeddings)"""
        expanded_queries = []
        llm_token_count = {}
        model = self.config.get("model", "alibayram/Qwen3-30B-A3B-Instruct-2507:latest")
        total_prompt_tokens = 0
        total_eval_count = 0
        num_expanded_queries = self.config.get("num_expanded_queries", 3)
        
        prompt = self.config.get("prompt", "")
        response = self.client.get_ollama_response(model, prompt.format(query=query, num_expanded_queries=num_expanded_queries))
        
        if isinstance(response, dict):
            total_prompt_tokens += float(response.get('prompt_tokens', len(prompt.split())))
            total_eval_count += float(response.get('eval_count', 0))
            response_text = response.get('response', '')
            
            # Debug: Log the raw response
            logger.debug(f"HyDE raw response: {repr(response_text)}")
            
            documents = self._parse_documents_from_response(response_text)
            logger.debug(f"Parsed documents: {documents}")
            
            for doc in documents:
                if doc.strip():
                    expanded_queries.append(Query(
                        original_text=doc,
                        processed_text=doc,
                        expanded_queries=None,
                        metadata={}
                    ))
        else:
            # Handle case where response is not a dict
            response_text = str(response)
            logger.debug(f"HyDE non-dict response: {repr(response_text)}")
            documents = self._parse_documents_from_response(response_text)
            
            for doc in documents:
                if doc.strip():
                    expanded_queries.append(Query(
                        original_text=doc,
                        processed_text=doc,
                        expanded_queries=None,
                        metadata={}
                    ))
        
        llm_token_count[model] = {"in": total_prompt_tokens, "out": total_eval_count}
        logger.debug(f"Expanded queries: {expanded_queries}")
        result = QueryExpansionResult(
            query=Query(
                original_text=query,
                processed_text=query,
                expanded_queries=expanded_queries,
                metadata={"technique": self.config.get("technique", "hyde")}
            ),
            embedding_token_count=0.0,
            llm_token_count=llm_token_count
        )
        return result

class StepBackPrompting(SimpleMultiQuery):
    """Step back prompting"""

    def __init__(self, config: Dict[str, Any]):
        config["prompt"] = config.get("step_back_prompting_prompt", "")
        super().__init__(config)

    async def expand_query(self, query: str) -> QueryExpansionResult:
        """Step back prompting"""
        return await super().expand_query(query)


class SimpleQueryRefinement(QueryExpansionComponent):
    """Simple Query Refinement/Rewriting with LLM - improves single query"""
    
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

    async def expand_query(self, query: str) -> QueryExpansionResult:
        """Refine/rewrite the query using LLM"""
        
        # Get configuration parameters
        prompt_template = self.config.get("refinement_clarification_prompt", "")
        strategy = self.config.get("refinement_strategy", "clarification")
        model = self.config.get("refinement_model", "alibayram/Qwen3-30B-A3B-Instruct-2507:latest")
        temperature = self.config.get("refinement_temperature", 0.1)
        max_tokens = self.config.get("refinement_max_tokens", 100)
        
        # Format prompt based on strategy - use config prompts
        if strategy == "clarification":
            prompt = prompt_template.format(query=query)
        elif strategy == "rephrasing":
            prompt = self.config.get("refinement_rephrasing_prompt", "").format(query=query)
        elif strategy == "keyword_extraction":
            prompt = self.config.get("refinement_keyword_extraction_prompt", "").format(query=query)
        else:
            # Default to clarification
            prompt = prompt_template.format(query=query)
        
        try:
            # Generate refined query using the correct method
            if self.config.get("provider", "ollama").lower() == "ollama":
                response = self.client.get_ollama_response(model, prompt)
                if response and isinstance(response, dict):
                    refined_query = response.get("response", "").strip()
                else:
                    logger.warning("Invalid response from Ollama, using original query")
                    refined_query = query
            elif self.config.get("provider", "ollama").lower() == "gemini":
                response = self.client.get_gemini_response(model, prompt)
                if response and isinstance(response, dict):
                    refined_query = response.get("response", "").strip()
                else:
                    logger.warning("Invalid response from Gemini, using original query")
                    refined_query = query
            else:
                logger.warning("Unknown provider, using original query")
                refined_query = query
            
            # If response is empty or too short, use original query
            if not refined_query or len(refined_query) < 3:
                logger.warning(f"Refined query too short, using original: {refined_query}")
                refined_query = query
            
            # Calculate token counts from response
            llm_token_count = {}
            
            if self.config.get("provider", "ollama").lower() == "ollama" and response and isinstance(response, dict):
                prompt_tokens = float(response.get("prompt_tokens", len(prompt.split())))
                output_tokens = float(response.get("eval_count", len(refined_query.split())))
                llm_token_count[model] = {"in": prompt_tokens, "out": output_tokens}
            elif self.config.get("provider", "ollama").lower() == "gemini" and response and isinstance(response, dict):
                prompt_tokens = float(response.get("prompt_tokens", len(prompt.split())))
                output_tokens = float(response.get("eval_count", len(refined_query.split())))
                llm_token_count[model] = {"in": prompt_tokens, "out": output_tokens}
            else:
                # Fallback to rough estimation
                prompt_tokens = float(len(prompt.split()))
                output_tokens = float(len(refined_query.split()))
                llm_token_count[model] = {"in": prompt_tokens, "out": output_tokens}
            
            result = QueryExpansionResult(
                query=Query(
                    original_text=query,
                    processed_text=refined_query,  # Use refined query as processed
                    expanded_queries=[refined_query],
                    metadata={
                        "technique": "simple_query_refinement",
                        "strategy": strategy,
                        "original_query": query,
                        "refined_query": refined_query
                    }
                ),
                embedding_token_count=0.0,  # Will be calculated during retrieval
                llm_token_count=llm_token_count
            )
            return result
            
        except Exception as e:
            logger.error(f"Error in simple query refinement: {e}")
            # Fallback to original query
            return QueryExpansionResult(
                query=Query(
                    original_text=query,
                    processed_text=query,
                    expanded_queries=[query],
                    metadata={
                        "technique": "simple_query_refinement", 
                        "error": str(e),
                        "strategy": strategy
                    }
                ),
                embedding_token_count=0.0,
                llm_token_count={}
            )

class GraphAsQueryExpansion(QueryExpansionComponent):
    """Graph as query expansion"""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.graph_rag = GraphRAG(config)

    async def expand_query(self, query: str) -> QueryExpansionResult:
        """Graph as query expansion"""

        query_obj = Query(
            original_text=query,
            processed_text=query,
            expanded_queries=None,
            metadata={}
        )
        expanded_queries = []
        expanded_queries.append(query_obj)

        r = await self.graph_rag.retrieve(query_obj, self.config.get("num_expanded_queries", 3))
        documents = r.get("documents", [])
        embedding_token_count = r.get("embedding_token_count", 0.0)
        
        for doc in documents:
            expanded_queries.append(Query(
                original_text=doc.content,
                processed_text=doc.content,
                expanded_queries=None,
                metadata={
                    "technique": "graph_as_query_expansion"
                }
            ))
            logger.info(f"Query: {query_obj.original_text} - Expanded query: {doc.content}")
        query_obj.expanded_queries = expanded_queries
        return QueryExpansionResult(
            query=query_obj,
            embedding_token_count=embedding_token_count,
            llm_token_count={}
        )