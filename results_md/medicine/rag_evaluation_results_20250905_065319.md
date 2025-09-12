# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 865.80s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:step_back_prompting_cc + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:step_back_prompting_cc + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:step_back_prompting_cc + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:step_back_prompting_cc + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:step_back_prompting_cc + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.730, mAP=0.563, nDCG@5=0.640, MRR=0.689
  Generation: LLM=0.812, Semantic=0.908
  Component Scores: Retrieval=0.656, Generation=0.860
  Overall Score: 0.758
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.483s, Retrieval=0.037s, Passage Augment=2.330s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=3.317s, Prompt Maker=0.000s, Generation=0.950s, Post-generation=0.000s
  Total Prediction Time: 7.117s
  Embedding Tokens: 875.5
  LLM Tokens: 3341.0 in, 699.9 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.540s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:step_back_prompting_cc + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - passage_compress: 875.5
  - LLM Tokens:
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2212.1 in, 571.3 out
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 210.1 in, 49.5 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 918.8 in, 79.1 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.483s
- Retrieval: 0.037s
- Passage Augment: 2.330s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 3.317s
- Prompt Maker: 0.000s
- Generation: 0.950s
- Post-generation: 0.000s
- Total Prediction Time: 7.117s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 153.99s
  - Total Evaluation: 153.99s

**Pipeline Total:** 865.80s

---

*Report generated on 2025-09-05 06:53:19*
