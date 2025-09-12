# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 3022.50s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.736, mAP=0.710, nDCG@5=0.763, MRR=0.903
  Generation: LLM=0.760, Semantic=0.904
  Component Scores: Retrieval=0.778, Generation=0.832
  Overall Score: 0.805
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=24.092s, Passage Augment=0.000s, Passage Rerank=0.161s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=0.934s, Post-generation=3.299s
  Total Prediction Time: 28.487s
  Embedding Tokens: 2942.4
  LLM Tokens: 1660.3 in, 470.1 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.737s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 40.5
    - passage_rerank: 2901.9
  - LLM Tokens:
    - generation:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 899.0 in, 77.2 out
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
    - post_generation:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 761.3 in, 392.9 out
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
- Retrieval: 24.092s
- Passage Augment: 0.000s
- Passage Rerank: 0.161s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.934s
- Post-generation: 3.299s
- Total Prediction Time: 28.487s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 173.70s
  - Total Evaluation: 173.71s

**Pipeline Total:** 3022.50s

---

*Report generated on 2025-09-09 17:15:03*
