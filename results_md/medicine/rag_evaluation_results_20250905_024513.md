# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1113.07s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.888, mAP=0.759, nDCG@5=0.820, MRR=0.854
  Generation: LLM=0.856, Semantic=0.911
  Component Scores: Retrieval=0.830, Generation=0.884
  Overall Score: 0.857
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.678s, Retrieval=0.138s, Passage Augment=0.003s, Passage Rerank=0.432s, Passage Filter=0.000s, Passage Compress=7.220s, Prompt Maker=0.000s, Generation=1.097s, Post-generation=0.000s
  Total Prediction Time: 9.569s
  Embedding Tokens: 9382.8
  LLM Tokens: 3435.9 in, 1014.0 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.560s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_rerank: 9362.6
  - LLM Tokens:
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2015.9 in, 854.7 out
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.1 in, 80.1 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1302.9 in, 79.2 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.678s
- Retrieval: 0.138s
- Passage Augment: 0.003s
- Passage Rerank: 0.432s
- Passage Filter: 0.000s
- Passage Compress: 7.220s
- Prompt Maker: 0.000s
- Generation: 1.097s
- Post-generation: 0.000s
- Total Prediction Time: 9.569s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 156.03s
  - Total Evaluation: 156.04s

**Pipeline Total:** 1113.07s

---

*Report generated on 2025-09-05 02:45:13*
