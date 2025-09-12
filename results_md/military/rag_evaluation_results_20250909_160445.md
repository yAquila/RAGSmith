# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1695.20s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.881, mAP=0.818, nDCG@5=0.851, MRR=0.919
  Generation: LLM=0.830, Semantic=0.906
  Component Scores: Retrieval=0.867, Generation=0.868
  Overall Score: 0.867
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.052s, Passage Augment=0.000s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=10.949s, Prompt Maker=0.000s, Generation=1.423s, Post-generation=2.824s
  Total Prediction Time: 15.248s
  Embedding Tokens: 20.2
  LLM Tokens: 5185.7 in, 1740.3 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.703s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 20.2
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1693.7 in, 99.3 out
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2808.8 in, 1306.8 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 683.2 in, 334.1 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.052s
- Passage Augment: 0.000s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 10.949s
- Prompt Maker: 0.000s
- Generation: 1.423s
- Post-generation: 2.824s
- Total Prediction Time: 15.248s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 170.30s
  - Total Evaluation: 170.31s

**Pipeline Total:** 1695.20s

---

*Report generated on 2025-09-09 16:04:45*
