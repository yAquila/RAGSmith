# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 813.73s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.874, mAP=0.812, nDCG@5=0.860, MRR=0.937
  Generation: LLM=0.865, Semantic=0.919
  Component Scores: Retrieval=0.871, Generation=0.892
  Overall Score: 0.882
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.680s, Retrieval=0.156s, Passage Augment=0.003s, Passage Rerank=4.230s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.575s, Post-generation=0.000s
  Total Prediction Time: 6.645s
  Embedding Tokens: 9440.2
  LLM Tokens: 11861.6 in, 1172.4 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.492s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_rerank: 9420.0
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.1 in, 80.0 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2324.5 in, 83.3 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 9420.0 in, 1009.1 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.680s
- Retrieval: 0.156s
- Passage Augment: 0.003s
- Passage Rerank: 4.230s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.575s
- Post-generation: 0.000s
- Total Prediction Time: 6.645s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 149.17s
  - Total Evaluation: 149.18s

**Pipeline Total:** 813.73s

---

*Report generated on 2025-09-05 14:47:34*
