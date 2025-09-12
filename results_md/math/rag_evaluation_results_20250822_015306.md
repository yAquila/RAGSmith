# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 9360.53s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:graph_rag + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:graph_rag + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:graph_rag + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:graph_rag + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:graph_rag + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.413, mAP=0.299, nDCG@5=0.373, MRR=0.484
  Generation: LLM=0.707, Semantic=0.870
  Component Scores: Retrieval=0.393, Generation=0.789
  Overall Score: 0.591
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.703s, Retrieval=79.968s, Passage Augment=0.000s, Passage Rerank=8.978s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=0.656s, Post-generation=1.467s
  Total Prediction Time: 91.772s
  Embedding Tokens: 3876.6
  LLM Tokens: 4460.2 in, 1196.8 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.832s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_simple_multi_query_borda + retrieval:graph_rag + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_rerank: 3856.5
    - retrieval: 20.0
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.8 in, 83.2 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 424.1 in, 169.2 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 61.8 in, 78.7 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 3856.5 in, 865.7 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.703s
- Retrieval: 79.968s
- Passage Augment: 0.000s
- Passage Rerank: 8.978s
- Passage Filter: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.656s
- Post-generation: 1.467s
- Total Prediction Time: 91.772s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 183.21s
  - Total Evaluation: 183.22s

**Pipeline Total:** 9360.53s

---

*Report generated on 2025-08-22 01:53:06*
