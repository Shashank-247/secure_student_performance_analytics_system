# backend/api/auth_routes.py

from fastapi import APIRouter, HTTPException
from backend.api.database import users
from backend.api.auth import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(email: str, password: str):
    for user in users:
        if user["email"] == email and user["password"] == password:
            token = create_access_token({
                "user_id": user["user_id"],
                "role": user["role"]
            })
            return {
                "access_token": token,
                "token_type": "bearer",
                "role": user["role"]
            }

    raise HTTPException(status_code=401, detail="Invalid email or password")
