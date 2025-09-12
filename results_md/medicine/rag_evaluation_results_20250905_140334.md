# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 438.71s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.888, mAP=0.828, nDCG@5=0.875, MRR=0.948
  Generation: LLM=0.869, Semantic=0.925
  Component Scores: Retrieval=0.885, Generation=0.897
  Overall Score: 0.891
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.691s, Retrieval=0.146s, Passage Augment=0.003s, Passage Rerank=0.447s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.582s, Post-generation=0.000s
  Total Prediction Time: 2.869s
  Embedding Tokens: 9379.5
  LLM Tokens: 2513.0 in, 163.4 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.517s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_rerank: 9359.3
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.1 in, 81.8 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2395.9 in, 81.5 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.691s
- Retrieval: 0.146s
- Passage Augment: 0.003s
- Passage Rerank: 0.447s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.582s
- Post-generation: 0.000s
- Total Prediction Time: 2.869s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 151.71s
  - Total Evaluation: 151.72s

**Pipeline Total:** 438.71s

---

*Report generated on 2025-09-05 14:03:34*
