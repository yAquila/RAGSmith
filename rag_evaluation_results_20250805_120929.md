# RAG EVALUATION RESULTS

**Dataset:** 3 test cases  
**Success rate:** 30/30 (100.0%)  
**Total runtime:** 250.10s

**Model combinations tested:** 10
  • query_expansion:simple_query_refinement_clarification + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • query_expansion:simple_query_refinement_rephrasing + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • query_expansion:no_expansion + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • query_expansion:simple_multi_query_cc + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • query_expansion:rag_fusion + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • query_expansion:decomposition_cc + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • query_expansion:hyde_cc + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • query_expansion:simple_multi_query_borda + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • query_expansion:step_back_prompting + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1
  • query_expansion:graph_as_query_expansion + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** query_expansion:simple_query_refinement_clarification + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1  
**Generation:** query_expansion:graph_as_query_expansion + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1  
**Overall:** query_expansion:graph_as_query_expansion + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1

## 📊 DETAILED METRICS BY COMBINATION:

**query_expansion:simple_query_refinement_clarification + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@10=1.000
  Generation: LLM=0.933, Semantic=0.847
  Component Scores: Retrieval=1.000, Generation=0.890
  Overall Score: 0.923
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=2.122s, Retrieval=1.166s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=5.929s
  Total Prediction Time: 9.217s
  Embedding Tokens:6.0
  LLM Input Tokens:1586.7
  LLM Output Tokens:368.3
  Avg Evaluation Times: Retrieval=0.001s, Generation=0.667s

**query_expansion:simple_query_refinement_rephrasing + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@10=1.000
  Generation: LLM=0.950, Semantic=0.868
  Component Scores: Retrieval=1.000, Generation=0.909
  Overall Score: 0.936
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.564s, Retrieval=0.185s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=7.003s
  Total Prediction Time: 7.752s
  Embedding Tokens:16.7
  LLM Input Tokens:1549.3
  LLM Output Tokens:448.7
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.705s

**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@10=1.000
  Generation: LLM=0.933, Semantic=0.888
  Component Scores: Retrieval=1.000, Generation=0.911
  Overall Score: 0.938
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.000s, Retrieval=0.231s, Passage Filter=0.000s, Prompt Maker=0.000s, Generation=4.766s
  Total Prediction Time: 4.997s
  Embedding Tokens:12.3
  LLM Input Tokens:1409.3
  LLM Output Tokens:287.3
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.604s

**query_expansion:simple_multi_query_cc + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@10=1.000
  Generation: LLM=0.950, Semantic=0.889
  Component Scores: Retrieval=1.000, Generation=0.919
  Overall Score: 0.944
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.970s, Retrieval=0.465s, Passage Filter=0.001s, Prompt Maker=0.000s, Generation=3.270s
  Total Prediction Time: 4.706s
  Embedding Tokens:12.3
  LLM Input Tokens:755.3
  LLM Output Tokens:254.3
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.569s

**query_expansion:rag_fusion + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@10=0.667
  Generation: LLM=0.927, Semantic=0.851
  Component Scores: Retrieval=0.667, Generation=0.889
  Overall Score: 0.822
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=1.058s, Retrieval=0.395s, Passage Filter=0.001s, Prompt Maker=0.000s, Generation=1.210s
  Total Prediction Time: 2.664s
  Embedding Tokens:12.3
  LLM Input Tokens:301.3
  LLM Output Tokens:123.3
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.550s

**query_expansion:decomposition_cc + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@10=1.000
  Generation: LLM=0.927, Semantic=0.896
  Component Scores: Retrieval=1.000, Generation=0.911
  Overall Score: 0.938
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.980s, Retrieval=0.419s, Passage Filter=0.001s, Prompt Maker=0.000s, Generation=3.778s
  Total Prediction Time: 5.178s
  Embedding Tokens:12.3
  LLM Input Tokens:1204.3
  LLM Output Tokens:283.3
  Avg Evaluation Times: Retrieval=0.001s, Generation=0.605s

**query_expansion:hyde_cc + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@10=1.000
  Generation: LLM=0.933, Semantic=0.885
  Component Scores: Retrieval=1.000, Generation=0.909
  Overall Score: 0.936
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=20.754s, Retrieval=0.364s, Passage Filter=0.001s, Prompt Maker=0.000s, Generation=4.433s
  Total Prediction Time: 25.552s
  Embedding Tokens:205.7
  LLM Input Tokens:1470.0
  LLM Output Tokens:1718.7
  Avg Evaluation Times: Retrieval=0.001s, Generation=0.612s

