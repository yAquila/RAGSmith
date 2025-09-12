# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 546.58s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.878, mAP=0.778, nDCG@5=0.835, MRR=0.891
  Generation: LLM=0.832, Semantic=0.894
  Component Scores: Retrieval=0.845, Generation=0.863
  Overall Score: 0.854
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.287s, Retrieval=0.050s, Passage Augment=0.000s, Passage Rerank=0.057s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=0.995s, Post-generation=2.387s
  Total Prediction Time: 3.777s
  Embedding Tokens: 1251.4
  LLM Tokens: 1517.9 in, 401.1 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.688s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 20.5
    - passage_rerank: 1231.0
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 144.1 in, 25.6 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 823.9 in, 90.1 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 549.9 in, 285.3 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.287s
- Retrieval: 0.050s
- Passage Augment: 0.000s
- Passage Rerank: 0.057s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.995s
- Post-generation: 2.387s
- Total Prediction Time: 3.777s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 168.81s
  - Total Evaluation: 168.82s

**Pipeline Total:** 546.58s

---

*Report generated on 2025-08-28 18:46:18*
