# RAG EVALUATION RESULTS

**Dataset:** 2 test cases  
**Success rate:** 8/8 (100.0%)  
**Total runtime:** 78.35s

**Model combinations tested:** 4
  • retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • retrieval:bm25 + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • retrieval:hybrid_search_rrf + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** retrieval:bm25 + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1  
**Generation:** retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1  
**Overall:** retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1

## 📊 DETAILED METRICS BY COMBINATION:

**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=0.667, mAP=0.667, nDCG@5=0.735, MRR=1.000
  Generation: LLM=0.825, Semantic=0.864
  Component Scores: Retrieval=0.767, Generation=0.844
  Overall Score: 0.821
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.146s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=8.104s
  Total Prediction Time: 8.251s
  Embedding Tokens:9.5
  LLM Input Tokens:2271.5
  LLM Output Tokens:358.5
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.553s

**retrieval:bm25 + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=0.833, mAP=0.778, nDCG@5=0.852, MRR=1.000
  Generation: LLM=0.925, Semantic=0.866
  Component Scores: Retrieval=0.866, Generation=0.896
  Overall Score: 0.887
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.196s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=8.838s
  Total Prediction Time: 9.034s
  LLM Input Tokens:3708.5
  LLM Output Tokens:512.5
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.669s

**retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=0.833, mAP=0.778, nDCG@5=0.852, MRR=1.000
  Generation: LLM=0.950, Semantic=0.871
  Component Scores: Retrieval=0.866, Generation=0.911
  Overall Score: 0.897
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.312s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=8.123s
  Total Prediction Time: 8.434s
  Embedding Tokens:9.5
  LLM Input Tokens:3141.5
  LLM Output Tokens:485.0
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.633s

**retrieval:hybrid_search_rrf + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=0.833, mAP=0.733, nDCG@5=0.825, MRR=1.000
  Generation: LLM=0.950, Semantic=0.860
  Component Scores: Retrieval=0.848, Generation=0.905
  Overall Score: 0.888
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.274s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=8.479s
  Total Prediction Time: 8.753s
  Embedding Tokens:9.5
  LLM Input Tokens:3256.5
  LLM Output Tokens:531.5
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.611s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 9.5
  - LLM Input Tokens:
    - generation: 2271.5
  - LLM Output Tokens:
    - generation: 358.5
**retrieval:bm25 + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - LLM Input Tokens:
    - generation: 3708.5
  - LLM Output Tokens:
    - generation: 512.5
**retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 9.5
  - LLM Input Tokens:
    - generation: 3141.5
  - LLM Output Tokens:
    - generation: 485.0
**retrieval:hybrid_search_rrf + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 9.5
  - LLM Input Tokens:
    - generation: 3256.5
  - LLM Output Tokens:
    - generation: 531.5

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Retrieval: 0.927s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 33.544s
- Total Prediction Time: 34.471s

**Evaluation Times:**
  - Retrieval: 0.00s
  - Generation: 4.93s
  - Total Evaluation: 4.93s

**Pipeline Total:** 78.35s

---

*Report generated on 2025-07-24 08:24:54*
