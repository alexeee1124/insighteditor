FROM python:3.11-slim

WORKDIR /app

# Copy all project files
COPY . /app

# Expose standard container port
EXPOSE 8080

ENV PORT=8080
ENV PYTHONUNBUFFERED=1

CMD ["python3", "server.py", "8080"]
