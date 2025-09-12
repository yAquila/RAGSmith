# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 950.40s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_cc_dbsf + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_cc_dbsf + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_cc_dbsf + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_cc_dbsf + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_cc_dbsf + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.000, mAP=0.000, nDCG@5=0.000, MRR=0.000
  Generation: LLM=0.635, Semantic=0.883
  Component Scores: Retrieval=0.000, Generation=0.759
  Overall Score: 0.379
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.686s, Retrieval=0.166s, Passage Augment=0.000s, Passage Rerank=0.715s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=0.582s, Post-generation=5.562s
  Total Prediction Time: 7.712s
  Embedding Tokens: 10150.8
  LLM Tokens: 724.7 in, 818.7 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.791s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_cc_dbsf + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_rerank: 10130.6
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.1 in, 81.3 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 61.0 in, 70.6 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 546.5 in, 666.8 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.686s
- Retrieval: 0.166s
- Passage Augment: 0.000s
- Passage Rerank: 0.715s
- Passage Filter: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.582s
- Post-generation: 5.562s
- Total Prediction Time: 7.712s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 179.10s
  - Total Evaluation: 179.11s

**Pipeline Total:** 950.40s

---

*Report generated on 2025-08-29 13:28:22*
