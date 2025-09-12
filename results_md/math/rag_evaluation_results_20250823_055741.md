# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1723.33s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_keyword_cc + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_keyword_cc + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_keyword_cc + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_keyword_cc + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_keyword_cc + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.888, mAP=0.782, nDCG@5=0.840, MRR=0.885
  Generation: LLM=0.775, Semantic=0.901
  Component Scores: Retrieval=0.849, Generation=0.838
  Overall Score: 0.843
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.708s, Retrieval=0.190s, Passage Augment=0.003s, Passage Rerank=7.094s, Passage Filter=0.000s, Passage Compress=5.049s, Prompt Maker=0.000s, Generation=0.974s, Post-generation=1.595s
  Total Prediction Time: 15.614s
  Embedding Tokens: 19839.8
  LLM Tokens: 22637.4 in, 2827.9 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.617s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_keyword_cc + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_rerank: 19239.4
    - retrieval: 20.0
    - passage_compress: 580.4
  - LLM Tokens:
    - passage_rerank:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 19239.4 in, 1809.2 out
      - keyword: 0.0 in, 0.0 out
    - query_expansion:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.8 in, 83.8 out
      - keyword: 0.0 in, 0.0 out
    - generation:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 709.5 in, 91.0 out
      - keyword: 0.0 in, 0.0 out
    - retrieval:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
      - keyword: 0.0 in, 0.0 out
    - post_generation:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 439.1 in, 185.1 out
      - keyword: 0.0 in, 0.0 out
    - passage_compress:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2131.6 in, 658.8 out
      - keyword: 0.0 in, 0.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.708s
- Retrieval: 0.190s
- Passage Augment: 0.003s
- Passage Rerank: 7.094s
- Passage Filter: 0.000s
- Passage Compress: 5.049s
- Prompt Maker: 0.000s
- Generation: 0.974s
- Post-generation: 1.595s
- Total Prediction Time: 15.614s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 161.74s
  - Total Evaluation: 161.75s

**Pipeline Total:** 1723.33s

---

*Report generated on 2025-08-23 05:57:41*
