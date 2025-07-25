# RAG EVALUATION RESULTS

**Dataset:** 3 test cases  
**Success rate:** 12/12 (100.0%)  
**Total runtime:** 148.25s

**Model combinations tested:** 4
  • retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • retrieval:bm25 + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • retrieval:hybrid_search_rrf + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** retrieval:bm25 + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1  
**Generation:** retrieval:hybrid_search_rrf + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1  
**Overall:** retrieval:bm25 + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1

## 📊 DETAILED METRICS BY COMBINATION:

**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=1.000, mAP=0.611, nDCG@5=0.710, MRR=0.611
  Generation: LLM=0.927, Semantic=0.734
  Component Scores: Retrieval=0.733, Generation=0.830
  Overall Score: 0.801
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=27.822s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=5.173s
  Total Prediction Time: 32.995s
  Embedding Tokens:5.3
  LLM Input Tokens:1013.0
  LLM Output Tokens:199.3
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.594s

**retrieval:bm25 + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=1.000, mAP=0.833, nDCG@5=0.877, MRR=0.833
  Generation: LLM=0.950, Semantic=0.687
  Component Scores: Retrieval=0.886, Generation=0.819
  Overall Score: 0.839
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.162s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=3.891s
  Total Prediction Time: 4.053s
  LLM Input Tokens:1032.0
  LLM Output Tokens:226.3
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.560s

**retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=1.000, mAP=0.667, nDCG@5=0.754, MRR=0.667
  Generation: LLM=0.950, Semantic=0.714
  Component Scores: Retrieval=0.772, Generation=0.832
  Overall Score: 0.814
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.331s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=4.110s
  Total Prediction Time: 4.441s
  Embedding Tokens:5.3
  LLM Input Tokens:1010.3
  LLM Output Tokens:250.3
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.585s

**retrieval:hybrid_search_rrf + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=1.000, mAP=0.611, nDCG@5=0.710, MRR=0.611
  Generation: LLM=0.927, Semantic=0.751
  Component Scores: Retrieval=0.733, Generation=0.839
  Overall Score: 0.807
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.329s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=3.130s
  Total Prediction Time: 3.460s
  Embedding Tokens:5.3
  LLM Input Tokens:1013.7
  LLM Output Tokens:188.0
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.557s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 5.3
  - LLM Input Tokens:
    - generation: 1013.0
  - LLM Output Tokens:
    - generation: 199.3
**retrieval:bm25 + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - LLM Input Tokens:
    - generation: 1032.0
  - LLM Output Tokens:
    - generation: 226.3
**retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 5.3
  - LLM Input Tokens:
    - generation: 1010.3
  - LLM Output Tokens:
    - generation: 250.3
**retrieval:hybrid_search_rrf + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 5.3
  - LLM Input Tokens:
    - generation: 1013.7
  - LLM Output Tokens:
    - generation: 188.0

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Retrieval: 28.644s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 16.304s
- Total Prediction Time: 44.948s

**Evaluation Times:**
  - Retrieval: 0.00s
  - Generation: 6.89s
  - Total Evaluation: 6.89s

**Pipeline Total:** 148.25s

---

*Report generated on 2025-07-25 07:20:03*
