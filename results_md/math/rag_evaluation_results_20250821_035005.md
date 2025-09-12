# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1939.97s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.624, mAP=0.531, nDCG@5=0.586, MRR=0.645
  Generation: LLM=0.757, Semantic=0.892
  Component Scores: Retrieval=0.596, Generation=0.824
  Overall Score: 0.710
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.708s, Retrieval=0.042s, Passage Augment=0.000s, Passage Rerank=8.823s, Passage Filter=0.000s, Passage Compress=5.417s, Prompt Maker=0.000s, Generation=1.006s, Post-generation=1.679s
  Total Prediction Time: 17.675s
  LLM Tokens: 18843.0 in, 2723.1 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.723s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - LLM Tokens:
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 15642.0 in, 1729.5 out
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.8 in, 83.8 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 967.3 in, 84.1 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 460.1 in, 195.0 out
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1655.7 in, 630.7 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.708s
- Retrieval: 0.042s
- Passage Augment: 0.000s
- Passage Rerank: 8.823s
- Passage Filter: 0.000s
- Passage Compress: 5.417s
- Prompt Maker: 0.000s
- Generation: 1.006s
- Post-generation: 1.679s
- Total Prediction Time: 17.675s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 172.35s
  - Total Evaluation: 172.36s

**Pipeline Total:** 1939.97s

---

*Report generated on 2025-08-21 03:50:05*
