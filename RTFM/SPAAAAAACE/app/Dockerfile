FROM python:3.11-slim

# Install OpenSSL for certificate generation
RUN apt-get update && apt-get install -y openssl && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy certificate generation script
COPY generate_cert.sh .
RUN chmod +x generate_cert.sh

# Generate self-signed certificate
RUN ./generate_cert.sh

# Copy application code
COPY app.py .

# Expose port 443
EXPOSE 443

# Run the application
CMD ["python", "app.py"] 