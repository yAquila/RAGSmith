# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 11836.99s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.178, mAP=0.148, nDCG@5=0.178, MRR=0.253
  Generation: LLM=0.693, Semantic=0.878
  Component Scores: Retrieval=0.189, Generation=0.785
  Overall Score: 0.487
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=4.067s, Retrieval=106.757s, Passage Augment=0.000s, Passage Rerank=4.768s, Passage Filter=0.000s, Passage Compress=0.248s, Prompt Maker=0.000s, Generation=0.580s, Post-generation=0.000s
  Total Prediction Time: 116.419s
  Embedding Tokens: 199.0
  LLM Tokens: 3997.8 in, 1344.8 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.950s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:hyde_cc + retrieval:graph_rag + passage_augment:no_augment + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_1 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - passage_compress: 66.9
    - retrieval: 132.1
  - LLM Tokens:
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 3433.2 in, 636.9 out
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 310.6 in, 109.4 out
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 120.7 in, 532.7 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 133.4 in, 65.8 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 4.067s
- Retrieval: 106.757s
- Passage Augment: 0.000s
- Passage Rerank: 4.768s
- Passage Filter: 0.000s
- Passage Compress: 0.248s
- Prompt Maker: 0.000s
- Generation: 0.580s
- Post-generation: 0.000s
- Total Prediction Time: 116.419s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 194.99s
  - Total Evaluation: 195.00s

**Pipeline Total:** 11836.99s

---

*Report generated on 2025-08-16 17:54:20*
