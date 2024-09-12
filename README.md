Here's a detailed `README.md` for your Book Management API project, explaining how to set up, run, and use the project:

---

# Book Management API

This is a simple REST API for managing books with full CRUD (Create, Read, Update, Delete) operations. The API is built with FastAPI, SQLAlchemy for database interactions, PostgreSQL as the database, and Docker for containerization.

## Table of Contents

1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Requirements](#requirements)
4. [Project Setup](#project-setup)
5. [Running with Docker](#running-with-docker)
6. [API Documentation](#api-documentation)
7. [Testing](#testing)
8. [Environment Variables](#environment-variables)


## Features

- **CRUD Operations**: Manage books with Create, Read, Update, Delete functionality.
- **Pagination**: Supports pagination for listing books.
- **API Documentation**: Auto-generated Swagger UI and ReDoc documentation.
- **PostgreSQL Integration**: Uses PostgreSQL for data storage.
- **Containerized**: Docker support for easy setup and deployment.

## Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Containerization**: Docker
- **Testing**: Pytest with FastAPI TestClient and SQLite (for tests)

## Requirements

- Docker
- Docker Compose

## Project Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/book-management-api.git
   cd book-management-api
   ```

2. Create a `.env` file in the root directory (next to `docker-compose.yml`) and add the following variables:

   ```bash
   POSTGRES_USER=your_postgres_user
   POSTGRES_PASSWORD=your_postgres_password
   POSTGRES_DB=book_db
   DATABASE_URL=postgresql://your_postgres_user:your_postgres_password@db:5432/book_db
   ```

3. Install Docker if you haven't already. Follow the instructions from the [Docker website](https://docs.docker.com/get-docker/).

## Running with Docker

1. Build and start the containers using Docker Compose:

   ```bash
   docker-compose up --build
   ```

   This will:

   - Build the FastAPI app image.
   - Start a PostgreSQL container.
   - Start the FastAPI container and serve the app.

2. Once the app is running, you can access it at [http://localhost:8000](http://localhost:8000).

## API Documentation

FastAPI automatically generates interactive API documentation via Swagger UI and ReDoc.

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Example Endpoints

- **List Books (with pagination)**: `GET /v1/books`
- **Create a Book**: `POST /v1/books`
- **Get a Book by ID**: `GET /v1/books/{book_id}`
- **Update a Book**: `PUT /v1/books/{book_id}`
- **Delete a Book**: `DELETE /v1/books/{book_id}`

## Testing

This project uses Pytest for testing, and the tests run against an in-memory SQLite database. The test client is built using FastAPI's TestClient.

1. To run the tests, first, install the necessary dependencies:

   ```bash
   pip install pytest
   ```

2. Then, run the tests:

   ```bash
   pytest
   ```

3. Test Output:

   Each test will output a success message if it passes, e.g.:

   ```
   test_get_all_books_empty passed
   test_create_book passed
   test_get_book_by_id passed
   test_update_book passed
   test_delete_book passed
   ```

## Environment Variables

The project requires the following environment variables:

- `POSTGRES_USER`: PostgreSQL user.
- `POSTGRES_PASSWORD`: PostgreSQL password.
- `POSTGRES_DB`: The name of the PostgreSQL database.
- `DATABASE_URL`: The URL of the PostgreSQL database (e.g., `postgresql://user:password@db:5432/book_db`).

Make sure to set these variables either in the `.env` file or your environment.



---

This `README.md` should provide a comprehensive guide for anyone setting up, running, or contributing to the project. If you have any additional information you'd like to include, feel free to adjust accordingly!