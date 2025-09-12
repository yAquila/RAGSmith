# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1043.27s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.848, mAP=0.731, nDCG@5=0.794, MRR=0.845
  Generation: LLM=0.856, Semantic=0.904
  Component Scores: Retrieval=0.804, Generation=0.880
  Overall Score: 0.842
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.032s, Passage Augment=0.003s, Passage Rerank=0.057s, Passage Filter=0.000s, Passage Compress=7.607s, Prompt Maker=0.000s, Generation=1.152s, Post-generation=0.000s
  Total Prediction Time: 8.850s
  Embedding Tokens: 1298.8
  LLM Tokens: 3504.6 in, 982.2 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.582s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - passage_rerank: 1298.8
  - LLM Tokens:
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2099.6 in, 901.3 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1405.0 in, 80.9 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.032s
- Passage Augment: 0.003s
- Passage Rerank: 0.057s
- Passage Filter: 0.000s
- Passage Compress: 7.607s
- Prompt Maker: 0.000s
- Generation: 1.152s
- Post-generation: 0.000s
- Total Prediction Time: 8.850s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 158.16s
  - Total Evaluation: 158.17s

**Pipeline Total:** 1043.27s

---

*Report generated on 2025-09-04 16:14:58*
