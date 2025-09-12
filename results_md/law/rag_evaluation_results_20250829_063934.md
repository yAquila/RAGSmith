# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1051.20s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.000, mAP=0.000, nDCG@5=0.000, MRR=0.000
  Generation: LLM=0.546, Semantic=0.872
  Component Scores: Retrieval=0.000, Generation=0.709
  Overall Score: 0.355
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.133s, Passage Augment=0.000s, Passage Rerank=0.476s, Passage Filter=0.000s, Passage Compress=7.466s, Prompt Maker=0.000s, Generation=0.776s, Post-generation=0.000s
  Total Prediction Time: 8.851s
  Embedding Tokens: 1507.2
  LLM Tokens: 3188.6 in, 2551.4 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.660s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_compress: 362.2
    - passage_rerank: 1124.8
  - LLM Tokens:
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1589.2 in, 903.7 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 474.6 in, 77.5 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1124.8 in, 1570.2 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.133s
- Passage Augment: 0.000s
- Passage Rerank: 0.476s
- Passage Filter: 0.000s
- Passage Compress: 7.466s
- Prompt Maker: 0.000s
- Generation: 0.776s
- Post-generation: 0.000s
- Total Prediction Time: 8.851s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 165.96s
  - Total Evaluation: 165.97s

**Pipeline Total:** 1051.20s

---

*Report generated on 2025-08-29 06:39:34*
