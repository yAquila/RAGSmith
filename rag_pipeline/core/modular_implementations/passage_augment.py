import logging
from typing import List, TypedDict, Dict, Any
import re
from collections import defaultdict
import numpy as np
from rag_pipeline.core.modular_framework import (
    PassageAugmentComponent, Document, Query
)
from rag_pipeline.core.dataset import RAGDataset
from rag_pipeline.util.comparison.semantic_comparison import SemanticComparison

logger = logging.getLogger(__name__)

class PassageAugmentResult(TypedDict):
    documents: List[Document]
    embedding_token_count: float
    llm_input_token_count: float
    llm_output_token_count: float

class NonePassageAugment(PassageAugmentComponent):
    """No passage augmentation - pass documents through unchanged"""
    
    async def augment_passages(self, documents: List[Document], query: Query) -> PassageAugmentResult:
        """Pass documents through unchanged"""
        result = PassageAugmentResult(
            documents=documents,
            embedding_token_count=0.0,
            llm_input_token_count=0.0,
            llm_output_token_count=0.0
        )
        return result


class PrevNextAugmenter(PassageAugmentComponent):
    """Augment passages with previous and next chunks"""
    
    @staticmethod
    def merge_chunks(chunk_ids, n=1):
        """
        Merge chunks by prefix and expand each chunk to include n previous and n next chunks.
        
        Args:
            chunk_ids: List of chunk IDs like 'prefix_c0001'
            n: Number of previous and next chunks to include

        Returns:
            List of merged chunk ID strings with underscores
        """
        group_dict = defaultdict(list)
        pattern = re.compile(r"^(.*)_c(\d{4})$")

        # Step 1: Group by prefix and extract numeric index
        for cid in chunk_ids:
            match = pattern.match(cid)
            if not match:
                raise ValueError(f"Invalid chunk ID format: {cid}")
            prefix, index = match.groups()
            group_dict[prefix].append(int(index))

        result = []

        # Step 2: Process each group
        for prefix, indices in group_dict.items():
            expanded_ranges = []

            for idx in indices:
                start = max(0, idx - n)
                end = idx + n
                expanded_ranges.append((start, end))

            # Step 3: Merge overlapping or adjacent ranges
            merged = []
            for start, end in sorted(expanded_ranges):
                if not merged or start > merged[-1][1] + 1:
                    merged.append([start, end])
                else:
                    merged[-1][1] = max(merged[-1][1], end)

            # Step 4: Build final chunk strings
            for start, end in merged:
                chunks = [f"{prefix}_c{str(i).zfill(4)}" for i in range(start, end + 1)]
                result.append("--".join(chunks))

        return result


    async def augment_passages(self, documents: List[Document], query: Query) -> PassageAugmentResult:
        """Augment passages with surrounding context"""
        n = self.config.get("n", 1)
        if n == 0:
            return PassageAugmentResult(
                documents=documents,
                embedding_token_count=0.0,
                llm_input_token_count=0.0,
                llm_output_token_count=0.0
            )
        else:
            doc_id_list = [doc.doc_id for doc in documents]
            merged_chunks = PrevNextAugmenter.merge_chunks(doc_id_list, n)
            logger.debug(f"Merged chunks: {merged_chunks}")

            merged_documents = []
            for chunk in merged_chunks:
                chunk_ids = chunk.split("--")
                merged_content = ""
                for cid in chunk_ids:
                    chunk_content = RAGDataset.get_chunk_by_id(cid).get("content","sdasd")
                    merged_content += chunk_content + "\n"
                merged_documents.append(Document(
                    doc_id=chunk,
                    content=merged_content,
                    metadata={
                        "doc_id": chunk,
                        "article_id": "_".join(chunk.split("--")[0].split("_")[:2])
                    }
                ))
            logger.debug(f"Merged documents: {merged_documents}")
            
            return PassageAugmentResult(
                documents=merged_documents,
                embedding_token_count=0.0,
                llm_input_token_count=0.0,
                llm_output_token_count=0.0
            )



