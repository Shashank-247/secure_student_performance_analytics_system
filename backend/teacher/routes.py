# from flask import Blueprint, request, jsonify

# teacher_bp = Blueprint('teacher', __name__, url_prefix='/teacher')

# @teacher_bp.route('/dashboard', methods=['GET'])
# def teacher_dashboard():
#     return jsonify({
#         "avgScore": 80,
#         "avgAttendance": 85,
#         "totalStudents": 20,
#         "atRisk": 3,
#         "students": [
#             {"id": 1, "name": "Student 1", "score": 80, "grade": "B", "attendance": 90},
#             {"id": 2, "name": "Student 2", "score": 60, "grade": "C", "attendance": 70}
#         ]
#     })


from flask import Blueprint, request, jsonify
from db import get_db
from jwt_utils import token_required

teacher_bp = Blueprint('teacher', __name__)

# Dashboard
@teacher_bp.route('/dashboard', methods=['GET'])
@token_required(role='teacher')
def dashboard():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    total_students = len(students)
    avgScore = sum(s['score'] for s in students)/total_students
    avgAttendance = sum(s['attendance'] for s in students)/total_students
    atRisk = len([s for s in students if s['score']<65 or s['attendance']<75])

    return jsonify({
        "avgScore": avgScore,
        "avgAttendance": avgAttendance,
        "totalStudents": total_students,
        "atRisk": atRisk,
        "students": students
    })

# Students list
@teacher_bp.route('/students', methods=['GET'])
@token_required(role='teacher')
def students():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT id, roll, name, avg_score, attendance FROM students")
    return jsonify(cursor.fetchall())

# Update marks/attendance
@teacher_bp.route('/student/<int:student_id>', methods=['PUT'])
@token_required(role='teacher')
def update_student(student_id):
    data = request.get_json()
    score = data['score']
    attendance = data['attendance']
    db = get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE students SET score=%s, attendance=%s WHERE id=%s", (score, attendance, student_id))
    db.commit()
    return jsonify({"message": "Student updated"})

# Analytics
@teacher_bp.route('/analytics', methods=['GET'])
@token_required(role='teacher')
def analytics():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT id, name, avg_score, attendance FROM students")
    students = cursor.fetchall()
    return jsonify(students)
