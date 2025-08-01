"""
Advanced RAG Modular Framework

This module defines the modular framework for building advanced RAG pipelines.
Each category in the RAG pipeline is represented as an abstract base class with
concrete implementations for specific techniques.

Categories:
1. Pre-Embedding
2. Query Expansion/Refinement  
3. Retrieval
4. Passage Augment
5. Passage Rerank
6. Passage Filter
7. Passage Compress
8. Prompt Maker
9. Generator
10. Post-generation
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass
import time
import logging

logger = logging.getLogger(__name__)

# Base data structures used across components
@dataclass
class Document:
    """Represents a document in the RAG pipeline"""
    doc_id: str
    content: str
    metadata: Optional[Dict[str, Any]] = None
    score: Optional[float] = None
    def to_dict(self):
        """Convert Document to dictionary"""
        return {
            "doc_id": self.doc_id,
            "content": self.content,
            "metadata": self.metadata,
            "score": self.score
        }


@dataclass
class Query:
    """Represents a query with potential expansion/refinement"""
    original_text: str
    processed_text: str
    expanded_queries: Optional[List[str]] = None
    metadata: Optional[Dict[str, Any]] = None


@dataclass
class Context:
    """Represents the context for generation"""
    documents: List[Document]
    formatted_text: str
    metadata: Optional[Dict[str, Any]] = None


# ==================== CATEGORY 1: PRE-EMBEDDING ====================

class PreEmbeddingComponent(ABC):
    """
    Abstract base class for pre-embedding techniques.
    
    These components process documents before they are embedded and stored,
    including chunking strategies, context enrichment, etc.
    """
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
    
    @abstractmethod
    async def process_documents(self, documents: List[Document]) -> List[Document]:
        """
        Process documents before embedding.
        
        Args:
            documents: List of raw documents
            
        Returns:
            List of processed documents ready for embedding
        """
        pass


# ==================== CATEGORY 2: QUERY EXPANSION/REFINEMENT ====================

class QueryExpansionComponent(ABC):
    """
    Abstract base class for query expansion/refinement techniques.
    
    These components modify or expand the original query to improve retrieval.
    """
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
    
    @abstractmethod
    async def expand_query(self, query: str) -> Query:
        """
        Expand or refine the input query.
        
        Args:
            query: Original query string
            
        Returns:
            Query object with expanded/refined versions
        """
        pass


# ==================== CATEGORY 3: RETRIEVAL ====================

class RetrievalComponent(ABC):
    """
    Abstract base class for retrieval techniques.
    
    These components retrieve relevant documents based on the query.
    """
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
    
    @abstractmethod
    async def retrieve(self, query: Query, k: Optional[int] = None) -> List[Document]:
        """
        Retrieve relevant documents for the query.
        
        Args:
            query: Query object (potentially expanded)
            k: Number of documents to retrieve
            
        Returns:
            List of retrieved documents with scores
        """
        pass
    
    @abstractmethod
    async def index_documents(self, documents: List[Document]) -> bool:
        """
        Index documents for retrieval.
        
        Args:
            documents: List of documents to index
            
        Returns:
            True if indexing successful, False otherwise
        """
        pass



# ==================== CATEGORY 4: PASSAGE RERANK ====================

class PassageRerankComponent(ABC):
    """
    Abstract base class for passage reranking techniques.
    
    These components rerank retrieved passages to improve relevance ordering.
    """
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
    
    @abstractmethod
    async def rerank_passages(self, documents: List[Document], query: Query) -> List[Document]:
        """
        Rerank retrieved passages based on relevance.
        
        Args:
            documents: List of retrieved documents
            query: Original query
            
        Returns:
            List of reranked documents
        """
        pass


# ==================== CATEGORY 5: PASSAGE FILTER ====================

class PassageFilterComponent(ABC):
    """
    Abstract base class for passage filtering techniques.
    
    These components filter passages based on various criteria.
    """
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
    
    @abstractmethod
    async def filter_passages(self, documents: List[Document], query: Query) -> List[Document]:
        """
        Filter passages based on relevance criteria.
        
        Args:
            documents: List of documents to filter
            query: Original query
            
        Returns:
            List of filtered documents
        """
        pass


# ==================== CATEGORY 6: PASSAGE AUGMENT ====================

class PassageAugmentComponent(ABC):
    """
    Abstract base class for passage augmentation techniques.
    
    These components enhance retrieved passages with additional context.
    """
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
    
    @abstractmethod
    async def augment_passages(self, documents: List[Document], query: Query) -> List[Document]:
        """
        Augment retrieved passages with additional context.
        
        Args:
            documents: List of retrieved documents
            query: Original query
            
        Returns:
            List of augmented documents
        """
        pass


# ==================== CATEGORY 7: PASSAGE COMPRESS ====================

class PassageCompressComponent(ABC):
    """
    Abstract base class for passage compression techniques.
    
    These components compress or summarize passages to fit context limits.
    """
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
    
    @abstractmethod
    async def compress_passages(self, documents: List[Document], query: Query) -> List[Document]:
        """
        Compress or summarize passages.
        
        Args:
            documents: List of documents to compress
            query: Original query for context
            
        Returns:
            List of compressed documents
        """
        pass


# ==================== CATEGORY 8: PROMPT MAKER ====================

class PromptMakerComponent(ABC):
    """
    Abstract base class for prompt construction techniques.
    
    These components format the context and query into prompts for generation.
    """
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
    
    @abstractmethod
    async def make_prompt(self, query: Query, documents: List[Document]) -> str:
        """
        Create a prompt from query and retrieved documents.
        
        Args:
            query: Query object
            documents: List of relevant documents
            
        Returns:
            Formatted prompt string
        """
        pass


# ==================== CATEGORY 9: GENERATOR ====================

class GeneratorComponent(ABC):
    """
    Abstract base class for generation techniques.
    
    These components generate answers based on the prompt.
    """
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
    
    @abstractmethod
    async def generate(self, prompt: str, query: Query) -> str:
        """
        Generate answer based on the prompt.
        
        Args:
            prompt: Formatted prompt
            query: Original query for context
            
        Returns:
            Generated answer
        """
        pass


# ==================== CATEGORY 10: POST-GENERATION ====================

class PostGenerationComponent(ABC):
    """
    Abstract base class for post-generation techniques.
    
    These components refine or validate the generated answer.
    """
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
    
    @abstractmethod
    async def post_process(self, generated_answer: str, query: Query, context: Context) -> str:
        """
        Post-process the generated answer.
        
        Args:
            generated_answer: Initial generated answer
            query: Original query
            context: Context used for generation
            
        Returns:
            Refined answer
        """
        pass


# ==================== PIPELINE EXECUTION RESULT ====================

@dataclass
class RAGExecutionResult:
    """Result of executing the RAG pipeline"""
    original_query: str
    processed_query: Query
    retrieved_documents: List[Document]
    final_documents: List[Document]
    prompt: str
    generated_answer: str
    final_answer: str
    
    # Timing information
    pre_embedding_time: float = 0.0
    query_expansion_time: float = 0.0
    retrieval_time: float = 0.0
    passage_augment_time: float = 0.0
    passage_rerank_time: float = 0.0
    passage_filter_time: float = 0.0
    passage_compress_time: float = 0.0
    prompt_maker_time: float = 0.0
    generation_time: float = 0.0
    post_generation_time: float = 0.0
    total_time: float = 0.0
    
    # Component information
    timing_info: Optional[Dict[str, float]] = None
    # Token counts
    embedding_token_counts: Dict[str, float] = None
    llm_input_token_counts: Dict[str, float] = None
    llm_output_token_counts: Dict[str, float] = None
    
    def __post_init__(self):
        if self.embedding_token_counts is None:
            self.embedding_token_counts = {}
        if self.llm_input_token_counts is None:
            self.llm_input_token_counts = {}
        if self.llm_output_token_counts is None:
            self.llm_output_token_counts = {} 