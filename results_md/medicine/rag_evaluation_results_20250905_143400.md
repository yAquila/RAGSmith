# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 513.57s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_hype + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_hype + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_hype + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_hype + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_hype + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.000, mAP=0.000, nDCG@5=0.000, MRR=0.000
  Generation: LLM=0.628, Semantic=0.885
  Component Scores: Retrieval=0.000, Generation=0.757
  Overall Score: 0.378
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.069s, Passage Augment=0.000s, Passage Rerank=0.455s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=0.578s, Post-generation=2.317s
  Total Prediction Time: 3.419s
  Embedding Tokens: 20.2
  LLM Tokens: 1720.8 in, 1772.7 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.716s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_hype + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 20.2
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 61.0 in, 69.9 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1110.9 in, 1426.8 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 548.8 in, 276.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.069s
- Passage Augment: 0.000s
- Passage Rerank: 0.455s
- Passage Filter: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.578s
- Post-generation: 2.317s
- Total Prediction Time: 3.419s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 171.64s
  - Total Evaluation: 171.65s

**Pipeline Total:** 513.57s

---

*Report generated on 2025-09-05 14:34:00*
