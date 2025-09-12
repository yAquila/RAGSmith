# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 377.45s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.888, mAP=0.828, nDCG@5=0.875, MRR=0.948
  Generation: LLM=0.855, Semantic=0.916
  Component Scores: Retrieval=0.885, Generation=0.885
  Overall Score: 0.885
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.686s, Retrieval=0.149s, Passage Augment=0.000s, Passage Rerank=0.436s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=0.940s, Post-generation=0.000s
  Total Prediction Time: 2.211s
  Embedding Tokens: 9368.8
  LLM Tokens: 982.5 in, 161.7 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.563s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_simple_multi_query_borda + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_rerank: 9348.6
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.1 in, 80.9 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 865.4 in, 80.8 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.686s
- Retrieval: 0.149s
- Passage Augment: 0.000s
- Passage Rerank: 0.436s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.940s
- Post-generation: 0.000s
- Total Prediction Time: 2.211s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 156.26s
  - Total Evaluation: 156.27s

**Pipeline Total:** 377.45s

---

*Report generated on 2025-08-28 18:56:46*
