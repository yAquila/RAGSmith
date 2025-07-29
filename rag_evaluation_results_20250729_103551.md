# RAG EVALUATION RESULTS

**Dataset:** 3 test cases  
**Success rate:** 6/6 (100.0%)  
**Total runtime:** 27.14s

**Model combinations tested:** 2
  • query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:no_augment + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:prev_next_augmenter + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:no_augment + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3  
**Generation:** query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:no_augment + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3  
**Overall:** query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:no_augment + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3

## 📊 DETAILED METRICS BY COMBINATION:

**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:no_augment + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=1.000
  Generation: LLM=0.883, Semantic=0.661
  Component Scores: Retrieval=1.000, Generation=0.772
  Overall Score: 0.840
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.148s, Passage Augment=0.000s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=2.913s
  Total Prediction Time: 3.062s
  Embedding Tokens:22.3
  LLM Input Tokens:1898.7
  LLM Output Tokens:185.7
  Avg Evaluation Times: Retrieval=0.000s, Generation=2.378s

**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:prev_next_augmenter + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=1.000
  Generation: LLM=0.833, Semantic=0.642
  Component Scores: Retrieval=1.000, Generation=0.738
  Overall Score: 0.816
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.130s, Passage Augment=0.029s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.794s
  Total Prediction Time: 1.954s
  Embedding Tokens:22.3
  LLM Input Tokens:3073.3
  LLM Output Tokens:166.7
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.559s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:no_augment + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 22.3
  - LLM Input Tokens:
    - generation: 1898.7
  - LLM Output Tokens:
    - generation: 185.7
**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:prev_next_augmenter + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 22.3
  - LLM Input Tokens:
    - generation: 3073.3
  - LLM Output Tokens:
    - generation: 166.7

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 0.278s
- Passage Augment: 0.029s
- Passage Rerank: 0.000s
- Passage Filter: 0.001s
- Passage Compress: 0.000s
- Prompt Maker: 0.000s
- Generation: 4.707s
- Total Prediction Time: 5.015s

**Evaluation Times:**
  - Retrieval: 0.00s
  - Generation: 8.81s
  - Total Evaluation: 8.81s

**Pipeline Total:** 27.14s

---

*Report generated on 2025-07-29 10:35:51*
