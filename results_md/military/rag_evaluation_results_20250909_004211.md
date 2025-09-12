# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 349.90s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_parent_document_retriever + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.000, mAP=0.000, nDCG@5=0.000, MRR=0.000
  Generation: LLM=0.486, Semantic=0.879
  Component Scores: Retrieval=0.000, Generation=0.682
  Overall Score: 0.341
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.308s, Retrieval=0.132s, Passage Augment=0.000s, Passage Rerank=0.499s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=0.803s, Post-generation=0.000s
  Total Prediction Time: 1.743s
  Embedding Tokens: 1116.6
  LLM Tokens: 1305.1 in, 1615.7 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.755s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 21.6
    - passage_rerank: 1095.0
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 64.6 in, 99.9 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1095.0 in, 1487.1 out
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 145.4 in, 28.6 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.308s
- Retrieval: 0.132s
- Passage Augment: 0.000s
- Passage Rerank: 0.499s
- Passage Filter: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.803s
- Post-generation: 0.000s
- Total Prediction Time: 1.743s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 175.51s
  - Total Evaluation: 175.52s

**Pipeline Total:** 349.90s

---

*Report generated on 2025-09-09 00:42:11*
