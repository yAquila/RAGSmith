# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1106.72s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.888, mAP=0.691, nDCG@5=0.769, MRR=0.781
  Generation: LLM=0.838, Semantic=0.905
  Component Scores: Retrieval=0.782, Generation=0.871
  Overall Score: 0.827
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=1.451s, Retrieval=0.111s, Passage Augment=0.000s, Passage Rerank=0.491s, Passage Filter=0.000s, Passage Compress=6.603s, Prompt Maker=0.000s, Generation=0.735s, Post-generation=0.000s
  Total Prediction Time: 9.391s
  Embedding Tokens: 10999.6
  LLM Tokens: 1830.5 in, 877.2 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.675s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 46.7
    - passage_compress: 347.4
    - query_expansion: 20.2
    - passage_rerank: 10585.4
  - LLM Tokens:
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1404.2 in, 802.4 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 426.3 in, 74.8 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 1.451s
- Retrieval: 0.111s
- Passage Augment: 0.000s
- Passage Rerank: 0.491s
- Passage Filter: 0.000s
- Passage Compress: 6.603s
- Prompt Maker: 0.000s
- Generation: 0.735s
- Post-generation: 0.000s
- Total Prediction Time: 9.391s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 167.48s
  - Total Evaluation: 167.49s

**Pipeline Total:** 1106.72s

---

*Report generated on 2025-09-04 17:54:46*
