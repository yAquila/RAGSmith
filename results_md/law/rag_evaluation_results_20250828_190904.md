# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 505.14s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.873, mAP=0.813, nDCG@5=0.860, MRR=0.934
  Generation: LLM=0.841, Semantic=0.907
  Component Scores: Retrieval=0.870, Generation=0.874
  Overall Score: 0.872
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.052s, Passage Augment=0.000s, Passage Rerank=0.056s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=0.993s, Post-generation=2.408s
  Total Prediction Time: 3.509s
  Embedding Tokens: 1239.5
  LLM Tokens: 1705.0 in, 361.1 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.541s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_rerank: 1219.3
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1128.0 in, 74.3 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 577.0 in, 286.8 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.052s
- Passage Augment: 0.000s
- Passage Rerank: 0.056s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.993s
- Post-generation: 2.408s
- Total Prediction Time: 3.509s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 154.15s
  - Total Evaluation: 154.16s

**Pipeline Total:** 505.14s

---

*Report generated on 2025-08-28 19:09:04*
