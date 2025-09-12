# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1672.11s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.880, mAP=0.776, nDCG@5=0.837, MRR=0.890
  Generation: LLM=0.771, Semantic=0.883
  Component Scores: Retrieval=0.846, Generation=0.827
  Overall Score: 0.836
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.707s, Retrieval=0.148s, Passage Augment=0.000s, Passage Rerank=4.602s, Passage Filter=0.000s, Passage Compress=6.980s, Prompt Maker=0.000s, Generation=0.814s, Post-generation=1.754s
  Total Prediction Time: 15.005s
  Embedding Tokens: 10375.2
  LLM Tokens: 12693.3 in, 3004.0 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.715s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_rerank: 10031.6
    - retrieval: 20.0
    - passage_compress: 323.5
  - LLM Tokens:
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 10031.6 in, 1798.7 out
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.8 in, 83.7 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 437.2 in, 84.1 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 469.3 in, 204.8 out
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1637.4 in, 832.7 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.707s
- Retrieval: 0.148s
- Passage Augment: 0.000s
- Passage Rerank: 4.602s
- Passage Filter: 0.000s
- Passage Compress: 6.980s
- Prompt Maker: 0.000s
- Generation: 0.814s
- Post-generation: 1.754s
- Total Prediction Time: 15.005s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 171.47s
  - Total Evaluation: 171.49s

**Pipeline Total:** 1672.11s

---

*Report generated on 2025-08-22 19:58:58*
