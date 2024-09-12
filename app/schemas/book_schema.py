from pydantic import BaseModel, Field
from typing import Optional

class BookBase(BaseModel):
    """
    Base schema for a book containing fields that are common across different operations.
    """

    title: str = Field(..., example="The Great Gatsby")
    author: str = Field(..., example="F. Scott Fitzgerald")
    published_year: int = Field(..., ge=1500, le=2100, example=1925)  # Adding sensible year range
    isbn: str = Field(..., example="978-3-16-148410-0")
    available: Optional[bool] = Field(default=True, example=True)


class BookCreate(BookBase):
    """
    Schema for creating a book. Inherits from BookBase as all fields are required.
    """
    pass  # No additional fields needed for creation, just use the base schema


class BookUpdate(BaseModel):
    """
    Schema for updating book details. All fields are optional to allow partial updates.
    """

    title: Optional[str] = Field(None, example="The Great Gatsby")
    author: Optional[str] = Field(None, example="F. Scott Fitzgerald")
    published_year: Optional[int] = Field(None, ge=1500, le=2100, example=1925)
    isbn: Optional[str] = Field(None, example="978-3-16-148410-0")
    available: Optional[bool] = Field(default=True, example=True)


class BookResponse(BookBase):
    """
    Schema used for returning a book from the API. Adds the ID field.
    """

    id: int = Field(..., example=1)

    class Config:
        orm_mode = True  # Tells Pydantic to convert SQLAlchemy objects to Pydantic models
