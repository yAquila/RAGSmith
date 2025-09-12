# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1352.69s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.848, mAP=0.731, nDCG@5=0.794, MRR=0.845
  Generation: LLM=0.858, Semantic=0.908
  Component Scores: Retrieval=0.804, Generation=0.883
  Overall Score: 0.844
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.031s, Passage Augment=0.000s, Passage Rerank=0.057s, Passage Filter=0.000s, Passage Compress=5.120s, Prompt Maker=0.000s, Generation=0.882s, Post-generation=5.710s
  Total Prediction Time: 11.800s
  Embedding Tokens: 1298.8
  LLM Tokens: 2759.3 in, 1367.9 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.726s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_rerank: 1298.8
  - LLM Tokens:
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1485.5 in, 605.0 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 681.1 in, 80.4 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 592.7 in, 682.5 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.031s
- Passage Augment: 0.000s
- Passage Rerank: 0.057s
- Passage Filter: 0.000s
- Passage Compress: 5.120s
- Prompt Maker: 0.000s
- Generation: 0.882s
- Post-generation: 5.710s
- Total Prediction Time: 11.800s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 172.64s
  - Total Evaluation: 172.65s

**Pipeline Total:** 1352.69s

---

*Report generated on 2025-08-28 11:57:44*
