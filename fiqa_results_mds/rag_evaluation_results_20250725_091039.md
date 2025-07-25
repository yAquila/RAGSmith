# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 400/400 (100.0%)  
**Total runtime:** 1841.82s

**Model combinations tested:** 4
  • retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • retrieval:bm25 + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • retrieval:hybrid_search_rrf + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1  
**Generation:** retrieval:hybrid_search_rrf + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1  
**Overall:** retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1

## 📊 DETAILED METRICS BY COMBINATION:

**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=0.830, mAP=0.571, nDCG@5=0.627, MRR=0.571
  Generation: LLM=0.910, Semantic=0.731
  Component Scores: Retrieval=0.650, Generation=0.820
  Overall Score: 0.769
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.208s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=3.842s
  Total Prediction Time: 4.050s
  Embedding Tokens:5.6
  LLM Input Tokens:996.6
  LLM Output Tokens:231.4
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.570s

**retrieval:bm25 + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=0.680, mAP=0.363, nDCG@5=0.421, MRR=0.363
  Generation: LLM=0.900, Semantic=0.727
  Component Scores: Retrieval=0.457, Generation=0.813
  Overall Score: 0.706
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.173s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=3.590s
  Total Prediction Time: 3.763s
  LLM Input Tokens:980.6
  LLM Output Tokens:217.6
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.558s

**retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=0.840, mAP=0.483, nDCG@5=0.564, MRR=0.483
  Generation: LLM=0.908, Semantic=0.730
  Component Scores: Retrieval=0.592, Generation=0.819
  Overall Score: 0.751
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.360s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=3.822s
  Total Prediction Time: 4.183s
  Embedding Tokens:5.6
  LLM Input Tokens:982.3
  LLM Output Tokens:233.4
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.572s

**retrieval:hybrid_search_rrf + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=0.820, mAP=0.508, nDCG@5=0.577, MRR=0.508
  Generation: LLM=0.915, Semantic=0.731
  Component Scores: Retrieval=0.603, Generation=0.823
  Overall Score: 0.757
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.387s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=3.723s
  Total Prediction Time: 4.110s
  Embedding Tokens:5.6
  LLM Input Tokens:989.4
  LLM Output Tokens:221.1
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.564s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 5.6
  - LLM Input Tokens:
    - generation: 996.6
  - LLM Output Tokens:
    - generation: 231.4
**retrieval:bm25 + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - LLM Input Tokens:
    - generation: 980.6
  - LLM Output Tokens:
    - generation: 217.6
**retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 5.6
  - LLM Input Tokens:
    - generation: 982.3
  - LLM Output Tokens:
    - generation: 233.4
**retrieval:hybrid_search_rrf + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 5.6
  - LLM Input Tokens:
    - generation: 989.4
  - LLM Output Tokens:
    - generation: 221.1

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Retrieval: 1.129s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 14.977s
- Total Prediction Time: 16.106s

**Evaluation Times:**
  - Retrieval: 0.03s
  - Generation: 226.36s
  - Total Evaluation: 226.39s

**Pipeline Total:** 1841.82s

---

*Report generated on 2025-07-25 09:10:39*
