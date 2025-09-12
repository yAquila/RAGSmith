# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 617.17s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.888, mAP=0.765, nDCG@5=0.824, MRR=0.863
  Generation: LLM=0.873, Semantic=0.918
  Component Scores: Retrieval=0.835, Generation=0.895
  Overall Score: 0.865
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.682s, Retrieval=0.143s, Passage Augment=0.003s, Passage Rerank=0.431s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.289s, Post-generation=2.109s
  Total Prediction Time: 4.656s
  Embedding Tokens: 9337.5
  LLM Tokens: 2325.4 in, 414.2 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.515s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_rerank: 9317.3
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.1 in, 80.7 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1696.1 in, 83.6 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 512.2 in, 249.8 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.682s
- Retrieval: 0.143s
- Passage Augment: 0.003s
- Passage Rerank: 0.431s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.289s
- Post-generation: 2.109s
- Total Prediction Time: 4.656s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 151.45s
  - Total Evaluation: 151.46s

**Pipeline Total:** 617.17s

---

*Report generated on 2025-08-29 10:02:37*
