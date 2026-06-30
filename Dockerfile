# Use the official Python 3.11 image
FROM python:3.11-slim

# Prevent Python from creating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Ensure Python output appears immediately
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy dependency list
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Expose the FastAPI port
EXPOSE 8000

# Start the application
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]