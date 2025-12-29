from fastapi import FastAPI
from backend.api.database import get_db_connection
from backend.api.routes import admin, teacher, student

app = FastAPI(title="Secure Student Analytics System")

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/test-db")
def test_db():
    db = get_db_connection()
    if db:
        return {"status": "Database connected successfully"}
    return {"status": "Database connection failed"}

# Register routes
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(teacher.router, prefix="/teacher", tags=["Teacher"])
app.include_router(student.router, prefix="/student", tags=["Student"])
