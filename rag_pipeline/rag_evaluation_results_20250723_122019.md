# RAG EVALUATION RESULTS

**Dataset:** 20 test cases  
**Success rate:** 60/60 (100.0%)  
**Total runtime:** 634.29s

**Model combinations tested:** 3
  • retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:multi_llm_llama3.2:1b-gemma3:4b-Ensemble:gemini-2.0-flash

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3  
**Generation:** retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:multi_llm_llama3.2:1b-gemma3:4b-Ensemble:gemini-2.0-flash  
**Overall:** retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:multi_llm_llama3.2:1b-gemma3:4b-Ensemble:gemini-2.0-flash

## 📊 DETAILED METRICS BY COMBINATION:

**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.613, mAP=0.617, nDCG@5=0.679, MRR=0.735
  Generation: LLM=0.789, Semantic=0.836
  Component Scores: Retrieval=0.661, Generation=0.812
  Overall Score: 0.767
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.153s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=2.829s
  Total Prediction Time: 2.982s
  Embedding Tokens:10.3
  LLM Input Tokens:2393.8
  LLM Output Tokens:316.9
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.958s

**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=0.613, mAP=0.617, nDCG@5=0.679, MRR=0.735
  Generation: LLM=0.907, Semantic=0.830
  Component Scores: Retrieval=0.661, Generation=0.869
  Overall Score: 0.807
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.151s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=9.365s
  Total Prediction Time: 9.515s
  Embedding Tokens:10.3
  LLM Input Tokens:2496.2
  LLM Output Tokens:572.7
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.765s

**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:multi_llm_llama3.2:1b-gemma3:4b-Ensemble:gemini-2.0-flash:**
  Retrieval: R@5=0.613, mAP=0.617, nDCG@5=0.679, MRR=0.735
  Generation: LLM=0.925, Semantic=0.816
  Component Scores: Retrieval=0.661, Generation=0.871
  Overall Score: 0.808
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.153s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=16.407s
  Total Prediction Time: 16.560s
  Embedding Tokens:10.3
  LLM Input Tokens:5637.1
  LLM Output Tokens:1500.5
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.776s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 10.3
  - LLM Input Tokens:
    - generation: 2393.8
  - LLM Output Tokens:
    - generation: 316.9
**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 10.3
  - LLM Input Tokens:
    - generation: 2496.2
  - LLM Output Tokens:
    - generation: 572.7
**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:multi_llm_llama3.2:1b-gemma3:4b-Ensemble:gemini-2.0-flash:**
  - Embedding Tokens:
    - retrieval: 10.3
  - LLM Input Tokens:
    - generation: 5637.1
  - LLM Output Tokens:
    - generation: 1500.5

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Retrieval: 0.457s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 28.601s
- Total Prediction Time: 29.058s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 49.98s
  - Total Evaluation: 49.98s

**Pipeline Total:** 634.29s

---

*Report generated on 2025-07-23 12:20:19*
