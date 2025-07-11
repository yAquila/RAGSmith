FROM python:3.9-slim

# Install system dependencies for GPU support and PyTorch
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Create cache directory for reranker models with proper permissions
RUN mkdir -p /root/.cache/rag_pipeline/reranker_models && \
    chmod -R 755 /root/.cache/rag_pipeline

# Copy application code
COPY . .

# Default to super-quick test (30 seconds)
CMD ["python", "main.py", "--full"] 