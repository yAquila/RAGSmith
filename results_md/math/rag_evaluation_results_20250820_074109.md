# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 944.59s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_rephrasing + retrieval:hybrid_vector_keyword_cc + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_rephrasing + retrieval:hybrid_vector_keyword_cc + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_rephrasing + retrieval:hybrid_vector_keyword_cc + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_rephrasing + retrieval:hybrid_vector_keyword_cc + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_rephrasing + retrieval:hybrid_vector_keyword_cc + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.655, mAP=0.622, nDCG@5=0.685, MRR=0.853
  Generation: LLM=0.769, Semantic=0.886
  Component Scores: Retrieval=0.704, Generation=0.827
  Overall Score: 0.766
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.297s, Retrieval=0.090s, Passage Augment=1.501s, Passage Rerank=1.083s, Passage Filter=0.000s, Passage Compress=2.133s, Prompt Maker=0.000s, Generation=1.258s, Post-generation=1.505s
  Total Prediction Time: 7.867s
  Embedding Tokens: 3161.4
  LLM Tokens: 6183.1 in, 2604.6 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.578s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_rephrasing + retrieval:hybrid_vector_keyword_cc + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_rerank: 2008.2
    - retrieval: 20.1
    - passage_compress: 1133.1
  - LLM Tokens:
    - passage_rerank:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2008.2 in, 1740.4 out
      - keyword: 0.0 in, 0.0 out
    - query_expansion:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 144.8 in, 26.7 out
      - keyword: 0.0 in, 0.0 out
    - generation:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1265.2 in, 100.5 out
      - keyword: 0.0 in, 0.0 out
    - retrieval:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
      - keyword: 0.0 in, 0.0 out
    - post_generation:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 431.1 in, 173.6 out
      - keyword: 0.0 in, 0.0 out
    - passage_compress:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2333.8 in, 563.4 out
      - keyword: 0.0 in, 0.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.297s
- Retrieval: 0.090s
- Passage Augment: 1.501s
- Passage Rerank: 1.083s
- Passage Filter: 0.000s
- Passage Compress: 2.133s
- Prompt Maker: 0.000s
- Generation: 1.258s
- Post-generation: 1.505s
- Total Prediction Time: 7.867s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 157.81s
  - Total Evaluation: 157.82s

**Pipeline Total:** 944.59s

---

*Report generated on 2025-08-20 07:41:09*
