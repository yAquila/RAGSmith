# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 7583.62s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@10=0.000, mAP=0.000, nDCG@10=0.000, MRR=0.000
  Generation: LLM=0.000, Semantic=0.009
  Component Scores: Retrieval=0.000, Generation=0.004
  Overall Score: 0.002
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.008s, Retrieval=0.713s, Prompt Maker=0.000s, Generation=0.003s, Post-generation=0.000s
  Total Prediction Time: 0.724s
  Embedding Tokens: 6518.0
  LLM Tokens: 6684.0 in, 639.0 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.088s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - passage_rerank: 6500.0
    - retrieval: 18.0
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 120.0 in, 92.0 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 64.0 in, 36.0 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 6500.0 in, 511.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.008s
- Retrieval: 0.713s
- Prompt Maker: 0.000s
- Generation: 0.003s
- Post-generation: 0.000s
- Total Prediction Time: 0.724s

**Evaluation Times:**
  - Retrieval: 0.00s
  - Generation: 8.82s
  - Total Evaluation: 8.82s

**Pipeline Total:** 7583.62s

---

*Report generated on 2025-08-23 11:54:41*
