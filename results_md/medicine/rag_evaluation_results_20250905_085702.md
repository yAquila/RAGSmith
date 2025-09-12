# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 592.66s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.905, mAP=0.780, nDCG@5=0.841, MRR=0.880
  Generation: LLM=0.862, Semantic=0.922
  Component Scores: Retrieval=0.852, Generation=0.892
  Overall Score: 0.872
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.051s, Passage Augment=0.003s, Passage Rerank=0.708s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.290s, Post-generation=2.333s
  Total Prediction Time: 4.384s
  Embedding Tokens: 1259.7
  LLM Tokens: 3429.0 in, 1236.2 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.542s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_rerank: 1239.5
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1617.3 in, 88.7 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1239.5 in, 870.0 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 572.2 in, 277.4 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.051s
- Passage Augment: 0.003s
- Passage Rerank: 0.708s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.290s
- Post-generation: 2.333s
- Total Prediction Time: 4.384s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 154.17s
  - Total Evaluation: 154.18s

**Pipeline Total:** 592.66s

---

*Report generated on 2025-09-05 08:57:02*
