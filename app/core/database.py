from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Create a new SQLAlchemy engine instance
engine = create_engine(settings.DATABASE_URL, echo=True)  # echo=True for SQL query logging (can be disabled in production)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative class definitions
Base = declarative_base()

def get_db():
    """
    Dependency that provides a new database session for each request and ensures it is closed after use.
    This is a context manager to handle session lifecycle cleanly.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
def create_tables():
    Base.metadata.create_all(bind=engine)