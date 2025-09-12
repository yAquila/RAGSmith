# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 843.01s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.787, mAP=0.742, nDCG@5=0.785, MRR=0.873
  Generation: LLM=0.836, Semantic=0.917
  Component Scores: Retrieval=0.797, Generation=0.877
  Overall Score: 0.837
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=1.449s, Retrieval=0.109s, Passage Augment=0.000s, Passage Rerank=4.451s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=0.867s, Post-generation=0.000s
  Total Prediction Time: 6.876s
  Embedding Tokens: 10672.4
  LLM Tokens: 11306.9 in, 1102.6 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.553s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:vector_mxbai + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 46.7
    - query_expansion: 20.2
    - passage_rerank: 10605.6
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 701.3 in, 78.2 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 10605.6 in, 1024.4 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 1.449s
- Retrieval: 0.109s
- Passage Augment: 0.000s
- Passage Rerank: 4.451s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.867s
- Post-generation: 0.000s
- Total Prediction Time: 6.876s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 155.30s
  - Total Evaluation: 155.31s

**Pipeline Total:** 843.01s

---

*Report generated on 2025-09-04 13:10:14*
