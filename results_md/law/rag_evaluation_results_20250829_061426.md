# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 525.57s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.905, mAP=0.811, nDCG@5=0.862, MRR=0.902
  Generation: LLM=0.862, Semantic=0.917
  Component Scores: Retrieval=0.870, Generation=0.889
  Overall Score: 0.880
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.049s, Passage Augment=1.702s, Passage Rerank=0.703s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.280s, Post-generation=0.000s
  Total Prediction Time: 3.734s
  Embedding Tokens: 1259.7
  LLM Tokens: 2906.2 in, 957.6 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.521s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:query_expansion_none + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 20.2
    - passage_rerank: 1239.5
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1666.7 in, 83.9 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1239.5 in, 873.7 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.049s
- Passage Augment: 1.702s
- Passage Rerank: 0.703s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 1.280s
- Post-generation: 0.000s
- Total Prediction Time: 3.734s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 152.12s
  - Total Evaluation: 152.13s

**Pipeline Total:** 525.57s

---

*Report generated on 2025-08-29 06:14:26*
