"""
Improved LLM-based reranking utilities for RAG pipeline using Ollama
"""

import logging
import json
import re
from typing import List, Dict, Any, Optional
from util.api.ollama_client import OllamaUtil

logger = logging.getLogger(__name__)

class LLMRerankerUtil:
    """Utility class for reranking documents using LLM models via Ollama"""
    
    def __init__(self, model_name: str = 'llama3.2:1b', max_tokens: int = 2048, temperature: float = 0.1):
        """
        Initialize the LLM reranker
        
        Args:
            model_name: Name of the LLM model to use for reranking
            max_tokens: Maximum tokens for the LLM response
            temperature: Temperature for LLM generation (lower = more deterministic)
        """
        self.model_name = model_name
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.ollama_client = OllamaUtil
        
    def _create_reranking_prompt(self, query: str, documents: List[Dict[str, Any]]) -> str:
        """
        Create an improved prompt for LLM-based document reranking
        
        Args:
            query: The search query
            documents: List of documents to rerank
            
        Returns:
            Formatted prompt for the LLM
        """
        prompt = f"""You are an expert document relevance assessor. Your task is to rank documents by how well they answer or relate to a given query.

RANKING CRITERIA:
- Direct relevance: Does the document directly answer the query?
- Topical alignment: Is the document about the same topic as the query?
- Information quality: Does the document provide useful, accurate information?
- Completeness: How comprehensively does the document address the query?

QUERY: "{query}"

DOCUMENTS TO RANK:
"""
        
        for i, doc in enumerate(documents, 1):
            content = doc.get('content', '')[:400]  # Truncate for better focus
            prompt += f"\n[{i}] {content}\n"
        
        prompt += f"""
TASK: Rank these {len(documents)} documents from MOST relevant (1st) to LEAST relevant (last) for answering the query.

IMPORTANT INSTRUCTIONS:
- Consider direct answers to the query as most relevant
- Prioritize documents that specifically address the query topic
- Lower-rank documents that are off-topic or tangentially related
- If documents seem equally relevant, consider information quality and completeness

OUTPUT FORMAT: Respond with ONLY a JSON array of document numbers in ranked order.
Example format: [3, 1, 5, 2, 4]

RANKING:"""
        
        return prompt
    
    def _parse_ranking_response(self, response: str, num_docs: int) -> List[int]:
        """
        Parse the LLM response to extract document ranking
        
        Args:
            response: Raw LLM response
            num_docs: Expected number of documents
            
        Returns:
            List of document indices (1-based) in ranked order
        """
        try:
            # Strategy 1: Try to parse as complete JSON first
            try:
                json_data = json.loads(response.strip())
                
                # Handle various JSON formats
                ranking = None
                
                # Format: [1, 2, 3, 4] (simple array)
                if isinstance(json_data, list):
                    if all(isinstance(x, int) for x in json_data):
                        ranking = json_data
                    elif all(isinstance(x, dict) for x in json_data):
                        # Format: [{"rank": 1, "documentNumber": 2}, ...]
                        if all("documentNumber" in x for x in json_data):
                            ranking = [x["documentNumber"] for x in json_data]
                        elif all("document_number" in x for x in json_data):
                            ranking = [x["document_number"] for x in json_data]
                
                # Format: {"ranked_documents": [1, 2, 3]} or similar
                elif isinstance(json_data, dict):
                    for key in ["ranked_documents", "document_numbers", "rankedDocumentNumbers", 
                               "ranked_document_numbers", "Documents", "documents", "ranking"]:
                        if key in json_data:
                            data = json_data[key]
                            if isinstance(data, list):
                                if all(isinstance(x, int) for x in data):
                                    ranking = data
                                elif all(isinstance(x, dict) for x in data):
                                    # Handle nested objects
                                    if all("documentNumber" in x for x in data):
                                        ranking = [x["documentNumber"] for x in data]
                                    elif all("document_number" in x for x in data):
                                        ranking = [x["document_number"] for x in data]
                                    elif all("rank" in x and "title" in x for x in data):
                                        # Sort by rank and extract position
                                        sorted_docs = sorted(data, key=lambda x: x.get("rank", 999))
                                        ranking = list(range(1, len(sorted_docs) + 1))
                                break
                
                # Validate the extracted ranking
                if (ranking and isinstance(ranking, list) and 
                    len(ranking) == num_docs and 
                    all(isinstance(x, int) and 1 <= x <= num_docs for x in ranking) and
                    len(set(ranking)) == num_docs):
                    return ranking
                    
            except json.JSONDecodeError:
                pass  # Fall through to other strategies
            
            # Strategy 2: Extract simple JSON array from text
            json_match = re.search(r'\[[\d\s,]+\]', response)
            if json_match:
                ranking_str = json_match.group()
                ranking = json.loads(ranking_str)
                
                # Validate ranking
                if (isinstance(ranking, list) and 
                    len(ranking) == num_docs and 
                    all(isinstance(x, int) and 1 <= x <= num_docs for x in ranking) and
                    len(set(ranking)) == num_docs):
                    return ranking
            
            # Strategy 3: Extract any JSON array and try to interpret it
            array_matches = re.findall(r'\[([^\]]+)\]', response)
            for match in array_matches:
                try:
                    # Try to parse the content inside brackets
                    numbers = [int(x.strip()) for x in match.split(',') if x.strip().isdigit()]
                    if (len(numbers) == num_docs and 
                        all(1 <= x <= num_docs for x in numbers) and
                        len(set(numbers)) == num_docs):
                        return numbers
                except (ValueError, TypeError):
                    continue
            
            # Strategy 4: Extract all numbers and use first valid permutation
            numbers = re.findall(r'\d+', response)
            if len(numbers) >= num_docs:
                ranking = [int(x) for x in numbers[:num_docs]]
                # Check if it's a valid permutation
                if (len(set(ranking)) == num_docs and 
                    all(1 <= x <= num_docs for x in ranking)):
                    return ranking
                
                # Try different subsets of numbers if first doesn't work
                for i in range(len(numbers) - num_docs + 1):
                    subset = [int(x) for x in numbers[i:i+num_docs]]
                    if (len(set(subset)) == num_docs and 
                        all(1 <= x <= num_docs for x in subset)):
                        return subset
            
        except Exception as e:
            logger.warning(f"Failed to parse LLM ranking response: {e}")
        
        # Fallback: return original order
        logger.warning(f"Could not parse LLM ranking, using original order. Response: {response[:200]}...")
        return list(range(1, num_docs + 1))
    
    def rerank_documents(
        self, 
        query: str, 
        documents: List[Dict[str, Any]], 
        top_k: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Rerank documents using LLM-based relevance assessment
        
        Args:
            query: The search query
            documents: List of documents with 'content' field
            top_k: Number of top documents to return (if None, return all)
            
        Returns:
            List of reranked documents with added 'llm_rerank_score' field
        """
        if not documents:
            return documents
        
        if len(documents) == 1:
            # Single document, just add score and return
            reranked_doc = documents[0].copy()
            reranked_doc['llm_rerank_score'] = 1.0
            return [reranked_doc]
        
        try:
            # Create reranking prompt
            prompt = self._create_reranking_prompt(query, documents)
            
            logger.info(f"LLM reranking {len(documents)} documents with {self.model_name}")
            
            # Get ranking from LLM
            response = self.ollama_client.get_ollama_response(
                model=self.model_name,
                prompt=prompt
            )
            
            # Extract response text
            if isinstance(response, dict):
                response_text = response.get('response', '')
            else:
                response_text = str(response)
            
            # Parse the ranking response
            ranking = self._parse_ranking_response(response_text, len(documents))
            
            # Apply ranking and add scores
            reranked_docs = []
            max_score = len(documents)
            
            for rank_position, doc_index in enumerate(ranking):
                # Convert to 0-based index
                doc_idx = doc_index - 1
                if 0 <= doc_idx < len(documents):
                    reranked_doc = documents[doc_idx].copy()
                    # Score decreases with rank position (first = highest score)
                    reranked_doc['llm_rerank_score'] = (max_score - rank_position) / max_score
                    reranked_docs.append(reranked_doc)
            
            # Apply top_k filtering if specified
            if top_k is not None:
                reranked_docs = reranked_docs[:top_k]
            
            logger.info(f"LLM reranking completed, returned {len(reranked_docs)} documents")
            return reranked_docs
            
        except Exception as e:
            logger.error(f"LLM reranking failed: {e}")
            # Return original documents with default scores
            fallback_docs = []
            for i, doc in enumerate(documents):
                fallback_doc = doc.copy()
                fallback_doc['llm_rerank_score'] = (len(documents) - i) / len(documents)
                fallback_docs.append(fallback_doc)
            
            if top_k is not None:
                fallback_docs = fallback_docs[:top_k]
            
            return fallback_docs


# Global instance for efficient model reuse across the entire pipeline
_llm_reranker_instance = None

def get_llm_reranker(model_name: str = 'llama3.2:1b', max_tokens: int = 2048, temperature: float = 0.1) -> LLMRerankerUtil:
    """Get a singleton LLM reranker instance for efficient model reuse"""
    global _llm_reranker_instance
    
    # Check if we need to create a new instance
    need_new_instance = (
        _llm_reranker_instance is None or 
        _llm_reranker_instance.model_name != model_name or
        _llm_reranker_instance.max_tokens != max_tokens or
        _llm_reranker_instance.temperature != temperature
    )
    
    if need_new_instance:
        logger.info(f"Creating new LLM reranker instance for model: {model_name}")
        _llm_reranker_instance = LLMRerankerUtil(model_name, max_tokens, temperature)
    else:
        logger.debug(f"Reusing existing LLM reranker instance for model: {model_name}")
    
    return _llm_reranker_instance 