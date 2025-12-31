from fastapi import APIRouter, Depends
from backend.api.auth import get_current_user
from backend.api.database import get_db_connection

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/dashboard")
def admin_dashboard(current_user=Depends(get_current_user)):
    if current_user["role"] != "admin":
        return {"error": "Not allowed"}

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM admin_view")
    return cursor.fetchall()
