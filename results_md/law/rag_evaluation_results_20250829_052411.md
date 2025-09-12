# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1171.83s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.000, mAP=0.000, nDCG@5=0.000, MRR=0.000
  Generation: LLM=0.543, Semantic=0.867
  Component Scores: Retrieval=0.000, Generation=0.705
  Overall Score: 0.353
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.675s, Retrieval=0.169s, Passage Augment=0.000s, Passage Rerank=0.706s, Passage Filter=0.000s, Passage Compress=7.717s, Prompt Maker=0.000s, Generation=0.758s, Post-generation=0.000s
  Total Prediction Time: 10.025s
  Embedding Tokens: 10533.3
  LLM Tokens: 2309.2 in, 1084.7 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.691s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_compress: 348.4
    - passage_rerank: 10164.7
  - LLM Tokens:
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1703.3 in, 930.5 out
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.1 in, 79.6 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 488.8 in, 74.6 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.675s
- Retrieval: 0.169s
- Passage Augment: 0.000s
- Passage Rerank: 0.706s
- Passage Filter: 0.000s
- Passage Compress: 7.717s
- Prompt Maker: 0.000s
- Generation: 0.758s
- Post-generation: 0.000s
- Total Prediction Time: 10.025s

**Evaluation Times:**
  - Retrieval: 0.02s
  - Generation: 169.15s
  - Total Evaluation: 169.17s

**Pipeline Total:** 1171.83s

---

*Report generated on 2025-08-29 05:24:11*
