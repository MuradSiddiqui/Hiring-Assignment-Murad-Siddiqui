from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.schemas.book_schema import BookCreate, BookUpdate, BookResponse
from app.services.book_service import BookService
from app.core.database import get_db

# Define the API router for books
router = APIRouter()

@router.get("/", response_model=List[BookResponse], tags=["Books"])
def get_all_books(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),  # The number of records to skip
    limit: int = Query(10, gt=0),  # The number of records to return
):
    """
    Retrieve a paginated list of books.
    - `skip`: the number of books to skip (for pagination).
    - `limit`: the maximum number of books to return.
    """
    return BookService.get_all_books(db, skip=skip, limit=limit)

@router.post("/", response_model=BookResponse, tags=["Books"])
def create_book(book_create: BookCreate, db: Session = Depends(get_db)):
    """
    Create a new book in the database.
    The book data is validated via the BookCreate Pydantic schema.
    """
    return BookService.create_book(db, book_create)

@router.get("/{book_id}", response_model=BookResponse, tags=["Books"])
def get_book(book_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific book by ID.
    If the book is not found, an HTTP 404 error is raised.
    """
    return BookService.get_book_by_id(db, book_id)

@router.put("/{book_id}", response_model=BookResponse, tags=["Books"])
def update_book(book_id: int, book_update: BookUpdate, db: Session = Depends(get_db)):
    """
    Update an existing book by its ID.
    The service layer handles the update logic and partial updates are supported.
    """
    return BookService.update_book(db, book_id, book_update)

@router.delete("/{book_id}", tags=["Books"])
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """
    Delete a specific book by its ID.
    If the book is not found, an HTTP 404 error is raised.
    """
    return BookService.delete_book(db, book_id)
