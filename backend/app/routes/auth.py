# from fastapi import APIRouter, HTTPException
# from app.services.auth_service import authenticate_user

# router = APIRouter()

# @router.post("/login")
# def login(data: dict):
#     user = authenticate_user(data["username"], data["password"])
#     if not user:
#         raise HTTPException(status_code=401, detail="Invalid credentials")
#     return {"message": "Login successful", "role": user["role"]}


# from fastapi import APIRouter, Depends, HTTPException
# from app.schemas.user import LoginRequest
# from app.services.auth_service import authenticate_user

# router = APIRouter()

# @router.post("/login")
# def login(request: LoginRequest):
#     user = authenticate_user(request.username, request.password)
#     if not user:
#         raise HTTPException(status_code=401, detail="Invalid username or password")
#     return {"message": f"Welcome {user['username']}!"}


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import LoginRequest, UserResponse
from app.services.auth_service import authenticate_user
from app.database.db import get_db  # fixed import

router = APIRouter()

@router.post("/login", response_model=UserResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, request.username, request.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return user
