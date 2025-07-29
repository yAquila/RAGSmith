import logging
from typing import List, TypedDict
import re
from collections import defaultdict

from rag_pipeline.core.modular_framework import (
    PassageAugmentComponent, Document, Query
)
from rag_pipeline.core.dataset import RAGDataset

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

