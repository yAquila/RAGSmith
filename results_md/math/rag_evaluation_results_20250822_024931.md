# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1834.43s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:decomposition_cc + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:decomposition_cc + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:decomposition_cc + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:decomposition_cc + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:decomposition_cc + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.821, mAP=0.748, nDCG@5=0.806, MRR=0.888
  Generation: LLM=0.805, Semantic=0.905
  Component Scores: Retrieval=0.816, Generation=0.855
  Overall Score: 0.835
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.631s, Retrieval=0.042s, Passage Augment=1.645s, Passage Rerank=9.339s, Passage Filter=0.000s, Passage Compress=2.146s, Prompt Maker=0.000s, Generation=1.166s, Post-generation=1.619s
  Total Prediction Time: 16.587s
  Embedding Tokens: 17692.6
  LLM Tokens: 20904.3 in, 2720.0 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.757s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:decomposition_cc + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_rerank: 16629.3
    - passage_compress: 1063.3
  - LLM Tokens:
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 16629.3 in, 1829.8 out
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 172.9 in, 71.0 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1195.2 in, 91.4 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 447.9 in, 187.9 out
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2458.9 in, 539.9 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.631s
- Retrieval: 0.042s
- Passage Augment: 1.645s
- Passage Rerank: 9.339s
- Passage Filter: 0.000s
- Passage Compress: 2.146s
- Prompt Maker: 0.000s
- Generation: 1.166s
- Post-generation: 1.619s
- Total Prediction Time: 16.587s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 175.66s
  - Total Evaluation: 175.67s

**Pipeline Total:** 1834.43s

---

*Report generated on 2025-08-22 02:49:31*
