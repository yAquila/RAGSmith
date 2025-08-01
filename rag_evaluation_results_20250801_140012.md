# RAG EVALUATION RESULTS

**Dataset:** 3 test cases  
**Success rate:** 6/6 (100.0%)  
**Total runtime:** 40.15s

**Model combinations tested:** 2
  • pre_embedding:no_pre_embedding + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • pre_embedding:hype + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:no_pre_embedding + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1  
**Generation:** pre_embedding:hype + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1  
**Overall:** pre_embedding:hype + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:no_pre_embedding + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@10=1.000
  Generation: LLM=0.933, Semantic=0.900
  Component Scores: Retrieval=1.000, Generation=0.917
  Overall Score: 0.942
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=1.303s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=6.777s
  Total Prediction Time: 8.080s
  Embedding Tokens:12.3
  LLM Input Tokens:1409.3
  LLM Output Tokens:277.3
  Avg Evaluation Times: Retrieval=0.001s, Generation=0.641s

**pre_embedding:hype + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@10=1.000
  Generation: LLM=0.950, Semantic=0.902
  Component Scores: Retrieval=1.000, Generation=0.926
  Overall Score: 0.948
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.219s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=3.829s
  Total Prediction Time: 4.049s
  Embedding Tokens:12.3
  LLM Input Tokens:1110.0
  LLM Output Tokens:216.0
  Avg Evaluation Times: Retrieval=0.001s, Generation=0.600s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:no_pre_embedding + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 12.3
  - LLM Input Tokens:
    - generation: 1409.3
  - LLM Output Tokens:
    - generation: 277.3
**pre_embedding:hype + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 12.3
  - LLM Input Tokens:
    - generation: 1110.0
  - LLM Output Tokens:
    - generation: 216.0

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Retrieval: 1.522s
- Passage Filter: 0.000s
- Prompt Maker: 0.000s
- Generation: 10.606s
- Total Prediction Time: 12.129s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 3.72s
  - Total Evaluation: 3.73s

**Pipeline Total:** 40.15s

---

*Report generated on 2025-08-01 14:00:12*
