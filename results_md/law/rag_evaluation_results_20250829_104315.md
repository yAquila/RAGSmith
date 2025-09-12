# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 376.03s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.888, mAP=0.828, nDCG@5=0.875, MRR=0.948
  Generation: LLM=0.859, Semantic=0.907
  Component Scores: Retrieval=0.885, Generation=0.883
  Overall Score: 0.884
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.685s, Retrieval=0.145s, Passage Augment=0.000s, Passage Rerank=0.435s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=0.946s, Post-generation=0.000s
  Total Prediction Time: 2.211s
  Embedding Tokens: 9353.5
  LLM Tokens: 1148.2 in, 153.9 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.549s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_rerank: 9333.3
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.1 in, 80.8 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1031.1 in, 73.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.685s
- Retrieval: 0.145s
- Passage Augment: 0.000s
- Passage Rerank: 0.435s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.946s
- Post-generation: 0.000s
- Total Prediction Time: 2.211s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 154.85s
  - Total Evaluation: 154.86s

**Pipeline Total:** 376.03s

---

*Report generated on 2025-08-29 10:43:15*
