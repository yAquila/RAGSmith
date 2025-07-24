import os
import pickle
import pandas as pd
import re
import numpy as np
from typing import List, Dict, Any, Optional
from rank_bm25 import BM25Okapi
import logging

logger = logging.getLogger(__name__)

class BM25IndexManager:
    """Utility class for managing BM25 indices"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.bm25 = None
        self.documents_data = []
        self.tokenized_corpus = []
        self.index_path = None
        self.documents_path = None
    
    def setup_index_paths(self, dataset_hash: str, dataset_path: str):
        """Setup index file paths based on dataset hash"""
        index_dir = os.path.join(
            os.path.dirname(dataset_path),
            "bm25_indices",
            f"bm25_{dataset_hash}"
        )
        os.makedirs(index_dir, exist_ok=True)
        
        self.index_path = os.path.join(index_dir, "bm25_index.pkl")
        self.documents_path = os.path.join(index_dir, "documents.pkl")
    
    def load_existing_index(self) -> bool:
        """Load existing BM25 index if it exists"""
        try:
            if os.path.exists(self.index_path) and os.path.exists(self.documents_path):
                with open(self.index_path, 'rb') as f:
                    index_data = pickle.load(f)
                    self.bm25 = index_data['bm25']
                    self.tokenized_corpus = index_data['tokenized_corpus']
                
                with open(self.documents_path, 'rb') as f:
                    self.documents_data = pickle.load(f)
                
                return True
        except Exception as e:
            logger.warning(f"Failed to load existing index: {e}")
        return False
    
    def save_index(self):
        """Save BM25 index and documents to disk"""
        try:
            if self.bm25 and self.index_path:
                # Save BM25 index
                index_data = {
                    'bm25': self.bm25,
                    'tokenized_corpus': self.tokenized_corpus
                }
                with open(self.index_path, 'wb') as f:
                    pickle.dump(index_data, f)
                
                # Save documents data
                with open(self.documents_path, 'wb') as f:
                    pickle.dump(self.documents_data, f)
                
                logger.info(f"BM25 index saved to {self.index_path}")
                
        except Exception as e:
            logger.error(f"Failed to save BM25 index: {e}")
    
  
    def index_documents(self, documents: List) -> bool:
        """Index documents for BM25 search"""
        try:
            if not documents:
                logger.warning("No documents to index")
                return False
            
            # Store document data
            self.documents_data = []
            corpus_texts = []
            
            for doc in documents:
                doc_data = {
                    'doc_id': doc.doc_id,
                    'content': doc.content,
                    'metadata': doc.metadata or {}
                }
                self.documents_data.append(doc_data)
                corpus_texts.append(doc.content)
            
            # Tokenize corpus
            logger.info(f"Tokenizing {len(corpus_texts)} documents...")
            tokenizer = BM25Tokenizer(self.config)
            self.tokenized_corpus = [tokenizer.tokenize(text) for text in corpus_texts]
            
            # Get BM25 parameters from config
            k1 = self.config.get("bm25_k1", 1.2)
            b = self.config.get("bm25_b", 0.75)
            
            # Create BM25 index
            logger.info("Creating BM25 index...")
            self.bm25 = BM25Okapi(self.tokenized_corpus, k1=k1, b=b)
            
            # Save index to disk
            self.save_index()
            
            logger.info(f"Successfully indexed {len(documents)} documents")
            return True
            
        except Exception as e:
            logger.error(f"Failed to index documents for BM25: {e}")
            return False
    
    def search(self, query_text: str, k: int = 10) -> List[Dict[str, Any]]:
        """Perform BM25 search and return results"""
        try:
            if not self.bm25 or not self.documents_data:
                return []
            
            # Tokenize query
            tokenizer = BM25Tokenizer(self.config)
            tokenized_query = tokenizer.tokenize(query_text)
            
            if not tokenized_query:
                return []
            
            # Get BM25 scores
            scores = self.bm25.get_scores(tokenized_query)
            normalized_scores = self._normalize_scores(scores)
            
            # Get top k results
            top_indices = np.argsort(normalized_scores)[::-1][:k]
            
            # Return results
            results = []
            for idx in top_indices:
                if idx < len(self.documents_data):
                    doc_data = self.documents_data[idx].copy()
                    doc_data['score'] = float(normalized_scores[idx])
                    results.append(doc_data)
            
            return results
            
        except Exception as e:
            logger.error(f"BM25 search failed: {e}")
            return []
    
    def _normalize_scores(self, scores: np.ndarray) -> np.ndarray:
        """Normalize BM25 scores to 0-1 range"""
        if len(scores) == 0:
            return scores
        
        if np.max(scores) == np.min(scores):
            return np.ones_like(scores)
        
        normalized = (scores - np.min(scores)) / (np.max(scores) - np.min(scores))
        return normalized
    
    def get_stats(self) -> Dict[str, Any]:
        """Get statistics about the BM25 index"""
        if not self.bm25 or not self.documents_data:
            return {"indexed_documents": 0, "vocabulary_size": 0}
        
        vocab_size = len(set(token for doc_tokens in self.tokenized_corpus for token in doc_tokens))
        
        return {
            "indexed_documents": len(self.documents_data),
            "vocabulary_size": vocab_size,
            "avg_doc_length": np.mean([len(doc_tokens) for doc_tokens in self.tokenized_corpus]),
            "bm25_k1": getattr(self.bm25, 'k1', 'N/A'),
            "bm25_b": getattr(self.bm25, 'b', 'N/A')
        }


class BM25Tokenizer:
    """Tokenizer for BM25 preprocessing"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.use_advanced = config.get("use_advanced_tokenizer", False)
        
        # Initialize NLTK components if needed
        if self.use_advanced:
            self._setup_nltk()
    
    def _setup_nltk(self):
        """Setup NLTK components"""
        try:
            import nltk
            
            # Download required data
            for resource in ['punkt', 'stopwords']:
                try:
                    nltk.data.find(f'tokenizers/{resource}' if resource == 'punkt' else f'corpora/{resource}')
                except LookupError:
                    nltk.download(resource, quiet=True)
                    
        except ImportError:
            logger.warning("NLTK not available, will use simple tokenization")
            self.use_advanced = False
    
    def tokenize(self, text: str) -> List[str]:
        """Tokenize text based on configuration"""
        if self.use_advanced:
            return self._advanced_tokenize(text)
        else:
            return self._simple_tokenize(text)
    
    def _simple_tokenize(self, text: str) -> List[str]:
        """Simple tokenization using regex"""
        text = text.lower()
        tokens = re.findall(r'\b\w+\b', text)
        return tokens
    
    def _advanced_tokenize(self, text: str) -> List[str]:
        """Advanced tokenization using NLTK"""
        try:
            import nltk
            from nltk.tokenize import word_tokenize
            from nltk.corpus import stopwords
            from nltk.stem import PorterStemmer
            
            # Tokenize and preprocess
            text = text.lower()
            tokens = word_tokenize(text)
            
            # Remove stopwords if configured
            if self.config.get("remove_stopwords", True):
                stop_words = set(stopwords.words('english'))
                tokens = [token for token in tokens if token not in stop_words]
            
            # Apply stemming if configured
            if self.config.get("apply_stemming", False):
                stemmer = PorterStemmer()
                tokens = [stemmer.stem(token) for token in tokens]
            
            # Filter out non-alphabetic tokens
            tokens = [token for token in tokens if token.isalpha()]
            
            return tokens
            
        except Exception as e:
            logger.warning(f"Advanced tokenization failed: {e}, falling back to simple")
            return self._simple_tokenize(text)