from fastapi import APIRouter, Depends, HTTPException
from backend.api.auth import get_current_user

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

@router.get("/dashboard")
def admin_dashboard(current_user=Depends(get_current_user)):
    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=403,
            detail="Not allowed"
        )

    return {
        "message": "Welcome Admin",
        "user_id": current_user["user_id"]
    }
