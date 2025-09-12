# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 12513.01s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.201, mAP=0.171, nDCG@5=0.209, MRR=0.313
  Generation: LLM=0.680, Semantic=0.876
  Component Scores: Retrieval=0.223, Generation=0.778
  Overall Score: 0.501
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=4.117s, Retrieval=106.594s, Passage Augment=0.000s, Passage Rerank=11.519s, Passage Filter=0.000s, Passage Compress=0.272s, Prompt Maker=0.000s, Generation=0.584s, Post-generation=0.000s
  Total Prediction Time: 123.086s
  Embedding Tokens: 193.4
  LLM Tokens: 4101.5 in, 1343.4 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=2.042s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - passage_compress: 62.9
    - retrieval: 130.5
  - LLM Tokens:
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 3518.7 in, 616.2 out
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 330.9 in, 121.4 out
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 120.7 in, 539.3 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 131.2 in, 66.4 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 4.117s
- Retrieval: 106.594s
- Passage Augment: 0.000s
- Passage Rerank: 11.519s
- Passage Filter: 0.000s
- Passage Compress: 0.272s
- Prompt Maker: 0.000s
- Generation: 0.584s
- Post-generation: 0.000s
- Total Prediction Time: 123.086s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 204.25s
  - Total Evaluation: 204.26s

**Pipeline Total:** 12513.01s

---

*Report generated on 2025-08-16 14:37:03*
