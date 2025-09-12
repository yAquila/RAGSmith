# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1311.76s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.792, mAP=0.755, nDCG@5=0.796, MRR=0.888
  Generation: LLM=0.820, Semantic=0.906
  Component Scores: Retrieval=0.808, Generation=0.863
  Overall Score: 0.836
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=1.443s, Retrieval=0.112s, Passage Augment=0.000s, Passage Rerank=4.578s, Passage Filter=0.000s, Passage Compress=4.659s, Prompt Maker=0.000s, Generation=0.687s, Post-generation=0.000s
  Total Prediction Time: 11.479s
  Embedding Tokens: 10960.3
  LLM Tokens: 12066.9 in, 1721.8 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.637s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 47.0
    - passage_compress: 296.3
    - query_expansion: 20.2
    - passage_rerank: 10596.8
  - LLM Tokens:
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1103.7 in, 626.7 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 366.4 in, 70.7 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 10596.8 in, 1024.5 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 1.443s
- Retrieval: 0.112s
- Passage Augment: 0.000s
- Passage Rerank: 4.578s
- Passage Filter: 0.000s
- Passage Compress: 4.659s
- Prompt Maker: 0.000s
- Generation: 0.687s
- Post-generation: 0.000s
- Total Prediction Time: 11.479s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 163.74s
  - Total Evaluation: 163.75s

**Pipeline Total:** 1311.76s

---

*Report generated on 2025-08-28 05:34:25*
