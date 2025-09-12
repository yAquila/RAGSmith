# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1671.88s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.000, mAP=0.000, nDCG@5=0.000, MRR=0.000
  Generation: LLM=0.322, Semantic=0.834
  Component Scores: Retrieval=0.000, Generation=0.578
  Overall Score: 0.289
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.134s, Passage Augment=0.000s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=14.139s, Prompt Maker=0.000s, Generation=0.827s, Post-generation=0.000s
  Total Prediction Time: 15.101s
  Embedding Tokens: 550.4
  LLM Tokens: 3661.1 in, 1771.3 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.617s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - passage_compress: 530.2
    - retrieval: 20.2
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 701.4 in, 72.1 out
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2959.7 in, 1699.2 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.134s
- Passage Augment: 0.000s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 14.139s
- Prompt Maker: 0.000s
- Generation: 0.827s
- Post-generation: 0.000s
- Total Prediction Time: 15.101s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 161.71s
  - Total Evaluation: 161.72s

**Pipeline Total:** 1671.88s

---

*Report generated on 2025-09-08 15:26:43*
