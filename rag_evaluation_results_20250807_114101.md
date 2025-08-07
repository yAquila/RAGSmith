# RAG EVALUATION RESULTS

**Dataset:** 3 test cases  
**Success rate:** 3/3 (100.0%)  
**Total runtime:** 22.52s

**Model combinations tested:** 1
  • pre_embedding:contextual_chunk_headers + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:contextual_chunk_headers + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1  
**Generation:** pre_embedding:contextual_chunk_headers + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1  
**Overall:** pre_embedding:contextual_chunk_headers + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:contextual_chunk_headers + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@10=1.000
  Generation: LLM=0.933, Semantic=0.921
  Component Scores: Retrieval=1.000, Generation=0.927
  Overall Score: 0.949
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=1.160s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=5.681s
  Total Prediction Time: 6.842s
  Embedding Tokens:12.3
  LLM Input Tokens:1753.3
  LLM Output Tokens:204.3
  Avg Evaluation Times: Retrieval=0.001s, Generation=0.659s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:contextual_chunk_headers + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 12.3
  - LLM Input Tokens:
    - generation: 1753.3
  - LLM Output Tokens:
    - generation: 204.3

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Retrieval: 1.160s
- Passage Filter: 0.000s
- Prompt Maker: 0.000s
- Generation: 5.681s
- Total Prediction Time: 6.842s

**Evaluation Times:**
  - Retrieval: 0.00s
  - Generation: 1.98s
  - Total Evaluation: 1.98s

**Pipeline Total:** 22.52s

---

*Report generated on 2025-08-07 11:41:01*
