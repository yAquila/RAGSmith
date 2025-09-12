# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1006.46s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.828, mAP=0.659, nDCG@5=0.738, MRR=0.772
  Generation: LLM=0.789, Semantic=0.891
  Component Scores: Retrieval=0.749, Generation=0.840
  Overall Score: 0.795
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.033s, Passage Augment=0.000s, Passage Rerank=0.687s, Passage Filter=0.000s, Passage Compress=6.863s, Prompt Maker=0.000s, Generation=0.813s, Post-generation=0.000s
  Total Prediction Time: 8.397s
  Embedding Tokens: 324.7
  LLM Tokens: 3316.1 in, 1765.4 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.667s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - passage_compress: 324.7
  - LLM Tokens:
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1349.4 in, 857.7 out
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1536.4 in, 823.5 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 430.4 in, 84.2 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.033s
- Passage Augment: 0.000s
- Passage Rerank: 0.687s
- Passage Filter: 0.000s
- Passage Compress: 6.863s
- Prompt Maker: 0.000s
- Generation: 0.813s
- Post-generation: 0.000s
- Total Prediction Time: 8.397s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 166.67s
  - Total Evaluation: 166.68s

**Pipeline Total:** 1006.46s

---

*Report generated on 2025-08-20 18:07:48*
