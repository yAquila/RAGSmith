# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 540.03s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.852, mAP=0.715, nDCG@5=0.782, MRR=0.827
  Generation: LLM=0.855, Semantic=0.920
  Component Scores: Retrieval=0.794, Generation=0.888
  Overall Score: 0.841
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.050s, Passage Augment=1.892s, Passage Rerank=0.647s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.326s, Post-generation=0.000s
  Total Prediction Time: 3.914s
  Embedding Tokens: 20.2
  LLM Tokens: 2974.3 in, 915.5 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.486s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 20.2
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1734.8 in, 85.5 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1239.5 in, 830.0 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.050s
- Passage Augment: 1.892s
- Passage Rerank: 0.647s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.326s
- Post-generation: 0.000s
- Total Prediction Time: 3.914s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 148.56s
  - Total Evaluation: 148.57s

**Pipeline Total:** 540.03s

---

*Report generated on 2025-09-05 11:26:35*
