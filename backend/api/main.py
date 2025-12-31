# backend/api/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api import admin, teacher, student
from backend.api.auth_routes import router as auth_router

app = FastAPI(title="Secure Student Analytics System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(admin.router)
app.include_router(teacher.router)
app.include_router(student.router)
