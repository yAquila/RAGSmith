# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 3486.69s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.782, mAP=0.733, nDCG@5=0.789, MRR=0.900
  Generation: LLM=0.797, Semantic=0.909
  Component Scores: Retrieval=0.801, Generation=0.853
  Overall Score: 0.827
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=25.470s, Passage Augment=0.000s, Passage Rerank=0.161s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=0.982s, Post-generation=6.530s
  Total Prediction Time: 33.143s
  Embedding Tokens: 2942.4
  LLM Tokens: 1686.4 in, 861.0 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.723s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 40.5
    - passage_rerank: 2901.9
  - LLM Tokens:
    - generation:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 916.1 in, 82.6 out
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
    - post_generation:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 770.3 in, 778.4 out
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
    - retrieval:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 25.470s
- Passage Augment: 0.000s
- Passage Rerank: 0.161s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.982s
- Post-generation: 6.530s
- Total Prediction Time: 33.143s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 172.25s
  - Total Evaluation: 172.26s

**Pipeline Total:** 3486.69s

---

*Report generated on 2025-09-09 10:18:01*
