# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 11855.13s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_hypergraph_simply + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_hypergraph_simply + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_hypergraph_simply + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_hypergraph_simply + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_hypergraph_simply + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.777, mAP=0.692, nDCG@5=0.762, MRR=0.873
  Generation: LLM=0.823, Semantic=0.905
  Component Scores: Retrieval=0.776, Generation=0.864
  Overall Score: 0.820
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.712s, Retrieval=93.368s, Passage Augment=1.475s, Passage Rerank=17.184s, Passage Filter=0.000s, Passage Compress=1.400s, Prompt Maker=0.000s, Generation=1.183s, Post-generation=1.515s
  Total Prediction Time: 116.836s
  Embedding Tokens: 20343.4
  LLM Tokens: 23360.4 in, 2337.9 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.714s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_hypergraph_simply + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_rerank: 19131.2
    - passage_compress: 1152.2
    - retrieval: 60.1
  - LLM Tokens:
    - generation:
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1205.6 in, 92.8 out
      - graph: 0.0 in, 0.0 out
    - query_expansion:
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.8 in, 84.9 out
      - graph: 0.0 in, 0.0 out
    - retrieval:
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
    - passage_rerank:
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 19131.2 in, 1480.3 out
      - graph: 0.0 in, 0.0 out
    - passage_compress:
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2465.2 in, 504.2 out
      - graph: 0.0 in, 0.0 out
    - post_generation:
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 440.6 in, 175.7 out
      - graph: 0.0 in, 0.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.712s
- Retrieval: 93.368s
- Passage Augment: 1.475s
- Passage Rerank: 17.184s
- Passage Filter: 0.000s
- Passage Compress: 1.400s
- Prompt Maker: 0.000s
- Generation: 1.183s
- Post-generation: 1.515s
- Total Prediction Time: 116.836s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 171.37s
  - Total Evaluation: 171.38s

**Pipeline Total:** 11855.13s

---

*Report generated on 2025-08-17 07:16:24*
