# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1092.89s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:decomposition_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:decomposition_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:decomposition_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:decomposition_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:decomposition_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.857, mAP=0.806, nDCG@5=0.853, MRR=0.937
  Generation: LLM=0.851, Semantic=0.902
  Component Scores: Retrieval=0.863, Generation=0.876
  Overall Score: 0.870
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.590s, Retrieval=0.149s, Passage Augment=0.000s, Passage Rerank=0.488s, Passage Filter=0.000s, Passage Compress=4.959s, Prompt Maker=0.000s, Generation=0.672s, Post-generation=2.360s
  Total Prediction Time: 9.219s
  Embedding Tokens: 10920.8
  LLM Tokens: 2213.3 in, 1022.0 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.709s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:decomposition_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_compress: 294.4
    - passage_rerank: 10606.2
  - LLM Tokens:
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1094.0 in, 606.2 out
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 172.1 in, 66.2 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 369.3 in, 68.9 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 577.9 in, 280.8 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.590s
- Retrieval: 0.149s
- Passage Augment: 0.000s
- Passage Rerank: 0.488s
- Passage Filter: 0.000s
- Passage Compress: 4.959s
- Prompt Maker: 0.000s
- Generation: 0.672s
- Post-generation: 2.360s
- Total Prediction Time: 9.219s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 170.94s
  - Total Evaluation: 170.95s

**Pipeline Total:** 1092.89s

---

*Report generated on 2025-08-28 22:33:31*
