# backend/api/routes/admin.py

from fastapi import APIRouter, Depends
from backend.api.auth import get_current_user

router = APIRouter()

@router.get("/dashboard")
def admin_dashboard(current_user: dict = Depends(get_current_user)):
    return {
        "message": "Admin dashboard",
        "user": current_user
    }
