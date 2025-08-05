# RAG EVALUATION RESULTS

**Dataset:** 1 test cases  
**Success rate:** 2/2 (100.0%)  
**Total runtime:** 35.21s

**Model combinations tested:** 2
  • retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • retrieval:complete_hybrid_vector_keyword_graph + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1  
**Generation:** retrieval:complete_hybrid_vector_keyword_graph + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1  
**Overall:** retrieval:complete_hybrid_vector_keyword_graph + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1

## 📊 DETAILED METRICS BY COMBINATION:

**retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@10=1.000
  Generation: LLM=0.950, Semantic=0.978
  Component Scores: Retrieval=1.000, Generation=0.964
  Overall Score: 0.975
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=3.237s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=6.520s
  Total Prediction Time: 9.757s
  Embedding Tokens:16.0
  LLM Input Tokens:1432.0
  LLM Output Tokens:41.0
  Avg Evaluation Times: Retrieval=0.002s, Generation=0.520s

**retrieval:complete_hybrid_vector_keyword_graph + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@10=1.000
  Generation: LLM=0.950, Semantic=0.993
  Component Scores: Retrieval=1.000, Generation=0.972
  Overall Score: 0.980
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=21.317s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=1.009s
  Total Prediction Time: 22.327s
  Embedding Tokens:48.0
  LLM Input Tokens:962.0
  LLM Output Tokens:35.0
  Avg Evaluation Times: Retrieval=0.001s, Generation=0.459s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 16.0
  - LLM Input Tokens:
    - generation: 1432.0
  - LLM Output Tokens:
    - generation: 41.0
**retrieval:complete_hybrid_vector_keyword_graph + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 48.0
  - LLM Input Tokens:
    - generation: 962.0
  - LLM Output Tokens:
    - generation: 35.0

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Retrieval: 24.554s
- Passage Filter: 0.001s
- Prompt Maker: 0.000s
- Generation: 7.529s
- Total Prediction Time: 32.084s

**Evaluation Times:**
  - Retrieval: 0.00s
  - Generation: 0.98s
  - Total Evaluation: 0.98s

**Pipeline Total:** 35.21s

---

*Report generated on 2025-08-05 06:36:29*
