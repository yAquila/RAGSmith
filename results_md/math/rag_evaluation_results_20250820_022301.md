# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 766.77s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.848, mAP=0.771, nDCG@5=0.803, MRR=0.845
  Generation: LLM=0.798, Semantic=0.894
  Component Scores: Retrieval=0.817, Generation=0.846
  Overall Score: 0.831
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.306s, Retrieval=0.049s, Passage Augment=2.015s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=2.361s, Prompt Maker=0.000s, Generation=1.287s, Post-generation=0.000s
  Total Prediction Time: 6.017s
  Embedding Tokens: 1013.4
  LLM Tokens: 3751.5 in, 676.9 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.650s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_contextual_chunk_headers + query_expansion:simple_query_refinement_rephrasing + retrieval:vector_mxbai + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 20.7
    - passage_compress: 992.8
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 144.8 in, 27.5 out
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2478.0 in, 538.9 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1128.7 in, 110.5 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.306s
- Retrieval: 0.049s
- Passage Augment: 2.015s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 2.361s
- Prompt Maker: 0.000s
- Generation: 1.287s
- Post-generation: 0.000s
- Total Prediction Time: 6.017s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 164.96s
  - Total Evaluation: 164.97s

**Pipeline Total:** 766.77s

---

*Report generated on 2025-08-20 02:23:01*
