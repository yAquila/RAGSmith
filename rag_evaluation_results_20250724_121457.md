# RAG EVALUATION RESULTS

**Dataset:** 10 test cases  
**Success rate:** 40/40 (100.0%)  
**Total runtime:** 808.21s

**Model combinations tested:** 4
  • retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • retrieval:bm25 + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • retrieval:hybrid_search_rrf + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1  
**Generation:** retrieval:hybrid_search_rrf + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1  
**Overall:** retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1

## 📊 DETAILED METRICS BY COMBINATION:

**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=0.573, mAP=0.516, nDCG@5=0.567, MRR=0.667
  Generation: LLM=0.871, Semantic=0.808
  Component Scores: Retrieval=0.581, Generation=0.839
  Overall Score: 0.762
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=37.246s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=9.245s
  Total Prediction Time: 46.492s
  Embedding Tokens:10.8
  LLM Input Tokens:2025.9
  LLM Output Tokens:541.9
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.737s

**retrieval:bm25 + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=0.342, mAP=0.264, nDCG@5=0.340, MRR=0.533
  Generation: LLM=0.863, Semantic=0.791
  Component Scores: Retrieval=0.370, Generation=0.827
  Overall Score: 0.690
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=1.045s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=8.309s
  Total Prediction Time: 9.354s
  LLM Input Tokens:2696.4
  LLM Output Tokens:509.7
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.729s

**retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=0.598, mAP=0.515, nDCG@5=0.575, MRR=0.675
  Generation: LLM=0.901, Semantic=0.795
  Component Scores: Retrieval=0.591, Generation=0.848
  Overall Score: 0.771
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=1.717s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=8.804s
  Total Prediction Time: 10.521s
  Embedding Tokens:10.8
  LLM Input Tokens:2537.4
  LLM Output Tokens:524.2
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.721s

**retrieval:hybrid_search_rrf + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=0.514, mAP=0.451, nDCG@5=0.495, MRR=0.620
  Generation: LLM=0.891, Semantic=0.814
  Component Scores: Retrieval=0.520, Generation=0.852
  Overall Score: 0.753
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=1.851s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=8.845s
  Total Prediction Time: 10.696s
  Embedding Tokens:10.8
  LLM Input Tokens:2559.1
  LLM Output Tokens:511.2
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.696s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 10.8
  - LLM Input Tokens:
    - generation: 2025.9
  - LLM Output Tokens:
    - generation: 541.9
**retrieval:bm25 + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - LLM Input Tokens:
    - generation: 2696.4
  - LLM Output Tokens:
    - generation: 509.7
**retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 10.8
  - LLM Input Tokens:
    - generation: 2537.4
  - LLM Output Tokens:
    - generation: 524.2
**retrieval:hybrid_search_rrf + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 10.8
  - LLM Input Tokens:
    - generation: 2559.1
  - LLM Output Tokens:
    - generation: 511.2

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Retrieval: 41.860s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 35.203s
- Total Prediction Time: 77.063s

**Evaluation Times:**
  - Retrieval: 0.00s
  - Generation: 28.83s
  - Total Evaluation: 28.83s

**Pipeline Total:** 808.21s

---

*Report generated on 2025-07-24 12:14:57*
