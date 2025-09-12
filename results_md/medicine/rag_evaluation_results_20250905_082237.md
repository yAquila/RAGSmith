# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 490.39s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Generation:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising  
**Overall:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  Retrieval: R@5=0.000, mAP=0.000, nDCG@5=0.000, MRR=0.000
  Generation: LLM=0.635, Semantic=0.885
  Component Scores: Retrieval=0.000, Generation=0.760
  Overall Score: 0.380
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.134s, Passage Augment=0.000s, Passage Rerank=0.413s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=0.603s, Post-generation=2.056s
  Total Prediction Time: 3.205s
  Embedding Tokens: 20.2
  LLM Tokens: 1698.8 in, 1846.7 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.698s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:reflection_revising:**
  - Embedding Tokens:
    - retrieval: 20.2
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 61.0 in, 73.3 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1124.8 in, 1529.2 out
    - post_generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 513.0 in, 244.1 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.134s
- Passage Augment: 0.000s
- Passage Rerank: 0.413s
- Passage Filter: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.603s
- Post-generation: 2.056s
- Total Prediction Time: 3.205s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 169.80s
  - Total Evaluation: 169.80s

**Pipeline Total:** 490.39s

---

*Report generated on 2025-09-05 08:22:37*
