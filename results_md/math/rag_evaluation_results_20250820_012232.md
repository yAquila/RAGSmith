# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1403.25s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_simply + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_simply + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_simply + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_simply + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_simply + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@10=0.010, mAP=0.010, nDCG@10=0.010, MRR=0.010
  Generation: LLM=0.004, Semantic=0.007
  Component Scores: Retrieval=0.010, Generation=0.005
  Overall Score: 0.008
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.007s, Retrieval=0.128s, Passage Augment=0.000s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=0.014s, Post-generation=0.038s
  Total Prediction Time: 0.188s
  Embedding Tokens: 36.0
  LLM Tokens: 4230.0 in, 551.0 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.095s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_simply + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 36.0
  - LLM Tokens:
    - query_expansion:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 120.0 in, 89.0 out
    - retrieval:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
    - post_generation:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 819.0 in, 456.0 out
    - generation:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 3291.0 in, 6.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.007s
- Retrieval: 0.128s
- Passage Augment: 0.000s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.014s
- Post-generation: 0.038s
- Total Prediction Time: 0.188s

**Evaluation Times:**
  - Retrieval: 0.00s
  - Generation: 9.46s
  - Total Evaluation: 9.46s

**Pipeline Total:** 1403.25s

---

*Report generated on 2025-08-20 01:22:32*
