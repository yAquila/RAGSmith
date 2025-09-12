# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 547.95s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.873, mAP=0.813, nDCG@5=0.860, MRR=0.934
  Generation: LLM=0.886, Semantic=0.921
  Component Scores: Retrieval=0.870, Generation=0.903
  Overall Score: 0.887
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.049s, Passage Augment=0.003s, Passage Rerank=0.056s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.284s, Post-generation=2.553s
  Total Prediction Time: 3.945s
  Embedding Tokens: 1239.5
  LLM Tokens: 2180.4 in, 393.8 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.534s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_rerank: 1219.3
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1585.4 in, 88.5 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 595.0 in, 305.3 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.049s
- Passage Augment: 0.003s
- Passage Rerank: 0.056s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.284s
- Post-generation: 2.553s
- Total Prediction Time: 3.945s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 153.38s
  - Total Evaluation: 153.39s

**Pipeline Total:** 547.95s

---

*Report generated on 2025-09-05 08:31:45*
