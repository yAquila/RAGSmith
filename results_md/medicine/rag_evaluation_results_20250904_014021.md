# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 587.66s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:rag_fusion + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:rag_fusion + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:rag_fusion + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:rag_fusion + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:rag_fusion + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.469, mAP=0.469, nDCG@5=0.534, MRR=0.770
  Generation: LLM=0.784, Semantic=0.897
  Component Scores: Retrieval=0.561, Generation=0.841
  Overall Score: 0.701
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.689s, Retrieval=0.144s, Passage Augment=0.000s, Passage Rerank=0.435s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=0.555s, Post-generation=2.317s
  Total Prediction Time: 4.140s
  Embedding Tokens: 9412.1
  LLM Tokens: 895.8 in, 417.5 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.735s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:rag_fusion + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_rerank: 9392.0
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.1 in, 81.7 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 227.2 in, 59.4 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 551.5 in, 276.4 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.689s
- Retrieval: 0.144s
- Passage Augment: 0.000s
- Passage Rerank: 0.435s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.555s
- Post-generation: 2.317s
- Total Prediction Time: 4.140s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 173.52s
  - Total Evaluation: 173.53s

**Pipeline Total:** 587.66s

---

*Report generated on 2025-09-04 01:40:21*
