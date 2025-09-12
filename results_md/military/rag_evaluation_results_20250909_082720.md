# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1513.55s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_parent_document_retriever + query_expansion:rag_fusion + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:rag_fusion + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:rag_fusion + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:rag_fusion + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:rag_fusion + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.000, mAP=0.000, nDCG@5=0.000, MRR=0.000
  Generation: LLM=0.290, Semantic=0.822
  Component Scores: Retrieval=0.000, Generation=0.556
  Overall Score: 0.278
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.739s, Retrieval=0.344s, Passage Augment=0.000s, Passage Rerank=4.842s, Passage Filter=0.000s, Passage Compress=6.990s, Prompt Maker=0.000s, Generation=0.672s, Post-generation=0.000s
  Total Prediction Time: 13.587s
  Embedding Tokens: 355.1
  LLM Tokens: 21464.7 in, 2578.0 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.546s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:rag_fusion + retrieval:hybrid_vector_keyword_cc + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - passage_compress: 334.8
    - retrieval: 20.2
  - LLM Tokens:
    - passage_rerank:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 19381.9 in, 1583.7 out
      - vector: 0.0 in, 0.0 out
    - generation:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 451.9 in, 64.9 out
      - vector: 0.0 in, 0.0 out
    - passage_compress:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1512.5 in, 841.3 out
      - vector: 0.0 in, 0.0 out
    - retrieval:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
    - query_expansion:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 118.4 in, 88.1 out
      - vector: 0.0 in, 0.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.739s
- Retrieval: 0.344s
- Passage Augment: 0.000s
- Passage Rerank: 4.842s
- Passage Filter: 0.000s
- Passage Compress: 6.990s
- Prompt Maker: 0.000s
- Generation: 0.672s
- Post-generation: 0.000s
- Total Prediction Time: 13.587s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 154.63s
  - Total Evaluation: 154.64s

**Pipeline Total:** 1513.55s

---

*Report generated on 2025-09-09 08:27:20*
