import logging
from typing import List, TypedDict, Dict, Any
import re
import hashlib
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
    llm_token_count: Dict[str, Dict[str, float]]  # {"model_name": {"in": float, "out": float}}

class NonePassageAugment(PassageAugmentComponent):
    """No passage augmentation - pass documents through unchanged"""
    
    async def augment_passages(self, documents: List[Document], query: Query) -> PassageAugmentResult:
        """Pass documents through unchanged"""
        result = PassageAugmentResult(
            documents=documents,
            embedding_token_count=0.0,
            llm_token_count={}
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
                llm_token_count={}
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
                    chunk_content = RAGDataset.get_chunk_by_id(cid).get("content","")
                    if chunk_content is "":
                        continue
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
                llm_token_count={}
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
        self.similarity_score_cache = {}

    def get_score(self, chunk_list: List[Dict], query: Query, ranks: List[int]) -> float:
        """Get the score of the chunk"""

        individual_scores = []
        for i, chunk in enumerate(chunk_list):
            chunk_content = chunk.get("content", "")
            # Use a simple hash as the key for similarity_score_cache
            key_str = chunk_content + "||" + query.processed_text
            key_hash = hashlib.sha256(key_str.encode()).hexdigest()
            if key_hash not in self.similarity_score_cache:
                self.similarity_score_cache[key_hash] = self.semantic_evaluator.get_similarity_score(chunk_content, query.processed_text)
            absolute_relevance_score = self.similarity_score_cache[key_hash]    
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

    def get_best_segments_in_an_article(self, documents: List[Document], article_id: str, query: Query) -> List[Dict]:
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
                seg = {
                    "chunk_list": chunk_list,
                    "score": chunk_score,
                    "chunk_ids": [chunk.get("id", "") for chunk in chunk_list],
                    "article_id": article_id
                }
                segment_candidates.append(seg)

        # Sort by score descending
        segment_candidates.sort(key=lambda x: x["score"], reverse=True)

        # selected_segments = []
        # total_chunks = 0
        # for score, segment in segment_candidates:
        #     segment_len = len(segment)
        #     # Avoid adding segments that would exceed the overall_max_chunk_number
        #     if total_chunks + segment_len > self.overall_max_chunk_number - current_used_chunk_number:
        #         continue
        #     # Avoid adding duplicate chunks (by id) across segments
        #     segment_chunk_ids = set(chunk.get("id", "") for chunk in segment)
        #     already_selected_ids = set(chunk.get("id", "") for seg in selected_segments for chunk in seg)
        #     if segment_chunk_ids & already_selected_ids:
        #         continue
        #     selected_segments.append(segment)
        #     total_chunks += segment_len
        #     if total_chunks >= self.overall_max_chunk_number - current_used_chunk_number:
        #         break

        # # Join the content of each segment, separated by double newlines
        # best_segments_content = "\n\n".join(
        #     "\n".join(chunk.get("content", "") for chunk in segment) for segment in selected_segments
        # )
        # return best_segments_content

        return segment_candidates[:5]

    def extract_article_ids(self, documents: List[Document]) -> List[str]:
        """Extract the article ids from the documents"""
        return list(set(doc.metadata.get("article_id", "") for doc in documents))

    def merge_segments_if_possible(self, segments: List[Dict]) -> List[Dict]:
        """Merge segments if they are close to each other"""
        merged_segments = []
        for segment in segments:
            if not merged_segments:
                merged_segments.append(segment)
            else:
                merged = False
                for merged_segment in merged_segments:
                    if merged_segment['article_id'] == segment['article_id']:
                        # Extract just the chunk numbers for comparison (e.g., c0002)
                        def extract_chunk_num(cid):
                            # Handles ids like coderefactoring_4b3a67fa_c0006
                            return cid.split('_')[-1] if cid else ""
                        merged_chunk_nums = set(extract_chunk_num(cid) for cid in merged_segment['chunk_ids'])
                        segment_chunk_nums = set(extract_chunk_num(cid) for cid in segment['chunk_ids'])
                        # Check for any overlap in chunk numbers
                        if merged_chunk_nums & segment_chunk_nums:
                            # Merge chunk_ids, preserving order and uniqueness
                            all_chunk_ids = merged_segment['chunk_ids'] + segment['chunk_ids']
                            seen = set()
                            merged_segment['chunk_ids'] = [x for x in all_chunk_ids if not (extract_chunk_num(x) in seen or seen.add(extract_chunk_num(x)))]
                            # Merge chunk_list, preserving order and uniqueness by chunk number
                            all_chunks = merged_segment['chunk_list'] + segment['chunk_list']
                            seen_chunks = set()
                            merged_segment['chunk_list'] = []
                            for chunk in all_chunks:
                                chunk_id = chunk.get("id", "")
                                chunk_num = extract_chunk_num(chunk_id)
                                if chunk_num not in seen_chunks:
                                    merged_segment['chunk_list'].append(chunk)
                                    seen_chunks.add(chunk_num)
                            merged_segment['score'] = max(merged_segment['score'], segment['score'])
                            merged = True
                            break
                if not merged:
                    merged_segments.append(segment)

        return merged_segments


    async def augment_passages(self, documents: List[Document], query: Query) -> PassageAugmentResult:
        """Extract relevant segments from the documents"""

        article_ids = self.extract_article_ids(documents)
        best_segments = []
        logger.info(f"Article IDs: {article_ids}")
        for article_id in article_ids:
            best_segments_in_article = self.get_best_segments_in_an_article(documents, article_id, query)
            if best_segments_in_article is not None and len(best_segments_in_article) > 0:
                best_segments.extend(best_segments_in_article)
        best_segments = self.merge_segments_if_possible(best_segments)
        best_segments.sort(key=lambda x: x["score"], reverse=True)
        new_documents = []
        total_chunk_number = 0
        while total_chunk_number < self.overall_max_chunk_number and len(best_segments) > 0:
            best_segment = best_segments.pop(0)
            if best_segment is None:
                break
            total_chunk_number += len(best_segment["chunk_ids"])
            article_id = best_segment['article_id']
            new_documents.append(Document(
                doc_id=f"{article_id}__{'--'.join([a.split('_')[-1] for a in best_segment['chunk_ids'] if a is not None])}",
                score=best_segment["score"],
                content="\n".join([chunk.get("content", "") for chunk in best_segment["chunk_list"]]),
                metadata={
                    "doc_id": f"{article_id}__{'--'.join([a.split('_')[-1] for a in best_segment['chunk_ids'] if a is not None])}",
                    "article_id": article_id,
                }
            ))

        logger.debug(f"RSE augmented documents: {new_documents}")

        return PassageAugmentResult(
            documents=new_documents,
            embedding_token_count=0.0,
            llm_token_count={}
        )