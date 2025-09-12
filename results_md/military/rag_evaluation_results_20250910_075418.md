# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 5354.31s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_cc_dbsf + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_cc_dbsf + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_cc_dbsf + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_cc_dbsf + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_cc_dbsf + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.732, mAP=0.608, nDCG@5=0.672, MRR=0.715
  Generation: LLM=0.738, Semantic=0.898
  Component Scores: Retrieval=0.682, Generation=0.818
  Overall Score: 0.750
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.729s, Retrieval=31.534s, Passage Augment=0.000s, Passage Rerank=10.988s, Passage Filter=0.000s, Passage Compress=7.603s, Prompt Maker=0.000s, Generation=0.837s, Post-generation=0.000s
  Total Prediction Time: 51.691s
  Embedding Tokens: 416.6
  LLM Tokens: 24549.5 in, 2047.6 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.851s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_cc_dbsf + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - passage_compress: 376.1
    - retrieval: 40.5
  - LLM Tokens:
    - passage_rerank:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 22481.1 in, 954.6 out
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
    - generation:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 501.2 in, 83.8 out
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
    - passage_compress:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1448.8 in, 922.7 out
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
    - retrieval:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
    - query_expansion:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 118.4 in, 86.5 out
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.729s
- Retrieval: 31.534s
- Passage Augment: 0.000s
- Passage Rerank: 10.988s
- Passage Filter: 0.000s
- Passage Compress: 7.603s
- Prompt Maker: 0.000s
- Generation: 0.837s
- Post-generation: 0.000s
- Total Prediction Time: 51.691s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 185.07s
  - Total Evaluation: 185.08s

**Pipeline Total:** 5354.31s

---

*Report generated on 2025-09-10 07:54:18*
