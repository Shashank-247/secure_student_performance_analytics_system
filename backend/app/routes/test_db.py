# # app/routes/test_db.py

# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from app.database.db import get_db

# router = APIRouter()

# @router.get("/test-db")
# def test_database(db: Session = Depends(get_db)):
#     try:
#         db.execute("SELECT 1")
#         return {"status": "SUCCESS", "message": "AWS RDS connected"}
#     except Exception as e:
#         return {"status": "FAILED", "error": str(e)}


from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database.db import get_db

router = APIRouter()

@router.get("/test-db")
def test_database(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {
            "status": "SUCCESS",
            "message": "Backend successfully connected to AWS RDS"
        }
    except Exception as e:
        return {
            "status": "FAILED",
            "error": str(e)
        }
