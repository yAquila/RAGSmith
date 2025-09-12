# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1072.31s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.436, mAP=0.436, nDCG@5=0.500, MRR=0.740
  Generation: LLM=0.774, Semantic=0.896
  Component Scores: Retrieval=0.528, Generation=0.835
  Overall Score: 0.681
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.710s, Retrieval=0.043s, Passage Augment=0.001s, Passage Rerank=5.679s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=0.880s, Post-generation=1.798s
  Total Prediction Time: 9.112s
  Embedding Tokens: 15739.1
  LLM Tokens: 16934.2 in, 2195.6 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.611s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_rerank: 15739.1
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.8 in, 84.2 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 484.6 in, 209.3 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 592.7 in, 83.2 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 15739.1 in, 1818.8 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.710s
- Retrieval: 0.043s
- Passage Augment: 0.001s
- Passage Rerank: 5.679s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.880s
- Post-generation: 1.798s
- Total Prediction Time: 9.112s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 161.05s
  - Total Evaluation: 161.06s

**Pipeline Total:** 1072.31s

---

*Report generated on 2025-08-22 06:00:56*
