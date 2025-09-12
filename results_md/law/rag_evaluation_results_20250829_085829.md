# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 601.88s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:rag_fusion + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:rag_fusion + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:rag_fusion + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:rag_fusion + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:rag_fusion + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.888, mAP=0.758, nDCG@5=0.819, MRR=0.854
  Generation: LLM=0.860, Semantic=0.923
  Component Scores: Retrieval=0.830, Generation=0.892
  Overall Score: 0.861
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.686s, Retrieval=0.143s, Passage Augment=1.910s, Passage Rerank=0.433s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.334s, Post-generation=0.000s
  Total Prediction Time: 4.506s
  Embedding Tokens: 9387.0
  LLM Tokens: 1902.0 in, 164.7 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.512s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:rag_fusion + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:ce_rerank_bge + passage_filter:simple_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_rerank: 9366.8
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.1 in, 81.0 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1784.9 in, 83.7 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.686s
- Retrieval: 0.143s
- Passage Augment: 1.910s
- Passage Rerank: 0.433s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.334s
- Post-generation: 0.000s
- Total Prediction Time: 4.506s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 151.16s
  - Total Evaluation: 151.16s

**Pipeline Total:** 601.88s

---

*Report generated on 2025-08-29 08:58:29*
