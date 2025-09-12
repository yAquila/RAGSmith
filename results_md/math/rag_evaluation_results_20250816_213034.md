# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 12973.87s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.167, mAP=0.140, nDCG@5=0.164, MRR=0.217
  Generation: LLM=0.692, Semantic=0.878
  Component Scores: Retrieval=0.172, Generation=0.785
  Overall Score: 0.478
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=4.131s, Retrieval=110.826s, Passage Augment=0.000s, Passage Rerank=11.602s, Passage Filter=0.000s, Passage Compress=0.279s, Prompt Maker=0.000s, Generation=0.606s, Post-generation=0.000s
  Total Prediction Time: 127.444s
  Embedding Tokens: 197.2
  LLM Tokens: 3883.1 in, 1318.1 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=2.293s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - passage_compress: 62.0
    - retrieval: 135.2
  - LLM Tokens:
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 3326.6 in, 602.5 out
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 306.1 in, 105.9 out
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 120.7 in, 540.2 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 129.7 in, 69.5 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 4.131s
- Retrieval: 110.826s
- Passage Augment: 0.000s
- Passage Rerank: 11.602s
- Passage Filter: 0.000s
- Passage Compress: 0.279s
- Prompt Maker: 0.000s
- Generation: 0.606s
- Post-generation: 0.000s
- Total Prediction Time: 127.444s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 229.30s
  - Total Evaluation: 229.31s

**Pipeline Total:** 12973.87s

---

*Report generated on 2025-08-16 21:30:34*
