# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1084.36s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.863, mAP=0.736, nDCG@5=0.801, MRR=0.848
  Generation: LLM=0.850, Semantic=0.912
  Component Scores: Retrieval=0.812, Generation=0.881
  Overall Score: 0.846
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.031s, Passage Augment=0.003s, Passage Rerank=0.709s, Passage Filter=0.000s, Passage Compress=7.499s, Prompt Maker=0.000s, Generation=1.028s, Post-generation=0.000s
  Total Prediction Time: 9.271s
  Embedding Tokens: 1319.0
  LLM Tokens: 4374.9 in, 1851.6 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.572s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - passage_rerank: 1319.0
  - LLM Tokens:
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2097.0 in, 888.6 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 958.9 in, 88.0 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1319.0 in, 875.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.031s
- Passage Augment: 0.003s
- Passage Rerank: 0.709s
- Passage Filter: 0.000s
- Passage Compress: 7.499s
- Prompt Maker: 0.000s
- Generation: 1.028s
- Post-generation: 0.000s
- Total Prediction Time: 9.271s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 157.20s
  - Total Evaluation: 157.21s

**Pipeline Total:** 1084.36s

---

*Report generated on 2025-09-05 08:14:27*
