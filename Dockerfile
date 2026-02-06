FROM python:3.13-slim

# Set working directory and copy requirements file
WORKDIR /app
COPY ./requirements.txt /app

# Install dependencies
RUN pip install -r requirements.txt

# Copy application code
COPY ./src/ /app

# Run the application
CMD ["python", "-m", "main"]