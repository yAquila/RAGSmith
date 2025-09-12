# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 2247.64s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.858, mAP=0.768, nDCG@5=0.803, MRR=0.841
  Generation: LLM=0.770, Semantic=0.875
  Component Scores: Retrieval=0.818, Generation=0.823
  Overall Score: 0.820
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.300s, Retrieval=0.048s, Passage Augment=0.000s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=17.871s, Prompt Maker=0.000s, Generation=0.999s, Post-generation=1.630s
  Total Prediction Time: 20.848s
  Embedding Tokens: 538.0
  LLM Tokens: 5164.0 in, 2447.8 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.628s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 20.7
    - passage_compress: 517.3
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 144.8 in, 27.4 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 454.6 in, 189.1 out
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 3895.3 in, 2134.7 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 669.3 in, 96.6 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.300s
- Retrieval: 0.048s
- Passage Augment: 0.000s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 17.871s
- Prompt Maker: 0.000s
- Generation: 0.999s
- Post-generation: 1.630s
- Total Prediction Time: 20.848s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 162.80s
  - Total Evaluation: 162.81s

**Pipeline Total:** 2247.64s

---

*Report generated on 2025-08-20 20:18:50*
