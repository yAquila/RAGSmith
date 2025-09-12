# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 7523.03s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@10=0.000, mAP=0.000, nDCG@10=0.000, MRR=0.000
  Generation: LLM=0.007, Semantic=0.017
  Component Scores: Retrieval=0.000, Generation=0.012
  Overall Score: 0.006
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.011s, Retrieval=1.498s, Prompt Maker=0.000s, Generation=0.007s, Post-generation=0.047s
  Total Prediction Time: 1.565s
  Embedding Tokens: 18.5
  LLM Tokens: 735.0 in, 388.5 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.192s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:rag_fusion + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 18.5
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 59.0 in, 41.5 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 561.0 in, 281.5 out
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 115.0 in, 65.5 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.011s
- Retrieval: 1.498s
- Prompt Maker: 0.000s
- Generation: 0.007s
- Post-generation: 0.047s
- Total Prediction Time: 1.565s

**Evaluation Times:**
  - Retrieval: 0.00s
  - Generation: 19.20s
  - Total Evaluation: 19.20s

**Pipeline Total:** 7523.03s

---

*Report generated on 2025-09-08 18:19:07*
