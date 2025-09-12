# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 629.89s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.699, mAP=0.619, nDCG@5=0.688, MRR=0.807
  Generation: LLM=0.812, Semantic=0.911
  Component Scores: Retrieval=0.703, Generation=0.861
  Overall Score: 0.782
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.073s, Passage Augment=2.278s, Passage Rerank=0.585s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.756s, Post-generation=0.000s
  Total Prediction Time: 4.692s
  Embedding Tokens: 994.6
  LLM Tokens: 3224.1 in, 1677.7 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.606s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - passage_rerank: 994.6
  - LLM Tokens:
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 994.6 in, 1567.8 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2229.5 in, 109.9 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.073s
- Passage Augment: 2.278s
- Passage Rerank: 0.585s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.756s
- Post-generation: 0.000s
- Total Prediction Time: 4.692s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 160.57s
  - Total Evaluation: 160.58s

**Pipeline Total:** 629.89s

---

*Report generated on 2025-08-20 08:05:36*
