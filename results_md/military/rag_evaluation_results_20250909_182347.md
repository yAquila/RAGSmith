# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1024.29s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:rag_fusion + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:rag_fusion + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:rag_fusion + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:rag_fusion + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:rag_fusion + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.515, mAP=0.515, nDCG@5=0.588, MRR=0.860
  Generation: LLM=0.815, Semantic=0.907
  Component Scores: Retrieval=0.620, Generation=0.861
  Overall Score: 0.740
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.732s, Retrieval=0.150s, Passage Augment=0.001s, Passage Rerank=4.062s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=0.893s, Post-generation=2.748s
  Total Prediction Time: 8.586s
  Embedding Tokens: 9664.7
  LLM Tokens: 10500.0 in, 1533.6 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.656s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:rag_fusion + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - passage_compress: 484.9
    - retrieval: 20.2
    - passage_rerank: 9159.6
  - LLM Tokens:
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 653.9 in, 325.6 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 9159.6 in, 1034.2 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 568.0 in, 86.5 out
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 118.4 in, 87.2 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.732s
- Retrieval: 0.150s
- Passage Augment: 0.001s
- Passage Rerank: 4.062s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.893s
- Post-generation: 2.748s
- Total Prediction Time: 8.586s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 165.58s
  - Total Evaluation: 165.59s

**Pipeline Total:** 1024.29s

---

*Report generated on 2025-09-09 18:23:47*
