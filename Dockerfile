# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the Flask app
COPY . .

# Expose the port for Flask app
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
