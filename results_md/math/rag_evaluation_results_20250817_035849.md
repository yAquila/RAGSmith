# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 11830.04s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_hypergraph_simply + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_hypergraph_simply + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_hypergraph_simply + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_hypergraph_simply + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_hypergraph_simply + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.795, mAP=0.711, nDCG@5=0.777, MRR=0.872
  Generation: LLM=0.820, Semantic=0.901
  Component Scores: Retrieval=0.789, Generation=0.860
  Overall Score: 0.825
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.708s, Retrieval=92.726s, Passage Augment=1.497s, Passage Rerank=17.534s, Passage Filter=0.000s, Passage Compress=1.459s, Prompt Maker=0.000s, Generation=1.162s, Post-generation=1.481s
  Total Prediction Time: 116.568s
  Embedding Tokens: 20195.5
  LLM Tokens: 23122.2 in, 2313.7 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.731s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_hypergraph_simply + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_rerank: 18996.9
    - passage_compress: 1138.5
    - retrieval: 60.1
  - LLM Tokens:
    - generation:
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1211.7 in, 90.2 out
      - graph: 0.0 in, 0.0 out
    - query_expansion:
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.8 in, 84.4 out
      - graph: 0.0 in, 0.0 out
    - retrieval:
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
    - passage_rerank:
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 18996.9 in, 1485.5 out
      - graph: 0.0 in, 0.0 out
    - passage_compress:
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2366.9 in, 481.8 out
      - graph: 0.0 in, 0.0 out
    - post_generation:
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 428.9 in, 171.7 out
      - graph: 0.0 in, 0.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.708s
- Retrieval: 92.726s
- Passage Augment: 1.497s
- Passage Rerank: 17.534s
- Passage Filter: 0.000s
- Passage Compress: 1.459s
- Prompt Maker: 0.000s
- Generation: 1.162s
- Post-generation: 1.481s
- Total Prediction Time: 116.568s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 173.12s
  - Total Evaluation: 173.13s

**Pipeline Total:** 11830.04s

---

*Report generated on 2025-08-17 03:58:49*
