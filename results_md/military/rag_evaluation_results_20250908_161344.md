# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 2820.42s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_parent_document_retriever + query_expansion:rag_fusion + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:rag_fusion + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:rag_fusion + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:rag_fusion + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:rag_fusion + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.000, mAP=0.000, nDCG@5=0.000, MRR=0.000
  Generation: LLM=0.284, Semantic=0.828
  Component Scores: Retrieval=0.000, Generation=0.556
  Overall Score: 0.278
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.741s, Retrieval=0.333s, Passage Augment=0.000s, Passage Rerank=4.674s, Passage Filter=0.000s, Passage Compress=7.097s, Prompt Maker=0.000s, Generation=4.114s, Post-generation=9.357s
  Total Prediction Time: 26.317s
  Embedding Tokens: 360.4
  LLM Tokens: 22194.3 in, 4110.5 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.885s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:rag_fusion + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_compress: 340.2
    - retrieval: 20.2
  - LLM Tokens:
    - post_generation:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 758.9 in, 1113.5 out
      - vector: 0.0 in, 0.0 out
    - passage_rerank:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 19333.3 in, 1574.1 out
      - vector: 0.0 in, 0.0 out
    - generation:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 458.0 in, 479.3 out
      - vector: 0.0 in, 0.0 out
    - passage_compress:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1525.8 in, 855.1 out
      - vector: 0.0 in, 0.0 out
    - retrieval:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
    - query_expansion:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 118.4 in, 88.6 out
      - vector: 0.0 in, 0.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.741s
- Retrieval: 0.333s
- Passage Augment: 0.000s
- Passage Rerank: 4.674s
- Passage Filter: 0.000s
- Passage Compress: 7.097s
- Prompt Maker: 0.000s
- Generation: 4.114s
- Post-generation: 9.357s
- Total Prediction Time: 26.317s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 188.51s
  - Total Evaluation: 188.52s

**Pipeline Total:** 2820.42s

---

*Report generated on 2025-09-08 16:13:44*
