# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1478.43s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_borda + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_borda + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_borda + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_borda + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_borda + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.614, mAP=0.485, nDCG@5=0.556, MRR=0.622
  Generation: LLM=0.779, Semantic=0.891
  Component Scores: Retrieval=0.569, Generation=0.835
  Overall Score: 0.702
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.709s, Retrieval=0.033s, Passage Augment=2.666s, Passage Rerank=3.436s, Passage Filter=0.000s, Passage Compress=3.596s, Prompt Maker=0.000s, Generation=1.080s, Post-generation=1.649s
  Total Prediction Time: 13.169s
  Embedding Tokens: 865.1
  LLM Tokens: 17718.4 in, 2575.0 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.614s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_hype + query_expansion:query_expansion_simple_multi_query_borda + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_compress: 865.1
  - LLM Tokens:
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 13431.6 in, 1636.8 out
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.8 in, 84.0 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1013.7 in, 89.5 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 458.3 in, 191.1 out
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2696.9 in, 573.7 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.709s
- Retrieval: 0.033s
- Passage Augment: 2.666s
- Passage Rerank: 3.436s
- Passage Filter: 0.000s
- Passage Compress: 3.596s
- Prompt Maker: 0.000s
- Generation: 1.080s
- Post-generation: 1.649s
- Total Prediction Time: 13.169s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 161.40s
  - Total Evaluation: 161.41s

**Pipeline Total:** 1478.43s

---

*Report generated on 2025-08-20 21:19:52*
