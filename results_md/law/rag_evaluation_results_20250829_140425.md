# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 284.87s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_parent_document_retriever + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_parent_document_retriever + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.000, mAP=0.000, nDCG@5=0.000, MRR=0.000
  Generation: LLM=0.613, Semantic=0.870
  Component Scores: Retrieval=0.000, Generation=0.741
  Overall Score: 0.371
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.287s, Retrieval=0.128s, Passage Augment=0.000s, Passage Rerank=0.062s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=0.624s, Post-generation=0.000s
  Total Prediction Time: 1.100s
  Embedding Tokens: 1154.9
  LLM Tokens: 205.7 in, 102.1 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.748s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_parent_document_retriever + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 20.4
    - passage_rerank: 1134.5
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 144.1 in, 25.6 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 61.6 in, 76.5 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.287s
- Retrieval: 0.128s
- Passage Augment: 0.000s
- Passage Rerank: 0.062s
- Passage Filter: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.624s
- Post-generation: 0.000s
- Total Prediction Time: 1.100s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 174.80s
  - Total Evaluation: 174.81s

**Pipeline Total:** 284.87s

---

*Report generated on 2025-08-29 14:04:25*
