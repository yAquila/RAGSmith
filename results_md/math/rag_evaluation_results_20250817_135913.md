# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 12245.73s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_hypergraph_simply + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_hypergraph_simply + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_hypergraph_simply + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_hypergraph_simply + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_hypergraph_simply + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.787, mAP=0.704, nDCG@5=0.769, MRR=0.866
  Generation: LLM=0.811, Semantic=0.898
  Component Scores: Retrieval=0.782, Generation=0.855
  Overall Score: 0.818
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.707s, Retrieval=93.543s, Passage Augment=1.459s, Passage Rerank=20.782s, Passage Filter=0.000s, Passage Compress=1.327s, Prompt Maker=0.000s, Generation=1.170s, Post-generation=1.709s
  Total Prediction Time: 120.698s
  Embedding Tokens: 20411.2
  LLM Tokens: 23334.5 in, 2327.6 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.757s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_hypergraph_simply + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_rerank: 19164.7
    - passage_compress: 1186.4
    - retrieval: 60.1
  - LLM Tokens:
    - generation:
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1215.1 in, 91.2 out
      - graph: 0.0 in, 0.0 out
    - query_expansion:
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.8 in, 84.2 out
      - graph: 0.0 in, 0.0 out
    - retrieval:
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
    - passage_rerank:
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 19164.7 in, 1457.4 out
      - graph: 0.0 in, 0.0 out
    - passage_compress:
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2359.4 in, 495.4 out
      - graph: 0.0 in, 0.0 out
    - post_generation:
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 477.6 in, 199.3 out
      - graph: 0.0 in, 0.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.707s
- Retrieval: 93.543s
- Passage Augment: 1.459s
- Passage Rerank: 20.782s
- Passage Filter: 0.000s
- Passage Compress: 1.327s
- Prompt Maker: 0.000s
- Generation: 1.170s
- Post-generation: 1.709s
- Total Prediction Time: 120.698s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 175.74s
  - Total Evaluation: 175.75s

**Pipeline Total:** 12245.73s

---

*Report generated on 2025-08-17 13:59:13*
