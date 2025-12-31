from fastapi import FastAPI
from backend.api.routes import admin, teacher, student
from backend.api.routes.auth_routes import router as auth_router

app = FastAPI(title="Secure Student Analytics System")

# Auth
app.include_router(auth_router, prefix="/auth", tags=["Auth"])

# Role based routes
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(teacher.router, prefix="/teacher", tags=["Teacher"])
app.include_router(student.router, prefix="/student", tags=["Student"])

@app.get("/")
def root():
    return {"message": "API is running"}
