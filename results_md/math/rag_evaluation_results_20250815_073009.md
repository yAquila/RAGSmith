# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 956.16s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.829, mAP=0.657, nDCG@5=0.741, MRR=0.783
  Generation: LLM=0.818, Semantic=0.897
  Component Scores: Retrieval=0.753, Generation=0.857
  Overall Score: 0.805
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.034s, Passage Augment=2.204s, Passage Rerank=0.069s, Passage Filter=0.000s, Passage Compress=3.073s, Prompt Maker=0.000s, Generation=1.122s, Post-generation=1.414s
  Total Prediction Time: 7.916s
  Embedding Tokens: 2242.5
  LLM Tokens: 4088.7 in, 802.3 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.645s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_rerank: 1329.3
    - passage_compress: 913.2
  - LLM Tokens:
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2635.2 in, 544.7 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 418.9 in, 163.3 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1034.5 in, 94.4 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.034s
- Passage Augment: 2.204s
- Passage Rerank: 0.069s
- Passage Filter: 0.000s
- Passage Compress: 3.073s
- Prompt Maker: 0.000s
- Generation: 1.122s
- Post-generation: 1.414s
- Total Prediction Time: 7.916s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 164.49s
  - Total Evaluation: 164.50s

**Pipeline Total:** 956.16s

---

*Report generated on 2025-08-15 07:30:09*
