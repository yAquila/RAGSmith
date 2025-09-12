# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 827.84s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.757, mAP=0.622, nDCG@5=0.668, MRR=0.720
  Generation: LLM=0.805, Semantic=0.900
  Component Scores: Retrieval=0.692, Generation=0.852
  Overall Score: 0.772
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.714s, Retrieval=0.231s, Passage Augment=2.440s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.521s, Post-generation=1.743s
  Total Prediction Time: 6.649s
  Embedding Tokens: 20.0
  LLM Tokens: 2683.9 in, 376.8 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.627s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 20.0
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.8 in, 84.6 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 481.6 in, 202.3 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2084.4 in, 89.8 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.714s
- Retrieval: 0.231s
- Passage Augment: 2.440s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.521s
- Post-generation: 1.743s
- Total Prediction Time: 6.649s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 162.73s
  - Total Evaluation: 162.74s

**Pipeline Total:** 827.84s

---

*Report generated on 2025-08-22 15:26:30*
