# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 3312.85s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_clarification + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_clarification + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_clarification + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_clarification + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_clarification + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@10=0.000, mAP=0.000, nDCG@10=0.000, MRR=0.000
  Generation: LLM=0.015, Semantic=0.026
  Component Scores: Retrieval=0.000, Generation=0.021
  Overall Score: 0.010
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.009s, Retrieval=0.947s, Prompt Maker=0.000s, Generation=0.017s, Post-generation=0.000s
  Total Prediction Time: 0.973s
  Embedding Tokens: 22.7
  LLM Tokens: 442.3 in, 482.7 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.126s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_clarification + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 22.7
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 135.3 in, 29.0 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 65.0 in, 69.0 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 242.0 in, 384.7 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.009s
- Retrieval: 0.947s
- Prompt Maker: 0.000s
- Generation: 0.017s
- Post-generation: 0.000s
- Total Prediction Time: 0.973s

**Evaluation Times:**
  - Retrieval: 0.00s
  - Generation: 12.62s
  - Total Evaluation: 12.62s

**Pipeline Total:** 3312.85s

---

*Report generated on 2025-08-27 17:44:01*
