import numpy as np
from typing import List, Dict, Any, Tuple, Set, Union
from collections import defaultdict
import logging
from rag_pipeline.core.modular_framework import Document

logger = logging.getLogger(__name__)

class ScoreCombiner:
    """Utility class for combining scores from multiple result lists"""
    
    @staticmethod
    def convex_combination(
        results_list: List[List[Dict[str, Any]]], 
        weights: Union[List[float], None] = None,
        method_names: Union[List[str], None] = None,
        excessive_k: int = 60
    ) -> List[Dict[str, Any]]:
        """
        Combine multiple result lists using convex combination of scores.
        
        Args:
            results_list: List of result lists, each containing dicts with keys 
                         ['doc_id', 'content', 'score', 'metadata']
            weights: List of weights for each method. If None, equal weights are used.
                    Must sum to 1.0 if provided.
            method_names: Optional names for each method (for metadata tracking)
            excessive_k: Excessive k for hybrid search
        Returns:
            Combined results sorted by combined score
        """
        try:
            if not results_list:
                logger.warning("Empty results list provided")
                return []
            
            num_methods = len(results_list)
            
            # Validate and setup weights
            if weights is None:
                weights = [1.0 / num_methods] * num_methods
            else:
                if len(weights) != num_methods:
                    raise ValueError(f"Number of weights ({len(weights)}) must match number of result lists ({num_methods})")
                
                # Normalize weights to sum to 1.0
                weight_sum = sum(weights)
                if abs(weight_sum - 1.0) > 1e-6:
                    logger.warning(f"Weights sum to {weight_sum}, normalizing to 1.0")
                    weights = [w / weight_sum for w in weights]
            
            # Setup method names for tracking
            if method_names is None:
                method_names = [f"method_{i}" for i in range(num_methods)]
            elif len(method_names) != num_methods:
                logger.warning("Method names length mismatch, using default names")
                method_names = [f"method_{i}" for i in range(num_methods)]
            
            # Create mappings for each method
            method_mappings = []
            for i, results in enumerate(results_list):
                mapping = {result['doc_id']: result for result in results}
                method_mappings.append(mapping)
            
            # Get all unique document IDs across all methods
            all_doc_ids = set()
            for mapping in method_mappings:
                all_doc_ids.update(mapping.keys())
            
            combined_results = []
            
            for doc_id in all_doc_ids:
                combined_score = 0.0
                doc_data = None
                method_contributions = {}
                
                # Calculate weighted combination of scores
                for i, (mapping, weight, method_name) in enumerate(zip(method_mappings, weights, method_names)):
                    if doc_id in mapping:
                        result = mapping[doc_id]
                        contribution = weight * result['score']
                        combined_score += contribution
                        method_contributions[method_name] = {
                            'score': result['score'],
                            'weight': weight,
                            'contribution': contribution
                        }
                        
                        # Use the first available result as base document data
                        if doc_data is None:
                            doc_data = result.copy()
                
                if doc_data is not None:
                    # Create combined result
                    combined_result = {
                        'doc_id': doc_data['doc_id'],
                        'content': doc_data['content'],
                        'score': combined_score,
                        'metadata': doc_data.get('metadata', {}).copy()
                    }
                    
                    # Add combination metadata
                    combined_result['metadata']['combination_info'] = {
                        'method': 'convex_combination',
                        'method_contributions': method_contributions,
                        'final_score': combined_score
                    }
                    
                    combined_results.append(combined_result)
            
            # Sort by combined score (descending)
            combined_results.sort(key=lambda x: x['score'], reverse=True)
            
            logger.info(f"Combined {len(combined_results)} unique documents from {num_methods} methods")
            return combined_results
            
        except Exception as e:
            logger.error(f"Convex combination failed: {e}")
            return []


