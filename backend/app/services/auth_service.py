# from app.database.db import get_db
# from app.core.security import verify_password

# def authenticate_user(username, password):
#     db = get_db()
#     cursor = db.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
#     user = cursor.fetchone()
#     if not user:
#         return None
#     if not verify_password(password, user["password"]):
#         return None
#     return {"username": user["username"], "role": user["role"]}


from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import verify_password

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if user and verify_password(password, user.password):
        return {"username": user.username, "role": user.role}
    return None
