from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base

class Book(Base):
    """
    Book model represents a book entity in the database.
    Adheres to the Single Responsibility Principle (SRP) by only handling the book schema definition.
    """

    __tablename__ = "books"  # Name of the database table

    id = Column(Integer, primary_key=True, index=True)  # Auto-incrementing ID for each book
    title = Column(String, nullable=False)  # Book title, must be provided
    author = Column(String, nullable=False)  # Author's name, must be provided
    published_year = Column(Integer, nullable=False)  # Year the book was published
    isbn = Column(String, unique=True, nullable=False)  # ISBN number, must be unique
    available = Column(Boolean, default=True)  # Boolean indicating if the book is available

    def __repr__(self):
        """
        Representation of the Book object for debugging purposes.
        """
        return f"<Book(title='{self.title}', author='{self.author}', published_year={self.published_year}, available={self.available})>"
