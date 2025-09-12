# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1356.20s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.787, mAP=0.742, nDCG@5=0.785, MRR=0.873
  Generation: LLM=0.815, Semantic=0.904
  Component Scores: Retrieval=0.797, Generation=0.860
  Overall Score: 0.828
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=1.450s, Retrieval=0.112s, Passage Augment=0.000s, Passage Rerank=4.776s, Passage Filter=0.000s, Passage Compress=4.866s, Prompt Maker=0.000s, Generation=0.681s, Post-generation=0.000s
  Total Prediction Time: 11.885s
  Embedding Tokens: 10973.2
  LLM Tokens: 12120.0 in, 1739.4 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.676s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 46.7
    - passage_compress: 300.8
    - query_expansion: 20.2
    - passage_rerank: 10605.6
  - LLM Tokens:
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1141.8 in, 648.3 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 372.6 in, 70.0 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 10605.6 in, 1021.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 1.450s
- Retrieval: 0.112s
- Passage Augment: 0.000s
- Passage Rerank: 4.776s
- Passage Filter: 0.000s
- Passage Compress: 4.866s
- Prompt Maker: 0.000s
- Generation: 0.681s
- Post-generation: 0.000s
- Total Prediction Time: 11.885s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 167.55s
  - Total Evaluation: 167.57s

**Pipeline Total:** 1356.20s

---

*Report generated on 2025-09-04 09:09:10*
