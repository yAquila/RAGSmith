# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 376.78s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.900, mAP=0.810, nDCG@5=0.861, MRR=0.902
  Generation: LLM=0.873, Semantic=0.921
  Component Scores: Retrieval=0.868, Generation=0.897
  Overall Score: 0.882
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.050s, Passage Augment=0.003s, Passage Rerank=0.704s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.506s, Post-generation=0.000s
  Total Prediction Time: 2.263s
  Embedding Tokens: 1259.7
  LLM Tokens: 3389.9 in, 957.0 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.504s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_rerank: 1239.5
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2150.4 in, 85.6 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1239.5 in, 871.4 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.050s
- Passage Augment: 0.003s
- Passage Rerank: 0.704s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.506s
- Post-generation: 0.000s
- Total Prediction Time: 2.263s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 150.40s
  - Total Evaluation: 150.41s

**Pipeline Total:** 376.78s

---

*Report generated on 2025-09-05 14:10:03*
