# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 1168.80s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_hype + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_hype + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_hype + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_hype + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_hype + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.659, mAP=0.518, nDCG@5=0.592, MRR=0.692
  Generation: LLM=0.792, Semantic=0.881
  Component Scores: Retrieval=0.615, Generation=0.836
  Overall Score: 0.726
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.269s, Retrieval=0.022s, Passage Augment=3.032s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=3.302s, Prompt Maker=0.000s, Generation=1.184s, Post-generation=0.000s
  Total Prediction Time: 7.808s
  Embedding Tokens: 944.0
  LLM Tokens: 105917.7 in, 23453.6 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.727s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_hype + query_expansion:simple_query_refinement_clarification + retrieval:keyword_bm25 + passage_augment:relevant_segment_extractor + passage_rerank:passage_rerank_none + passage_filter:similarity_threshold + passage_compress:tree_summarize + prompt_maker:long_context_reorder_2 + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - passage_compress: 944.0
  - LLM Tokens:
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 1096.0 in, 99.0 out
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 130.8 in, 22.9 out
    - pre_embedding:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 101938.0 in, 22749.0 out
    - passage_compress:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 2752.9 in, 582.7 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.269s
- Retrieval: 0.022s
- Passage Augment: 3.032s
- Passage Rerank: 0.000s
- Passage Filter: 0.000s
- Passage Compress: 3.302s
- Prompt Maker: 0.000s
- Generation: 1.184s
- Post-generation: 0.000s
- Total Prediction Time: 7.808s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 172.74s
  - Total Evaluation: 172.75s

**Pipeline Total:** 1168.80s

---

*Report generated on 2025-08-20 00:59:09*
