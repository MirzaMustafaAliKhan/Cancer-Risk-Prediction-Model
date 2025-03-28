# Use lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose port used by Uvicorn
EXPOSE 8080

# Run FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]


# docker login (login into docker)
# docker ps -a (preview container details)
# docker images (preview images)
# docker ps (preview current running container details)