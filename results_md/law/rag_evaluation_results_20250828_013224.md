# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1165.54s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.875, mAP=0.782, nDCG@5=0.825, MRR=0.877
  Generation: LLM=0.854, Semantic=0.914
  Component Scores: Retrieval=0.840, Generation=0.884
  Overall Score: 0.862
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.050s, Passage Augment=0.000s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=8.940s, Prompt Maker=0.000s, Generation=1.090s, Post-generation=0.000s
  Total Prediction Time: 10.081s
  Embedding Tokens: 20.2
  LLM Tokens: 3803.1 in, 1143.0 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.574s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 20.2
  - LLM Tokens:
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2656.8 in, 1056.7 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1146.3 in, 86.4 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.050s
- Passage Augment: 0.000s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 8.940s
- Prompt Maker: 0.000s
- Generation: 1.090s
- Post-generation: 0.000s
- Total Prediction Time: 10.081s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 157.37s
  - Total Evaluation: 157.38s

**Pipeline Total:** 1165.54s

---

*Report generated on 2025-08-28 01:32:24*
