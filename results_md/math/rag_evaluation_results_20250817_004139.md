# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 11465.05s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.184, mAP=0.151, nDCG@5=0.181, MRR=0.250
  Generation: LLM=0.699, Semantic=0.879
  Component Scores: Retrieval=0.192, Generation=0.789
  Overall Score: 0.490
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=7.462s, Retrieval=99.455s, Passage Augment=0.000s, Passage Rerank=4.837s, Passage Filter=0.000s, Passage Compress=0.333s, Prompt Maker=0.000s, Generation=0.592s, Post-generation=0.000s
  Total Prediction Time: 112.678s
  Embedding Tokens: 187.6
  LLM Tokens: 4170.2 in, 1784.2 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.971s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - passage_compress: 55.3
    - retrieval: 132.3
  - LLM Tokens:
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 3485.0 in, 601.5 out
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 440.6 in, 171.7 out
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 120.7 in, 943.2 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 123.9 in, 67.8 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 7.462s
- Retrieval: 99.455s
- Passage Augment: 0.000s
- Passage Rerank: 4.837s
- Passage Filter: 0.000s
- Passage Compress: 0.333s
- Prompt Maker: 0.000s
- Generation: 0.592s
- Post-generation: 0.000s
- Total Prediction Time: 112.678s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 197.11s
  - Total Evaluation: 197.12s

**Pipeline Total:** 11465.05s

---

*Report generated on 2025-08-17 00:41:39*
