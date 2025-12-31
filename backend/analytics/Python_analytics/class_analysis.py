from utils import get_db_connection

def get_class_average(class_name):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT s.class,
           AVG(a.total) AS avg_total,
           AVG(a.attendance) AS avg_attendance
    FROM students s
    JOIN academic_records a ON s.student_id = a.student_id
    WHERE s.class = %s
    GROUP BY s.class
    """
    cursor.execute(query, (class_name,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()
    return result
