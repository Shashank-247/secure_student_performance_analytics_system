# backend/api/routes/teacher.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard")
def teacher_dashboard():
    return {
        "message": "Teacher Dashboard",
        "can_edit_marks": True,
        "assigned_classes": ["9", "10"]
    }
