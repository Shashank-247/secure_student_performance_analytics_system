# from flask import Blueprint, request, jsonify

# admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# # Example route
# @admin_bp.route('/dashboard', methods=['GET'])
# def get_dashboard():
#     # Here you would fetch data from DB
#     return jsonify({
#         "total_users": 10,
#         "students": 5,
#         "teachers": 3,
#         "pending": 2
#     })


from flask import Blueprint, request, jsonify

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# Dashboard endpoint
@admin_bp.route('/dashboard', methods=['GET'])
def admin_dashboard():
    return jsonify({
        "total_users": 10,
        "students": 5,
        "teachers": 3,
        "pending": 2
    })

# Users endpoint
@admin_bp.route('/users', methods=['GET'])
def get_users():
    # Fetch users from DB
    users = [
        {"id": 1, "name": "Amit", "role": "student", "status": "Pending"},
        {"id": 2, "name": "Rahul", "role": "teacher", "status": "Active"}
    ]
    return jsonify(users)

# Approve user
@admin_bp.route('/users/<int:user_id>/approve', methods=['PUT'])
def approve_user(user_id):
    # Update DB to approve user_id
    return jsonify({"message": f"user {user_id} approved"})

# Reject user
@admin_bp.route('/users/<int:user_id>/reject', methods=['PUT'])
def reject_user(user_id):
    # Update DB to reject user_id
    return jsonify({"message": f"user {user_id} rejected"})

# Disable user
@admin_bp.route('/users/<int:user_id>/disable', methods=['PUT'])
def disable_user(user_id):
    # Update DB to disable user_id
    return jsonify({"message": f"user {user_id} disabled"})

# Change role
@admin_bp.route('/users/<int:user_id>/role', methods=['PUT'])
def change_role(user_id):
    data = request.get_json()
    # Update DB to change role of user_id
    return jsonify({"message": f"user {user_id} role updated to {data.get('role')}"})

# Settings GET
@admin_bp.route('/settings', methods=['GET'])
def get_settings():
    settings = {
        "registration_enabled": True,
        "two_factor_enabled": False,
        "session_timeout": 30,
        "password_policy": {
            "min_length": 8,
            "uppercase": True,
            "numbers": True,
            "special": False
        }
    }
    return jsonify(settings)

# Settings PUT
@admin_bp.route('/settings', methods=['PUT'])
def update_settings():
    data = request.get_json()
    # Save settings to DB
    return jsonify({"message": "Settings updated"})

# Logs
@admin_bp.route('/logs', methods=['GET'])
def get_logs():
    logs = [
        {"time": "2026-01-05 10:00", "user": "Amit", "role": "admin", "event": "LOGIN", "description": "Logged in", "ip": "127.0.0.1"}
    ]
    return jsonify(logs)
