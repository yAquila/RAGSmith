# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 852.68s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.625, mAP=0.499, nDCG@5=0.554, MRR=0.583
  Generation: LLM=0.806, Semantic=0.916
  Component Scores: Retrieval=0.565, Generation=0.861
  Overall Score: 0.713
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=1.450s, Retrieval=0.109s, Passage Augment=0.003s, Passage Rerank=4.033s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.301s, Post-generation=0.000s
  Total Prediction Time: 6.897s
  Embedding Tokens: 66.9
  LLM Tokens: 12299.9 in, 1042.2 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.629s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 46.7
    - query_expansion: 20.2
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1694.3 in, 84.8 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 10605.6 in, 957.4 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 1.450s
- Retrieval: 0.109s
- Passage Augment: 0.003s
- Passage Rerank: 4.033s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.301s
- Post-generation: 0.000s
- Total Prediction Time: 6.897s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 162.92s
  - Total Evaluation: 162.93s

**Pipeline Total:** 852.68s

---

*Report generated on 2025-09-04 23:49:50*
