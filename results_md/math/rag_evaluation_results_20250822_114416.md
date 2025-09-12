# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 406.18s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.752, mAP=0.634, nDCG@5=0.675, MRR=0.742
  Generation: LLM=0.823, Semantic=0.897
  Component Scores: Retrieval=0.701, Generation=0.860
  Overall Score: 0.780
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.703s, Retrieval=0.220s, Passage Augment=0.000s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.476s, Post-generation=0.000s
  Total Prediction Time: 2.399s
  Embedding Tokens: 20.0
  LLM Tokens: 2042.3 in, 177.1 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.662s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 20.0
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.8 in, 82.7 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1924.4 in, 94.3 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.703s
- Retrieval: 0.220s
- Passage Augment: 0.000s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.476s
- Post-generation: 0.000s
- Total Prediction Time: 2.399s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 166.15s
  - Total Evaluation: 166.16s

**Pipeline Total:** 406.18s

---

*Report generated on 2025-08-22 11:44:16*
