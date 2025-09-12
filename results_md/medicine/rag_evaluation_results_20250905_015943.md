# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 2598.81s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_graph_simply + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_graph_simply + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_graph_simply + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_graph_simply + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_graph_simply + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.826, mAP=0.695, nDCG@5=0.749, MRR=0.793
  Generation: LLM=0.844, Semantic=0.918
  Component Scores: Retrieval=0.766, Generation=0.881
  Overall Score: 0.824
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=21.172s, Passage Augment=2.023s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.271s, Post-generation=0.000s
  Total Prediction Time: 24.467s
  Embedding Tokens: 40.4
  LLM Tokens: 1634.5 in, 83.7 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.521s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_graph_simply + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 40.4
  - LLM Tokens:
    - retrieval:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
    - generation:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1634.5 in, 83.7 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 21.172s
- Passage Augment: 2.023s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.271s
- Post-generation: 0.000s
- Total Prediction Time: 24.467s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 152.07s
  - Total Evaluation: 152.08s

**Pipeline Total:** 2598.81s

---

*Report generated on 2025-09-05 01:59:43*