class RankFusionCombiner:
    """Utility class for Reciprocal Rank Fusion (RRF) with multiple methods"""
    
    @staticmethod
    def reciprocal_rank_fusion(
        results_list: List[List[Dict[str, Any]]], 
        excessive_k: int = 60,
        method_names: Union[List[str], None] = None
    ) -> List[Dict[str, Any]]:
        """
        Combine multiple result lists using Reciprocal Rank Fusion.
        
        Args:
            results_list: List of result lists, each containing dicts with keys 
                         ['doc_id', 'content', 'score', 'metadata']
            excessive_k: Excessive k for hybrid search
            method_names: Optional names for each method (for metadata tracking)
            
        Returns:
            Combined results sorted by RRF score
        """
        try:
            if not results_list:
                logger.warning("Empty results list provided")
                return []
            
            num_methods = len(results_list)
            
            # Setup method names for tracking
            if method_names is None:
                method_names = [f"method_{i}" for i in range(num_methods)]
            elif len(method_names) != num_methods:
                logger.warning("Method names length mismatch, using default names")
                method_names = [f"method_{i}" for i in range(num_methods)]
            
            # Create document registry to store all unique documents
            doc_registry = {}
            
            # Process each method's results
            for method_idx, (results, method_name) in enumerate(zip(results_list, method_names)):
                for rank, result in enumerate(results):
                    doc_id = result['doc_id']
                    
                    if doc_id not in doc_registry:
                        doc_registry[doc_id] = {
                            'doc_id': doc_id,
                            'content': result['content'],
                            'metadata': result['metadata'],
                            'method_ranks': {},
                            'rrf_score': 0.0
                        }
                    
                    # Store rank for this method (1-indexed)
                    doc_registry[doc_id]['method_ranks'][method_name] = rank + 1
            
            # Calculate RRF scores
            for doc_id, doc_info in doc_registry.items():
                rrf_score = 0.0
                method_contributions = {}
                
                # Add contribution from each method that found this document
                for method_name, rank in doc_info['method_ranks'].items():
                    contribution = 1.0 / (excessive_k + rank)
                    rrf_score += contribution
                    method_contributions[method_name] = {
                        'rank': rank,
                        'contribution': contribution
                    }
                
                doc_info['rrf_score'] = rrf_score
                doc_info['method_contributions'] = method_contributions
            
            # Convert to list and sort by RRF score
            combined_results = []
            for doc_info in doc_registry.values():
                result = {
                    'doc_id': doc_info['doc_id'],
                    'content': doc_info['content'],
                    'score': doc_info['rrf_score'],
                    'metadata': doc_info['metadata'].copy() if doc_info['metadata'] else {}
                }
                
                # Add RRF metadata
                result['metadata']['combination_info'] = {
                    'method': 'reciprocal_rank_fusion',
                    'excessive_k': excessive_k,
                    'method_contributions': doc_info['method_contributions'],
                    'methods_found_in': list(doc_info['method_ranks'].keys()),
                    'final_score': doc_info['rrf_score']
                }
                
                combined_results.append(result)
            
            # Sort by RRF score (descending)
            combined_results.sort(key=lambda x: x['score'], reverse=True)
            
            logger.info(f"RRF combined {len(combined_results)} unique documents from {num_methods} methods")
            return combined_results
            
        except Exception as e:
            logger.error(f"Reciprocal rank fusion failed: {e}")
            return []

    @staticmethod
    def borda_count_fusion(
        results_list: List[List[Dict[str, Any]]], 
        excessive_k: int = 60,
        method_names: Union[List[str], None] = None
    ) -> List[Dict[str, Any]]:
        """
        Combine multiple result lists using Borda count method.
        
        Args:
            results_list: List of result lists
            method_names: Optional names for each method
            excessive_k: Excessive k for hybrid search
        Returns:
            Combined results sorted by Borda count score
        """
        try:
            if not results_list:
                return []
            
            num_methods = len(results_list)
            
            # Setup method names
            if method_names is None:
                method_names = [f"method_{i}" for i in range(num_methods)]
            
            # Create document registry
            doc_registry = {}
            
            # Process each method's results
            for method_idx, (results, method_name) in enumerate(zip(results_list, method_names)):
                num_docs = len(results)
                
                for rank, result in enumerate(results):
                    doc_id = result['doc_id']
                    
                    if doc_id not in doc_registry:
                        doc_registry[doc_id] = {
                            'doc_id': doc_id,
                            'content': result['content'],
                            'metadata': result['metadata'],
                            'borda_score': 0.0,
                            'method_contributions': {}
                        }
                    
                    # Borda count: points = (total_docs - rank)
                    points = num_docs - rank
                    doc_registry[doc_id]['borda_score'] += points
                    doc_registry[doc_id]['method_contributions'][method_name] = {
                        'rank': rank + 1,
                        'points': points
                    }
            
            # Convert to list and sort by Borda score
            combined_results = []
            for doc_info in doc_registry.values():
                result = {
                    'doc_id': doc_info['doc_id'],
                    'content': doc_info['content'],
                    'score': doc_info['borda_score'],
                    'metadata': doc_info['metadata'].copy() if doc_info['metadata'] else {}
                }
                
                result['metadata']['combination_info'] = {
                    'method': 'borda_count',
                    'method_contributions': doc_info['method_contributions'],
                    'final_score': doc_info['borda_score']
                }
                
                combined_results.append(result)
            
            combined_results.sort(key=lambda x: x['score'], reverse=True)
            
            logger.info(f"Borda count combined {len(combined_results)} unique documents from {num_methods} methods")
            return combined_results
            
        except Exception as e:
            logger.error(f"Borda count fusion failed: {e}")
            return []

