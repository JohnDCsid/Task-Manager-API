# syntax=docker/dockerfile:1
FROM python:3.12-slim


ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1


WORKDIR /app


# System deps (optional but useful)
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    build-essential curl && rm -rf /var/lib/apt/lists/*


COPY requirements.txt ./
RUN pip install -r requirements.txt


COPY . .


EXPOSE 5000


# Use gunicorn to serve the app in container
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:create_app()"]
