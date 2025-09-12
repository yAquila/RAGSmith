# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 507.55s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.788, mAP=0.660, nDCG@5=0.732, MRR=0.802
  Generation: LLM=0.812, Semantic=0.887
  Component Scores: Retrieval=0.746, Generation=0.850
  Overall Score: 0.798
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.266s, Retrieval=0.037s, Passage Augment=0.004s, Passage Rerank=0.072s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.519s, Post-generation=1.548s
  Total Prediction Time: 3.444s
  Embedding Tokens: 1379.3
  LLM Tokens: 2528.7 in, 300.0 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.630s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_rerank: 1379.3
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 130.8 in, 23.0 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 442.1 in, 179.2 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1955.7 in, 97.8 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.266s
- Retrieval: 0.037s
- Passage Augment: 0.004s
- Passage Rerank: 0.072s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.519s
- Post-generation: 1.548s
- Total Prediction Time: 3.444s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 163.03s
  - Total Evaluation: 163.03s

**Pipeline Total:** 507.55s

---

*Report generated on 2025-08-21 13:21:08*
