FROM python:3.11-slim

WORKDIR /app

# Install Flask
RUN pip install flask

# Copy the flag directory structure from parent directory
COPY . /app/

# Expose port
EXPOSE 9010

# Run the application
CMD ["python", "app.py"] 