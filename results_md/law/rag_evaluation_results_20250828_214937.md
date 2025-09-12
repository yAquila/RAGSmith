# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 2942.87s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.428, mAP=0.397, nDCG@5=0.438, MRR=0.532
  Generation: LLM=0.691, Semantic=0.890
  Component Scores: Retrieval=0.449, Generation=0.790
  Overall Score: 0.620
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=27.114s, Passage Augment=0.000s, Passage Rerank=0.030s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=0.600s, Post-generation=0.000s
  Total Prediction Time: 27.745s
  Embedding Tokens: 427.8
  LLM Tokens: 361.9 in, 58.7 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.683s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_rerank: 407.6
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 361.9 in, 58.7 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 27.114s
- Passage Augment: 0.000s
- Passage Rerank: 0.030s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.600s
- Post-generation: 0.000s
- Total Prediction Time: 27.745s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 168.29s
  - Total Evaluation: 168.30s

**Pipeline Total:** 2942.87s

---

*Report generated on 2025-08-28 21:49:37*
