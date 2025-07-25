# RAG EVALUATION RESULTS

**Dataset:** 3 test cases  
**Success rate:** 30/30 (100.0%)  
**Total runtime:** 135.96s

**Model combinations tested:** 10
  • query_expansion:no_expansion + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • query_expansion:no_expansion + retrieval:bm25 + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • query_expansion:no_expansion + retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • query_expansion:no_expansion + retrieval:hybrid_search_rrf + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • query_expansion:no_expansion + retrieval:hybrid_search_borda + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • query_expansion:simple_multi_query + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • query_expansion:simple_multi_query + retrieval:bm25 + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • query_expansion:simple_multi_query + retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • query_expansion:simple_multi_query + retrieval:hybrid_search_rrf + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • query_expansion:simple_multi_query + retrieval:hybrid_search_borda + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** query_expansion:no_expansion + retrieval:bm25 + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1  
**Generation:** query_expansion:simple_multi_query + retrieval:hybrid_search_rrf + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1  
**Overall:** query_expansion:no_expansion + retrieval:bm25 + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1

## 📊 DETAILED METRICS BY COMBINATION:

**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=1.000, mAP=0.611, nDCG@5=0.710, MRR=0.611
  Generation: LLM=0.927, Semantic=0.728
  Component Scores: Retrieval=0.733, Generation=0.827
  Overall Score: 0.799
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.204s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=4.174s
  Total Prediction Time: 4.378s
  Embedding Tokens:5.3
  LLM Input Tokens:1013.0
  LLM Output Tokens:154.3
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.560s

**query_expansion:no_expansion + retrieval:bm25 + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=1.000, mAP=0.833, nDCG@5=0.877, MRR=0.833
  Generation: LLM=0.950, Semantic=0.707
  Component Scores: Retrieval=0.886, Generation=0.829
  Overall Score: 0.846
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.162s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=4.625s
  Total Prediction Time: 4.786s
  LLM Input Tokens:1032.0
  LLM Output Tokens:271.7
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.561s

**query_expansion:no_expansion + retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=1.000, mAP=0.667, nDCG@5=0.754, MRR=0.667
  Generation: LLM=0.927, Semantic=0.731
  Component Scores: Retrieval=0.772, Generation=0.829
  Overall Score: 0.812
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.340s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=3.385s
  Total Prediction Time: 3.726s
  Embedding Tokens:5.3
  LLM Input Tokens:1040.7
  LLM Output Tokens:198.3
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.559s

**query_expansion:no_expansion + retrieval:hybrid_search_rrf + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=1.000, mAP=0.611, nDCG@5=0.710, MRR=0.611
  Generation: LLM=0.927, Semantic=0.688
  Component Scores: Retrieval=0.733, Generation=0.808
  Overall Score: 0.785
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.327s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=2.772s
  Total Prediction Time: 3.099s
  Embedding Tokens:5.3
  LLM Input Tokens:974.0
  LLM Output Tokens:161.7
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.548s

**query_expansion:no_expansion + retrieval:hybrid_search_borda + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=1.000, mAP=0.611, nDCG@5=0.710, MRR=0.611
  Generation: LLM=0.927, Semantic=0.717
  Component Scores: Retrieval=0.733, Generation=0.822
  Overall Score: 0.795
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.387s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=3.000s
  Total Prediction Time: 3.387s
  Embedding Tokens:5.3
  LLM Input Tokens:970.7
  LLM Output Tokens:178.0
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.584s

**query_expansion:simple_multi_query + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=1.000, mAP=0.667, nDCG@5=0.754, MRR=0.667
  Generation: LLM=0.933, Semantic=0.744
  Component Scores: Retrieval=0.772, Generation=0.839
  Overall Score: 0.819
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.320s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=2.887s
  Total Prediction Time: 3.207s
  Embedding Tokens:6.3
  LLM Input Tokens:1025.7
  LLM Output Tokens:167.7
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.542s

