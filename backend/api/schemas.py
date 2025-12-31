# backend/api/schemas.py

from pydantic import BaseModel

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    role: str


class StudentSchema(BaseModel):
    student_id: int
    name: str
    class_: str
    marks: int
    attendance: str
