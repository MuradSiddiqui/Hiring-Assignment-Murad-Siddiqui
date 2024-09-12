import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.core.database import Base, get_db
from app.schemas.book_schema import BookCreate

# Set up a test database in memory for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency override for testing
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

# Override the database dependency in the FastAPI app
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

# Create tables for the test database
@pytest.fixture(scope="module")
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


# Test to get all books (initially it should return an empty list)
def test_get_all_books_empty(setup_database):
    response = client.get("/v1/books/")
    assert response.status_code == 200
    assert response.json() == []
    print("test_get_all_books_empty passed")


# Test to create a new book
def test_create_book(setup_database):
    book_data = {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "published_year": 1925,
        "isbn": "978-3-16-148410-0",
        "available": True
    }
    response = client.post("/v1/books/", json=book_data)
    assert response.status_code == 200
    assert response.json()["title"] == "The Great Gatsby"
    assert response.json()["author"] == "F. Scott Fitzgerald"
    assert response.json()["isbn"] == "978-3-16-148410-0"
    print("test_create_book passed")


# Test to retrieve a book by ID
def test_get_book_by_id(setup_database):
    response = client.get("/v1/books/1")
    assert response.status_code == 200
    assert response.json()["title"] == "The Great Gatsby"
    assert response.json()["id"] == 1
    print("test_get_book_by_id passed")


# Test to update a book
def test_update_book(setup_database):
    update_data = {
        "title": "The Great Gatsby - Updated",
        "author": "F. Scott Fitzgerald",
        "published_year": 1925,
        "isbn": "978-3-16-148410-0",
        "available": False
    }
    response = client.put("/v1/books/1", json=update_data)
    assert response.status_code == 200
    assert response.json()["title"] == "The Great Gatsby - Updated"
    assert response.json()["available"] is False
    print("test_update_book passed")


# Test to delete a book
def test_delete_book(setup_database):
    response = client.delete("/v1/books/1")
    assert response.status_code == 200

    # Check that the book no longer exists
    get_response = client.get("/v1/books/1")
    assert get_response.status_code == 404
    print("test_delete_book passed")
