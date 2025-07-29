# RAG EVALUATION RESULTS

**Dataset:** 10 test cases  
**Success rate:** 80/80 (100.0%)  
**Total runtime:** 257.76s

**Model combinations tested:** 8
  • query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:no_augment + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:no_augment + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:long_context_reorder_1 + generator:llama3.2:1b-t0.3
  • query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:no_augment + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:long_context_reorder_2 + generator:llama3.2:1b-t0.3
  • query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:no_augment + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:long_context_reorder_3 + generator:llama3.2:1b-t0.3
  • query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:prev_next_augmenter + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3
  • query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:prev_next_augmenter + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:long_context_reorder_1 + generator:llama3.2:1b-t0.3
  • query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:prev_next_augmenter + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:long_context_reorder_2 + generator:llama3.2:1b-t0.3
  • query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:prev_next_augmenter + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:long_context_reorder_3 + generator:llama3.2:1b-t0.3

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:no_augment + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3  
**Generation:** query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:no_augment + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:long_context_reorder_1 + generator:llama3.2:1b-t0.3  
**Overall:** query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:no_augment + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:long_context_reorder_1 + generator:llama3.2:1b-t0.3

## 📊 DETAILED METRICS BY COMBINATION:

**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:no_augment + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.967
  Generation: LLM=0.881, Semantic=0.785
  Component Scores: Retrieval=0.967, Generation=0.833
  Overall Score: 0.873
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.135s, Passage Augment=0.000s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=2.332s
  Total Prediction Time: 2.466s
  Embedding Tokens:21.5
  LLM Input Tokens:1767.0
  LLM Output Tokens:233.8
  Avg Evaluation Times: Retrieval=0.000s, Generation=1.098s

**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:no_augment + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:long_context_reorder_1 + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.967
  Generation: LLM=0.923, Semantic=0.806
  Component Scores: Retrieval=0.967, Generation=0.864
  Overall Score: 0.895
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.143s, Passage Augment=0.000s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.794s
  Total Prediction Time: 1.938s
  Embedding Tokens:21.5
  LLM Input Tokens:1933.2
  LLM Output Tokens:197.0
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.615s

**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:no_augment + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:long_context_reorder_2 + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.967
  Generation: LLM=0.887, Semantic=0.792
  Component Scores: Retrieval=0.967, Generation=0.839
  Overall Score: 0.877
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.145s, Passage Augment=0.000s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=2.068s
  Total Prediction Time: 2.214s
  Embedding Tokens:21.5
  LLM Input Tokens:1933.2
  LLM Output Tokens:239.1
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.622s

**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:no_augment + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:long_context_reorder_3 + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.967
  Generation: LLM=0.927, Semantic=0.792
  Component Scores: Retrieval=0.967, Generation=0.859
  Overall Score: 0.892
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.135s, Passage Augment=0.000s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=1.983s
  Total Prediction Time: 2.119s
  Embedding Tokens:21.5
  LLM Input Tokens:1933.2
  LLM Output Tokens:219.6
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.609s

**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:prev_next_augmenter + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.967
  Generation: LLM=0.862, Semantic=0.778
  Component Scores: Retrieval=0.967, Generation=0.820
  Overall Score: 0.864
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.129s, Passage Augment=0.027s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=2.590s
  Total Prediction Time: 2.747s
  Embedding Tokens:21.5
  LLM Input Tokens:2889.3
  LLM Output Tokens:275.7
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.623s

**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:prev_next_augmenter + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:long_context_reorder_1 + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.967
  Generation: LLM=0.862, Semantic=0.789
  Component Scores: Retrieval=0.967, Generation=0.826
  Overall Score: 0.868
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.145s, Passage Augment=0.032s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=2.369s
  Total Prediction Time: 2.546s
  Embedding Tokens:21.5
  LLM Input Tokens:3399.9
  LLM Output Tokens:229.9
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.610s

**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:prev_next_augmenter + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:long_context_reorder_2 + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.967
  Generation: LLM=0.877, Semantic=0.779
  Component Scores: Retrieval=0.967, Generation=0.828
  Overall Score: 0.870
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.134s, Passage Augment=0.030s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=2.710s
  Total Prediction Time: 2.875s
  Embedding Tokens:21.5
  LLM Input Tokens:3399.9
  LLM Output Tokens:274.0
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.631s

**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:prev_next_augmenter + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:long_context_reorder_3 + generator:llama3.2:1b-t0.3:**
  Retrieval: R@5=0.967
  Generation: LLM=0.865, Semantic=0.780
  Component Scores: Retrieval=0.967, Generation=0.822
  Overall Score: 0.866
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.125s, Passage Augment=0.025s, Passage Rerank=0.000s, Passage Filter=0.000s, Passage Compress=0.000s, Prompt Maker=0.000s, Generation=2.881s
  Total Prediction Time: 3.032s
  Embedding Tokens:21.5
  LLM Input Tokens:3399.9
  LLM Output Tokens:263.7
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.599s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:no_augment + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 21.5
  - LLM Input Tokens:
    - generation: 1767.0
  - LLM Output Tokens:
    - generation: 233.8
**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:no_augment + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:long_context_reorder_1 + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 21.5
  - LLM Input Tokens:
    - generation: 1933.2
  - LLM Output Tokens:
    - generation: 197.0
**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:no_augment + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:long_context_reorder_2 + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 21.5
  - LLM Input Tokens:
    - generation: 1933.2
  - LLM Output Tokens:
    - generation: 239.1
**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:no_augment + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:long_context_reorder_3 + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 21.5
  - LLM Input Tokens:
    - generation: 1933.2
  - LLM Output Tokens:
    - generation: 219.6
**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:prev_next_augmenter + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:simple_listing + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 21.5
  - LLM Input Tokens:
    - generation: 2889.3
  - LLM Output Tokens:
    - generation: 275.7
**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:prev_next_augmenter + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:long_context_reorder_1 + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 21.5
  - LLM Input Tokens:
    - generation: 3399.9
  - LLM Output Tokens:
    - generation: 229.9
**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:prev_next_augmenter + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:long_context_reorder_2 + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 21.5
  - LLM Input Tokens:
    - generation: 3399.9
  - LLM Output Tokens:
    - generation: 274.0
**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_augment:prev_next_augmenter + passage_rerank:no_rerank + passage_filter:similarity_threshold + passage_compress:no_compress + prompt_maker:long_context_reorder_3 + generator:llama3.2:1b-t0.3:**
  - Embedding Tokens:
    - retrieval: 21.5
  - LLM Input Tokens:
    - generation: 3399.9
  - LLM Output Tokens:
    - generation: 263.7

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 0.000s
- Retrieval: 1.092s
- Passage Augment: 0.115s
- Passage Rerank: 0.000s
- Passage Filter: 0.002s
- Passage Compress: 0.000s
- Prompt Maker: 0.001s
- Generation: 18.728s
- Total Prediction Time: 19.938s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 54.07s
  - Total Evaluation: 54.08s

**Pipeline Total:** 257.76s

---

*Report generated on 2025-07-29 11:12:57*
