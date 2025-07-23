# RAG EVALUATION RESULTS

**Dataset:** 2 test cases  
**Success rate:** 12/12 (100.0%)  
**Total runtime:** 63.54s

**Model combinations tested:** 6
  • retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • retrieval:mxbai-cosine + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • retrieval:mxbai-cosine + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3  
**Generation:** retrieval:mxbai-cosine + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3  
**Overall:** retrieval:mxbai-cosine + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3

## 📊 DETAILED METRICS BY COMBINATION:

**retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.667, mAP=0.667, nDCG@5=0.735, MRR=1.000
  Generation: LLM=0.925, Semantic=0.849
  Component Scores: Retrieval=0.767, Generation=0.887
  Overall Score: 0.851
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.122s, Passage Rerank=4.601s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=3.825s
  Total Prediction Time: 8.549s
  Embedding Tokens:1644.0
  LLM Input Tokens:1495.0
  LLM Output Tokens:312.5
  Avg Evaluation Times: Retrieval=0.000s, Generation=3.120s

**retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.667, mAP=0.667, nDCG@5=0.735, MRR=1.000
  Generation: LLM=0.925, Semantic=0.864
  Component Scores: Retrieval=0.767, Generation=0.895
  Overall Score: 0.856
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.138s, Passage Rerank=0.342s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=2.577s
  Total Prediction Time: 3.057s
  Embedding Tokens:1644.0
  LLM Input Tokens:1094.5
  LLM Output Tokens:343.5
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.629s

**retrieval:mxbai-cosine + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.667, mAP=0.667, nDCG@5=0.735, MRR=1.000
  Generation: LLM=0.915, Semantic=0.905
  Component Scores: Retrieval=0.767, Generation=0.910
  Overall Score: 0.867
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.124s, Passage Rerank=0.998s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=1.730s
  Total Prediction Time: 2.853s
  Embedding Tokens:9.5
  LLM Input Tokens:2683.0
  LLM Output Tokens:1029.5
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.655s

**retrieval:mxbai-cosine + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.667, mAP=0.583, nDCG@5=0.648, MRR=0.750
  Generation: LLM=0.935, Semantic=0.881
  Component Scores: Retrieval=0.662, Generation=0.908
  Overall Score: 0.834
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.142s, Passage Rerank=1.018s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=2.093s
  Total Prediction Time: 3.254s
  Embedding Tokens:9.5
  LLM Input Tokens:2247.0
  LLM Output Tokens:1212.0
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.703s

**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.667, mAP=0.667, nDCG@5=0.735, MRR=1.000
  Generation: LLM=0.915, Semantic=0.833
  Component Scores: Retrieval=0.767, Generation=0.874
  Overall Score: 0.842
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.135s, Passage Rerank=0.000s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=2.964s
  Total Prediction Time: 3.099s
  Embedding Tokens:9.5
  LLM Input Tokens:2175.0
  LLM Output Tokens:372.0
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.679s

**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.667, mAP=0.667, nDCG@5=0.735, MRR=1.000
  Generation: LLM=0.935, Semantic=0.862
  Component Scores: Retrieval=0.767, Generation=0.899
  Overall Score: 0.859
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.153s, Passage Rerank=0.000s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=2.276s
  Total Prediction Time: 2.430s
  Embedding Tokens:9.5
  LLM Input Tokens:1147.0
  LLM Output Tokens:293.5
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.679s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - passage_rerank: 1634.5
    - retrieval: 9.5
  - LLM Input Tokens:
    - generation: 1495.0
  - LLM Output Tokens:
    - generation: 312.5
**retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - passage_rerank: 1634.5
    - retrieval: 9.5
  - LLM Input Tokens:
    - generation: 1094.5
  - LLM Output Tokens:
    - generation: 343.5
**retrieval:mxbai-cosine + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 9.5
  - LLM Input Tokens:
    - generation: 1039.0
    - passage_rerank: 1644.0
  - LLM Output Tokens:
    - generation: 226.0
    - passage_rerank: 803.5
**retrieval:mxbai-cosine + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 9.5
  - LLM Input Tokens:
    - generation: 603.0
    - passage_rerank: 1644.0
  - LLM Output Tokens:
    - generation: 287.5
    - passage_rerank: 924.5
**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 9.5
  - LLM Input Tokens:
    - generation: 2175.0
  - LLM Output Tokens:
    - generation: 372.0
**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 9.5
  - LLM Input Tokens:
    - generation: 1147.0
  - LLM Output Tokens:
    - generation: 293.5

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Retrieval: 0.815s
- Passage Rerank: 6.959s
- Passage Filter: 0.001s
- Prompt Maker: 0.000s
- Generation: 15.466s
- Total Prediction Time: 23.241s

**Evaluation Times:**
  - Retrieval: 0.00s
  - Generation: 12.93s
  - Total Evaluation: 12.93s

**Pipeline Total:** 63.54s

---

*Report generated on 2025-07-23 07:34:59*
