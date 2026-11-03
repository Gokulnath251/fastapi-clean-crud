# FastAPI Clean Architecture & CRUD Microservice

A production-grade REST API built with FastAPI, SQLAlchemy, and Pydantic V2, containerized with Docker and verified with automated Pytest suites.

## Features
- **Layered Clean Architecture**: Strict separation of database configuration, ORM models, Pydantic schemas, and route controllers.
- **Request Validation & Error Handling**: Strict type checking with automatic 422 Unprocessable Entity responses.
- **Data Security**: Response models filter sensitive internal fields from API responses.
- **Persistence**: Relational SQLite database with persistent Docker bind-mount storage.
- **Containerization**: Packaged via Docker for consistent cross-environment deployment.
- **Automated Testing**: Integration test suite verifying HTTP status codes and contract boundaries using Pytest and TestClient.

## Project Structure
```text
├── database.py       # SQLAlchemy engine & session dependency
├── models.py         # SQLAlchemy database models
├── schemas.py        # Pydantic validation & response schemas
├── main.py           # FastAPI routes & business logic
├── test_main.py      # Automated Pytest suite
├── Dockerfile        # Container build instructions
├── .dockerignore     # Build context exclusions
├── .gitignore        # Git tracking exclusions
└── requirements.txt  # Project dependencies
