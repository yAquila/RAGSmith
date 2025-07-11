# RAG EVALUATION RESULTS

**Dataset:** 100 test cases  
**Success rate:** 1600/1600 (100.0%)  
**Total runtime:** 48014.89s

**Model combinations tested:** 16
  • nomic-embed-text + llama3.2:1b
  • nomic-embed-text + LLM-rerank(gemma3:4b) + llama3.2:1b
  • nomic-embed-text + BAAI/bge-reranker-v2-m3 + llama3.2:1b
  • nomic-embed-text + BAAI/bge-reranker-v2-m3 + LLM-rerank(gemma3:4b) + llama3.2:1b
  • nomic-embed-text + gemma3:4b
  • nomic-embed-text + LLM-rerank(gemma3:4b) + gemma3:4b
  • nomic-embed-text + BAAI/bge-reranker-v2-m3 + gemma3:4b
  • nomic-embed-text + BAAI/bge-reranker-v2-m3 + LLM-rerank(gemma3:4b) + gemma3:4b
  • mxbai-embed-large + llama3.2:1b
  • mxbai-embed-large + LLM-rerank(gemma3:4b) + llama3.2:1b
  • mxbai-embed-large + BAAI/bge-reranker-v2-m3 + llama3.2:1b
  • mxbai-embed-large + BAAI/bge-reranker-v2-m3 + LLM-rerank(gemma3:4b) + llama3.2:1b
  • mxbai-embed-large + gemma3:4b
  • mxbai-embed-large + LLM-rerank(gemma3:4b) + gemma3:4b
  • mxbai-embed-large + BAAI/bge-reranker-v2-m3 + gemma3:4b
  • mxbai-embed-large + BAAI/bge-reranker-v2-m3 + LLM-rerank(gemma3:4b) + gemma3:4b

## 🏆 BEST PERFORMING COMBINATIONS:

**Retrieval:** mxbai-embed-large||llama3.2:1b  
**Generation:** mxbai-embed-large||LLM-rerank(gemma3:4b)||gemma3:4b  
**Overall:** mxbai-embed-large||gemma3:4b

## 📊 DETAILED METRICS BY COMBINATION:

**nomic-embed-text + llama3.2:1b:**
  Retrieval: R@10=0.733, mAP=0.619, nDCG@10=0.710, MRR=0.810
  Generation: LLM=0.770, Semantic=0.831
  Component Scores: Retrieval=0.718, Generation=0.800
  Overall Score: 0.775
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.058s, Generation=11.175s
  Avg Evaluation Times: Retrieval=0.000s, Generation=10.217s

**nomic-embed-text + LLM-rerank(gemma3:4b) + llama3.2:1b:**
  Retrieval: R@5=0.522, mAP=0.340, nDCG@5=0.497, MRR=0.600
  LLM Reranking: Model=gemma3:4b, Avg Time=12.968s
  Generation: LLM=0.713, Semantic=0.808
  Component Scores: Retrieval=0.490, Generation=0.760
  Overall Score: 0.679
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.056s, Generation=4.113s
  Avg Rerank Times: LLM: 12.968s
  Avg Evaluation Times: Retrieval=0.000s, Generation=11.089s

**nomic-embed-text + BAAI/bge-reranker-v2-m3 + llama3.2:1b:**
  Retrieval: R@5=0.640, mAP=0.592, nDCG@5=0.727, MRR=0.855
  Cross-encoder Reranking: Model=BAAI/bge-reranker-v2-m3, Avg Time=0.339s
  Generation: LLM=0.766, Semantic=0.832
  Component Scores: Retrieval=0.703, Generation=0.799
  Overall Score: 0.770
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.056s, Generation=10.962s
  Avg Rerank Times: CE: 0.339s
  Avg Evaluation Times: Retrieval=0.000s, Generation=10.123s

