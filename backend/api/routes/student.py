# backend/api/student.py

from fastapi import APIRouter, Depends
from backend.api.auth import get_current_user
from backend.api.database import get_db_connection

router = APIRouter(prefix="/student", tags=["Student"])

@router.get("/dashboard")
def student_dashboard(current_user=Depends(get_current_user)):
    if current_user["role"] != "student":
        return {"error": "Not allowed"}

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM student_view WHERE student_id = %s",
        (current_user["linked_id"],)
    )

    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data
