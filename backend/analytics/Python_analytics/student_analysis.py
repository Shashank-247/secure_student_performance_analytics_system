from utils import get_db_connection

def get_student_report(student_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT s.student_name, s.class,
           a.english, a.hindi, a.maths, a.science, a.sst,
           a.total, a.grade, a.attendance
    FROM students s
    JOIN academic_records a ON s.student_id = a.student_id
    WHERE s.student_id = %s
    """
    cursor.execute(query, (student_id,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()
    return result
