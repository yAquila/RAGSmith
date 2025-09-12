# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1064.17s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_keyword_cc + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_keyword_cc + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_keyword_cc + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_keyword_cc + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_keyword_cc + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.822, mAP=0.700, nDCG@5=0.771, MRR=0.834
  Generation: LLM=0.842, Semantic=0.913
  Component Scores: Retrieval=0.782, Generation=0.877
  Overall Score: 0.830
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.712s, Retrieval=0.342s, Passage Augment=0.003s, Passage Rerank=4.245s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.975s, Post-generation=1.712s
  Total Prediction Time: 8.991s
  Embedding Tokens: 12178.3
  LLM Tokens: 15469.8 in, 2138.4 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.649s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_keyword_cc + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_rerank: 12158.2
    - retrieval: 20.0
  - LLM Tokens:
    - passage_rerank:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 12158.2 in, 1747.7 out
      - keyword: 0.0 in, 0.0 out
    - query_expansion:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.8 in, 84.4 out
      - keyword: 0.0 in, 0.0 out
    - generation:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2708.8 in, 108.2 out
      - keyword: 0.0 in, 0.0 out
    - retrieval:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
      - keyword: 0.0 in, 0.0 out
    - post_generation:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 484.9 in, 198.1 out
      - keyword: 0.0 in, 0.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.712s
- Retrieval: 0.342s
- Passage Augment: 0.003s
- Passage Rerank: 4.245s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.975s
- Post-generation: 1.712s
- Total Prediction Time: 8.991s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 164.85s
  - Total Evaluation: 164.86s

**Pipeline Total:** 1064.17s

---

*Report generated on 2025-08-22 15:12:42*
