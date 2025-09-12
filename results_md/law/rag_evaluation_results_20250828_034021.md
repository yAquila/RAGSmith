# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 325.23s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.834, mAP=0.726, nDCG@5=0.788, MRR=0.848
  Generation: LLM=0.850, Semantic=0.906
  Component Scores: Retrieval=0.799, Generation=0.878
  Overall Score: 0.838
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.031s, Passage Augment=0.000s, Passage Rerank=0.654s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.032s, Post-generation=0.000s
  Total Prediction Time: 1.717s
  LLM Tokens: 2519.1 in, 909.9 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.535s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1200.1 in, 76.5 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1319.0 in, 833.4 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.031s
- Passage Augment: 0.000s
- Passage Rerank: 0.654s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.032s
- Post-generation: 0.000s
- Total Prediction Time: 1.717s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 153.45s
  - Total Evaluation: 153.46s

**Pipeline Total:** 325.23s

---

*Report generated on 2025-08-28 03:40:21*
