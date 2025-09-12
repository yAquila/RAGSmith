# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 2484.35s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_clarification + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_clarification + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_clarification + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_clarification + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_clarification + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@10=0.000, mAP=0.000, nDCG@10=0.000, MRR=0.000
  Generation: LLM=0.029, Semantic=0.061
  Component Scores: Retrieval=0.000, Generation=0.045
  Overall Score: 0.023
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.024s, Retrieval=1.627s, Prompt Maker=0.000s, Generation=0.035s, Post-generation=0.000s
  Total Prediction Time: 1.685s
  Embedding Tokens: 23.4
  LLM Tokens: 550.6 in, 585.3 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.203s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_clarification + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 23.4
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 68.4 in, 57.1 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 345.9 in, 495.7 out
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 136.3 in, 32.4 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.024s
- Retrieval: 1.627s
- Prompt Maker: 0.000s
- Generation: 0.035s
- Post-generation: 0.000s
- Total Prediction Time: 1.685s

**Evaluation Times:**
  - Retrieval: 0.00s
  - Generation: 20.31s
  - Total Evaluation: 20.31s

**Pipeline Total:** 2484.35s

---

*Report generated on 2025-09-09 01:23:35*
