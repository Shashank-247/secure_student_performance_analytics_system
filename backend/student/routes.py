# from flask import Blueprint, request, jsonify

# student_bp = Blueprint('student', __name__, url_prefix='/student')

# @student_bp.route('/dashboard', methods=['GET'])
# def student_dashboard():
#     # Example student data
#     return jsonify({
#         "name": "Amit Kumar",
#         "total_score": 450,
#         "grade": "A",
#         "attendance": 90,
#         "weekly_study_hours": 15,
#         "fees_status": "Paid",
#         "subjects": {
#             "Math": 90,
#             "English": 85,
#             "Science": 95
#         }
#     })


from flask import Blueprint, jsonify, request
from db import get_db
from jwt_utils import token_required

student_bp = Blueprint('student', __name__)

# Dashboard
@student_bp.route('/dashboard', methods=['GET'])
@token_required(role='student')
def dashboard():
    user_id = request.user_id  # set from token_required
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT name, total_score, grade, attendance, weekly_study_hours, fees_status 
        FROM students 
        WHERE id=%s
    """, (user_id,))
    student = cursor.fetchone()

    cursor.execute("SELECT subject, marks FROM marks WHERE student_id=%s", (user_id,))
    subjects = {row['subject']: row['marks'] for row in cursor.fetchall()}

    student['subjects'] = subjects
    return jsonify(student)

# Profile
@student_bp.route('/profile', methods=['GET'])
@token_required(role='student')
def profile():
    user_id = request.user_id
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students WHERE id=%s", (user_id,))
    profile = cursor.fetchone()
    return jsonify(profile)

# Performance
@student_bp.route('/performance', methods=['GET'])
@token_required(role='student')
def performance():
    user_id = request.user_id
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT subject, marks FROM marks WHERE student_id=%s", (user_id,))
    subjects = {row['subject']: row['marks'] for row in cursor.fetchall()}

    # Placeholder values; replace with DB queries if available
    monthly_trend = [80, 82, 85, 78, 90, 88]  
    attendance = 90  

    return jsonify({
        "subjects": subjects,
        "monthly_trend": monthly_trend,
        "attendance": attendance
    })
