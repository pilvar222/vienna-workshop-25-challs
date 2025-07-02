FROM node:18-alpine

# Install security updates
RUN apk update && apk upgrade

# Create app directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install --only=production

# Create a non-root user
RUN addgroup -g 1001 -S appgroup && \
    adduser -S appuser -u 1001 -G appgroup

# Copy application code
COPY . .

# Create the flag file in the root directory
COPY flag.txt /flag.txt

# Set proper permissions
RUN chown -R appuser:appgroup /app && \
    chmod -R 755 /app && \
    chown root:root /flag.txt && \
    chmod 644 /flag.txt

# Create some additional system files for realism
RUN echo "root:x:0:0:root:/root:/bin/sh" > /etc/passwd.bak && \
    echo "Vienna Hacking Bootcamp System" > /etc/hostname && \
    echo "127.0.0.1 localhost" > /etc/hosts.bak

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD node -e "const http = require('http'); \
    const options = {hostname: 'localhost', port: 3000, path: '/', method: 'GET'}; \
    const req = http.request(options, (res) => { \
        process.exit(res.statusCode === 200 ? 0 : 1); \
    }); \
    req.on('error', () => process.exit(1)); \
    req.end();"

# Start the application
CMD ["npm", "start"] 