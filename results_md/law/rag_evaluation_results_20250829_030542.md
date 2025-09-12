# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 4144.28s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:decomposition_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:decomposition_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:decomposition_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:decomposition_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:decomposition_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.370, mAP=0.370, nDCG@5=0.418, MRR=0.590
  Generation: LLM=0.656, Semantic=0.885
  Component Scores: Retrieval=0.437, Generation=0.770
  Overall Score: 0.604
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.603s, Retrieval=31.208s, Passage Augment=0.000s, Passage Rerank=7.335s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=0.488s, Post-generation=0.000s
  Total Prediction Time: 39.634s
  Embedding Tokens: 4273.7
  LLM Tokens: 4594.8 in, 914.6 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.808s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:decomposition_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_rerank: 4253.5
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 172.1 in, 67.7 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 169.2 in, 51.7 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 4253.5 in, 795.2 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.603s
- Retrieval: 31.208s
- Passage Augment: 0.000s
- Passage Rerank: 7.335s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.488s
- Post-generation: 0.000s
- Total Prediction Time: 39.634s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 180.80s
  - Total Evaluation: 180.81s

**Pipeline Total:** 4144.28s

---

*Report generated on 2025-08-29 03:05:42*
