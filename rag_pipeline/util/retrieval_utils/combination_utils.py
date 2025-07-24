import numpy as np
from typing import List, Dict, Any, Tuple, Set
from collections import defaultdict
import logging

logger = logging.getLogger(__name__)

class ScoreCombiner:
    """Utility class for combining scores from different retrieval methods"""
    
    @staticmethod
    def convex_combination(
        vector_results: List[Dict[str, Any]], 
        keyword_results: List[Dict[str, Any]], 
        alpha: float = 0.5
    ) -> List[Dict[str, Any]]:
        """
        Combine results using convex combination of scores.
        
        Args:
            vector_results: List of dicts with keys ['doc_id', 'content', 'score', 'metadata']
            keyword_results: List of dicts with keys ['doc_id', 'content', 'score', 'metadata'] 
            alpha: Weight for vector scores (1-alpha for keyword scores)
            
        Returns:
            Combined results sorted by combined score
        """
        try:
            # Create mappings for quick lookup
            vector_scores = {result['doc_id']: result for result in vector_results}
            keyword_scores = {result['doc_id']: result for result in keyword_results}
            
            # Get all unique document IDs
            all_doc_ids = set(vector_scores.keys()) | set(keyword_scores.keys())
            
            combined_results = []
            
            for doc_id in all_doc_ids:
                vector_result = vector_scores.get(doc_id)
                keyword_result = keyword_scores.get(doc_id)
                
                # Handle cases where document appears in only one result set
                if vector_result and keyword_result:
                    # Both methods found this document
                    combined_score = alpha * vector_result['score'] + (1 - alpha) * keyword_result['score']
                    # Use vector result as base (could also merge metadata)
                    result = vector_result.copy()
                    result['score'] = combined_score
                    
                elif vector_result:
                    # Only vector search found this document
                    combined_score = alpha * vector_result['score']
                    result = vector_result.copy()
                    result['score'] = combined_score
                    
                elif keyword_result:
                    # Only keyword search found this document
                    combined_score = (1 - alpha) * keyword_result['score']
                    result = keyword_result.copy()
                    result['score'] = combined_score
                
                combined_results.append(result)
            
            # Sort by combined score (descending)
            combined_results.sort(key=lambda x: x['score'], reverse=True)
            
            return combined_results
            
        except Exception as e:
            logger.error(f"Convex combination failed: {e}")
            return []

class RankFusionCombiner:
    """Utility class for Reciprocal Rank Fusion (RRF)"""
    
    @staticmethod
    def reciprocal_rank_fusion(
        vector_results: List[Dict[str, Any]], 
        keyword_results: List[Dict[str, Any]], 
        k: int = 60
    ) -> List[Dict[str, Any]]:
        """
        Combine results using Reciprocal Rank Fusion.
        
        Args:
            vector_results: List of dicts with keys ['doc_id', 'content', 'score', 'metadata']
            keyword_results: List of dicts with keys ['doc_id', 'content', 'score', 'metadata']
            k: RRF parameter (typically 60)
            
        Returns:
            Combined results sorted by RRF score
        """
        try:
            # Create document registry to store all unique documents
            doc_registry = {}
            
            # Process vector results
            for rank, result in enumerate(vector_results):
                doc_id = result['doc_id']
                if doc_id not in doc_registry:
                    doc_registry[doc_id] = {
                        'doc_id': doc_id,
                        'content': result['content'],
                        'metadata': result['metadata'],
                        'vector_rank': rank + 1,
                        'keyword_rank': None,
                        'rrf_score': 0.0
                    }
                else:
                    doc_registry[doc_id]['vector_rank'] = rank + 1
            
            # Process keyword results
            for rank, result in enumerate(keyword_results):
                doc_id = result['doc_id']
                if doc_id not in doc_registry:
                    doc_registry[doc_id] = {
                        'doc_id': doc_id,
                        'content': result['content'],
                        'metadata': result['metadata'],
                        'vector_rank': None,
                        'keyword_rank': rank + 1,
                        'rrf_score': 0.0
                    }
                else:
                    doc_registry[doc_id]['keyword_rank'] = rank + 1
            
            # Calculate RRF scores
            for doc_id, doc_info in doc_registry.items():
                rrf_score = 0.0
                
                # Add vector contribution
                if doc_info['vector_rank'] is not None:
                    rrf_score += 1.0 / (k + doc_info['vector_rank'])
                
                # Add keyword contribution
                if doc_info['keyword_rank'] is not None:
                    rrf_score += 1.0 / (k + doc_info['keyword_rank'])
                
                doc_info['rrf_score'] = rrf_score
            
            # Convert to list and sort by RRF score
            combined_results = []
            for doc_info in doc_registry.values():
                result = {
                    'doc_id': doc_info['doc_id'],
                    'content': doc_info['content'],
                    'score': doc_info['rrf_score'],
                    'metadata': doc_info['metadata']
                }
                combined_results.append(result)
            
            # Sort by RRF score (descending)
            combined_results.sort(key=lambda x: x['score'], reverse=True)
            
            return combined_results
            
        except Exception as e:
            logger.error(f"Reciprocal rank fusion failed: {e}")
            return []

