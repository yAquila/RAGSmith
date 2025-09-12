# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 4075.78s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.736, mAP=0.710, nDCG@5=0.763, MRR=0.903
  Generation: LLM=0.795, Semantic=0.898
  Component Scores: Retrieval=0.778, Generation=0.846
  Overall Score: 0.812
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=25.377s, Passage Augment=1.989s, Passage Rerank=0.161s, Passage Filter=0.000s, Passage Compress=7.422s, Prompt Maker=0.000s, Generation=1.082s, Post-generation=2.983s
  Total Prediction Time: 39.014s
  Embedding Tokens: 2942.4
  LLM Tokens: 3523.8 in, 1300.7 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.743s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:hybrid_vector_keyword_graph_simply + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 40.5
    - passage_rerank: 2901.9
  - LLM Tokens:
    - generation:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 916.3 in, 96.3 out
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
    - passage_compress:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1901.1 in, 850.0 out
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
    - retrieval:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 0.0 in, 0.0 out
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out
    - post_generation:
      - keyword: 0.0 in, 0.0 out
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 706.4 in, 354.3 out
      - vector: 0.0 in, 0.0 out
      - graph: 0.0 in, 0.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 25.377s
- Passage Augment: 1.989s
- Passage Rerank: 0.161s
- Passage Filter: 0.000s
- Passage Compress: 7.422s
- Prompt Maker: 0.000s
- Generation: 1.082s
- Post-generation: 2.983s
- Total Prediction Time: 39.014s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 174.28s
  - Total Evaluation: 174.29s

**Pipeline Total:** 4075.78s

---

*Report generated on 2025-09-10 01:50:02*
