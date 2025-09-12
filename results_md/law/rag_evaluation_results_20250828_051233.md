# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 5532.55s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.722, mAP=0.593, nDCG@5=0.643, MRR=0.691
  Generation: LLM=0.820, Semantic=0.903
  Component Scores: Retrieval=0.662, Generation=0.861
  Overall Score: 0.762
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=1.446s, Retrieval=37.178s, Passage Augment=0.000s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=11.978s, Prompt Maker=0.000s, Generation=0.779s, Post-generation=2.315s
  Total Prediction Time: 53.695s
  Embedding Tokens: 545.0
  LLM Tokens: 3639.2 in, 1829.3 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.629s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 94.0
    - passage_compress: 430.8
    - query_expansion: 20.2
  - LLM Tokens:
    - retrieval:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
    - passage_compress:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2572.8 in, 1477.5 out
    - generation:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 513.9 in, 76.1 out
    - post_generation:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 552.4 in, 275.7 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 1.446s
- Retrieval: 37.178s
- Passage Augment: 0.000s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 11.978s
- Prompt Maker: 0.000s
- Generation: 0.779s
- Post-generation: 2.315s
- Total Prediction Time: 53.695s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 162.88s
  - Total Evaluation: 162.89s

**Pipeline Total:** 5532.55s

---

*Report generated on 2025-08-28 05:12:33*
