# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1358.03s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_cc_dbsf + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_cc_dbsf + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_cc_dbsf + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_cc_dbsf + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_cc_dbsf + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.806, mAP=0.762, nDCG@5=0.807, MRR=0.893
  Generation: LLM=0.833, Semantic=0.909
  Component Scores: Retrieval=0.817, Generation=0.871
  Overall Score: 0.844
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.678s, Retrieval=0.037s, Passage Augment=1.725s, Passage Rerank=0.653s, Passage Filter=0.000s, Passage Compress=2.503s, Prompt Maker=0.000s, Generation=0.980s, Post-generation=5.377s
  Total Prediction Time: 11.953s
  Embedding Tokens: 16231.6
  LLM Tokens: 3786.8 in, 1338.4 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.626s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_cc_dbsf + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_compress: 948.1
    - passage_rerank: 15283.5
  - LLM Tokens:
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2141.7 in, 536.8 out
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.1 in, 80.4 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 977.1 in, 80.0 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 550.9 in, 641.1 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.678s
- Retrieval: 0.037s
- Passage Augment: 1.725s
- Passage Rerank: 0.653s
- Passage Filter: 0.000s
- Passage Compress: 2.503s
- Prompt Maker: 0.000s
- Generation: 0.980s
- Post-generation: 5.377s
- Total Prediction Time: 11.953s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 162.60s
  - Total Evaluation: 162.61s

**Pipeline Total:** 1358.03s

---

*Report generated on 2025-09-04 22:00:30*
