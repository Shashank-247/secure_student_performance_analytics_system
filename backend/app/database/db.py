# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import os
# from dotenv import load_dotenv

# backend/app/database/db.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

DB_HOST = os.getenv("database-1.cpmwmw02uxdq.ap-south-1.rds.amazonaws.com")
DB_USER = os.getenv("admin")
DB_PASSWORD = os.getenv("87654321")
DB_NAME = os.getenv("database-1")
DB_PORT = os.getenv("DB_PORT", 3306)

# DATABASE_URL = "mysql+pymysql://admin:87654321@database-1.cpmwmw02uxdq.ap-south-1.rds.amazonaws.com:3306/student_db"
DATABASE_URL = "mysql+pymysql://admin:87654321@database-1.cpmwmw02uxdq.ap-south-1.rds.amazonaws.com:3306/student_db"



# # Create engine and session
# engine = create_engine(DATABASE_URL, echo=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# # Dependency for FastAPI
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()