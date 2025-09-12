# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 7191.71s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@10=0.000, mAP=0.000, nDCG@10=0.000, MRR=0.000
  Generation: LLM=0.004, Semantic=0.017
  Component Scores: Retrieval=0.000, Generation=0.011
  Overall Score: 0.005
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.014s, Retrieval=1.399s, Prompt Maker=0.000s, Generation=0.012s, Post-generation=0.074s
  Total Prediction Time: 1.499s
  Embedding Tokens: 21.0
  LLM Tokens: 1084.5 in, 595.0 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.191s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 21.0
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 116.0 in, 84.5 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 60.0 in, 73.5 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 908.5 in, 437.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.014s
- Retrieval: 1.399s
- Prompt Maker: 0.000s
- Generation: 0.012s
- Post-generation: 0.074s
- Total Prediction Time: 1.499s

**Evaluation Times:**
  - Retrieval: 0.00s
  - Generation: 19.07s
  - Total Evaluation: 19.07s

**Pipeline Total:** 7191.71s

---

*Report generated on 2025-09-03 11:35:22*
