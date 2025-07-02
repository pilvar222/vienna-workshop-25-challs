FROM php:8.2-cli

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Copy flag to root directory
COPY flag.txt /flag.txt

# Expose port 9001
EXPOSE 9001

# Run PHP development server
CMD ["php", "-S", "0.0.0.0:9001"] 