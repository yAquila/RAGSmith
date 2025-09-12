# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 10105.28s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_parent_document_retriever + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@10=0.134, mAP=0.113, nDCG@10=0.135, MRR=0.183
  Generation: LLM=0.242, Semantic=0.346
  Component Scores: Retrieval=0.141, Generation=0.294
  Overall Score: 0.218
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.579s, Retrieval=36.652s, Passage Augment=0.000s, Passage Rerank=2.213s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=0.263s, Post-generation=0.000s
  Total Prediction Time: 39.707s
  Embedding Tokens: 109.2
  LLM Tokens: 5368.4 in, 1040.0 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.463s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 88.2
    - query_expansion: 21.0
  - LLM Tokens:
    - retrieval:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
    - generation:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 366.9 in, 66.1 out
    - passage_rerank:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 5001.5 in, 973.9 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.579s
- Retrieval: 36.652s
- Passage Augment: 0.000s
- Passage Rerank: 2.213s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.263s
- Post-generation: 0.000s
- Total Prediction Time: 39.707s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 146.26s
  - Total Evaluation: 146.27s

**Pipeline Total:** 10105.28s

---

*Report generated on 2025-09-03 23:28:11*
