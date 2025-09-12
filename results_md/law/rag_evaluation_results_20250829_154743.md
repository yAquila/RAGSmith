# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 2076.32s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.878, mAP=0.815, nDCG@5=0.863, MRR=0.937
  Generation: LLM=0.871, Semantic=0.907
  Component Scores: Retrieval=0.873, Generation=0.889
  Overall Score: 0.881
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.683s, Retrieval=0.143s, Passage Augment=0.003s, Passage Rerank=4.295s, Passage Filter=0.000s, Passage Compress=7.266s, Prompt Maker=0.000s, Generation=0.990s, Post-generation=5.648s
  Total Prediction Time: 19.028s
  Embedding Tokens: 9407.6
  LLM Tokens: 13044.0 in, 2701.5 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.734s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_rerank: 9387.4
  - LLM Tokens:
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2026.8 in, 858.3 out
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.1 in, 80.9 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 9387.4 in, 1001.1 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 927.9 in, 84.7 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 584.8 in, 676.5 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.683s
- Retrieval: 0.143s
- Passage Augment: 0.003s
- Passage Rerank: 4.295s
- Passage Filter: 0.000s
- Passage Compress: 7.266s
- Prompt Maker: 0.000s
- Generation: 0.990s
- Post-generation: 5.648s
- Total Prediction Time: 19.028s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 173.39s
  - Total Evaluation: 173.40s

**Pipeline Total:** 2076.32s

---

*Report generated on 2025-08-29 15:47:43*
