# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 480.31s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.873, mAP=0.765, nDCG@5=0.824, MRR=0.882
  Generation: LLM=0.863, Semantic=0.922
  Component Scores: Retrieval=0.836, Generation=0.893
  Overall Score: 0.864
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.051s, Passage Augment=1.884s, Passage Rerank=0.056s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.280s, Post-generation=0.000s
  Total Prediction Time: 3.271s
  Embedding Tokens: 1239.5
  LLM Tokens: 1738.8 in, 86.5 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.531s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_rerank: 1219.3
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1738.8 in, 86.5 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.051s
- Passage Augment: 1.884s
- Passage Rerank: 0.056s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.280s
- Post-generation: 0.000s
- Total Prediction Time: 3.271s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 153.14s
  - Total Evaluation: 153.15s

**Pipeline Total:** 480.31s

---

*Report generated on 2025-09-05 00:46:59*