**nomic-embed-text + BAAI/bge-reranker-v2-m3 + LLM-rerank(gemma3:4b) + llama3.2:1b:**
  Retrieval: R@5=0.613, mAP=0.568, nDCG@5=0.705, MRR=0.863
  Cross-encoder Reranking: Model=BAAI/bge-reranker-v2-m3, Avg Time=0.312s
  LLM Reranking: Model=gemma3:4b, Avg Time=12.901s
  Generation: LLM=0.719, Semantic=0.826
  Component Scores: Retrieval=0.687, Generation=0.772
  Overall Score: 0.747
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.059s, Generation=4.079s
  Avg Rerank Times: CE: 0.312s, LLM: 12.901s
  Avg Evaluation Times: Retrieval=0.000s, Generation=11.040s

**nomic-embed-text + gemma3:4b:**
  Retrieval: R@10=0.733, mAP=0.619, nDCG@10=0.710, MRR=0.810
  Generation: LLM=0.792, Semantic=0.792
  Component Scores: Retrieval=0.718, Generation=0.792
  Overall Score: 0.770
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.054s, Generation=18.338s
  Avg Evaluation Times: Retrieval=0.000s, Generation=10.277s

**nomic-embed-text + LLM-rerank(gemma3:4b) + gemma3:4b:**
  Retrieval: R@5=0.518, mAP=0.354, nDCG@5=0.508, MRR=0.614
  LLM Reranking: Model=gemma3:4b, Avg Time=12.877s
  Generation: LLM=0.802, Semantic=0.834
  Component Scores: Retrieval=0.499, Generation=0.818
  Overall Score: 0.722
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.055s, Generation=4.599s
  Avg Rerank Times: LLM: 12.877s
  Avg Evaluation Times: Retrieval=0.000s, Generation=10.115s

**nomic-embed-text + BAAI/bge-reranker-v2-m3 + gemma3:4b:**
  Retrieval: R@5=0.640, mAP=0.592, nDCG@5=0.727, MRR=0.855
  Cross-encoder Reranking: Model=BAAI/bge-reranker-v2-m3, Avg Time=0.311s
  Generation: LLM=0.810, Semantic=0.825
  Component Scores: Retrieval=0.703, Generation=0.818
  Overall Score: 0.783
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.054s, Generation=17.062s
  Avg Rerank Times: CE: 0.311s
  Avg Evaluation Times: Retrieval=0.000s, Generation=10.186s

**nomic-embed-text + BAAI/bge-reranker-v2-m3 + LLM-rerank(gemma3:4b) + gemma3:4b:**
  Retrieval: R@5=0.623, mAP=0.572, nDCG@5=0.710, MRR=0.864
  Cross-encoder Reranking: Model=BAAI/bge-reranker-v2-m3, Avg Time=0.312s
  LLM Reranking: Model=gemma3:4b, Avg Time=12.965s
  Generation: LLM=0.804, Semantic=0.846
  Component Scores: Retrieval=0.692, Generation=0.825
  Overall Score: 0.785
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=0.056s, Generation=4.849s
  Avg Rerank Times: CE: 0.312s, LLM: 12.965s
  Avg Evaluation Times: Retrieval=0.000s, Generation=10.145s

**mxbai-embed-large + llama3.2:1b:**
  Retrieval: R@10=0.814, mAP=0.704, nDCG@10=0.785, MRR=0.855
  Generation: LLM=0.753, Semantic=0.829
  Component Scores: Retrieval=0.789, Generation=0.791
  Overall Score: 0.791
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=1.478s, Generation=16.881s
  Avg Evaluation Times: Retrieval=0.000s, Generation=9.493s

**mxbai-embed-large + LLM-rerank(gemma3:4b) + llama3.2:1b:**
  Retrieval: R@5=0.590, mAP=0.362, nDCG@5=0.538, MRR=0.606
  LLM Reranking: Model=gemma3:4b, Avg Time=18.302s
  Generation: LLM=0.747, Semantic=0.822
  Component Scores: Retrieval=0.524, Generation=0.785
  Overall Score: 0.706
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=1.461s, Generation=4.109s
  Avg Rerank Times: LLM: 18.302s
  Avg Evaluation Times: Retrieval=0.000s, Generation=11.167s

