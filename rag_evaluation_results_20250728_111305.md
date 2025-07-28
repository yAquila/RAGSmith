# RAG EVALUATION RESULTS

**Dataset:** 10 test cases  
**Success rate:** 30/30 (100.0%)  
**Total runtime:** 316.03s

**Model combinations tested:** 3
  • query_expansion:no_expansion + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • query_expansion:simple_multi_query_cc + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • query_expansion:hyde_cc + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** query_expansion:no_expansion + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3  
**Generation:** query_expansion:simple_multi_query_cc + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3  
**Overall:** query_expansion:no_expansion + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3

## 📊 DETAILED METRICS BY COMBINATION:

**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.950, mAP=0.700, nDCG@5=0.758, MRR=0.708
  Generation: LLM=0.876, Semantic=0.722
  Component Scores: Retrieval=0.779, Generation=0.799
  Overall Score: 0.793
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.218s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.585s
  Total Prediction Time: 1.803s
  Embedding Tokens:5.8
  LLM Input Tokens:841.8
  LLM Output Tokens:150.8
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.067s

**query_expansion:simple_multi_query_cc + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.950, mAP=0.558, nDCG@5=0.663, MRR=0.575
  Generation: LLM=0.888, Semantic=0.723
  Component Scores: Retrieval=0.687, Generation=0.806
  Overall Score: 0.770
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.780s, Retrieval=0.352s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.425s
  Total Prediction Time: 2.558s
  Embedding Tokens:10.1
  LLM Input Tokens:656.1
  LLM Output Tokens:211.0
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.599s

**query_expansion:hyde_cc + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.550, mAP=0.308, nDCG@5=0.350, MRR=0.325
  Generation: LLM=0.826, Semantic=0.698
  Component Scores: Retrieval=0.383, Generation=0.762
  Overall Score: 0.648
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=22.952s, Retrieval=0.293s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.428s
  Total Prediction Time: 24.674s
  Embedding Tokens:344.2
  LLM Input Tokens:510.5
  LLM Output Tokens:1750.4
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.526s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 5.8
  - LLM Input Tokens:
    - generation: 841.8
  - LLM Output Tokens:
    - generation: 150.8
**query_expansion:simple_multi_query_cc + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 10.1
  - LLM Input Tokens:
    - generation: 570.9
    - query_expansion: 85.2
  - LLM Output Tokens:
    - generation: 172.7
    - query_expansion: 38.3
**query_expansion:hyde_cc + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 344.2
  - LLM Input Tokens:
    - generation: 424.3
    - query_expansion: 86.2
  - LLM Output Tokens:
    - generation: 165.2
    - query_expansion: 1585.2

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 23.732s
- Retrieval: 0.863s
- Passage Rerank: 0.000s
- Passage Filter: 0.001s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 4.438s
- Total Prediction Time: 29.034s

**Evaluation Times:**
  - Retrieval: 0.00s
  - Generation: 21.92s
  - Total Evaluation: 21.92s

**Pipeline Total:** 316.03s

---

*Report generated on 2025-07-28 11:13:05*
