# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 322.96s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_parent_document_retriever + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.000, mAP=0.000, nDCG@5=0.000, MRR=0.000
  Generation: LLM=0.591, Semantic=0.867
  Component Scores: Retrieval=0.000, Generation=0.729
  Overall Score: 0.364
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.287s, Retrieval=0.132s, Passage Augment=0.000s, Passage Rerank=0.486s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=0.614s, Post-generation=0.000s
  Total Prediction Time: 1.518s
  Embedding Tokens: 1162.0
  LLM Tokens: 1347.3 in, 1669.9 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.711s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 20.4
    - passage_rerank: 1141.5
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 144.1 in, 25.7 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 61.7 in, 74.5 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1141.5 in, 1569.6 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.287s
- Retrieval: 0.132s
- Passage Augment: 0.000s
- Passage Rerank: 0.486s
- Passage Filter: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.614s
- Post-generation: 0.000s
- Total Prediction Time: 1.518s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 171.09s
  - Total Evaluation: 171.10s

**Pipeline Total:** 322.96s

---

*Report generated on 2025-08-27 16:48:48*
