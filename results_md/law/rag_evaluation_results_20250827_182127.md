# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 246.08s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.000, mAP=0.000, nDCG@5=0.000, MRR=0.000
  Generation: LLM=0.636, Semantic=0.885
  Component Scores: Retrieval=0.000, Generation=0.760
  Overall Score: 0.380
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.036s, Passage Augment=0.000s, Passage Rerank=0.000s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=0.577s, Post-generation=0.000s
  Total Prediction Time: 0.613s
  LLM Tokens: 61.0 in, 70.1 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.846s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 61.0 in, 70.1 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.036s
- Passage Augment: 0.000s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.577s
- Post-generation: 0.000s
- Total Prediction Time: 0.613s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 184.64s
  - Total Evaluation: 184.66s

**Pipeline Total:** 246.08s

---

*Report generated on 2025-08-27 18:21:27*
