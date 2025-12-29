# backend/api/routes/student.py

from fastapi import APIRouter, Depends
from backend.api.auth import get_current_user

router = APIRouter()

@router.get("/dashboard")
def student_dashboard(current_user: dict = Depends(get_current_user)):
    return {
        "message": "Student dashboard",
        "user": current_user
    }
