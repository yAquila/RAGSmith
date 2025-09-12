# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 862.52s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.722, mAP=0.587, nDCG@5=0.665, MRR=0.737
  Generation: LLM=0.794, Semantic=0.897
  Component Scores: Retrieval=0.678, Generation=0.846
  Overall Score: 0.762
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.076s, Passage Augment=0.000s, Passage Rerank=0.586s, Passage Filter=0.000s, Passage Compress=5.288s, Prompt Maker=0.000s, Generation=0.981s, Post-generation=0.000s
  Total Prediction Time: 6.932s
  Embedding Tokens: 994.6
  LLM Tokens: 3397.8 in, 2273.6 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.692s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:keyword_bm25 + passage_augment:no_augment + passage_rerank:cellm_parallel_rerank + passage_filter:simple_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - passage_rerank: 994.6
  - LLM Tokens:
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 994.6 in, 1568.5 out
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1574.8 in, 618.3 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 828.3 in, 86.8 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.076s
- Passage Augment: 0.000s
- Passage Rerank: 0.586s
- Passage Filter: 0.000s
- Passage Compress: 5.288s
- Prompt Maker: 0.000s
- Generation: 0.981s
- Post-generation: 0.000s
- Total Prediction Time: 6.932s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 169.21s
  - Total Evaluation: 169.22s

**Pipeline Total:** 862.52s

---

*Report generated on 2025-08-20 20:55:13*
