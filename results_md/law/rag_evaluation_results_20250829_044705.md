# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1110.40s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.873, mAP=0.813, nDCG@5=0.860, MRR=0.934
  Generation: LLM=0.839, Semantic=0.906
  Component Scores: Retrieval=0.870, Generation=0.872
  Overall Score: 0.871
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.051s, Passage Augment=0.000s, Passage Rerank=0.056s, Passage Filter=0.000s, Passage Compress=6.111s, Prompt Maker=0.000s, Generation=0.712s, Post-generation=2.544s
  Total Prediction Time: 9.473s
  Embedding Tokens: 1577.2
  LLM Tokens: 2311.0 in, 1116.7 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.630s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_compress: 337.7
    - passage_rerank: 1219.3
  - LLM Tokens:
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1299.7 in, 740.9 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 412.4 in, 72.4 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 599.0 in, 303.4 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.051s
- Passage Augment: 0.000s
- Passage Rerank: 0.056s
- Passage Filter: 0.000s
- Passage Compress: 6.111s
- Prompt Maker: 0.000s
- Generation: 0.712s
- Post-generation: 2.544s
- Total Prediction Time: 9.473s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 163.00s
  - Total Evaluation: 163.01s

**Pipeline Total:** 1110.40s

---

*Report generated on 2025-08-29 04:47:05*
