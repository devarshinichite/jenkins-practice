# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Create and set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY app.py .

# Set the command to run the application
CMD ["python", "app.py"]

# Expose the port the app runs on
EXPOSE 5000

