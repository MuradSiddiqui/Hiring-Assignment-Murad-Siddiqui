from fastapi import FastAPI
from app.api.v1 import router as v1_router
from app.core.database import create_tables

# Initialize FastAPI app with metadata for Swagger documentation
app = FastAPI(
    title="Book Management API",
    description="An API for managing books with full CRUD operations. Built with FastAPI, PostgreSQL, and Docker.",
    version="1.0.0",
    contact={
        "name": "API Support",
        "email": "support@bookapi.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

# Ensure tables are created when the app starts
@app.on_event("startup")
def on_startup():
    create_tables()

app.include_router(v1_router, prefix="/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Management API"}
