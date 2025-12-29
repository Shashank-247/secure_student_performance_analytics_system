from fastapi import APIRouter, HTTPException
from backend.api.auth import (
    verify_password,
    create_access_token,
    hash_password
)
from backend.api.database import get_db_connection

router = APIRouter()

@router.post("/login")
def login(email: str, password: str):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT user_id, password_hash, role FROM users WHERE email=%s",
        (email,)
    )
    user = cursor.fetchone()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not verify_password(password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token(
        data={
            "user_id": user["user_id"],
            "role": user["role"]
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": user["role"]
    }
