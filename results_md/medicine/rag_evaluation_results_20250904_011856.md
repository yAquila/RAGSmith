# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 2541.31s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.722, mAP=0.654, nDCG@5=0.719, MRR=0.858
  Generation: LLM=0.824, Semantic=0.910
  Component Scores: Retrieval=0.738, Generation=0.867
  Overall Score: 0.803
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=21.338s, Passage Augment=0.000s, Passage Rerank=1.742s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=0.771s, Post-generation=0.000s
  Total Prediction Time: 23.851s
  Embedding Tokens: 40.4
  LLM Tokens: 3564.7 in, 873.6 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.561s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 40.4
  - LLM Tokens:
    - retrieval:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
      - keyword: 0.0 in, 0.0 out
    - generation:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 638.0 in, 69.0 out
      - keyword: 0.0 in, 0.0 out
    - passage_rerank:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2926.7 in, 804.6 out
      - keyword: 0.0 in, 0.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 21.338s
- Passage Augment: 0.000s
- Passage Rerank: 1.742s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.771s
- Post-generation: 0.000s
- Total Prediction Time: 23.851s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 156.10s
  - Total Evaluation: 156.11s

**Pipeline Total:** 2541.31s

---

*Report generated on 2025-09-04 01:18:56*
