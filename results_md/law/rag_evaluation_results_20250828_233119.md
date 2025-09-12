# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 3467.56s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.821, mAP=0.781, nDCG@5=0.831, MRR=0.943
  Generation: LLM=0.835, Semantic=0.912
  Component Scores: Retrieval=0.844, Generation=0.874
  Overall Score: 0.859
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.679s, Retrieval=30.845s, Passage Augment=0.000s, Passage Rerank=0.765s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=0.827s, Post-generation=0.000s
  Total Prediction Time: 33.115s
  Embedding Tokens: 13202.1
  LLM Tokens: 784.4 in, 154.5 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.559s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 40.4
    - passage_rerank: 13161.7
  - LLM Tokens:
    - retrieval:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
    - query_expansion:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.1 in, 80.0 out
    - generation:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 667.3 in, 74.5 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.679s
- Retrieval: 30.845s
- Passage Augment: 0.000s
- Passage Rerank: 0.765s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.827s
- Post-generation: 0.000s
- Total Prediction Time: 33.115s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 155.89s
  - Total Evaluation: 155.90s

**Pipeline Total:** 3467.56s

---

*Report generated on 2025-08-28 23:31:19*