**query_expansion:simple_multi_query_borda + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@10=1.000
  Generation: LLM=0.927, Semantic=0.887
  Component Scores: Retrieval=1.000, Generation=0.907
  Overall Score: 0.935
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=1.007s, Retrieval=0.424s, Passage Filter=0.001s, Prompt Maker=0.000s, Generation=4.540s
  Total Prediction Time: 5.972s
  Embedding Tokens:12.3
  LLM Input Tokens:1555.0
  LLM Output Tokens:329.3
  Avg Evaluation Times: Retrieval=0.001s, Generation=0.623s

**query_expansion:step_back_prompting + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@10=0.667
  Generation: LLM=0.927, Semantic=0.878
  Component Scores: Retrieval=0.667, Generation=0.902
  Overall Score: 0.832
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=0.838s, Retrieval=0.443s, Passage Filter=0.001s, Prompt Maker=0.000s, Generation=3.662s
  Total Prediction Time: 4.944s
  Embedding Tokens:12.3
  LLM Input Tokens:1076.3
  LLM Output Tokens:266.7
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.638s

**query_expansion:graph_as_query_expansion + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  Retrieval: R@10=1.000
  Generation: LLM=0.950, Semantic=0.893
  Component Scores: Retrieval=1.000, Generation=0.921
  Overall Score: 0.945
  Success Rate: 100.0%
  Avg Prediction Times: Query Expansion=1.004s, Retrieval=0.394s, Passage Filter=0.001s, Prompt Maker=0.000s, Generation=4.076s
  Total Prediction Time: 5.474s
  Embedding Tokens:42.0
  LLM Input Tokens:1428.7
  LLM Output Tokens:236.0
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.610s

## 🔢 TOKEN COUNT BREAKDOWN (AVERAGE PER COMPONENT):

**query_expansion:simple_query_refinement_clarification + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 6.0
  - LLM Input Tokens:
    - generation: 1482.7
    - query_expansion: 104.0
  - LLM Output Tokens:
    - generation: 357.7
    - query_expansion: 10.7
**query_expansion:simple_query_refinement_rephrasing + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 16.7
  - LLM Input Tokens:
    - generation: 1425.3
    - query_expansion: 124.0
  - LLM Output Tokens:
    - generation: 425.3
    - query_expansion: 23.3
**query_expansion:no_expansion + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 12.3
  - LLM Input Tokens:
    - generation: 1409.3
  - LLM Output Tokens:
    - generation: 287.3
**query_expansion:simple_multi_query_cc + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 12.3
  - LLM Input Tokens:
    - generation: 661.3
    - query_expansion: 94.0
  - LLM Output Tokens:
    - generation: 201.3
    - query_expansion: 53.0
**query_expansion:rag_fusion + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 12.3
  - LLM Input Tokens:
    - generation: 207.3
    - query_expansion: 94.0
  - LLM Output Tokens:
    - generation: 67.3
    - query_expansion: 56.0
**query_expansion:decomposition_cc + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 12.3
  - LLM Input Tokens:
    - generation: 1052.3
    - query_expansion: 152.0
  - LLM Output Tokens:
    - generation: 229.0
    - query_expansion: 54.3
**query_expansion:hyde_cc + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 205.7
  - LLM Input Tokens:
    - generation: 1376.0
    - query_expansion: 94.0
  - LLM Output Tokens:
    - generation: 266.3
    - query_expansion: 1452.3
**query_expansion:simple_multi_query_borda + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 12.3
  - LLM Input Tokens:
    - generation: 1461.0
    - query_expansion: 94.0
  - LLM Output Tokens:
    - generation: 271.0
    - query_expansion: 58.3
**query_expansion:step_back_prompting + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 12.3
  - LLM Input Tokens:
    - generation: 887.3
    - query_expansion: 189.0
  - LLM Output Tokens:
    - generation: 225.0
    - query_expansion: 41.7
**query_expansion:graph_as_query_expansion + retrieval:mxbai-cosine + passage_filter:similarity_threshold + prompt_maker:simple_listing + generator:gemma3:4b-t0.1:**
  - Embedding Tokens:
    - retrieval: 29.7
    - query_expansion: 12.3
  - LLM Input Tokens:
    - generation: 1428.7
  - LLM Output Tokens:
    - generation: 236.0

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
- Query Expansion: 29.297s
- Retrieval: 4.485s
- Passage Filter: 0.006s
- Prompt Maker: 0.001s
- Generation: 42.666s
- Total Prediction Time: 76.455s

**Evaluation Times:**
  - Retrieval: 0.01s
  - Generation: 18.55s
  - Total Evaluation: 18.57s

**Pipeline Total:** 250.10s

---

*Report generated on 2025-08-05 12:09:29*
