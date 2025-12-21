# Lightweight production Dockerfile for FastAPI + Gunicorn/Uvicorn
FROM python:3.10-slim

# Environment
ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1 \
	PORT=8000

# Install minimal system deps (curl for healthcheck)
RUN apt-get update && apt-get install -y --no-install-recommends \
	curl \
	&& rm -rf /var/lib/apt/lists/*

# Workdir
WORKDIR /app

# Copy project files first (needed for -e . in requirements.txt)
COPY . .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
	&& pip install --no-cache-dir -r requirements.txt

# Optional: create non-root user
RUN useradd -ms /bin/bash appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Healthcheck hitting the root endpoint
HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
  CMD curl -fsS http://localhost:8000/ || exit 1

# Start with Gunicorn using Uvicorn workers
# Adjust workers via ECS task CPU; 2 is safe default for small tasks
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "app:app", "--workers", "2", "--bind", "0.0.0.0:8000"]
