# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1112.16s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.804, mAP=0.655, nDCG@5=0.732, MRR=0.783
  Generation: LLM=0.769, Semantic=0.884
  Component Scores: Retrieval=0.744, Generation=0.827
  Overall Score: 0.785
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.130s, Passage Augment=0.000s, Passage Rerank=0.048s, Passage Filter=0.000s, Passage Compress=6.675s, Prompt Maker=0.000s, Generation=0.777s, Post-generation=1.779s
  Total Prediction Time: 9.410s
  Embedding Tokens: 1197.8
  LLM Tokens: 2395.5 in, 1087.9 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.711s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_rerank: 859.6
    - retrieval: 20.0
    - passage_compress: 318.1
  - LLM Tokens:
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 469.6 in, 208.1 out
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1500.0 in, 800.1 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 425.9 in, 79.7 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.130s
- Passage Augment: 0.000s
- Passage Rerank: 0.048s
- Passage Filter: 0.000s
- Passage Compress: 6.675s
- Prompt Maker: 0.000s
- Generation: 0.777s
- Post-generation: 1.779s
- Total Prediction Time: 9.410s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 171.06s
  - Total Evaluation: 171.07s

**Pipeline Total:** 1112.16s

---

*Report generated on 2025-08-20 04:41:09*
