# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 2075.49s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.881, mAP=0.818, nDCG@5=0.851, MRR=0.919
  Generation: LLM=0.768, Semantic=0.894
  Component Scores: Retrieval=0.867, Generation=0.831
  Overall Score: 0.849
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.056s, Passage Augment=2.780s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=8.423s, Prompt Maker=0.000s, Generation=1.184s, Post-generation=6.411s
  Total Prediction Time: 18.855s
  Embedding Tokens: 20.2
  LLM Tokens: 3915.9 in, 1838.6 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.899s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 20.2
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1037.6 in, 102.8 out
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2135.1 in, 970.5 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 743.2 in, 765.3 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.056s
- Passage Augment: 2.780s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 8.423s
- Prompt Maker: 0.000s
- Generation: 1.184s
- Post-generation: 6.411s
- Total Prediction Time: 18.855s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 189.94s
  - Total Evaluation: 189.95s

**Pipeline Total:** 2075.49s

---

*Report generated on 2025-09-10 05:18:42*
