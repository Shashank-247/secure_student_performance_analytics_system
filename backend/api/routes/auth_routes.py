# backend/api/auth_routes.py

from fastapi import APIRouter, HTTPException
from backend.api.database import get_db_connection
from backend.api.auth import verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(email: str, password: str):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT user_id, email, password_hash, role, linked_id FROM users WHERE email=%s",
        (email,)
    )
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if not user or not verify_password(password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token({
        "user_id": user["user_id"],
        "role": user["role"],
        "linked_id": user["linked_id"]
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": user["role"]
    }
