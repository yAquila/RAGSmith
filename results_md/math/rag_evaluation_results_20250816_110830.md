# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 15627.65s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.182, mAP=0.149, nDCG@5=0.183, MRR=0.266
  Generation: LLM=0.715, Semantic=0.884
  Component Scores: Retrieval=0.195, Generation=0.799
  Overall Score: 0.497
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=3.960s, Retrieval=144.546s, Passage Augment=0.000s, Passage Rerank=4.902s, Passage Filter=0.000s, Passage Compress=0.291s, Prompt Maker=0.000s, Generation=0.584s, Post-generation=0.000s
  Total Prediction Time: 154.284s
  Embedding Tokens: 191.9
  LLM Tokens: 3875.1 in, 1316.5 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.991s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - passage_compress: 59.4
    - retrieval: 132.4
  - LLM Tokens:
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 3300.7 in, 605.5 out
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 328.2 in, 125.8 out
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 120.7 in, 518.5 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 125.5 in, 66.8 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 3.960s
- Retrieval: 144.546s
- Passage Augment: 0.000s
- Passage Rerank: 4.902s
- Passage Filter: 0.000s
- Passage Compress: 0.291s
- Prompt Maker: 0.000s
- Generation: 0.584s
- Post-generation: 0.000s
- Total Prediction Time: 154.284s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 199.07s
  - Total Evaluation: 199.08s

**Pipeline Total:** 15627.65s

---

*Report generated on 2025-08-16 11:08:30*
