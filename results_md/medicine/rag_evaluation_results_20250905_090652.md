# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 589.61s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_cc + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_cc + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_cc + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_cc + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_cc + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.920, mAP=0.804, nDCG@5=0.861, MRR=0.898
  Generation: LLM=0.863, Semantic=0.922
  Component Scores: Retrieval=0.871, Generation=0.893
  Overall Score: 0.882
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.079s, Passage Augment=1.860s, Passage Rerank=1.041s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.318s, Post-generation=0.000s
  Total Prediction Time: 4.297s
  Embedding Tokens: 1935.2
  LLM Tokens: 3624.0 in, 1048.1 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.598s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_cc + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_rerank: 1915.0
  - LLM Tokens:
    - retrieval:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
      - keyword: 0.0 in, 0.0 out
    - generation:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1709.0 in, 86.5 out
      - keyword: 0.0 in, 0.0 out
    - passage_rerank:
      - vector: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1915.0 in, 961.6 out
      - keyword: 0.0 in, 0.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.079s
- Passage Augment: 1.860s
- Passage Rerank: 1.041s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.318s
- Post-generation: 0.000s
- Total Prediction Time: 4.297s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 159.77s
  - Total Evaluation: 159.78s

**Pipeline Total:** 589.61s

---

*Report generated on 2025-09-05 09:06:52*
