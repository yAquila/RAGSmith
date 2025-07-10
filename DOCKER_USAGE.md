# Docker Usage Guide for RAG Pipeline

## Current Issue
Your pipeline was running the **full evaluation** (10+ minutes) instead of a quick test!

## Fixed Configuration
- **Dockerfile now defaults to `--super-quick`** (30 seconds max)
- **Full evaluation takes 10+ minutes** with all model combinations

## Running Different Test Modes

### 1. Super Quick Test (30 seconds) - DEFAULT
```bash
# This now runs by default
docker-compose up rag_pipeline

# Or restart the container
docker-compose restart rag_pipeline
```
**Tests:** 1 test case, 1 model combination (nomic-embed-text + llama3.2:1b)

### 2. Quick Test (1-2 minutes)
```bash
# Override the command
docker-compose run --rm rag_pipeline python main.py --quick
```
**Tests:** 2 test cases, 1 model combination

### 3. Full Evaluation (10+ minutes)
```bash
# Override the command for full evaluation
docker-compose run --rm rag_pipeline python main.py --full
```
**Tests:** All test cases, all model combinations (nomic-embed-text + mxbai-embed-large × llama3.2:1b + gemma3:4b)

## Why Your Previous Run Was Slow

Looking at your logs, you were running the **full evaluation**:
- Processing `batch 6/20` (20 batches total)
- Using `gemma3:4b` model (slower than llama3.2:1b)  
- Testing all model combinations
- Each LLM call taking 4-10 seconds

## Stopping Long-Running Containers

```bash
# Stop the current container
docker-compose down rag_pipeline

# Remove and restart with quick test
docker-compose up rag_pipeline
```

## Monitoring Progress

```bash
# Watch the logs
docker-compose logs -f rag_pipeline
```

The new super-quick test should complete in ~30 seconds and show:
```
⚡ Super quick test completed successfully!
Best combination: nomic-embed-text_llama3.2:1b
Pipeline is working correctly!
``` 