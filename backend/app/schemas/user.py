# from pydantic import BaseModel

# class LoginRequest(BaseModel):
#     username: str
#     password: str


from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    username: str
    role: str

    class Config:
        orm_mode = True
