# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 9140.61s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@10=0.000, mAP=0.000, nDCG@10=0.000, MRR=0.000
  Generation: LLM=0.010, Semantic=0.017
  Component Scores: Retrieval=0.000, Generation=0.014
  Overall Score: 0.007
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.014s, Retrieval=1.761s, Prompt Maker=0.000s, Generation=0.006s, Post-generation=0.017s
  Total Prediction Time: 1.798s
  Embedding Tokens: 18.5
  LLM Tokens: 432.5 in, 212.5 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.182s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 18.5
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 119.0 in, 82.5 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 250.5 in, 98.5 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 63.0 in, 31.5 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.014s
- Retrieval: 1.761s
- Prompt Maker: 0.000s
- Generation: 0.006s
- Post-generation: 0.017s
- Total Prediction Time: 1.798s

**Evaluation Times:**
  - Retrieval: 0.00s
  - Generation: 18.18s
  - Total Evaluation: 18.18s

**Pipeline Total:** 9140.61s

---

*Report generated on 2025-08-19 12:48:06*
