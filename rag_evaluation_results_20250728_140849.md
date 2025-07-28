# RAG EVALUATION RESULTS

**Dataset:** 3 test cases  
**Success rate:** 6/6 (100.0%)  
**Total runtime:** 63.01s

**Model combinations tested:** 2
  • query_expansion:no_expansion + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • query_expansion:simple_multi_query_cc + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** query_expansion:no_expansion + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3  
**Generation:** query_expansion:simple_multi_query_cc + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3  
**Overall:** query_expansion:no_expansion + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3

## 📊 DETAILED METRICS BY COMBINATION:

**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=1.000, mAP=1.000, nDCG@5=1.000, MRR=1.000
  Generation: LLM=0.917, Semantic=0.840
  Component Scores: Retrieval=1.000, Generation=0.878
  Overall Score: 0.915
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=11.335s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=2.965s
  Total Prediction Time: 14.301s
  Embedding Tokens:12.0
  LLM Input Tokens:1271.7
  LLM Output Tokens:188.3
  Avg Evaluation Times: Retrieval=0.000s, Generation=2.243s

**query_expansion:simple_multi_query_cc + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=1.000, mAP=0.833, nDCG@5=0.877, MRR=0.833
  Generation: LLM=0.933, Semantic=0.877
  Component Scores: Retrieval=0.886, Generation=0.905
  Overall Score: 0.899
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=1.099s, Retrieval=0.378s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=0.979s
  Total Prediction Time: 2.456s
  Embedding Tokens:16.7
  LLM Input Tokens:463.0
  LLM Output Tokens:169.3
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.569s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 12.0
  - LLM Input Tokens:
    - generation: 1271.7
  - LLM Output Tokens:
    - generation: 188.3
**query_expansion:simple_multi_query_cc + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 16.7
  - LLM Input Tokens:
    - generation: 368.0
    - query_expansion: 95.0
  - LLM Output Tokens:
    - generation: 108.3
    - query_expansion: 61.0

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 1.099s
- Retrieval: 11.713s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 3.945s
- Total Prediction Time: 16.757s

**Evaluation Times:**
  - Retrieval: 0.00s
  - Generation: 8.44s
  - Total Evaluation: 8.44s

**Pipeline Total:** 63.01s

---

*Report generated on 2025-07-28 14:08:49*
