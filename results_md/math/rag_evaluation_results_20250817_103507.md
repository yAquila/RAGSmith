# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 11923.16s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_hypergraph_simply + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_hypergraph_simply + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_hypergraph_simply + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_hypergraph_simply + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_hypergraph_simply + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.795, mAP=0.705, nDCG@5=0.775, MRR=0.872
  Generation: LLM=0.808, Semantic=0.895
  Component Scores: Retrieval=0.787, Generation=0.852
  Overall Score: 0.819
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.705s, Retrieval=93.930s, Passage Augment=1.517s, Passage Rerank=17.146s, Passage Filter=0.000s, Passage Compress=1.473s, Prompt Maker=0.000s, Generation=1.164s, Post-generation=1.578s
  Total Prediction Time: 117.515s
  Embedding Tokens: 20336.1
  LLM Tokens: 23290.1 in, 2340.6 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.715s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_hypergraph_simply + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_rerank: 19124.9
    - passage_compress: 1151.1
    - retrieval: 60.1
  - LLM Tokens:
    - generation:
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1205.4 in, 90.8 out
      - graph: 0.0 in, 0.0 out
    - query_expansion:
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.8 in, 84.0 out
      - graph: 0.0 in, 0.0 out
    - retrieval:
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
    - passage_rerank:
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 19124.9 in, 1472.7 out
      - graph: 0.0 in, 0.0 out
    - passage_compress:
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2395.2 in, 509.3 out
      - graph: 0.0 in, 0.0 out
    - post_generation:
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 446.7 in, 183.8 out
      - graph: 0.0 in, 0.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.705s
- Retrieval: 93.930s
- Passage Augment: 1.517s
- Passage Rerank: 17.146s
- Passage Filter: 0.000s
- Passage Compress: 1.473s
- Prompt Maker: 0.000s
- Generation: 1.164s
- Post-generation: 1.578s
- Total Prediction Time: 117.515s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 171.54s
  - Total Evaluation: 171.55s

**Pipeline Total:** 11923.16s

---

*Report generated on 2025-08-17 10:35:07*
