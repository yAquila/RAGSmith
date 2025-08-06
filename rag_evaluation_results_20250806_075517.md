# RAG EVALUATION RESULTS

**Dataset:** 3 test cases  
**Success rate:** 12/12 (100.0%)  
**Total runtime:** 346.10s

**Model combinations tested:** 4
  • pre_embedding:no_pre_embedding + retrieval:mxbai-cosine + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • pre_embedding:no_pre_embedding + retrieval:mxbai-cosine + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • pre_embedding:contextual_chunk_headers + retrieval:mxbai-cosine + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • pre_embedding:contextual_chunk_headers + retrieval:mxbai-cosine + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:gemma3:4b-t0.1

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:no_pre_embedding + retrieval:mxbai-cosine + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3  
**Generation:** pre_embedding:no_pre_embedding + retrieval:mxbai-cosine + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:gemma3:4b-t0.1  
**Overall:** pre_embedding:no_pre_embedding + retrieval:mxbai-cosine + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:gemma3:4b-t0.1

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:no_pre_embedding + retrieval:mxbai-cosine + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@10=1.000
  Generation: LLM=0.843, Semantic=0.872
  Component Scores: Retrieval=1.000, Generation=0.858
  Overall Score: 0.900
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=1.133s, Passage Filter=0.000s, Passage Compress=25.169s, Prompt Maker=0.000s, Generation=1.832s
  Total Prediction Time: 28.134s
  Embedding Tokens: 235.9
  LLM Tokens: 3045.0 in, 1506.3 out
  Avg Evaluation Times: Retrieval=0.001s, Generation=0.647s

**pre_embedding:no_pre_embedding + retrieval:mxbai-cosine + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@10=1.000
  Generation: LLM=0.903, Semantic=0.881
  Component Scores: Retrieval=1.000, Generation=0.892
  Overall Score: 0.925
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.224s, Passage Filter=0.000s, Passage Compress=23.901s, Prompt Maker=0.000s, Generation=1.789s
  Total Prediction Time: 25.914s
  Embedding Tokens: 276.8
  LLM Tokens: 3097.7 in, 1572.0 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.627s

**pre_embedding:contextual_chunk_headers + retrieval:mxbai-cosine + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@10=1.000
  Generation: LLM=0.900, Semantic=0.874
  Component Scores: Retrieval=1.000, Generation=0.887
  Overall Score: 0.921
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.255s, Passage Filter=0.000s, Passage Compress=27.180s, Prompt Maker=0.000s, Generation=1.261s
  Total Prediction Time: 28.697s
  Embedding Tokens: 259.9
  LLM Tokens: 3674.7 in, 1828.3 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.644s

**pre_embedding:contextual_chunk_headers + retrieval:mxbai-cosine + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@10=1.000
  Generation: LLM=0.810, Semantic=0.808
  Component Scores: Retrieval=1.000, Generation=0.809
  Overall Score: 0.866
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.197s, Passage Filter=0.000s, Passage Compress=27.470s, Prompt Maker=0.000s, Generation=2.388s
  Total Prediction Time: 30.055s
  Embedding Tokens: 269.2
  LLM Tokens: 3685.3 in, 1839.0 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.627s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:no_pre_embedding + retrieval:mxbai-cosine + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 12.3
    - passage_compress: 223.6
  - LLM Tokens:
    - generation:
      - llama3.2:1b: 290.0 in, 96.0 out
      - gemma3:4b: 0.0 in, 0.0 out
    - passage_compress:
      - llama3.2:1b: 0.0 in, 0.0 out
      - gemma3:4b: 2755.0 in, 1410.3 out
**pre_embedding:no_pre_embedding + retrieval:mxbai-cosine + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 12.3
    - passage_compress: 264.4
  - LLM Tokens:
    - generation:
      - gemma3:4b: 316.3 in, 101.7 out
    - passage_compress:
      - gemma3:4b: 2781.3 in, 1470.3 out
**pre_embedding:contextual_chunk_headers + retrieval:mxbai-cosine + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 12.3
    - passage_compress: 247.6
  - LLM Tokens:
    - generation:
      - llama3.2:1b: 327.3 in, 157.0 out
      - gemma3:4b: 0.0 in, 0.0 out
    - passage_compress:
      - llama3.2:1b: 0.0 in, 0.0 out
      - gemma3:4b: 3347.3 in, 1671.3 out
**pre_embedding:contextual_chunk_headers + retrieval:mxbai-cosine + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 12.3
    - passage_compress: 256.9
  - LLM Tokens:
    - generation:
      - gemma3:4b: 323.3 in, 143.3 out
    - passage_compress:
      - gemma3:4b: 3362.0 in, 1695.7 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Retrieval: 1.809s
- Passage Filter: 0.000s
- Passage Compress: 103.720s
- Prompt Maker: 0.000s
- Generation: 7.270s
- Total Prediction Time: 112.800s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 7.64s
  - Total Evaluation: 7.64s

**Pipeline Total:** 346.10s

---

*Report generated on 2025-08-06 07:55:17*
