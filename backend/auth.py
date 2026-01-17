# from db import get_db_connection
# from jwt_utils import generate_token
# import bcrypt

# def login_user(data):
#     username = data.get("username")
#     password = data.get("password")

#     if not username or not password:
#         return {"msg": "Missing credentials"}, 400

#     conn = get_db_connection()
#     cursor = conn.cursor(dictionary=True)

#     # Make sure your users table has 'password_hash' column
#     cursor.execute(
#         "SELECT id, password_hash, role FROM users WHERE username=%s",
#         (username,)
#     )
#     user = cursor.fetchone()

#     cursor.close()
#     conn.close()

#     if not user:
#         return {"msg": "Invalid credentials"}, 401

#     try:
#         # Password in DB is hashed
#         if bcrypt.checkpw(password.encode(), user["password_hash"].encode()):
#             token = generate_token(user["id"], user["role"])
#             return {"access_token": token, "role": user["role"]}, 200
#         else:
#             return {"msg": "Invalid credentials"}, 401
#     except Exception as e:
#         # Catch unexpected bcrypt errors
#         return {"msg": f"Server error: {str(e)}"}, 500




# from flask import Blueprint, request, jsonify
# from werkzeug.security import generate_password_hash, check_password_hash
# from db import get_user_by_username, create_user
# from jwt_utils import create_token

# auth_bp = Blueprint("auth", __name__)


# # ----------------------------
# # LOGIN
# # ----------------------------
# @auth_bp.route("/login", methods=["POST"])
# def login():
#     data = request.get_json()

#     username = data.get("username")
#     password = data.get("password")

#     if not username or not password:
#         return jsonify({"detail": "Missing username or password"}), 400

#     user = get_user_by_username(username)

#     if not user or not check_password_hash(user["password"], password):
#         return jsonify({"detail": "Invalid username or password"}), 401

#     # ✅ MATCHES jwt_utils.py
#     token = create_token(user["username"], user["role"])

#     return jsonify({
#         "access_token": token,
#         "role": user["role"]
#     })


# # ----------------------------
# # REGISTER
# # ----------------------------
# @auth_bp.route("/register", methods=["POST"])
# def register():
#     data = request.get_json()

#     username = data.get("username")
#     password = data.get("password")
#     role = data.get("role")
#     name = data.get("name")

#     if not username or not password or not role or not name:
#         return jsonify({"detail": "Missing required fields"}), 400

#     if get_user_by_username(username):
#         return jsonify({"detail": "Username already exists"}), 400

#     hashed_password = generate_password_hash(password)
#     create_user(username, hashed_password, role, name)

#     return jsonify({"detail": "Registration successful, pending admin approval"})



from db import get_user_by_email, get_user_by_username, create_user
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
# from db import get_user_by_email, create_user
from jwt_utils import create_access_token

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"detail": "Missing username or password"}), 400

    user = get_user_by_username(username)

    if not user or not check_password_hash(user["password_hash"], password):
        return jsonify({"detail": "Invalid username or password"}), 401

    token = create_access_token({
        "user_id": user["user_id"],
        "role": user["role"]
    })

    return jsonify({
        "access_token": token,
        "role": user["role"]
    })

# @auth_bp.route("/login", methods=["POST"])
# def login():
#     data = request.get_json()

#     email = data.get("email")
#     password = data.get("password")

#     if not email or not password:
#         return jsonify({"detail": "Missing email or password"}), 400

#     user = get_user_by_email(email)

#     if not user or not check_password_hash(user["password_hash"], password):
#         return jsonify({"detail": "Invalid email or password"}), 401

#     # token = create_token(user["email"], user["role"])
#     token = create_access_token({
#     "user_id": user["user_id"],
#     "role": user["role"]
#     })


#     return jsonify({
#         "access_token": token,
#         "role": user["role"]
#     })


# @auth_bp.route("/login", methods=["POST"])
# def login():
#     data = request.get_json()

#     email = data.get("email")
#     password = data.get("password")

#     if not email or not password:
#         return jsonify({"detail": "Missing email or password"}), 400

#     user = get_user_by_email(email)

#     if not user or not check_password_hash(user["password_hash"], password):
#         return jsonify({"detail": "Invalid email or password"}), 401

#     token = create_access_token({
#         "user_id": user["user_id"],
#         "role": user["role"]
#     })

#     return jsonify({
#         "access_token": token,
#         "role": user["role"]
#     })


# @auth_bp.route("/register", methods=["POST"])
# def register():
#     data = request.get_json()

#     email = data.get("email")
#     password = data.get("password")
#     role = data.get("role")

#     if not email or not password or not role:
#         return jsonify({"detail": "Missing fields"}), 400

#     if get_user_by_email(email):
#         return jsonify({"detail": "Email already exists"}), 400

#     hashed_password = generate_password_hash(password)
#     create_user(email, hashed_password, role)

#     return jsonify({"detail": "Registration successful"})

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role")

    if not username or not email or not password or not role:
        return jsonify({"detail": "Missing fields"}), 400

    if get_user_by_username(username):
        return jsonify({"detail": "Username already exists"}), 400

    if get_user_by_email(email):
        return jsonify({"detail": "Email already exists"}), 400

    hashed_password = generate_password_hash(password)

    create_user(username, email, hashed_password, role)

    return jsonify({"detail": "Registration successful"})

