# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 616.02s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.873, mAP=0.774, nDCG@5=0.829, MRR=0.880
  Generation: LLM=0.831, Semantic=0.899
  Component Scores: Retrieval=0.839, Generation=0.865
  Overall Score: 0.852
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.284s, Retrieval=0.048s, Passage Augment=0.003s, Passage Rerank=0.057s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.543s, Post-generation=2.694s
  Total Prediction Time: 4.629s
  Embedding Tokens: 1254.7
  LLM Tokens: 2872.2 in, 440.0 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.531s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_rerank: 1234.5
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 144.1 in, 25.3 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2108.5 in, 91.8 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 619.6 in, 322.9 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.284s
- Retrieval: 0.048s
- Passage Augment: 0.003s
- Passage Rerank: 0.057s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.543s
- Post-generation: 2.694s
- Total Prediction Time: 4.629s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 153.09s
  - Total Evaluation: 153.10s

**Pipeline Total:** 616.02s

---

*Report generated on 2025-09-05 15:52:15*