class RelevantSegmentExtractor(PassageAugmentComponent):
    """Extract relevant segments from the documents"""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.semantic_evaluator = SemanticComparison(config.get("embedding_model", "mxbai-embed-large"))
        self.max_chunk_number_in_segment = config.get("max_chunk_number_in_segment", 3)
        self.irrelevant_chunk_penalty = config.get("irrelevant_chunk_penalty", 0.18)
        self.decay_rate = config.get("decay_rate", 30)
        self.overall_max_chunk_number = config.get("overall_max_chunk_number", 10)

    def get_score(self, chunk_list: List[Dict], query: Query, ranks: List[int]) -> float:
        """Get the score of the chunk"""

        individual_scores = []
        for i, chunk in enumerate(chunk_list):
            chunk_content = chunk.get("content", "")
            absolute_relevance_score = self.semantic_evaluator.get_similarity_score(chunk_content, query.processed_text)
            chunk_score = np.exp(-ranks[i] / self.decay_rate) * absolute_relevance_score - self.irrelevant_chunk_penalty
            individual_scores.append(chunk_score)

        return sum(individual_scores)

    def find_ranks(self, documents: List[Document], chunk_ids: List[str]) -> List[int]:
        """Find the ranks of the chunks in the article"""
        ranks = [len(documents)*2] * len(chunk_ids)
        for i, chunk_id in enumerate(chunk_ids):
            for j, doc in enumerate(documents):
                if doc.doc_id == chunk_id:
                    ranks[i] = j+1
                    break
        
        return ranks

    def get_best_segments_in_an_article(self, documents: List[Document], article_id: str, query: Query) -> List[str]:
        """Extract relevant segments from the documents"""


        # Get all the chunks in the article
        chunks = RAGDataset.get_all_chunks_by_article_id(article_id)
        if chunks is None:
            return []

        # Find the best n segments (by score) in the article
        segment_candidates = []
        for start in range(len(chunks)):
            for end in range(start+1, min(start+self.max_chunk_number_in_segment+1, len(chunks))):
                chunk_list = chunks[start:end]
                ranks = self.find_ranks(documents, [chunk.get("id", "") for chunk in chunk_list])
                chunk_score = self.get_score(chunk_list, query, ranks)
                segment_candidates.append((chunk_score, chunk_list))

        # Sort by score descending
        segment_candidates.sort(key=lambda x: x[0], reverse=True)

        selected_segments = []
        total_chunks = 0
        for score, segment in segment_candidates:
            segment_len = len(segment)
            # Avoid adding segments that would exceed the overall_max_chunk_number
            if total_chunks + segment_len > self.overall_max_chunk_number:
                continue
            # Avoid adding duplicate chunks (by id) across segments
            segment_chunk_ids = set(chunk.get("id", "") for chunk in segment)
            already_selected_ids = set(chunk.get("id", "") for seg in selected_segments for chunk in seg)
            if segment_chunk_ids & already_selected_ids:
                continue
            selected_segments.append(segment)
            total_chunks += segment_len
            if total_chunks >= self.overall_max_chunk_number:
                break

        # Join the content of each segment, separated by double newlines
        best_segments_content = "\n\n".join(
            "\n".join(chunk.get("content", "") for chunk in segment) for segment in selected_segments
        )
        return best_segments_content


    def extract_article_ids(self, documents: List[Document]) -> List[str]:
        """Extract the article ids from the documents"""
        return list(set(doc.metadata.get("article_id", "") for doc in documents))

    async def augment_passages(self, documents: List[Document], query: Query) -> PassageAugmentResult:
        """Extract relevant segments from the documents"""
        
        article_ids = self.extract_article_ids(documents)
        best_segments = []
        logger.info(f"Article IDs: {article_ids}")
        for article_id in article_ids:
            best_segment = self.get_best_segments_in_an_article(documents, article_id, query)
            if best_segment is not None and len(best_segment) > 0:
                best_segments.append(best_segment)
        best_segments_content = "\n------------------------------\n".join(best_segments)
        logger.info(f"Best segments: {best_segments_content}")

        return PassageAugmentResult(
            documents=documents,
            embedding_token_count=0.0,
            llm_input_token_count=0.0,
            llm_output_token_count=0.0)