# RAG EVALUATION RESULTS

**Dataset:** 2 test cases  
**Success rate:** 12/12 (100.0%)  
**Total runtime:** 68.55s

**Model combinations tested:** 6
  • retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • retrieval:mxbai-cosine + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • retrieval:mxbai-cosine + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3  
**Generation:** retrieval:mxbai-cosine + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3  
**Overall:** retrieval:mxbai-cosine + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3

## 📊 DETAILED METRICS BY COMBINATION:

**retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.667, mAP=0.667, nDCG@5=0.735, MRR=1.000
  Generation: LLM=0.925, Semantic=0.869
  Component Scores: Retrieval=0.767, Generation=0.897
  Overall Score: 0.858
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.123s, Passage Rerank=5.609s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=4.750s
  Total Prediction Time: 10.482s
  Embedding Tokens:1644.0
  LLM Input Tokens:1495.0
  LLM Output Tokens:359.5
  Avg Evaluation Times: Retrieval=0.000s, Generation=2.993s

**retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.667, mAP=0.667, nDCG@5=0.735, MRR=1.000
  Generation: LLM=0.935, Semantic=0.876
  Component Scores: Retrieval=0.767, Generation=0.906
  Overall Score: 0.864
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.109s, Passage Rerank=0.349s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=2.376s
  Total Prediction Time: 2.835s
  Embedding Tokens:1644.0
  LLM Input Tokens:1094.5
  LLM Output Tokens:268.5
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.529s

**retrieval:mxbai-cosine + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.667, mAP=0.667, nDCG@5=0.735, MRR=1.000
  Generation: LLM=0.915, Semantic=0.873
  Component Scores: Retrieval=0.767, Generation=0.894
  Overall Score: 0.856
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.095s, Passage Rerank=0.946s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=3.072s
  Total Prediction Time: 4.114s
  Embedding Tokens:9.5
  LLM Input Tokens:2883.5
  LLM Output Tokens:1289.5
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.572s

**retrieval:mxbai-cosine + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.667, mAP=0.667, nDCG@5=0.735, MRR=1.000
  Generation: LLM=0.935, Semantic=0.899
  Component Scores: Retrieval=0.767, Generation=0.917
  Overall Score: 0.872
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.102s, Passage Rerank=1.047s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=1.888s
  Total Prediction Time: 3.037s
  Embedding Tokens:9.5
  LLM Input Tokens:2556.0
  LLM Output Tokens:1150.5
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.576s

**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.667, mAP=0.667, nDCG@5=0.735, MRR=1.000
  Generation: LLM=0.850, Semantic=0.856
  Component Scores: Retrieval=0.767, Generation=0.853
  Overall Score: 0.827
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.104s, Passage Rerank=0.000s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=3.296s
  Total Prediction Time: 3.400s
  Embedding Tokens:9.5
  LLM Input Tokens:2175.0
  LLM Output Tokens:364.0
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.626s

**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.667, mAP=0.667, nDCG@5=0.735, MRR=1.000
  Generation: LLM=0.915, Semantic=0.871
  Component Scores: Retrieval=0.767, Generation=0.893
  Overall Score: 0.855
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.120s, Passage Rerank=0.000s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=2.129s
  Total Prediction Time: 2.250s
  Embedding Tokens:9.5
  LLM Input Tokens:1147.0
  LLM Output Tokens:234.0
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.560s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - passage_rerank: 1634.5
    - retrieval: 9.5
  - LLM Input Tokens:
    - generation: 1495.0
  - LLM Output Tokens:
    - generation: 359.5
**retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - passage_rerank: 1634.5
    - retrieval: 9.5
  - LLM Input Tokens:
    - generation: 1094.5
  - LLM Output Tokens:
    - generation: 268.5
**retrieval:mxbai-cosine + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 9.5
  - LLM Input Tokens:
    - generation: 1239.5
    - passage_rerank: 1644.0
  - LLM Output Tokens:
    - generation: 347.0
    - passage_rerank: 942.5
**retrieval:mxbai-cosine + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 9.5
  - LLM Input Tokens:
    - generation: 912.0
    - passage_rerank: 1644.0
  - LLM Output Tokens:
    - generation: 208.0
    - passage_rerank: 942.5
**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 9.5
  - LLM Input Tokens:
    - generation: 2175.0
  - LLM Output Tokens:
    - generation: 364.0
**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 9.5
  - LLM Input Tokens:
    - generation: 1147.0
  - LLM Output Tokens:
    - generation: 234.0

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Retrieval: 0.653s
- Passage Rerank: 7.951s
- Passage Filter: 0.001s
- Prompt Maker: 0.000s
- Generation: 17.511s
- Total Prediction Time: 26.116s

**Evaluation Times:**
  - Retrieval: 0.00s
  - Generation: 11.71s
  - Total Evaluation: 11.71s

**Pipeline Total:** 68.55s

---

*Report generated on 2025-07-23 07:43:04*
