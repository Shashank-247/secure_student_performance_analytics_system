# backend/api/routes/student.py

from fastapi import APIRouter
from backend.api.database import students

router = APIRouter()

@router.get("/dashboard")
def student_dashboard():
    return {
        "message": "Student Dashboard",
        "data": students
    }
