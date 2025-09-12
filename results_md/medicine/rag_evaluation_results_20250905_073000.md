# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 283.19s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.000, mAP=0.000, nDCG@5=0.000, MRR=0.000
  Generation: LLM=0.607, Semantic=0.880
  Component Scores: Retrieval=0.000, Generation=0.743
  Overall Score: 0.372
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.051s, Passage Augment=0.000s, Passage Rerank=0.470s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=0.564s, Post-generation=0.000s
  Total Prediction Time: 1.085s
  Embedding Tokens: 20.2
  LLM Tokens: 1417.0 in, 1618.7 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.746s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 20.2
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 61.0 in, 68.3 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1355.9 in, 1550.3 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.051s
- Passage Augment: 0.000s
- Passage Rerank: 0.470s
- Passage Filter: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.564s
- Post-generation: 0.000s
- Total Prediction Time: 1.085s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 174.62s
  - Total Evaluation: 174.63s

**Pipeline Total:** 283.19s

---

*Report generated on 2025-09-05 07:30:00*
