# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1230.53s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:decomposition_cc + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:decomposition_cc + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:decomposition_cc + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:decomposition_cc + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:decomposition_cc + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.856, mAP=0.762, nDCG@5=0.820, MRR=0.879
  Generation: LLM=0.826, Semantic=0.900
  Component Scores: Retrieval=0.829, Generation=0.863
  Overall Score: 0.846
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.634s, Retrieval=0.157s, Passage Augment=1.720s, Passage Rerank=4.904s, Passage Filter=0.000s, Passage Compress=2.066s, Prompt Maker=0.000s, Generation=1.192s, Post-generation=0.000s
  Total Prediction Time: 10.674s
  Embedding Tokens: 12291.5
  LLM Tokens: 15080.3 in, 2547.9 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.630s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:decomposition_cc + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:cellm_parallel_rerank + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - passage_rerank: 11177.8
    - retrieval: 20.0
    - passage_compress: 1093.7
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1223.8 in, 92.9 out
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 172.9 in, 71.1 out
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2505.8 in, 544.6 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 11177.8 in, 1839.3 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.634s
- Retrieval: 0.157s
- Passage Augment: 1.720s
- Passage Rerank: 4.904s
- Passage Filter: 0.000s
- Passage Compress: 2.066s
- Prompt Maker: 0.000s
- Generation: 1.192s
- Post-generation: 0.000s
- Total Prediction Time: 10.674s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 162.97s
  - Total Evaluation: 162.99s

**Pipeline Total:** 1230.53s

---

*Report generated on 2025-08-21 18:56:05*
