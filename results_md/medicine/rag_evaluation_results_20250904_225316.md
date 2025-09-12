# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1428.04s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:hyde_cc + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:hyde_cc + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:hyde_cc + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:hyde_cc + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:hyde_cc + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.672, mAP=0.587, nDCG@5=0.630, MRR=0.670
  Generation: LLM=0.777, Semantic=0.914
  Component Scores: Retrieval=0.640, Generation=0.846
  Overall Score: 0.743
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=3.958s, Retrieval=0.075s, Passage Augment=0.003s, Passage Rerank=7.102s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.554s, Post-generation=0.000s
  Total Prediction Time: 12.692s
  Embedding Tokens: 149.8
  LLM Tokens: 11370.0 in, 1559.5 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.587s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:hyde_cc + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 149.8
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 120.0 in, 518.2 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2255.1 in, 85.8 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 8995.0 in, 955.5 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 3.958s
- Retrieval: 0.075s
- Passage Augment: 0.003s
- Passage Rerank: 7.102s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.554s
- Post-generation: 0.000s
- Total Prediction Time: 12.692s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 158.72s
  - Total Evaluation: 158.73s

**Pipeline Total:** 1428.04s

---

*Report generated on 2025-09-04 22:53:16*
