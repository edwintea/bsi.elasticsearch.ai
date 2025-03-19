# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError
import logging

# Database URL format: "mysql+pymysql://<username>:<password>@<host>/<dbname>"
DATABASE_URL = "mysql+pymysql://root:@localhost/ktbfuso"  # Blank password

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"charset": "utf8mb4"})

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
Base = declarative_base()

# Function to initialize the database
def init_db():
    try:
        Base.metadata.create_all(bind=engine)
        print("Database tables created successfully.")
    except SQLAlchemyError as e:
        logging.error(f"Error creating database tables: {e}")

# Dependency to get the database session
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()