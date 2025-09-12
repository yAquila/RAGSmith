# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 3505.40s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.868, mAP=0.800, nDCG@5=0.834, MRR=0.906
  Generation: LLM=0.790, Semantic=0.899
  Component Scores: Retrieval=0.852, Generation=0.844
  Overall Score: 0.848
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.731s, Retrieval=0.152s, Passage Augment=0.000s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=24.880s, Prompt Maker=0.000s, Generation=1.175s, Post-generation=6.277s
  Total Prediction Time: 33.215s
  Embedding Tokens: 799.0
  LLM Tokens: 6104.9 in, 3949.4 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.837s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_compress: 778.7
    - retrieval: 20.2
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 992.3 in, 104.5 out
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 4262.9 in, 3009.9 out
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 118.4 in, 87.1 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 731.3 in, 748.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.731s
- Retrieval: 0.152s
- Passage Augment: 0.000s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 24.880s
- Prompt Maker: 0.000s
- Generation: 1.175s
- Post-generation: 6.277s
- Total Prediction Time: 33.215s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 183.75s
  - Total Evaluation: 183.76s

**Pipeline Total:** 3505.40s

---

*Report generated on 2025-09-10 12:48:30*