**query_expansion:simple_multi_query + retrieval:bm25 + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=1.000, mAP=0.833, nDCG@5=0.877, MRR=0.833
  Generation: LLM=0.927, Semantic=0.708
  Component Scores: Retrieval=0.886, Generation=0.817
  Overall Score: 0.838
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.155s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=3.059s
  Total Prediction Time: 3.214s
  LLM Input Tokens:1075.7
  LLM Output Tokens:181.3
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.503s

**query_expansion:simple_multi_query + retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=1.000, mAP=0.611, nDCG@5=0.710, MRR=0.611
  Generation: LLM=0.927, Semantic=0.736
  Component Scores: Retrieval=0.733, Generation=0.831
  Overall Score: 0.802
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.511s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=3.296s
  Total Prediction Time: 3.807s
  Embedding Tokens:6.3
  LLM Input Tokens:1071.7
  LLM Output Tokens:189.3
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.598s

**query_expansion:simple_multi_query + retrieval:hybrid_search_rrf + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=1.000, mAP=0.611, nDCG@5=0.710, MRR=0.611
  Generation: LLM=0.933, Semantic=0.750
  Component Scores: Retrieval=0.733, Generation=0.842
  Overall Score: 0.809
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.540s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=3.613s
  Total Prediction Time: 4.153s
  Embedding Tokens:6.3
  LLM Input Tokens:1001.7
  LLM Output Tokens:218.3
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.609s

**query_expansion:simple_multi_query + retrieval:hybrid_search_borda + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=1.000, mAP=0.667, nDCG@5=0.754, MRR=0.667
  Generation: LLM=0.927, Semantic=0.717
  Component Scores: Retrieval=0.772, Generation=0.822
  Overall Score: 0.807
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.474s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=3.054s
  Total Prediction Time: 3.527s
  Embedding Tokens:6.3
  LLM Input Tokens:991.7
  LLM Output Tokens:181.7
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.566s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 5.3
  - LLM Input Tokens:
    - generation: 1013.0
  - LLM Output Tokens:
    - generation: 154.3
**query_expansion:no_expansion + retrieval:bm25 + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - LLM Input Tokens:
    - generation: 1032.0
  - LLM Output Tokens:
    - generation: 271.7
**query_expansion:no_expansion + retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 5.3
  - LLM Input Tokens:
    - generation: 1040.7
  - LLM Output Tokens:
    - generation: 198.3
**query_expansion:no_expansion + retrieval:hybrid_search_rrf + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 5.3
  - LLM Input Tokens:
    - generation: 974.0
  - LLM Output Tokens:
    - generation: 161.7
**query_expansion:no_expansion + retrieval:hybrid_search_borda + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 5.3
  - LLM Input Tokens:
    - generation: 970.7
  - LLM Output Tokens:
    - generation: 178.0
**query_expansion:simple_multi_query + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 6.3
  - LLM Input Tokens:
    - generation: 1025.7
  - LLM Output Tokens:
    - generation: 167.7
**query_expansion:simple_multi_query + retrieval:bm25 + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - LLM Input Tokens:
    - generation: 1075.7
  - LLM Output Tokens:
    - generation: 181.3
**query_expansion:simple_multi_query + retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 6.3
  - LLM Input Tokens:
    - generation: 1071.7
  - LLM Output Tokens:
    - generation: 189.3
**query_expansion:simple_multi_query + retrieval:hybrid_search_rrf + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 6.3
  - LLM Input Tokens:
    - generation: 1001.7
  - LLM Output Tokens:
    - generation: 218.3
**query_expansion:simple_multi_query + retrieval:hybrid_search_borda + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 6.3
  - LLM Input Tokens:
    - generation: 991.7
  - LLM Output Tokens:
    - generation: 181.7

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 3.421s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 33.863s
- Total Prediction Time: 37.285s

**Evaluation Times:**
  - Retrieval: 0.00s
  - Generation: 16.89s
  - Total Evaluation: 16.90s

**Pipeline Total:** 135.96s

---

*Report generated on 2025-07-25 13:50:20*
