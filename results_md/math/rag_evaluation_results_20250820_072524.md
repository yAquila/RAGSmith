# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1198.12s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_hype + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_hype + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_hype + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_hype + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_hype + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.649, mAP=0.524, nDCG@5=0.592, MRR=0.697
  Generation: LLM=0.763, Semantic=0.880
  Component Scores: Retrieval=0.616, Generation=0.821
  Overall Score: 0.719
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.269s, Retrieval=0.021s, Passage Augment=0.005s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=8.931s, Prompt Maker=0.000s, Generation=1.057s, Post-generation=0.000s
  Total Prediction Time: 10.283s
  Embedding Tokens: 685.5
  LLM Tokens: 4770.9 in, 1458.7 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.697s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_hype + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - passage_compress: 685.5
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 130.8 in, 23.0 out
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 3789.3 in, 1340.8 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 850.7 in, 94.9 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.269s
- Retrieval: 0.021s
- Passage Augment: 0.005s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 8.931s
- Prompt Maker: 0.000s
- Generation: 1.057s
- Post-generation: 0.000s
- Total Prediction Time: 10.283s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 169.70s
  - Total Evaluation: 169.71s

**Pipeline Total:** 1198.12s

---

*Report generated on 2025-08-20 07:25:24*