class HybridUtils:
    """General utilities for hybrid retrieval"""
    
    @staticmethod
    def convert_to_documents(results: List[Dict[str, Any]]) -> List[Document]:
        """Convert results to Document objects"""
        documents = []
        for result in results:
            documents.append(Document(
                doc_id=result['doc_id'],
                content=result['content'],
                score=result['score'],
                metadata=result['metadata']
            ))
        return documents

    @staticmethod
    def convert_documents_to_results(documents: List[Document]) -> List[Dict[str, Any]]:
        """Convert Document objects to results"""
        results = []
        for document in documents:
            results.append(document.to_dict())
        return results
    
    @staticmethod
    def combine_with_convex_combination(
        results_list: List[List[Dict[str, Any]]], 
        method_names: List[str],
        weights: Union[List[float], None] = None,
        normalization_method: str = "minmax",
        excessive_k: int = 60
    ) -> List[Dict[str, Any]]:
        """Combine results using convex combination"""
        try:
            # Normalize scores before combination if requested
            results_list = HybridUtils.normalize_results_list(results_list, normalization_method)
            
            return ScoreCombiner.convex_combination(results_list, weights, method_names, excessive_k)
            
        except Exception as e:
            logger.error(f"Convex combination failed: {e}")
            return []

    @staticmethod
    def combine_with_rrf(
        results_list: List[List[Dict[str, Any]]], 
        method_names: List[str],
        excessive_k: int = 60
    ) -> List[Dict[str, Any]]:
        """Combine results using Reciprocal Rank Fusion"""
        try:
            return RankFusionCombiner.reciprocal_rank_fusion(results_list, excessive_k, method_names)
            
        except Exception as e:
            logger.error(f"RRF combination failed: {e}")
            return []
    
    @staticmethod
    def combine_with_borda_count(
        results_list: List[List[Dict[str, Any]]], 
        method_names: List[str],
        excessive_k: int = 60
    ) -> List[Dict[str, Any]]:
        """Combine results using Borda Count"""
        try:
            return RankFusionCombiner.borda_count_fusion(results_list, excessive_k, method_names)
            
        except Exception as e:
            logger.error(f"Borda count combination failed: {e}")
            return []

    @staticmethod
    def normalize_results_list(
        results_list: List[List[Dict[str, Any]]], 
        method: str = "minmax"
    ) -> List[List[Dict[str, Any]]]:
        """
        Normalize scores in multiple result lists.
        
        Args:
            results_list: List of result lists to normalize
            method: Normalization method ("minmax", "zscore", "global_minmax")
            
        Returns:
            List of normalized result lists
        """
        if not results_list:
            return results_list
        
        if method == "global_minmax":
            return HybridUtils._global_minmax_normalize(results_list)
        else:
            # Normalize each list independently
            normalized_lists = []
            for results in results_list:
                if method == "minmax":
                    normalized = HybridUtils.normalize_scores_minmax(results)
                elif method == "zscore":
                    normalized = HybridUtils.normalize_scores_zscore(results)
                else:
                    logger.warning(f"Unknown normalization method: {method}")
                    normalized = results
                normalized_lists.append(normalized)
            return normalized_lists
    
    @staticmethod
    def _global_minmax_normalize(results_list: List[List[Dict[str, Any]]]) -> List[List[Dict[str, Any]]]:
        """Normalize all scores using global min and max across all methods"""
        # Collect all scores
        all_scores = []
        for results in results_list:
            all_scores.extend([result['score'] for result in results])
        
        if not all_scores:
            return results_list
        
        global_min = min(all_scores)
        global_max = max(all_scores)
        
        if global_max == global_min:
            # All scores are the same
            normalized_lists = []
            for results in results_list:
                normalized = [r.copy() for r in results]
                for r in normalized:
                    r['score'] = 1.0
                normalized_lists.append(normalized)
            return normalized_lists
        
        # Normalize using global min/max
        normalized_lists = []
        for results in results_list:
            normalized = []
            for result in results:
                normalized_result = result.copy()
                normalized_result['score'] = (result['score'] - global_min) / (global_max - global_min)
                normalized.append(normalized_result)
            normalized_lists.append(normalized)
        
        return normalized_lists
    
    @staticmethod
    def normalize_scores_minmax(results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Normalize scores using min-max normalization"""
        if not results:
            return results
        
        scores = [result['score'] for result in results]
        min_score = min(scores)
        max_score = max(scores)
        
        if max_score == min_score:
            for result in results:
                result['score'] = 1.0
            return results
        
        normalized_results = []
        for result in results:
            normalized_result = result.copy()
            normalized_result['score'] = (result['score'] - min_score) / (max_score - min_score)
            normalized_results.append(normalized_result)
        
        return normalized_results
    
    @staticmethod
    def normalize_scores_zscore(results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Normalize scores using z-score normalization"""
        if not results:
            return results
        
        scores = np.array([result['score'] for result in results])
        mean_score = np.mean(scores)
        std_score = np.std(scores)
        
        if std_score == 0:
            for result in results:
                result['score'] = 0.0
            return results
        
        normalized_results = []
        for i, result in enumerate(results):
            normalized_result = result.copy()
            normalized_result['score'] = (scores[i] - mean_score) / std_score
            normalized_results.append(normalized_result)
        
        return normalized_results
    
    @staticmethod
    def filter_top_k(results: List[Dict[str, Any]], k: int) -> List[Dict[str, Any]]:
        """Filter results to top k items"""
        if not results or k <= 0:
            return []
        return results[:k]
    
    @staticmethod
    def calculate_multi_method_overlap(
        results_list: List[List[Dict[str, Any]]], 
        method_names: Union[List[str], None] = None
    ) -> Dict[str, Any]:
        """
        Calculate overlap statistics between multiple result lists.
        
        Args:
            results_list: List of result lists
            method_names: Optional names for each method
            
        Returns:
            Dictionary with comprehensive overlap statistics
        """
        if not results_list:
            return {}
        
        num_methods = len(results_list)
        
        if method_names is None:
            method_names = [f"method_{i}" for i in range(num_methods)]
        
        # Get document IDs for each method
        method_doc_sets = []
        for results in results_list:
            doc_set = set(result['doc_id'] for result in results)
            method_doc_sets.append(doc_set)
        
        # Calculate statistics
        all_union = set()
        for doc_set in method_doc_sets:
            all_union.update(doc_set)
        
        # Find intersection of all methods
        all_intersection = method_doc_sets[0].copy() if method_doc_sets else set()
        for doc_set in method_doc_sets[1:]:
            all_intersection &= doc_set
        
        # Pairwise overlaps
        pairwise_overlaps = {}
        for i in range(num_methods):
            for j in range(i + 1, num_methods):
                intersection = method_doc_sets[i] & method_doc_sets[j]
                union = method_doc_sets[i] | method_doc_sets[j]
                pairwise_overlaps[f"{method_names[i]}_vs_{method_names[j]}"] = {
                    'intersection_size': len(intersection),
                    'union_size': len(union),
                    'jaccard_similarity': len(intersection) / len(union) if union else 0.0
                }
        
        # Method-specific stats
        method_stats = {}
        for i, (method_name, doc_set) in enumerate(zip(method_names, method_doc_sets)):
            unique_docs = doc_set.copy()
            for j, other_set in enumerate(method_doc_sets):
                if i != j:
                    unique_docs -= other_set
            
            method_stats[method_name] = {
                'total_docs': len(doc_set),
                'unique_docs': len(unique_docs),
                'overlap_with_others': len(doc_set) - len(unique_docs)
            }
        
        overlap_stats = {
            'num_methods': num_methods,
            'method_names': method_names,
            'total_unique_docs': len(all_union),
            'docs_in_all_methods': len(all_intersection),
            'all_methods_jaccard': len(all_intersection) / len(all_union) if all_union else 0.0,
            'method_stats': method_stats,
            'pairwise_overlaps': pairwise_overlaps
        }
        
        return overlap_stats
    
    @staticmethod
    def analyze_score_distributions(
        results_list: List[List[Dict[str, Any]]], 
        method_names: Union[List[str], None] = None
    ) -> Dict[str, Any]:
        """
        Analyze score distributions across multiple methods.
        """
        if not results_list:
            return {}
        
        if method_names is None:
            method_names = [f"method_{i}" for i in range(len(results_list))]
        
        distributions = {}
        
        for method_name, results in zip(method_names, results_list):
            if not results:
                distributions[method_name] = {
                    'count': 0,
                    'mean': 0.0,
                    'std': 0.0,
                    'min': 0.0,
                    'max': 0.0
                }
                continue
            
            scores = [result['score'] for result in results]
            distributions[method_name] = {
                'count': len(scores),
                'mean': float(np.mean(scores)),
                'std': float(np.std(scores)),
                'min': float(np.min(scores)),
                'max': float(np.max(scores)),
                'median': float(np.median(scores))
            }
        
        return distributions