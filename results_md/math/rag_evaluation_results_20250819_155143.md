# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 11016.75s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.659, mAP=0.542, nDCG@5=0.588, MRR=0.649
  Generation: LLM=0.770, Semantic=0.889
  Component Scores: Retrieval=0.609, Generation=0.830
  Overall Score: 0.719
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=1.047s, Retrieval=91.490s, Passage Augment=0.000s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=14.916s, Prompt Maker=0.000s, Generation=0.935s, Post-generation=0.000s
  Total Prediction Time: 108.388s
  Embedding Tokens: 518.7
  LLM Tokens: 3791.1 in, 1877.0 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.777s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:graph_as_qe_cc + retrieval:hybrid_vector_graph_simply + passage_augment:no_augment + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - query_expansion: 20.0
    - retrieval: 59.1
    - passage_compress: 439.5
  - LLM Tokens:
    - retrieval:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
    - passage_compress:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 3217.1 in, 1784.7 out
    - generation:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 574.1 in, 92.3 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 1.047s
- Retrieval: 91.490s
- Passage Augment: 0.000s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 14.916s
- Prompt Maker: 0.000s
- Generation: 0.935s
- Post-generation: 0.000s
- Total Prediction Time: 108.388s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 177.73s
  - Total Evaluation: 177.74s

**Pipeline Total:** 11016.75s

---

*Report generated on 2025-08-19 15:51:43*
