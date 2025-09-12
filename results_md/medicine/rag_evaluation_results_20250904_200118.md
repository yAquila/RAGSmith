# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1538.58s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.782, mAP=0.690, nDCG@5=0.744, MRR=0.832
  Generation: LLM=0.864, Semantic=0.907
  Component Scores: Retrieval=0.762, Generation=0.886
  Overall Score: 0.824
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.031s, Passage Augment=0.005s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=10.269s, Prompt Maker=0.000s, Generation=1.118s, Post-generation=2.407s
  Total Prediction Time: 13.830s
  LLM Tokens: 4684.5 in, 1585.7 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.555s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - LLM Tokens:
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2823.2 in, 1218.0 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1291.3 in, 80.8 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 570.0 in, 287.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.031s
- Passage Augment: 0.005s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 10.269s
- Prompt Maker: 0.000s
- Generation: 1.118s
- Post-generation: 2.407s
- Total Prediction Time: 13.830s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 155.51s
  - Total Evaluation: 155.52s

**Pipeline Total:** 1538.58s

---

*Report generated on 2025-09-04 20:01:18*
