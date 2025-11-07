FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Run the application
CMD ["python", "app.py"]
