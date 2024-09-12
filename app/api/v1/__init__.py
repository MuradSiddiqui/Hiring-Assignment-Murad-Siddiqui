from fastapi import APIRouter
from app.api.v1.endpoints import books

# Create a main API router for version v1
router = APIRouter()

# Include the book-related routes from the books module
router.include_router(books.router, prefix="/books", tags=["Books"])
