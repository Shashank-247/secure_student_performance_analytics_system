# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from flask import Flask
# from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
# from auth import login_user
# from db import get_db_connection


# app = Flask(__name__)
# # CORS(app)

# # ✅ Enable CORS for all routes and all origins
# CORS(app, supports_credentials=True)  # ye lin mene add kari hai cors(app) ko comment kara



# app.config["JWT_SECRET_KEY"] = "SUPER_SECRET_KEY_CHANGE_LATER"
# jwt = JWTManager(app)

# @app.route("/api/login", methods=["POST"])
# def login():
#     data = request.json
#     response, status = login_user(data)
#     return jsonify(response), status


# @app.route("/api/student/dashboard", methods=["GET"])
# @jwt_required()
# def student_dashboard():
#     identity = get_jwt_identity()
#     if identity["role"] != "student":
#         return {"msg": "Unauthorized"}, 403

#     conn = get_db_connection()
#     cursor = conn.cursor(dictionary=True)

#     cursor.execute(
#         "SELECT * FROM academic_records WHERE student_id=%s",
#         (identity["user_id"],)
#     )
#     data = cursor.fetchall()

#     cursor.close()
#     conn.close()
#     return jsonify(data), 200


# @app.route("/api/teacher/dashboard", methods=["GET"])
# @jwt_required()
# def teacher_dashboard():
#     identity = get_jwt_identity()
#     if identity["role"] != "teacher":
#         return {"msg": "Unauthorized"}, 403
#     return jsonify({"msg": "Teacher dashboard"}), 200


# @app.route("/api/admin/dashboard", methods=["GET"])
# @jwt_required()
# def admin_dashboard():
#     identity = get_jwt_identity()
#     if identity["role"] != "admin":
#         return {"msg": "Unauthorized"}, 403
#     return jsonify({"msg": "Admin dashboard"}), 200


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)


from flask import Flask
from flask_cors import CORS
from auth import auth_bp
from admin.routes import admin_bp
from student.routes import student_bp
from teacher.routes import teacher_bp

app = Flask(__name__)

# ✅ Secret key for JWT signing
app.config['SECRET_KEY'] = "my_super_secret_key_123456"  # Replace with your own secure key in production

# Enable CORS for frontend (Live Server)
CORS(app)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix="/api")
app.register_blueprint(admin_bp, url_prefix="/api/admin")
app.register_blueprint(student_bp, url_prefix="/api/student")
app.register_blueprint(teacher_bp, url_prefix="/api/teacher")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
