# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1470.76s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_keyword_cc + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_keyword_cc + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_keyword_cc + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_keyword_cc + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_keyword_cc + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.882, mAP=0.776, nDCG@5=0.838, MRR=0.893
  Generation: LLM=0.824, Semantic=0.891
  Component Scores: Retrieval=0.847, Generation=0.857
  Overall Score: 0.852
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.712s, Retrieval=0.200s, Passage Augment=1.920s, Passage Rerank=1.178s, Passage Filter=0.000s, Passage Compress=6.345s, Prompt Maker=0.000s, Generation=1.002s, Post-generation=1.681s
  Total Prediction Time: 13.038s
  Embedding Tokens: 19294.0
  LLM Tokens: 3522.4 in, 1073.6 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.668s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_keyword_cc + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_rerank: 19274.0
    - retrieval: 20.0
  - LLM Tokens:
    - query_expansion:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.8 in, 84.2 out
      - keyword: 0.0 in, 0.0 out
    - generation:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 768.0 in, 92.5 out
      - keyword: 0.0 in, 0.0 out
    - retrieval:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
      - keyword: 0.0 in, 0.0 out
    - post_generation:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 465.6 in, 195.0 out
      - keyword: 0.0 in, 0.0 out
    - passage_compress:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2170.9 in, 701.9 out
      - keyword: 0.0 in, 0.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.712s
- Retrieval: 0.200s
- Passage Augment: 1.920s
- Passage Rerank: 1.178s
- Passage Filter: 0.000s
- Passage Compress: 6.345s
- Prompt Maker: 0.000s
- Generation: 1.002s
- Post-generation: 1.681s
- Total Prediction Time: 13.038s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 166.76s
  - Total Evaluation: 166.77s

**Pipeline Total:** 1470.76s

---

*Report generated on 2025-08-21 01:22:57*
