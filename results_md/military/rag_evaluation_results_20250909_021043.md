# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 265.50s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.000, mAP=0.000, nDCG@5=0.000, MRR=0.000
  Generation: LLM=0.491, Semantic=0.887
  Component Scores: Retrieval=0.000, Generation=0.689
  Overall Score: 0.344
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.036s, Passage Augment=0.000s, Passage Rerank=0.000s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=0.726s, Post-generation=0.000s
  Total Prediction Time: 0.762s
  LLM Tokens: 62.4 in, 90.3 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.892s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 62.4 in, 90.3 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.036s
- Passage Augment: 0.000s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.726s
- Post-generation: 0.000s
- Total Prediction Time: 0.762s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 189.23s
  - Total Evaluation: 189.24s

**Pipeline Total:** 265.50s

---

*Report generated on 2025-09-09 02:10:43*
