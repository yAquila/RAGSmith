# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 775.57s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:step_back_prompting_cc + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:step_back_prompting_cc + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:step_back_prompting_cc + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:step_back_prompting_cc + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:step_back_prompting_cc + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.849, mAP=0.806, nDCG@5=0.851, MRR=0.938
  Generation: LLM=0.842, Semantic=0.918
  Component Scores: Retrieval=0.861, Generation=0.880
  Overall Score: 0.870
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.483s, Retrieval=0.158s, Passage Augment=1.692s, Passage Rerank=0.525s, Passage Filter=0.000s, Passage Compress=2.407s, Prompt Maker=0.000s, Generation=0.974s, Post-generation=0.000s
  Total Prediction Time: 6.239s
  Embedding Tokens: 12316.0
  LLM Tokens: 3323.0 in, 654.4 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.515s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:step_back_prompting_cc + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_compress: 953.4
    - passage_rerank: 11342.4
  - LLM Tokens:
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2132.6 in, 525.2 out
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 210.1 in, 49.7 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 980.3 in, 79.5 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.483s
- Retrieval: 0.158s
- Passage Augment: 1.692s
- Passage Rerank: 0.525s
- Passage Filter: 0.000s
- Passage Compress: 2.407s
- Prompt Maker: 0.000s
- Generation: 0.974s
- Post-generation: 0.000s
- Total Prediction Time: 6.239s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 151.53s
  - Total Evaluation: 151.54s

**Pipeline Total:** 775.57s

---

*Report generated on 2025-09-05 04:57:14*
