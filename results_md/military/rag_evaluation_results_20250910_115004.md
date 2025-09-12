# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 2552.59s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:hyde_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:hyde_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:hyde_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:hyde_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:hyde_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.863, mAP=0.749, nDCG@5=0.795, MRR=0.849
  Generation: LLM=0.817, Semantic=0.901
  Component Scores: Retrieval=0.814, Generation=0.859
  Overall Score: 0.836
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=3.943s, Retrieval=0.078s, Passage Augment=0.000s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=11.798s, Prompt Maker=0.000s, Generation=1.377s, Post-generation=6.538s
  Total Prediction Time: 23.734s
  Embedding Tokens: 138.9
  LLM Tokens: 5415.4 in, 2804.3 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.790s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:hyde_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 138.9
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1499.5 in, 104.3 out
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 3039.6 in, 1406.6 out
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 121.2 in, 513.6 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 755.0 in, 779.8 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 3.943s
- Retrieval: 0.078s
- Passage Augment: 0.000s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 11.798s
- Prompt Maker: 0.000s
- Generation: 1.377s
- Post-generation: 6.538s
- Total Prediction Time: 23.734s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 179.04s
  - Total Evaluation: 179.05s

**Pipeline Total:** 2552.59s

---

*Report generated on 2025-09-10 11:50:04*
