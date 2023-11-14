# Stage 1: Build Stage
FROM python:3.8-slim AS builder

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Production Stage
FROM jenkins/jenkins:latest

USER root

RUN apt-get update && apt-get install -y docker.io

# Copy the built artifacts from the builder stage
COPY --from=builder /app /app

WORKDIR /app

EXPOSE 5000

CMD ["python", "app.py"]
