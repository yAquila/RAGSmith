# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 8392.69s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_clarification + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_clarification + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_clarification + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_clarification + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_clarification + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@10=0.000, mAP=0.000, nDCG@10=0.000, MRR=0.000
  Generation: LLM=0.009, Semantic=0.014
  Component Scores: Retrieval=0.000, Generation=0.012
  Overall Score: 0.006
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.006s, Retrieval=1.691s, Prompt Maker=0.000s, Generation=0.011s, Post-generation=0.000s
  Total Prediction Time: 1.708s
  Embedding Tokens: 19.5
  LLM Tokens: 574.0 in, 627.0 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.184s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:simple_query_refinement_clarification + retrieval:graph_rag + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 19.5
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 135.5 in, 28.0 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 64.0 in, 63.0 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 374.5 in, 536.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.006s
- Retrieval: 1.691s
- Prompt Maker: 0.000s
- Generation: 0.011s
- Post-generation: 0.000s
- Total Prediction Time: 1.708s

**Evaluation Times:**
  - Retrieval: 0.00s
  - Generation: 18.39s
  - Total Evaluation: 18.39s

**Pipeline Total:** 8392.69s

---

*Report generated on 2025-08-20 00:39:40*
