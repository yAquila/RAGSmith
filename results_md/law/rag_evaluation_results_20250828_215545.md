# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 368.27s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:decomposition_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:decomposition_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:decomposition_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:decomposition_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:decomposition_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.888, mAP=0.740, nDCG@5=0.803, MRR=0.822
  Generation: LLM=0.870, Semantic=0.917
  Component Scores: Retrieval=0.814, Generation=0.894
  Overall Score: 0.854
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.603s, Retrieval=0.154s, Passage Augment=0.000s, Passage Rerank=0.495s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=0.951s, Post-generation=0.000s
  Total Prediction Time: 2.203s
  Embedding Tokens: 10671.9
  LLM Tokens: 1037.6 in, 149.4 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.479s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:decomposition_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_rerank: 10651.7
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 172.1 in, 67.4 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 865.5 in, 82.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.603s
- Retrieval: 0.154s
- Passage Augment: 0.000s
- Passage Rerank: 0.495s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.951s
- Post-generation: 0.000s
- Total Prediction Time: 2.203s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 147.89s
  - Total Evaluation: 147.90s

**Pipeline Total:** 368.27s

---

*Report generated on 2025-08-28 21:55:45*
