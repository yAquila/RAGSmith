"""
Retrieval evaluation metrics.

Provides standard retrieval evaluation metrics including:
- Recall@K
- Precision@K  
- Average Precision (AP)
- Normalized Discounted Cumulative Gain (NDCG)
"""

import math
from typing import List, Dict


class RetrievalMetrics:
    """Calculate retrieval evaluation metrics"""
    
    @staticmethod
    def calculate_recall_at_k(retrieved_docs: List[str], relevant_docs: List[str], k: int) -> float:
        """
        Calculate Recall@K
        
        Args:
            retrieved_docs: List of retrieved document IDs
            relevant_docs: List of relevant document IDs
            k: Number of top documents to consider
            
        Returns:
            Recall@K score
        """
        if not relevant_docs:
            return 0.0
        
        retrieved_k = retrieved_docs[:k]
        relevant_retrieved = sum(1 for doc in retrieved_k if doc in relevant_docs)
        return relevant_retrieved / len(relevant_docs)
    
    @staticmethod
    def calculate_precision_at_k(retrieved_docs: List[str], relevant_docs: List[str], k: int) -> float:
        """
        Calculate Precision@K
        
        Args:
            retrieved_docs: List of retrieved document IDs
            relevant_docs: List of relevant document IDs
            k: Number of top documents to consider
            
        Returns:
            Precision@K score
        """
        if not retrieved_docs:
            return 0.0
        
        retrieved_k = retrieved_docs[:k]
        relevant_retrieved = sum(1 for doc in retrieved_k if doc in relevant_docs)
        return relevant_retrieved / len(retrieved_k)
    
    @staticmethod
    def calculate_ap(retrieved_docs: List[str], relevant_docs: List[str]) -> float:
        """
        Calculate Average Precision (AP)
        
        Args:
            retrieved_docs: List of retrieved document IDs
            relevant_docs: List of relevant document IDs
            
        Returns:
            Average Precision score
        """
        if not relevant_docs:
            return 0.0
        
        score = 0.0
        num_hits = 0.0
        
        for i, doc in enumerate(retrieved_docs):
            if doc in relevant_docs:
                num_hits += 1.0
                score += num_hits / (i + 1.0)
        
        return score / len(relevant_docs)
    
    @staticmethod
    def calculate_ndcg_at_k(retrieved_docs: List[str], relevant_docs: List[str], k: int) -> float:
        """
        Calculate Normalized Discounted Cumulative Gain at K
        
        Args:
            retrieved_docs: List of retrieved document IDs
            relevant_docs: List of relevant document IDs
            k: Number of top documents to consider
            
        Returns:
            NDCG@K score
        """
        if not relevant_docs:
            return 0.0
        
        retrieved_k = retrieved_docs[:k]
        
        # Calculate DCG
        dcg = 0.0
        for i, doc in enumerate(retrieved_k):
            if doc in relevant_docs:
                dcg += 1.0 / math.log2(i + 2)  # +2 because log2(1) = 0
        
        # Calculate IDCG (ideal DCG)
        idcg = 0.0
        for i in range(min(len(relevant_docs), k)):
            idcg += 1.0 / math.log2(i + 2)
        
        return dcg / idcg if idcg > 0 else 0.0
    
    @staticmethod
    def calculate_mrr(retrieved_docs: List[str], relevant_docs: List[str]) -> float:
        """
        Calculate Mean Reciprocal Rank (MRR)
        
        Args:
            retrieved_docs: List of retrieved document IDs
            relevant_docs: List of relevant document IDs
            
        Returns:
            MRR score
        """
        if not relevant_docs:
            return 0.0
        
        for i, doc in enumerate(retrieved_docs):
            if doc in relevant_docs:
                return 1.0 / (i + 1)
        
        return 0.0
    
    @staticmethod
    def calculate_all_metrics(retrieved_docs: List[str], relevant_docs: List[str], 
                            k_values: List[int] = [1, 3, 5, 10]) -> Dict[str, float]:
        """
        Calculate all retrieval metrics
        
        Args:
            retrieved_docs: List of retrieved document IDs
            relevant_docs: List of relevant document IDs
            k_values: List of K values to calculate metrics for
            
        Returns:
            Dictionary containing all calculated metrics
        """
        metrics = {}
        
        for k in k_values:
            metrics[f'recall@{k}'] = RetrievalMetrics.calculate_recall_at_k(retrieved_docs, relevant_docs, k)
            metrics[f'precision@{k}'] = RetrievalMetrics.calculate_precision_at_k(retrieved_docs, relevant_docs, k)
            metrics[f'ndcg@{k}'] = RetrievalMetrics.calculate_ndcg_at_k(retrieved_docs, relevant_docs, k)
        
        metrics['map'] = RetrievalMetrics.calculate_ap(retrieved_docs, relevant_docs)
        metrics['mrr'] = RetrievalMetrics.calculate_mrr(retrieved_docs, relevant_docs)
        
        return metrics 