# RAG EVALUATION RESULTS

**Dataset:** 3 test cases  
**Success rate:** 6/6 (100.0%)  
**Total runtime:** 23.03s

**Model combinations tested:** 2
  • query_expansion:no_expansion + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • query_expansion:simple_multi_query + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** query_expansion:simple_multi_query + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3  
**Generation:** query_expansion:no_expansion + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3  
**Overall:** query_expansion:no_expansion + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3

## 📊 DETAILED METRICS BY COMBINATION:

**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=1.000, mAP=0.611, nDCG@5=0.710, MRR=0.611
  Generation: LLM=0.927, Semantic=0.721
  Component Scores: Retrieval=0.733, Generation=0.824
  Overall Score: 0.797
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.209s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=2.095s
  Total Prediction Time: 2.304s
  Embedding Tokens:5.3
  LLM Input Tokens:806.7
  LLM Output Tokens:147.0
  Avg Evaluation Times: Retrieval=0.000s, Generation=2.191s

**query_expansion:simple_multi_query + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=1.000, mAP=0.667, nDCG@5=0.754, MRR=0.667
  Generation: LLM=0.893, Semantic=0.681
  Component Scores: Retrieval=0.772, Generation=0.787
  Overall Score: 0.783
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.328s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.079s
  Total Prediction Time: 1.407s
  Embedding Tokens:6.3
  LLM Input Tokens:623.3
  LLM Output Tokens:118.7
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.596s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 5.3
  - LLM Input Tokens:
    - generation: 806.7
  - LLM Output Tokens:
    - generation: 147.0
**query_expansion:simple_multi_query + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 6.3
  - LLM Input Tokens:
    - generation: 623.3
  - LLM Output Tokens:
    - generation: 118.7

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.536s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 3.174s
- Total Prediction Time: 3.711s

**Evaluation Times:**
  - Retrieval: 0.00s
  - Generation: 8.36s
  - Total Evaluation: 8.36s

**Pipeline Total:** 23.03s

---

*Report generated on 2025-07-28 07:11:50*
