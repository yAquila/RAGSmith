# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1456.03s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.891, mAP=0.772, nDCG@5=0.836, MRR=0.882
  Generation: LLM=0.804, Semantic=0.899
  Component Scores: Retrieval=0.846, Generation=0.852
  Overall Score: 0.849
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.716s, Retrieval=0.192s, Passage Augment=0.000s, Passage Rerank=10.861s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.102s, Post-generation=0.000s
  Total Prediction Time: 12.872s
  Embedding Tokens: 19283.8
  LLM Tokens: 20450.6 in, 1973.3 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.687s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - passage_rerank: 19263.8
    - retrieval: 20.0
  - LLM Tokens:
    - query_expansion:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.8 in, 84.3 out
      - keyword: 0.0 in, 0.0 out
    - retrieval:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
      - keyword: 0.0 in, 0.0 out
    - generation:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1069.0 in, 90.3 out
      - keyword: 0.0 in, 0.0 out
    - passage_rerank:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 19263.8 in, 1798.7 out
      - keyword: 0.0 in, 0.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.716s
- Retrieval: 0.192s
- Passage Augment: 0.000s
- Passage Rerank: 10.861s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.102s
- Post-generation: 0.000s
- Total Prediction Time: 12.872s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 168.66s
  - Total Evaluation: 168.67s

**Pipeline Total:** 1456.03s

---

*Report generated on 2025-08-22 18:50:11*
