# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1473.57s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.687, mAP=0.591, nDCG@5=0.649, MRR=0.708
  Generation: LLM=0.827, Semantic=0.918
  Component Scores: Retrieval=0.659, Generation=0.873
  Overall Score: 0.766
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.685s, Retrieval=0.037s, Passage Augment=2.985s, Passage Rerank=7.943s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.470s, Post-generation=0.000s
  Total Prediction Time: 13.119s
  LLM Tokens: 17469.9 in, 1136.4 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.616s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.1 in, 80.7 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2022.5 in, 87.7 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 15330.3 in, 968.1 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.685s
- Retrieval: 0.037s
- Passage Augment: 2.985s
- Passage Rerank: 7.943s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.470s
- Post-generation: 0.000s
- Total Prediction Time: 13.119s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 161.59s
  - Total Evaluation: 161.60s

**Pipeline Total:** 1473.57s

---

*Report generated on 2025-08-29 12:20:43*
