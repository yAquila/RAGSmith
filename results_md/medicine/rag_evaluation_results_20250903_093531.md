# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 2078.03s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_parent_document_retriever + query_expansion:rag_fusion + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:rag_fusion + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:rag_fusion + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:rag_fusion + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:rag_fusion + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.000, mAP=0.000, nDCG@5=0.000, MRR=0.000
  Generation: LLM=0.538, Semantic=0.869
  Component Scores: Retrieval=0.000, Generation=0.704
  Overall Score: 0.352
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.676s, Retrieval=0.344s, Passage Augment=0.000s, Passage Rerank=4.317s, Passage Filter=0.000s, Passage Compress=7.303s, Prompt Maker=0.000s, Generation=0.793s, Post-generation=5.599s
  Total Prediction Time: 19.032s
  Embedding Tokens: 366.6
  LLM Tokens: 23524.7 in, 3382.5 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.746s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:rag_fusion + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_compress: 346.5
  - LLM Tokens:
    - passage_compress:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1569.0 in, 881.9 out
      - keyword: 0.0 in, 0.0 out
    - query_expansion:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.1 in, 80.1 out
      - keyword: 0.0 in, 0.0 out
    - passage_rerank:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 20816.4 in, 1668.4 out
      - keyword: 0.0 in, 0.0 out
    - retrieval:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
      - keyword: 0.0 in, 0.0 out
    - generation:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 464.5 in, 80.3 out
      - keyword: 0.0 in, 0.0 out
    - post_generation:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 557.7 in, 671.8 out
      - keyword: 0.0 in, 0.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.676s
- Retrieval: 0.344s
- Passage Augment: 0.000s
- Passage Rerank: 4.317s
- Passage Filter: 0.000s
- Passage Compress: 7.303s
- Prompt Maker: 0.000s
- Generation: 0.793s
- Post-generation: 5.599s
- Total Prediction Time: 19.032s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 174.60s
  - Total Evaluation: 174.61s

**Pipeline Total:** 2078.03s

---

*Report generated on 2025-09-03 09:35:31*
