from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.book import Book
from app.schemas.book_schema import BookCreate, BookUpdate

class BookRepository:
    """
    Repository class for managing book database operations.
    It follows the Single Responsibility Principle (SRP) by encapsulating all 
    operations related to the Book model and database access.
    """

    @staticmethod
    def get_all_books(db: Session, skip: int = 0, limit: int = 10):
        """
        Retrieves books from the database with pagination.
        :param db: Database session
        :param skip: The number of records to skip
        :param limit: The maximum number of records to return
        """
        return db.query(Book).offset(skip).limit(limit).all()

    @staticmethod
    def get_book_by_id(db: Session, book_id: int) -> Optional[Book]:
        """
        Retrieve a book by its ID. 
        Returns None if the book is not found.
        """
        return db.query(Book).filter(Book.id == book_id).first()

    @staticmethod
    def create_book(db: Session, book: BookCreate) -> Book:
        """
        Create a new book in the database.
        The book is passed as a Pydantic schema object, which ensures the data is valid.
        """
        db_book = Book(
            title=book.title,
            author=book.author,
            published_year=book.published_year,
            isbn=book.isbn,
            available=book.available
        )
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book

    @staticmethod
    def update_book(db: Session, db_book: Book, book_update: BookUpdate) -> Book:
        """
        Update an existing book with new values. Fields in the book_update that are set 
        will overwrite the existing values in db_book.
        """
        for field, value in book_update.dict(exclude_unset=True).items():
            setattr(db_book, field, value)
        
        db.commit()
        db.refresh(db_book)
        return db_book

    @staticmethod
    def delete_book(db: Session, db_book: Book) -> None:
        """
        Delete a book from the database. 
        """
        db.delete(db_book)
        db.commit()