class HybridUtils:
    """General utilities for hybrid retrieval"""
    
    @staticmethod
    def normalize_scores_minmax(results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Normalize scores in results using min-max normalization.
        
        Args:
            results: List of result dictionaries with 'score' key
            
        Returns:
            Results with normalized scores
        """
        if not results:
            return results
        
        scores = [result['score'] for result in results]
        min_score = min(scores)
        max_score = max(scores)
        
        # Handle case where all scores are the same
        if max_score == min_score:
            for result in results:
                result['score'] = 1.0
            return results
        
        # Normalize scores
        normalized_results = []
        for result in results:
            normalized_result = result.copy()
            normalized_result['score'] = (result['score'] - min_score) / (max_score - min_score)
            normalized_results.append(normalized_result)
        
        return normalized_results
    
    @staticmethod
    def normalize_scores_zscore(results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Normalize scores using z-score normalization.
        
        Args:
            results: List of result dictionaries with 'score' key
            
        Returns:
            Results with z-score normalized scores
        """
        if not results:
            return results
        
        scores = np.array([result['score'] for result in results])
        mean_score = np.mean(scores)
        std_score = np.std(scores)
        
        # Handle case where std is 0
        if std_score == 0:
            for result in results:
                result['score'] = 0.0
            return results
        
        # Normalize scores
        normalized_results = []
        for i, result in enumerate(results):
            normalized_result = result.copy()
            normalized_result['score'] = (scores[i] - mean_score) / std_score
            normalized_results.append(normalized_result)
        
        return normalized_results
    
    @staticmethod
    def filter_top_k(results: List[Dict[str, Any]], k: int) -> List[Dict[str, Any]]:
        """
        Filter results to top k items.
        
        Args:
            results: List of result dictionaries
            k: Number of top results to return
            
        Returns:
            Top k results
        """
        if not results or k <= 0:
            return []
        
        return results[:k]
    
    @staticmethod
    def merge_metadata(
        vector_metadata: Dict[str, Any], 
        keyword_metadata: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Merge metadata from vector and keyword results.
        
        Args:
            vector_metadata: Metadata from vector search
            keyword_metadata: Metadata from keyword search
            
        Returns:
            Merged metadata
        """
        merged = vector_metadata.copy() if vector_metadata else {}
        
        if keyword_metadata:
            # Add keyword-specific metadata with prefix to avoid conflicts
            for key, value in keyword_metadata.items():
                if key not in merged:
                    merged[key] = value
                elif merged[key] != value:
                    # Handle conflicts by keeping both with prefixes
                    merged[f'vector_{key}'] = merged[key]
                    merged[f'keyword_{key}'] = value
                    merged[key] = value  # Keep keyword version as default
        
        return merged
    
    @staticmethod
    def calculate_result_overlap(
        vector_results: List[Dict[str, Any]], 
        keyword_results: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Calculate overlap statistics between vector and keyword results.
        
        Args:
            vector_results: Results from vector search
            keyword_results: Results from keyword search
            
        Returns:
            Dictionary with overlap statistics
        """
        vector_ids = set(result['doc_id'] for result in vector_results)
        keyword_ids = set(result['doc_id'] for result in keyword_results)
        
        intersection = vector_ids & keyword_ids
        union = vector_ids | keyword_ids
        
        overlap_stats = {
            'vector_count': len(vector_ids),
            'keyword_count': len(keyword_ids),
            'intersection_count': len(intersection),
            'union_count': len(union),
            'jaccard_similarity': len(intersection) / len(union) if union else 0.0,
            'vector_unique': len(vector_ids - keyword_ids),
            'keyword_unique': len(keyword_ids - vector_ids)
        }
        
        return overlap_stats