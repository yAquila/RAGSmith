# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 4317.86s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.722, mAP=0.595, nDCG@5=0.643, MRR=0.691
  Generation: LLM=0.796, Semantic=0.905
  Component Scores: Retrieval=0.663, Generation=0.850
  Overall Score: 0.756
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=1.450s, Retrieval=25.169s, Passage Augment=0.000s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=11.757s, Prompt Maker=0.000s, Generation=0.774s, Post-generation=2.357s
  Total Prediction Time: 41.507s
  Embedding Tokens: 524.4
  LLM Tokens: 3600.0 in, 1806.4 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.670s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 93.4
    - passage_compress: 410.8
    - query_expansion: 20.2
  - LLM Tokens:
    - retrieval:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
    - passage_compress:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2554.4 in, 1448.5 out
    - generation:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 495.9 in, 76.2 out
    - post_generation:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 549.7 in, 281.7 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 1.450s
- Retrieval: 25.169s
- Passage Augment: 0.000s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 11.757s
- Prompt Maker: 0.000s
- Generation: 0.774s
- Post-generation: 2.357s
- Total Prediction Time: 41.507s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 166.96s
  - Total Evaluation: 166.97s

**Pipeline Total:** 4317.86s

---

*Report generated on 2025-09-04 08:46:34*
