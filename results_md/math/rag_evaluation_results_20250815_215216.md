# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 11448.98s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:hybrid_vector_graph_simply + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:hybrid_vector_graph_simply + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:hybrid_vector_graph_simply + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:hybrid_vector_graph_simply + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:hybrid_vector_graph_simply + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.858, mAP=0.772, nDCG@5=0.805, MRR=0.844
  Generation: LLM=0.805, Semantic=0.893
  Component Scores: Retrieval=0.820, Generation=0.849
  Overall Score: 0.835
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.707s, Retrieval=101.522s, Passage Augment=0.006s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=8.232s, Post-generation=1.807s
  Total Prediction Time: 112.274s
  Embedding Tokens: 40.1
  LLM Tokens: 4784.6 in, 1070.7 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=2.214s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:hybrid_vector_graph_simply + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 40.1
  - LLM Tokens:
    - query_expansion:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.8 in, 84.0 out
      - graph: 0.0 in, 0.0 out
    - retrieval:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
    - generation:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 3852.9 in, 793.2 out
      - graph: 0.0 in, 0.0 out
    - post_generation:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 813.8 in, 193.5 out
      - graph: 0.0 in, 0.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.707s
- Retrieval: 101.522s
- Passage Augment: 0.006s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 8.232s
- Post-generation: 1.807s
- Total Prediction Time: 112.274s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 221.40s
  - Total Evaluation: 221.41s

**Pipeline Total:** 11448.98s

---

*Report generated on 2025-08-15 21:52:16*
