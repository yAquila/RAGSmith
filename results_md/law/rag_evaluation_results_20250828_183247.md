# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 3397.87s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.849, mAP=0.749, nDCG@5=0.809, MRR=0.883
  Generation: LLM=0.847, Semantic=0.912
  Component Scores: Retrieval=0.823, Generation=0.880
  Overall Score: 0.851
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=29.187s, Passage Augment=0.000s, Passage Rerank=0.098s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=0.872s, Post-generation=2.256s
  Total Prediction Time: 32.413s
  Embedding Tokens: 1646.4
  LLM Tokens: 1312.4 in, 342.8 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.565s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 40.4
    - passage_rerank: 1606.0
  - LLM Tokens:
    - retrieval:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
    - generation:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 752.5 in, 76.6 out
    - post_generation:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 560.0 in, 266.2 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 29.187s
- Passage Augment: 0.000s
- Passage Rerank: 0.098s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.872s
- Post-generation: 2.256s
- Total Prediction Time: 32.413s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 156.54s
  - Total Evaluation: 156.55s

**Pipeline Total:** 3397.87s

---

*Report generated on 2025-08-28 18:32:47*