**mxbai-embed-large + BAAI/bge-reranker-v2-m3 + llama3.2:1b:**
  Retrieval: R@5=0.692, mAP=0.634, nDCG@5=0.768, MRR=0.866
  Cross-encoder Reranking: Model=BAAI/bge-reranker-v2-m3, Avg Time=0.346s
  Generation: LLM=0.763, Semantic=0.831
  Component Scores: Retrieval=0.740, Generation=0.797
  Overall Score: 0.780
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=1.449s, Generation=16.307s
  Avg Rerank Times: CE: 0.346s
  Avg Evaluation Times: Retrieval=0.000s, Generation=10.205s

**mxbai-embed-large + BAAI/bge-reranker-v2-m3 + LLM-rerank(gemma3:4b) + llama3.2:1b:**
  Retrieval: R@5=0.672, mAP=0.601, nDCG@5=0.747, MRR=0.873
  Cross-encoder Reranking: Model=BAAI/bge-reranker-v2-m3, Avg Time=0.345s
  LLM Reranking: Model=gemma3:4b, Avg Time=18.267s
  Generation: LLM=0.749, Semantic=0.822
  Component Scores: Retrieval=0.723, Generation=0.785
  Overall Score: 0.767
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=1.450s, Generation=4.107s
  Avg Rerank Times: CE: 0.345s, LLM: 18.267s
  Avg Evaluation Times: Retrieval=0.000s, Generation=11.171s

**mxbai-embed-large + gemma3:4b:**
  Retrieval: R@10=0.814, mAP=0.704, nDCG@10=0.785, MRR=0.855
  Generation: LLM=0.803, Semantic=0.809
  Component Scores: Retrieval=0.789, Generation=0.806
  Overall Score: 0.801
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=1.447s, Generation=24.268s
  Avg Evaluation Times: Retrieval=0.000s, Generation=10.318s

**mxbai-embed-large + LLM-rerank(gemma3:4b) + gemma3:4b:**
  Retrieval: R@5=0.596, mAP=0.372, nDCG@5=0.543, MRR=0.602
  LLM Reranking: Model=gemma3:4b, Avg Time=18.206s
  Generation: LLM=0.822, Semantic=0.831
  Component Scores: Retrieval=0.528, Generation=0.826
  Overall Score: 0.737
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=1.456s, Generation=5.083s
  Avg Rerank Times: LLM: 18.206s
  Avg Evaluation Times: Retrieval=0.000s, Generation=10.227s

**mxbai-embed-large + BAAI/bge-reranker-v2-m3 + gemma3:4b:**
  Retrieval: R@5=0.692, mAP=0.634, nDCG@5=0.768, MRR=0.866
  Cross-encoder Reranking: Model=BAAI/bge-reranker-v2-m3, Avg Time=0.345s
  Generation: LLM=0.806, Semantic=0.825
  Component Scores: Retrieval=0.740, Generation=0.815
  Overall Score: 0.793
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=1.447s, Generation=22.776s
  Avg Rerank Times: CE: 0.345s
  Avg Evaluation Times: Retrieval=0.000s, Generation=10.273s

**mxbai-embed-large + BAAI/bge-reranker-v2-m3 + LLM-rerank(gemma3:4b) + gemma3:4b:**
  Retrieval: R@5=0.676, mAP=0.611, nDCG@5=0.755, MRR=0.878
  Cross-encoder Reranking: Model=BAAI/bge-reranker-v2-m3, Avg Time=0.344s
  LLM Reranking: Model=gemma3:4b, Avg Time=18.291s
  Generation: LLM=0.816, Semantic=0.825
  Component Scores: Retrieval=0.730, Generation=0.821
  Overall Score: 0.794
  Success Rate: 100.0%
  Avg Prediction Times: Retrieval=1.456s, Generation=5.599s
  Avg Rerank Times: CE: 0.344s, LLM: 18.291s
  Avg Evaluation Times: Retrieval=0.000s, Generation=10.260s

## ⏱️ TIMING BREAKDOWN:

**Prediction Times:**
  - Retrieval: 1209.18s
  - Generation: 17430.59s
  - Total Prediction: 18639.77s

**Evaluation Times:**
  - Retrieval: 0.19s
  - Generation: 16630.74s
  - Total Evaluation: 16630.93s

**Pipeline Total:** 48014.89s

---

*Report generated on 2025-07-11 05:51:22*
