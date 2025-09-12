# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 690.58s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:hyde_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:hyde_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:hyde_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:hyde_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:hyde_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.857, mAP=0.805, nDCG@5=0.851, MRR=0.932
  Generation: LLM=0.855, Semantic=0.914
  Component Scores: Retrieval=0.861, Generation=0.884
  Overall Score: 0.873
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=4.017s, Retrieval=0.074s, Passage Augment=0.000s, Passage Rerank=0.422s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=0.875s, Post-generation=0.000s
  Total Prediction Time: 5.388s
  Embedding Tokens: 9130.7
  LLM Tokens: 848.9 in, 604.9 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.517s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:hyde_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 149.6
    - passage_rerank: 8981.1
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 120.0 in, 526.4 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 728.9 in, 78.5 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 4.017s
- Retrieval: 0.074s
- Passage Augment: 0.000s
- Passage Rerank: 0.422s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.875s
- Post-generation: 0.000s
- Total Prediction Time: 5.388s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 151.69s
  - Total Evaluation: 151.70s

**Pipeline Total:** 690.58s

---

*Report generated on 2025-09-05 12:34:18*
