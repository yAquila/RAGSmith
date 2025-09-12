# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 282.28s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.000, mAP=0.000, nDCG@5=0.000, MRR=0.000
  Generation: LLM=0.628, Semantic=0.882
  Component Scores: Retrieval=0.000, Generation=0.755
  Overall Score: 0.377
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.049s, Passage Augment=0.000s, Passage Rerank=0.470s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=0.596s, Post-generation=0.000s
  Total Prediction Time: 1.115s
  Embedding Tokens: 20.2
  LLM Tokens: 1417.0 in, 1630.4 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.707s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 20.2
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 61.0 in, 72.4 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1355.9 in, 1558.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.049s
- Passage Augment: 0.000s
- Passage Rerank: 0.470s
- Passage Filter: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.596s
- Post-generation: 0.000s
- Total Prediction Time: 1.115s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 170.68s
  - Total Evaluation: 170.69s

**Pipeline Total:** 282.28s

---

*Report generated on 2025-09-05 14:52:16*
