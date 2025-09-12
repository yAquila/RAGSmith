# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1502.79s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:step_back_prompting_cc + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:step_back_prompting_cc + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:step_back_prompting_cc + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:step_back_prompting_cc + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:step_back_prompting_cc + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.722, mAP=0.593, nDCG@5=0.648, MRR=0.669
  Generation: LLM=0.782, Semantic=0.906
  Component Scores: Retrieval=0.658, Generation=0.844
  Overall Score: 0.751
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.479s, Retrieval=0.150s, Passage Augment=0.003s, Passage Rerank=4.024s, Passage Filter=0.000s, Passage Compress=5.674s, Prompt Maker=0.000s, Generation=0.845s, Post-generation=2.217s
  Total Prediction Time: 13.393s
  Embedding Tokens: 633.3
  LLM Tokens: 14820.1 in, 2135.5 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.634s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:step_back_prompting_cc + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_compress: 613.1
  - LLM Tokens:
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2061.5 in, 759.8 out
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 210.1 in, 49.4 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 11332.1 in, 985.5 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 684.6 in, 76.4 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 531.8 in, 264.4 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.479s
- Retrieval: 0.150s
- Passage Augment: 0.003s
- Passage Rerank: 4.024s
- Passage Filter: 0.000s
- Passage Compress: 5.674s
- Prompt Maker: 0.000s
- Generation: 0.845s
- Post-generation: 2.217s
- Total Prediction Time: 13.393s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 163.43s
  - Total Evaluation: 163.44s

**Pipeline Total:** 1502.79s

---

*Report generated on 2025-09-05 03:19:16*
