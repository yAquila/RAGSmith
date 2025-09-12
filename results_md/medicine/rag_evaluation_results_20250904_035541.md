# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 260.02s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.000, mAP=0.000, nDCG@5=0.000, MRR=0.000
  Generation: LLM=0.614, Semantic=0.874
  Component Scores: Retrieval=0.000, Generation=0.744
  Overall Score: 0.372
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.256s, Retrieval=0.039s, Passage Augment=0.000s, Passage Rerank=0.000s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=0.609s, Post-generation=0.000s
  Total Prediction Time: 0.905s
  LLM Tokens: 188.3 in, 97.0 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.694s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 130.1 in, 22.1 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 58.2 in, 74.8 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.256s
- Retrieval: 0.039s
- Passage Augment: 0.000s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.609s
- Post-generation: 0.000s
- Total Prediction Time: 0.905s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 169.45s
  - Total Evaluation: 169.46s

**Pipeline Total:** 260.02s

---

*Report generated on 2025-09-04 03:55:41*
