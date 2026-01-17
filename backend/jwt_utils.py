# import jwt
# from datetime import datetime, timedelta

# # 🔐 Secret key (for development)
# SECRET_KEY = "my_super_secret_key_123456"

# # ⏰ Token expiry
# TOKEN_EXPIRE_HOURS = 1


# def create_access_token(payload: dict):
#     """
#     payload example:
#     {
#         "user_id": 1,
#         "role": "admin"
#     }
#     """
#     data = payload.copy()
#     data["exp"] = datetime.utcnow() + timedelta(hours=TOKEN_EXPIRE_HOURS)

#     token = jwt.encode(data, SECRET_KEY, algorithm="HS256")
#     return token


# def decode_access_token(token: str):
#     try:
#         decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
#         return decoded
#     except jwt.ExpiredSignatureError:
#         return None
#     except jwt.InvalidTokenError:
#         return None



# import jwt
# from datetime import datetime, timedelta
# from functools import wraps
# from flask import request, jsonify

# # 🔐 Secret key
# SECRET_KEY = "my_super_secret_key_123456"

# # ⏰ Token expiry
# TOKEN_EXPIRE_HOURS = 1


# # ----------------------------
# # CREATE TOKEN
# # ----------------------------
# def create_token(username, role):
#     payload = {
#         "username": username,
#         "role": role,
#         "exp": datetime.utcnow() + timedelta(hours=TOKEN_EXPIRE_HOURS)
#     }
#     return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


# # ----------------------------
# # DECODE TOKEN
# # ----------------------------
# def decode_token(token):
#     try:
#         return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
#     except jwt.ExpiredSignatureError:
#         return None
#     except jwt.InvalidTokenError:
#         return None


# # ----------------------------
# # TOKEN REQUIRED DECORATOR
# # ----------------------------
# def token_required(role=None):
#     def decorator(f):
#         @wraps(f)
#         def wrapper(*args, **kwargs):
#             auth_header = request.headers.get("Authorization")

#             if not auth_header:
#                 return jsonify({"detail": "Authorization header missing"}), 401

#             try:
#                 token = auth_header.split(" ")[1]
#             except IndexError:
#                 return jsonify({"detail": "Invalid token format"}), 401

#             payload = decode_token(token)
#             if not payload:
#                 return jsonify({"detail": "Invalid or expired token"}), 401

#             if role and payload["role"] != role:
#                 return jsonify({"detail": "Unauthorized access"}), 403

#             # attach info to request
#             request.username = payload["username"]
#             request.role = payload["role"]

#             return f(*args, **kwargs)
#         return wrapper
#     return decorator



import jwt
from datetime import datetime, timedelta
from functools import wraps
from flask import request, jsonify

SECRET_KEY = "my_super_secret_key_123456"
TOKEN_EXPIRE_HOURS = 1


def create_access_token(payload: dict):
    data = payload.copy()
    data["exp"] = datetime.utcnow() + timedelta(hours=TOKEN_EXPIRE_HOURS)
    return jwt.encode(data, SECRET_KEY, algorithm="HS256")


def decode_access_token(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


def token_required(role=None):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            auth_header = request.headers.get("Authorization")

            if not auth_header or not auth_header.startswith("Bearer "):
                return jsonify({"detail": "Token missing"}), 401

            token = auth_header.split(" ")[1]
            payload = decode_access_token(token)

            if not payload:
                return jsonify({"detail": "Invalid or expired token"}), 401

            if role and payload.get("role") != role:
                return jsonify({"detail": "Unauthorized"}), 403

            request.user_id = payload["user_id"]
            request.user_role = payload["role"]

            return fn(*args, **kwargs)
        return wrapper
    return decorator
