# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 274.22s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_hype + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_hype + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_hype + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_hype + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_hype + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.000, mAP=0.000, nDCG@5=0.000, MRR=0.000
  Generation: LLM=0.649, Semantic=0.875
  Component Scores: Retrieval=0.000, Generation=0.762
  Overall Score: 0.381
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.258s, Retrieval=0.021s, Passage Augment=0.000s, Passage Rerank=0.000s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=0.622s, Post-generation=0.000s
  Total Prediction Time: 0.901s
  LLM Tokens: 188.5 in, 98.9 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.838s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_hype + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 130.1 in, 22.3 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 58.4 in, 76.6 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.258s
- Retrieval: 0.021s
- Passage Augment: 0.000s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.622s
- Post-generation: 0.000s
- Total Prediction Time: 0.901s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 183.81s
  - Total Evaluation: 183.82s

**Pipeline Total:** 274.22s

---

*Report generated on 2025-08-27 17:48:35*
