# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1940.74s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:step_back_prompting_cc + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:step_back_prompting_cc + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:step_back_prompting_cc + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:step_back_prompting_cc + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:step_back_prompting_cc + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.879, mAP=0.783, nDCG@5=0.843, MRR=0.906
  Generation: LLM=0.775, Semantic=0.882
  Component Scores: Retrieval=0.853, Generation=0.828
  Overall Score: 0.841
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.497s, Retrieval=0.209s, Passage Augment=0.000s, Passage Rerank=8.233s, Passage Filter=0.000s, Passage Compress=6.345s, Prompt Maker=0.000s, Generation=0.829s, Post-generation=1.610s
  Total Prediction Time: 17.722s
  Embedding Tokens: 22596.1
  LLM Tokens: 24870.5 in, 2943.8 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.683s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:step_back_prompting_cc + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_rerank: 22267.0
    - retrieval: 20.0
    - passage_compress: 309.1
  - LLM Tokens:
    - passage_rerank:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 22267.0 in, 1838.4 out
      - keyword: 0.0 in, 0.0 out
    - query_expansion:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 210.9 in, 51.3 out
      - keyword: 0.0 in, 0.0 out
    - generation:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 418.2 in, 87.0 out
      - keyword: 0.0 in, 0.0 out
    - retrieval:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
      - keyword: 0.0 in, 0.0 out
    - post_generation:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 448.6 in, 187.1 out
      - keyword: 0.0 in, 0.0 out
    - passage_compress:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1525.9 in, 780.1 out
      - keyword: 0.0 in, 0.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.497s
- Retrieval: 0.209s
- Passage Augment: 0.000s
- Passage Rerank: 8.233s
- Passage Filter: 0.000s
- Passage Compress: 6.345s
- Prompt Maker: 0.000s
- Generation: 0.829s
- Post-generation: 1.610s
- Total Prediction Time: 17.722s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 168.31s
  - Total Evaluation: 168.32s

**Pipeline Total:** 1940.74s

---

*Report generated on 2025-08-22 05:43:03*
