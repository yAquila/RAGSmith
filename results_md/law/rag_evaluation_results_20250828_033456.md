# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 3777.27s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.447, mAP=0.407, nDCG@5=0.442, MRR=0.506
  Generation: LLM=0.475, Semantic=0.512
  Component Scores: Retrieval=0.450, Generation=0.494
  Overall Score: 0.472
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=18.407s, Passage Augment=0.002s, Passage Rerank=0.960s, Passage Filter=0.000s, Passage Compress=1.862s, Prompt Maker=0.000s, Generation=0.505s, Post-generation=0.000s
  Total Prediction Time: 21.736s
  Embedding Tokens: 654.1
  LLM Tokens: 5284.1 in, 1470.4 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.925s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 40.5
    - passage_compress: 613.6
  - LLM Tokens:
    - retrieval:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
      - keyword: 0.0 in, 0.0 out
    - passage_compress:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1709.3 in, 565.3 out
      - keyword: 0.0 in, 0.0 out
    - generation:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 669.7 in, 85.2 out
      - keyword: 0.0 in, 0.0 out
    - passage_rerank:
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2905.1 in, 819.8 out
      - keyword: 0.0 in, 0.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 18.407s
- Passage Augment: 0.002s
- Passage Rerank: 0.960s
- Passage Filter: 0.000s
- Passage Compress: 1.862s
- Prompt Maker: 0.000s
- Generation: 0.505s
- Post-generation: 0.000s
- Total Prediction Time: 21.736s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 92.54s
  - Total Evaluation: 92.55s

**Pipeline Total:** 3777.27s

---

*Report generated on 2025-08-28 03:34:56*
