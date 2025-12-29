# backend/api/routes/teacher.py

from fastapi import APIRouter, Depends
from backend.api.auth import get_current_user

router = APIRouter()

@router.get("/dashboard")
def teacher_dashboard(current_user: dict = Depends(get_current_user)):
    return {
        "message": "Teacher dashboard",
        "user": current_user
    }
