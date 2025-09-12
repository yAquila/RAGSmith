# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 13118.26s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:hybrid_vector_graph_simply + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:hybrid_vector_graph_simply + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:hybrid_vector_graph_simply + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:hybrid_vector_graph_simply + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:hybrid_vector_graph_simply + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.859, mAP=0.778, nDCG@5=0.811, MRR=0.856
  Generation: LLM=0.828, Semantic=0.896
  Component Scores: Retrieval=0.826, Generation=0.862
  Overall Score: 0.844
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.704s, Retrieval=122.096s, Passage Augment=0.006s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=4.734s, Post-generation=1.751s
  Total Prediction Time: 129.290s
  Embedding Tokens: 40.1
  LLM Tokens: 4713.6 in, 647.9 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.891s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:hybrid_vector_graph_simply + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 40.1
  - LLM Tokens:
    - query_expansion:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.8 in, 83.7 out
      - graph: 0.0 in, 0.0 out
    - retrieval:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
    - generation:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 3861.4 in, 372.9 out
      - graph: 0.0 in, 0.0 out
    - post_generation:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 734.3 in, 191.3 out
      - graph: 0.0 in, 0.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.704s
- Retrieval: 122.096s
- Passage Augment: 0.006s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 4.734s
- Post-generation: 1.751s
- Total Prediction Time: 129.290s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 189.07s
  - Total Evaluation: 189.08s

**Pipeline Total:** 13118.26s

---

*Report generated on 2025-08-15 11:57:58*
