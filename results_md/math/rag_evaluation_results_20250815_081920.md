# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 2950.86s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_keyword_hypergraph_simply + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_keyword_hypergraph_simply + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_keyword_hypergraph_simply + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_keyword_hypergraph_simply + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_keyword_hypergraph_simply + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.631, mAP=0.436, nDCG@5=0.515, MRR=0.535
  Generation: LLM=0.774, Semantic=0.879
  Component Scores: Retrieval=0.529, Generation=0.826
  Overall Score: 0.678
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.523s, Retrieval=2.384s, Passage Augment=0.000s, Passage Rerank=16.249s, Passage Filter=0.000s, Passage Compress=6.276s, Prompt Maker=0.000s, Generation=0.752s, Post-generation=1.410s
  Total Prediction Time: 27.594s
  Embedding Tokens: 428.1
  LLM Tokens: 26733.8 in, 2683.5 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.903s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_keyword_hypergraph_simply + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_compress: 300.8
    - query_expansion: 20.0
    - retrieval: 107.2
  - LLM Tokens:
    - generation:
      - keyword: 0.0 in, 0.0 out
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 402.2 in, 77.6 out
    - retrieval:
      - keyword: 0.0 in, 0.0 out
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
    - passage_rerank:
      - keyword: 0.0 in, 0.0 out
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 24419.8 in, 1691.5 out
    - passage_compress:
      - keyword: 0.0 in, 0.0 out
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1505.3 in, 750.7 out
    - post_generation:
      - keyword: 0.0 in, 0.0 out
      - hypergraph: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 406.6 in, 163.8 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.523s
- Retrieval: 2.384s
- Passage Augment: 0.000s
- Passage Rerank: 16.249s
- Passage Filter: 0.000s
- Passage Compress: 6.276s
- Prompt Maker: 0.000s
- Generation: 0.752s
- Post-generation: 1.410s
- Total Prediction Time: 27.594s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 190.29s
  - Total Evaluation: 190.30s

**Pipeline Total:** 2950.86s

---

*Report generated on 2025-08-15 08:19:20*
