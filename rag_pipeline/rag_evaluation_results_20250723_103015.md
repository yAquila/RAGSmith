# RAG EVALUATION RESULTS

**Dataset:** 1 test cases  
**Success rate:** 8/8 (100.0%)  
**Total runtime:** 108.93s

**Model combinations tested:** 8
  • retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3  
**Generation:** retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:gemma3:4b-t0.1  
**Overall:** retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:gemma3:4b-t0.1

## 📊 DETAILED METRICS BY COMBINATION:

**retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=1.000, mAP=1.000, nDCG@5=1.000, MRR=1.000
  Generation: LLM=0.100, Semantic=0.569
  Component Scores: Retrieval=1.000, Generation=0.335
  Overall Score: 0.534
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.105s, Passage Rerank=8.648s, Passage Filter=0.000s, Passage Compress=16.331s, Prompt Maker=0.000s, Generation=3.212s
  Total Prediction Time: 28.298s
  Embedding Tokens:1363.0
  LLM Input Tokens:2767.0
  LLM Output Tokens:710.0
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.550s

**retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=1.000, mAP=1.000, nDCG@5=1.000, MRR=1.000
  Generation: LLM=0.950, Semantic=0.905
  Component Scores: Retrieval=1.000, Generation=0.928
  Overall Score: 0.949
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.137s, Passage Rerank=0.372s, Passage Filter=0.000s, Passage Compress=12.421s, Prompt Maker=0.000s, Generation=2.349s
  Total Prediction Time: 15.279s
  Embedding Tokens:1363.0
  LLM Input Tokens:2882.0
  LLM Output Tokens:891.0
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.607s

**retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=1.000, mAP=1.000, nDCG@5=1.000, MRR=1.000
  Generation: LLM=0.750, Semantic=0.835
  Component Scores: Retrieval=1.000, Generation=0.792
  Overall Score: 0.855
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.156s, Passage Rerank=0.338s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.154s
  Total Prediction Time: 1.648s
  Embedding Tokens:1363.0
  LLM Input Tokens:1466.0
  LLM Output Tokens:132.0
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.544s

**retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=1.000, mAP=1.000, nDCG@5=1.000, MRR=1.000
  Generation: LLM=0.950, Semantic=0.743
  Component Scores: Retrieval=1.000, Generation=0.847
  Overall Score: 0.893
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.126s, Passage Rerank=0.329s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=10.349s
  Total Prediction Time: 10.803s
  Embedding Tokens:1363.0
  LLM Input Tokens:1535.0
  LLM Output Tokens:651.0
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.718s

**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=1.000, mAP=1.000, nDCG@5=1.000, MRR=1.000
  Generation: LLM=0.100, Semantic=0.485
  Component Scores: Retrieval=1.000, Generation=0.293
  Overall Score: 0.505
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.133s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=17.105s, Prompt Maker=0.000s, Generation=0.267s
  Total Prediction Time: 17.506s
  Embedding Tokens:4.0
  LLM Input Tokens:4092.0
  LLM Output Tokens:1043.0
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.526s

**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=1.000, mAP=1.000, nDCG@5=1.000, MRR=1.000
  Generation: LLM=0.950, Semantic=0.865
  Component Scores: Retrieval=1.000, Generation=0.908
  Overall Score: 0.935
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.128s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=17.248s, Prompt Maker=0.000s, Generation=1.985s
  Total Prediction Time: 19.362s
  Embedding Tokens:4.0
  LLM Input Tokens:4186.0
  LLM Output Tokens:1143.0
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.608s

**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=1.000, mAP=1.000, nDCG@5=1.000, MRR=1.000
  Generation: LLM=0.950, Semantic=0.794
  Component Scores: Retrieval=1.000, Generation=0.872
  Overall Score: 0.911
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.116s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=0.948s
  Total Prediction Time: 1.063s
  Embedding Tokens:4.0
  LLM Input Tokens:1867.0
  LLM Output Tokens:91.0
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.535s

**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@5=1.000, mAP=1.000, nDCG@5=1.000, MRR=1.000
  Generation: LLM=0.950, Semantic=0.870
  Component Scores: Retrieval=1.000, Generation=0.910
  Overall Score: 0.937
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.115s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=5.611s
  Total Prediction Time: 5.726s
  Embedding Tokens:4.0
  LLM Input Tokens:1964.0
  LLM Output Tokens:339.0
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.645s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - passage_rerank: 1359.0
    - retrieval: 4.0
  - LLM Input Tokens:
    - generation: 688.0
    - passage_compress: 2079.0
  - LLM Output Tokens:
    - generation: 28.0
    - passage_compress: 682.0
**retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - passage_rerank: 1359.0
    - retrieval: 4.0
  - LLM Input Tokens:
    - generation: 803.0
    - passage_compress: 2079.0
  - LLM Output Tokens:
    - generation: 132.0
    - passage_compress: 759.0
**retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - passage_rerank: 1359.0
    - retrieval: 4.0
  - LLM Input Tokens:
    - generation: 1466.0
  - LLM Output Tokens:
    - generation: 132.0
**retrieval:mxbai-cosine + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - passage_rerank: 1359.0
    - retrieval: 4.0
  - LLM Input Tokens:
    - generation: 1535.0
  - LLM Output Tokens:
    - generation: 651.0
**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 4.0
  - LLM Input Tokens:
    - generation: 1020.0
    - passage_compress: 3072.0
  - LLM Output Tokens:
    - generation: 8.0
    - passage_compress: 1035.0
**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 4.0
  - LLM Input Tokens:
    - generation: 1114.0
    - passage_compress: 3072.0
  - LLM Output Tokens:
    - generation: 100.0
    - passage_compress: 1043.0
**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 4.0
  - LLM Input Tokens:
    - generation: 1867.0
  - LLM Output Tokens:
    - generation: 91.0
**retrieval:mxbai-cosine + passage_rerank:no_rerank + passage_filter:simple_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 4.0
  - LLM Input Tokens:
    - generation: 1964.0
  - LLM Output Tokens:
    - generation: 339.0

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Retrieval: 1.016s
- Passage Rerank: 9.687s
- Passage Filter: 0.000s
- Passage Compress: 63.107s
- Prompt Maker: 0.001s
- Generation: 25.875s
- Total Prediction Time: 99.686s

**Evaluation Times:**
  - Retrieval: 0.00s
  - Generation: 4.73s
  - Total Evaluation: 4.73s

**Pipeline Total:** 108.93s

---

*Report generated on 2025-07-23 10:30:15*
