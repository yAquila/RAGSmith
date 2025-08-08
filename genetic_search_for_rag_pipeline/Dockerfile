# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app/genetic_search_for_rag_pipeline

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user for security
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app/genetic_search_for_rag_pipeline
USER appuser

# Expose port
EXPOSE 8009

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8009/health || exit 1

# Default command
CMD ["uvicorn", "genetic_search_for_rag_pipeline.api:app", "--host", "0.0.0.0", "--port", "8009"] 