from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.book_repository import BookRepository
from app.schemas.book_schema import BookCreate, BookUpdate

class BookService:
    """
    Service layer for handling book-related business logic.
    This class follows the Single Responsibility Principle (SRP) by handling all business rules for the Book entity.
    It delegates database operations to the BookRepository, adhering to the Dependency Inversion Principle (DIP).
    """

    @staticmethod
    def get_all_books(db: Session, skip: int = 0, limit: int = 10):
        """
        Retrieves books with pagination.
        :param db: Database session
        :param skip: The number of records to skip
        :param limit: The maximum number of records to return
        """
        return BookRepository.get_all_books(db, skip=skip, limit=limit)

    @staticmethod
    def get_book_by_id(db: Session, book_id: int):
        """
        Retrieve a specific book by ID.
        If the book is not found, raise an HTTP 404 exception.
        """
        book = BookRepository.get_book_by_id(db, book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found.")
        return book

    @staticmethod
    def create_book(db: Session, book_create: BookCreate):
        """
        Create a new book in the database.
        This method validates the input using the Pydantic schema and calls the repository to persist the data.
        """
        return BookRepository.create_book(db, book_create)

    @staticmethod
    def update_book(db: Session, book_id: int, book_update: BookUpdate):
        """
        Update an existing book in the database by its ID.
        The method checks if the book exists and updates only the fields provided in the update schema.
        """
        db_book = BookRepository.get_book_by_id(db, book_id)
        if not db_book:
            raise HTTPException(status_code=404, detail="Book not found.")
        
        # Delegate the update operation to the repository
        return BookRepository.update_book(db, db_book, book_update)

    @staticmethod
    def delete_book(db: Session, book_id: int):
        """
        Delete a book from the database by its ID.
        The method checks if the book exists and deletes it if found.
        """
        db_book = BookRepository.get_book_by_id(db, book_id)
        if not db_book:
            raise HTTPException(status_code=404, detail="Book not found.")
        
        # Delegate the delete operation to the repository
        return BookRepository.delete_book(db, db_book)
