# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1392.56s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.893, mAP=0.794, nDCG@5=0.852, MRR=0.902
  Generation: LLM=0.847, Semantic=0.907
  Component Scores: Retrieval=0.860, Generation=0.877
  Overall Score: 0.869
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.708s, Retrieval=0.138s, Passage Augment=0.003s, Passage Rerank=8.069s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.480s, Post-generation=1.775s
  Total Prediction Time: 12.174s
  Embedding Tokens: 9976.3
  LLM Tokens: 12466.1 in, 2183.2 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.750s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_rerank: 9956.2
    - retrieval: 20.0
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.8 in, 83.9 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 484.5 in, 206.7 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1907.5 in, 94.9 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 9956.2 in, 1797.7 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.708s
- Retrieval: 0.138s
- Passage Augment: 0.003s
- Passage Rerank: 8.069s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.480s
- Post-generation: 1.775s
- Total Prediction Time: 12.174s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 175.00s
  - Total Evaluation: 175.01s

**Pipeline Total:** 1392.56s

---

*Report generated on 2025-08-22 17:54:00*
