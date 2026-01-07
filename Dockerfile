# Dockerfile
FROM docker.io/library/python:3.12.2-slim

# Set the Current Working Directory inside the container
WORKDIR /app
RUN mkdir /env

# Copy the application code to the working directory
COPY requirements.txt .
COPY main.py .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Expose port 8080 to the outside world
EXPOSE 8080

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "main:app", "--reload","--host", "0.0.0.0", "--port", "8080"]
