# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1653.38s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_cc_dbsf + retrieval:hybrid_vector_keyword_cc + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_cc_dbsf + retrieval:hybrid_vector_keyword_cc + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_cc_dbsf + retrieval:hybrid_vector_keyword_cc + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_cc_dbsf + retrieval:hybrid_vector_keyword_cc + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_cc_dbsf + retrieval:hybrid_vector_keyword_cc + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.872, mAP=0.772, nDCG@5=0.832, MRR=0.887
  Generation: LLM=0.864, Semantic=0.914
  Component Scores: Retrieval=0.841, Generation=0.889
  Overall Score: 0.865
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.705s, Retrieval=0.191s, Passage Augment=0.003s, Passage Rerank=10.674s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.763s, Post-generation=1.461s
  Total Prediction Time: 14.798s
  Embedding Tokens: 19110.4
  LLM Tokens: 21919.1 in, 2200.6 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.734s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_cc_dbsf + retrieval:hybrid_vector_keyword_cc + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_rerank: 19090.4
    - retrieval: 20.0
  - LLM Tokens:
    - passage_rerank:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 19090.4 in, 1843.2 out
      - keyword: 0.0 in, 0.0 out
    - query_expansion:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.8 in, 83.4 out
      - keyword: 0.0 in, 0.0 out
    - generation:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2279.6 in, 106.1 out
      - keyword: 0.0 in, 0.0 out
    - retrieval:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
      - keyword: 0.0 in, 0.0 out
    - post_generation:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 431.3 in, 167.8 out
      - keyword: 0.0 in, 0.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.705s
- Retrieval: 0.191s
- Passage Augment: 0.003s
- Passage Rerank: 10.674s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.763s
- Post-generation: 1.461s
- Total Prediction Time: 14.798s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 173.40s
  - Total Evaluation: 173.41s

**Pipeline Total:** 1653.38s

---

*Report generated on 2025-08-22 16:05:59*
