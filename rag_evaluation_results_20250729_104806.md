# RAG EVALUATION RESULTS

**Dataset:** 10 test cases  
**Success rate:** 70/70 (100.0%)  
**Total runtime:** 474.55s

**Model combinations tested:** 7
  • query_expansion:no_expansion + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • query_expansion:no_expansion + retrieval:nomic-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • query_expansion:no_expansion + retrieval:bm25 + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • query_expansion:no_expansion + retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • query_expansion:no_expansion + retrieval:hybrid_search_dbsf + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • query_expansion:no_expansion + retrieval:hybrid_search_rrf + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • query_expansion:no_expansion + retrieval:hybrid_search_borda + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** query_expansion:no_expansion + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3  
**Generation:** query_expansion:no_expansion + retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3  
**Overall:** query_expansion:no_expansion + retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3

## 📊 DETAILED METRICS BY COMBINATION:

**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.967
  Generation: LLM=0.827, Semantic=0.791
  Component Scores: Retrieval=0.967, Generation=0.809
  Overall Score: 0.856
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.140s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=2.172s
  Total Prediction Time: 2.313s
  Embedding Tokens:21.5
  LLM Input Tokens:1767.0
  LLM Output Tokens:207.4
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.088s

**query_expansion:no_expansion + retrieval:nomic-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.917
  Generation: LLM=0.882, Semantic=0.751
  Component Scores: Retrieval=0.917, Generation=0.816
  Overall Score: 0.846
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=1.641s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=2.815s
  Total Prediction Time: 4.456s
  Embedding Tokens:21.5
  LLM Input Tokens:1528.6
  LLM Output Tokens:234.1
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.608s

**query_expansion:no_expansion + retrieval:bm25 + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.917
  Generation: LLM=0.875, Semantic=0.824
  Component Scores: Retrieval=0.917, Generation=0.850
  Overall Score: 0.870
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.078s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=9.097s
  Total Prediction Time: 9.175s
  LLM Input Tokens:738.5
  LLM Output Tokens:212.0
  Avg Evaluation Times: Retrieval=0.000s, Generation=2.667s

**query_expansion:no_expansion + retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.917
  Generation: LLM=0.921, Semantic=0.795
  Component Scores: Retrieval=0.917, Generation=0.858
  Overall Score: 0.876
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.203s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=10.844s
  Total Prediction Time: 11.047s
  Embedding Tokens:21.5
  LLM Input Tokens:654.4
  LLM Output Tokens:231.8
  Avg Evaluation Times: Retrieval=0.000s, Generation=2.836s

**query_expansion:no_expansion + retrieval:hybrid_search_dbsf + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.917
  Generation: LLM=0.895, Semantic=0.778
  Component Scores: Retrieval=0.917, Generation=0.837
  Overall Score: 0.861
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.189s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=5.474s
  Total Prediction Time: 5.664s
  Embedding Tokens:21.5
  LLM Input Tokens:1812.3
  LLM Output Tokens:264.0
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.292s

**query_expansion:no_expansion + retrieval:hybrid_search_rrf + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.783
  Generation: LLM=0.825, Semantic=0.816
  Component Scores: Retrieval=0.783, Generation=0.821
  Overall Score: 0.809
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.195s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.688s
  Total Prediction Time: 1.883s
  Embedding Tokens:21.5
  LLM Input Tokens:238.3
  LLM Output Tokens:201.1
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.547s

**query_expansion:no_expansion + retrieval:hybrid_search_borda + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.917
  Generation: LLM=0.907, Semantic=0.783
  Component Scores: Retrieval=0.917, Generation=0.845
  Overall Score: 0.866
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.196s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=2.442s
  Total Prediction Time: 2.639s
  Embedding Tokens:21.5
  LLM Input Tokens:1856.8
  LLM Output Tokens:258.2
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.578s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 21.5
  - LLM Input Tokens:
    - generation: 1767.0
  - LLM Output Tokens:
    - generation: 207.4
**query_expansion:no_expansion + retrieval:nomic-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 21.5
  - LLM Input Tokens:
    - generation: 1528.6
  - LLM Output Tokens:
    - generation: 234.1
**query_expansion:no_expansion + retrieval:bm25 + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - LLM Input Tokens:
    - generation: 738.5
  - LLM Output Tokens:
    - generation: 212.0
**query_expansion:no_expansion + retrieval:hybrid_search_cc + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 21.5
  - LLM Input Tokens:
    - generation: 654.4
  - LLM Output Tokens:
    - generation: 231.8
**query_expansion:no_expansion + retrieval:hybrid_search_dbsf + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 21.5
  - LLM Input Tokens:
    - generation: 1812.3
  - LLM Output Tokens:
    - generation: 264.0
**query_expansion:no_expansion + retrieval:hybrid_search_rrf + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 21.5
  - LLM Input Tokens:
    - generation: 238.3
  - LLM Output Tokens:
    - generation: 201.1
**query_expansion:no_expansion + retrieval:hybrid_search_borda + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 21.5
  - LLM Input Tokens:
    - generation: 1856.8
  - LLM Output Tokens:
    - generation: 258.2

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 2.642s
- Passage Rerank: 0.000s
- Passage Filter: 0.002s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 34.532s
- Total Prediction Time: 37.177s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 96.17s
  - Total Evaluation: 96.17s

**Pipeline Total:** 474.55s

---

*Report generated on 2025-07-29 10:48:06*
