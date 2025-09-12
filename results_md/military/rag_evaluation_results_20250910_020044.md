# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 642.01s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.777, mAP=0.709, nDCG@5=0.767, MRR=0.871
  Generation: LLM=0.841, Semantic=0.910
  Component Scores: Retrieval=0.781, Generation=0.875
  Overall Score: 0.828
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.043s, Passage Augment=0.004s, Passage Rerank=0.060s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.395s, Post-generation=3.226s
  Total Prediction Time: 4.728s
  Embedding Tokens: 1315.7
  LLM Tokens: 2425.2 in, 479.4 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.692s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:prev_next_augmenter + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_rerank: 1315.7
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1641.6 in, 97.3 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 783.7 in, 382.1 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.043s
- Passage Augment: 0.004s
- Passage Rerank: 0.060s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.395s
- Post-generation: 3.226s
- Total Prediction Time: 4.728s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 169.15s
  - Total Evaluation: 169.16s

**Pipeline Total:** 642.01s

---

*Report generated on 2025-09-10 02:00:44*
