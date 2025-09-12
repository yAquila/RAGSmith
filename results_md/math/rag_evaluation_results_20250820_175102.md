# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 979.91s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.804, mAP=0.655, nDCG@5=0.732, MRR=0.783
  Generation: LLM=0.773, Semantic=0.887
  Component Scores: Retrieval=0.744, Generation=0.830
  Overall Score: 0.787
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.130s, Passage Augment=0.000s, Passage Rerank=0.048s, Passage Filter=0.000s, Passage Compress=5.264s, Prompt Maker=0.000s, Generation=0.974s, Post-generation=1.680s
  Total Prediction Time: 8.096s
  Embedding Tokens: 879.6
  LLM Tokens: 2715.1 in, 901.7 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.703s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_rerank: 859.6
    - retrieval: 20.0
  - LLM Tokens:
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 473.0 in, 194.4 out
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1549.6 in, 615.9 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 692.5 in, 91.3 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.130s
- Passage Augment: 0.000s
- Passage Rerank: 0.048s
- Passage Filter: 0.000s
- Passage Compress: 5.264s
- Prompt Maker: 0.000s
- Generation: 0.974s
- Post-generation: 1.680s
- Total Prediction Time: 8.096s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 170.25s
  - Total Evaluation: 170.26s

**Pipeline Total:** 979.91s

---

*Report generated on 2025-08-20 17:51:02*
