# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 963.24s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.752, mAP=0.659, nDCG@5=0.727, MRR=0.825
  Generation: LLM=0.755, Semantic=0.897
  Component Scores: Retrieval=0.741, Generation=0.826
  Overall Score: 0.783
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.045s, Passage Augment=0.000s, Passage Rerank=0.668s, Passage Filter=0.000s, Passage Compress=6.314s, Prompt Maker=0.000s, Generation=0.867s, Post-generation=0.000s
  Total Prediction Time: 7.894s
  Embedding Tokens: 366.3
  LLM Tokens: 3202.3 in, 1825.3 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.738s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - passage_compress: 366.3
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 489.5 in, 87.9 out
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1376.9 in, 892.9 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1335.9 in, 844.6 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.045s
- Passage Augment: 0.000s
- Passage Rerank: 0.668s
- Passage Filter: 0.000s
- Passage Compress: 6.314s
- Prompt Maker: 0.000s
- Generation: 0.867s
- Post-generation: 0.000s
- Total Prediction Time: 7.894s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 173.77s
  - Total Evaluation: 173.78s

**Pipeline Total:** 963.24s

---

*Report generated on 2025-09-10 03:10:09*
