# Use an official Python image as the base
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir --timeout=120 -r requirements.txt

# Copy the application code
COPY ./app ./app

# Expose the port Uvicorn will run on
EXPOSE 8000

# Run the migration script and then start the application with Uvicorn
CMD ["sh", "-c", "python app/es_migration.py && uvicorn app.main:app --host 0.0.0.0 --port 8000"]