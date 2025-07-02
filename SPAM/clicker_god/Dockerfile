# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .
COPY templates/ templates/
COPY gunicorn_config.py .

# Create directories for Flask-Session files
RUN mkdir -p /tmp/flask_session && \
    chmod 777 /tmp/flask_session

# Create non-root user for security
RUN groupadd -r ctfuser && useradd -r -g ctfuser ctfuser
RUN chown -R ctfuser:ctfuser /app /tmp/flask_session

# Expose port 5001 (matching gunicorn config)
EXPOSE 5001

# Set environment variables
ENV ENVIRONMENT=production
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Switch to non-root user
USER ctfuser

# Run with Gunicorn for production
CMD ["gunicorn", "--config", "gunicorn_config.py", "app:app"] 