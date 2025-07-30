# RAG EVALUATION RESULTS

**Dataset:** 3 test cases  
**Success rate:** 6/6 (100.0%)  
**Total runtime:** 23.96s

**Model combinations tested:** 2
  • retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3  
**Generation:** retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1  
**Overall:** retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1

## 📊 DETAILED METRICS BY COMBINATION:

**retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@10=1.000
  Generation: LLM=0.933, Semantic=0.944
  Component Scores: Retrieval=1.000, Generation=0.938
  Overall Score: 0.957
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.324s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=2.051s
  Total Prediction Time: 2.375s
  Embedding Tokens:19.0
  LLM Input Tokens:1597.3
  LLM Output Tokens:89.0
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.917s

**retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@10=1.000
  Generation: LLM=0.917, Semantic=0.973
  Component Scores: Retrieval=1.000, Generation=0.945
  Overall Score: 0.961
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.345s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=1.634s
  Total Prediction Time: 1.979s
  Embedding Tokens:19.0
  LLM Input Tokens:1623.3
  LLM Output Tokens:72.3
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.496s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 19.0
  - LLM Input Tokens:
    - generation: 1597.3
  - LLM Output Tokens:
    - generation: 89.0
**retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 19.0
  - LLM Input Tokens:
    - generation: 1623.3
  - LLM Output Tokens:
    - generation: 72.3

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Retrieval: 0.669s
- Passage Filter: 0.000s
- Prompt Maker: 0.000s
- Generation: 3.685s
- Total Prediction Time: 4.354s

**Evaluation Times:**
  - Retrieval: 0.00s
  - Generation: 7.24s
  - Total Evaluation: 7.24s

**Pipeline Total:** 23.96s

---

*Report generated on 2025-07-30 12:24:10*
