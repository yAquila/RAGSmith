# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1371.46s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.563, mAP=0.457, nDCG@5=0.523, MRR=0.613
  Generation: LLM=0.753, Semantic=0.885
  Component Scores: Retrieval=0.539, Generation=0.819
  Overall Score: 0.679
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=4.077s, Retrieval=0.195s, Passage Augment=0.000s, Passage Rerank=2.675s, Passage Filter=0.000s, Passage Compress=4.303s, Prompt Maker=0.000s, Generation=0.711s, Post-generation=0.000s
  Total Prediction Time: 11.962s
  Embedding Tokens: 269.9
  LLM Tokens: 9734.4 in, 2913.6 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.752s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - passage_compress: 269.9
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 369.5 in, 73.3 out
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 120.7 in, 530.9 out
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1172.2 in, 620.2 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 8072.0 in, 1689.1 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 4.077s
- Retrieval: 0.195s
- Passage Augment: 0.000s
- Passage Rerank: 2.675s
- Passage Filter: 0.000s
- Passage Compress: 4.303s
- Prompt Maker: 0.000s
- Generation: 0.711s
- Post-generation: 0.000s
- Total Prediction Time: 11.962s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 175.15s
  - Total Evaluation: 175.17s

**Pipeline Total:** 1371.46s

---

*Report generated on 2025-08-19 18:51:33*
