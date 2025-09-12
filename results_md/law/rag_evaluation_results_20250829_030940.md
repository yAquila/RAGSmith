# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 238.10s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.000, mAP=0.000, nDCG@5=0.000, MRR=0.000
  Generation: LLM=0.637, Semantic=0.883
  Component Scores: Retrieval=0.000, Generation=0.760
  Overall Score: 0.380
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.133s, Passage Augment=0.000s, Passage Rerank=0.000s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=0.557s, Post-generation=0.000s
  Total Prediction Time: 0.690s
  Embedding Tokens: 20.2
  LLM Tokens: 61.0 in, 67.2 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.691s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:llm_summarize + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 20.2
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 61.0 in, 67.2 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.133s
- Passage Augment: 0.000s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.557s
- Post-generation: 0.000s
- Total Prediction Time: 0.690s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 169.06s
  - Total Evaluation: 169.07s

**Pipeline Total:** 238.10s

---

*Report generated on 2025-08-29 03:09:40*
