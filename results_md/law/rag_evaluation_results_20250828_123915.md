# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 566.28s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.848, mAP=0.731, nDCG@5=0.794, MRR=0.845
  Generation: LLM=0.883, Semantic=0.923
  Component Scores: Retrieval=0.804, Generation=0.903
  Overall Score: 0.854
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.031s, Passage Augment=0.003s, Passage Rerank=0.057s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.656s, Post-generation=2.407s
  Total Prediction Time: 4.154s
  Embedding Tokens: 1298.8
  LLM Tokens: 3127.5 in, 367.5 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.508s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_rerank: 1298.8
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2554.7 in, 80.9 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 572.8 in, 286.6 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.031s
- Passage Augment: 0.003s
- Passage Rerank: 0.057s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.656s
- Post-generation: 2.407s
- Total Prediction Time: 4.154s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 150.84s
  - Total Evaluation: 150.85s

**Pipeline Total:** 566.28s

---

*Report generated on 2025-08-28 12:39:15*
