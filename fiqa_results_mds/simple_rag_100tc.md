# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 400/400 (100.0%)  
**Total runtime:** 2956.48s

**Model combinations tested:** 4
  • nomic-embed-text_llama3.2:1b
  • nomic-embed-text_gemma3:4b
  • mxbai-embed-large_llama3.2:1b
  • mxbai-embed-large_gemma3:4b

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** mxbai-embed-large_llama3.2:1b  
**Generation:** mxbai-embed-large_gemma3:4b  
**Overall:** mxbai-embed-large_gemma3:4b

## 📊 DETAILED METRICS BY COMBINATION:

**nomic-embed-text_llama3.2:1b:**
  Retrieval: R@10=0.733, mAP=0.619, nDCG@10=0.710, MRR=0.810
  Generation: LLM=0.847, Semantic=0.820
  Component Scores: Retrieval=0.718, Generation=0.833
  Overall Score: 0.799
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.047s, Generation=1.982s
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.551s

**nomic-embed-text_gemma3:4b:**
  Retrieval: R@10=0.733, mAP=0.619, nDCG@10=0.710, MRR=0.810
  Generation: LLM=0.893, Semantic=0.807
  Component Scores: Retrieval=0.718, Generation=0.850
  Overall Score: 0.810
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.049s, Generation=6.372s
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.559s

**mxbai-embed-large_llama3.2:1b:**
  Retrieval: R@10=0.814, mAP=0.704, nDCG@10=0.785, MRR=0.855
  Generation: LLM=0.845, Semantic=0.823
  Component Scores: Retrieval=0.789, Generation=0.834
  Overall Score: 0.821
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=2.114s, Generation=9.986s
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.483s

**mxbai-embed-large_gemma3:4b:**
  Retrieval: R@10=0.814, mAP=0.704, nDCG@10=0.785, MRR=0.855
  Generation: LLM=0.904, Semantic=0.808
  Component Scores: Retrieval=0.789, Generation=0.856
  Overall Score: 0.836
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.093s, Generation=6.761s
  Avg Evaluation Times: Retrieval=0.000s, Generation=0.564s

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
  - Retrieval: 230.27s
  - Generation: 2510.19s
  - Total Prediction: 2740.47s

**Evaluation Times:**
  - Retrieval: 0.06s
  - Generation: 215.75s
  - Total Evaluation: 215.80s

**Pipeline Total:** 2956.48s

---

*Report generated on 2025-07-11 05:55:58*
