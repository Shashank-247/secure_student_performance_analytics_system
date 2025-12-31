from fastapi import APIRouter, Depends
from backend.api.auth import get_current_user
from backend.api.database import get_db_connection

router = APIRouter(prefix="/teacher", tags=["Teacher"])

@router.get("/students")
def view_students(current_user=Depends(get_current_user)):
    if current_user["role"] != "teacher":
        return {"error": "Not allowed"}

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM teacher_view")
    return cursor.fetchall()
