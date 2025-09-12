"""
Semantic text comparison utilities using embeddings.

Provides semantic similarity measurement using:
- Embedding models (via Ollama)
- Cosine similarity calculation
"""

import os
import numpy as np
from langchain_community.embeddings import OllamaEmbeddings


class SemanticComparison:
    """Semantic text comparison using embedding models"""
    
    def __init__(self, embedding_model):
        """
        Initialize semantic comparison with embedding model.
        
        Args:
            embedding_model: Name of the embedding model to use
        """
        # Get the Ollama API URL from environment variable
        ollama_api_url = os.getenv("OLLAMA_API_URL", "http://localhost:11435/api")
        # Extract the base URL without the '/api' suffix for OllamaEmbeddings
        base_url = ollama_api_url.replace("/api", "")
        
        self.embedding = OllamaEmbeddings(
            model=embedding_model,
            base_url=base_url
        )
    
    def get_similarity_score(self, pred: str, gt: str) -> float:
        """
        Calculate semantic similarity score between prediction and ground truth.
        
        Args:
            pred: Predicted text
            gt: Ground truth text
            
        Returns:
            Cosine similarity score between embeddings
        """
        embedding1 = self.embedding.embed_query(pred)
        embedding2 = self.embedding.embed_query(gt)
        return self.__cosine_similarity(embedding1, embedding2)

    def __cosine_similarity(self, vec1, vec2) -> float:
        """Calculate cosine similarity between two vectors"""
        vec1 = np.array(vec1)
        vec2 = np.array(vec2)
        return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)) 