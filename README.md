# Task-Manager-API

A simple Flask REST API with **CRUD**, **Docker**, and **CI/CD (GitHub Actions)**.

---

## Live Demo
Try it here: [https://task-manager-api-w10t.onrender.com](https://task-manager-api-w10t.onrender.com)

- Health check: `GET /health`  
- Tasks CRUD: `/tasks` (GET, POST, PUT, DELETE)

---

## Status / Badges
<!-- Optional: Add CI and coverage badges -->
[![CI](https://github.com/JohnDCsid/Task-Manager-API/actions/workflows/ci.yml/badge.svg)](https://github.com/JohnDCsid/Task-Manager-API/actions)
[![Coverage](https://img.shields.io/badge/coverage-0%25-red)](https://github.com/JohnDCsid/Task-Manager-API)

---

## Quick Start (Local)

```bash
# Clone the repo
git clone https://github.com/<YOUR-USERNAME>/Task-Manager-API.git
cd Task-Manager-API

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py

# API available at: http://localhost:5000


##  Testing with curl

# Health check:

curl http://localhost:5000/health


# Create a task:

curl -X POST http://localhost:5000/tasks \
-H "Content-Type: application/json" \
-d '{"title":"Demo task"}'


# List tasks:

curl http://localhost:5000/tasks


# Complete a task:

curl -X PUT http://localhost:5000/tasks/1


# Delete a task:

curl -X DELETE http://localhost:5000/tasks/1

## Docker

docker build -t task-manager-api .
docker run -p 5000:5000 task-manager-api


## Tech Stack

Python 3.12

Flask

SQLAlchemy

## Docker

Render.com (deployment)

Pytest (tests & coverage)

GitHub Actions (CI/CD)

## Features

Full CRUD API for managing tasks

Health check endpoint

In-memory SQLite for testing / persistent SQLite for local use

Optional PostgreSQL for production via DATABASE_URL

Dockerized for easy deployment

CI/CD setup via GitHub Actions
