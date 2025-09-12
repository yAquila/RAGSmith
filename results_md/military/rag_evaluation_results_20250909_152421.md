# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 645.77s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_rephrasing + retrieval:hybrid_vector_keyword_cc + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_rephrasing + retrieval:hybrid_vector_keyword_cc + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_rephrasing + retrieval:hybrid_vector_keyword_cc + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_rephrasing + retrieval:hybrid_vector_keyword_cc + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_rephrasing + retrieval:hybrid_vector_keyword_cc + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.000, mAP=0.000, nDCG@5=0.000, MRR=0.000
  Generation: LLM=0.474, Semantic=0.879
  Component Scores: Retrieval=0.000, Generation=0.676
  Overall Score: 0.338
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.307s, Retrieval=0.089s, Passage Augment=0.000s, Passage Rerank=0.892s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=0.816s, Post-generation=2.526s
  Total Prediction Time: 4.631s
  Embedding Tokens: 2520.3
  LLM Tokens: 3352.6 in, 2076.5 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.826s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_rephrasing + retrieval:hybrid_vector_keyword_cc + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 21.4
    - passage_rerank: 2499.0
  - LLM Tokens:
    - post_generation:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 644.1 in, 298.1 out
      - vector: 0.0 in, 0.0 out
    - passage_rerank:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2499.0 in, 1648.5 out
      - vector: 0.0 in, 0.0 out
    - generation:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 64.1 in, 101.7 out
      - vector: 0.0 in, 0.0 out
    - retrieval:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
    - query_expansion:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 145.4 in, 28.2 out
      - vector: 0.0 in, 0.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.307s
- Retrieval: 0.089s
- Passage Augment: 0.000s
- Passage Rerank: 0.892s
- Passage Filter: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.816s
- Post-generation: 2.526s
- Total Prediction Time: 4.631s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 182.59s
  - Total Evaluation: 182.60s

**Pipeline Total:** 645.77s

---

*Report generated on 2025-09-09 15:24:21*
