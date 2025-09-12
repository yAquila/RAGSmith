# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 100/100 (100.0%)  
**Total runtime:** 701.51s

**Model combinations tested:** 1
  • pre_embedding:pre_embedding_none + query_expansion:rag_fusion + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** pre_embedding:pre_embedding_none + query_expansion:rag_fusion + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Generation:** pre_embedding:pre_embedding_none + query_expansion:rag_fusion + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none  
**Overall:** pre_embedding:pre_embedding_none + query_expansion:rag_fusion + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none

## 📊 DETAILED METRICS BY COMBINATION:

**pre_embedding:pre_embedding_none + query_expansion:rag_fusion + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  Retrieval: R@5=0.395, mAP=0.395, nDCG@5=0.452, MRR=0.660
  Generation: LLM=0.798, Semantic=0.911
  Component Scores: Retrieval=0.476, Generation=0.854
  Overall Score: 0.665
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.676s, Retrieval=0.146s, Passage Augment=0.001s, Passage Rerank=3.824s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=0.768s, Post-generation=0.000s
  Total Prediction Time: 5.415s
  Embedding Tokens: 20.2
  LLM Tokens: 10080.5 in, 1123.6 out
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.599s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**pre_embedding:pre_embedding_none + query_expansion:rag_fusion + retrieval:vector_mxbai + passage_augment:prev_next_augmenter + passage_rerank:llm_rerank_gemma + passage_filter:similarity_threshold + passage_compress:passage_compress_none + prompt_maker:simple_listing + generator:alibayram/Qwen3-30B-A3B-Instruct-2507:latest + post_generation:post_generation_none:**
  - Embedding Tokens:
    - retrieval: 20.2
  - LLM Tokens:
    - query_expansion:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 117.1 in, 79.7 out
    - generation:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 492.9 in, 74.6 out
    - passage_rerank:
      - alibayram/Qwen3-30B-A3B-Instruct-2507:latest: 9470.5 in, 969.3 out

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.676s
- Retrieval: 0.146s
- Passage Augment: 0.001s
- Passage Rerank: 3.824s
- Passage Filter: 0.000s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 0.768s
- Post-generation: 0.000s
- Total Prediction Time: 5.415s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 159.91s
  - Total Evaluation: 159.92s

**Pipeline Total:** 701.51s

---

*Report generated on 2025-08-27 14:08:32*
