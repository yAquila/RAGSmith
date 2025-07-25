# RAG EVALUATION RESULTS

**Dataset:** 10 test cases  
**Success rate:** 20/20 (100.0%)  
**Total runtime:** 97.70s

**Model combinations tested:** 2
  • query_expansion:no_expansion + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • query_expansion:simple_multi_query + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** query_expansion:simple_multi_query + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1  
**Generation:** query_expansion:simple_multi_query + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1  
**Overall:** query_expansion:simple_multi_query + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1

## 📊 DETAILED METRICS BY COMBINATION:

**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=0.900, mAP=0.658, nDCG@5=0.719, MRR=0.658
  Generation: LLM=0.916, Semantic=0.753
  Component Scores: Retrieval=0.734, Generation=0.835
  Overall Score: 0.804
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.207s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=3.817s
  Total Prediction Time: 4.024s
  Embedding Tokens:5.8
  LLM Input Tokens:985.5
  LLM Output Tokens:200.4
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.566s

**query_expansion:simple_multi_query + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=0.900, mAP=0.675, nDCG@5=0.732, MRR=0.675
  Generation: LLM=0.925, Semantic=0.759
  Component Scores: Retrieval=0.746, Generation=0.842
  Overall Score: 0.813
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.349s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=3.877s
  Total Prediction Time: 4.227s
  Embedding Tokens:6.8
  LLM Input Tokens:989.3
  LLM Output Tokens:237.9
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.608s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 5.8
  - LLM Input Tokens:
    - generation: 985.5
  - LLM Output Tokens:
    - generation: 200.4
**query_expansion:simple_multi_query + retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 6.8
  - LLM Input Tokens:
    - generation: 989.3
  - LLM Output Tokens:
    - generation: 237.9

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.556s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 7.694s
- Total Prediction Time: 8.250s

**Evaluation Times:**
  - Retrieval: 0.00s
  - Generation: 11.74s
  - Total Evaluation: 11.74s

**Pipeline Total:** 97.70s

---

*Report generated on 2025-07-25 13:55:03*
