# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 153.68s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@10=0.000, mAP=0.000, nDCG@10=0.000, MRR=0.000
  Generation: LLM=0.000, Semantic=0.000
  Component Scores: Retrieval=0.000, Generation=0.000
  Overall Score: 0.000
  Success Rate: 100.0%
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.000s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Total Prediction Time: 0.000s

**Evaluation Times:**
  - Retrieval: 0.00s
  - Generation: 0.00s
  - Total Evaluation: 0.00s

**Pipeline Total:** 153.68s

---

*Report generated on 2025-09-05 15:54:49*
