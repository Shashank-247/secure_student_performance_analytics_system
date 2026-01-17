# import mysql.connector

# def get_db_connection():
#     return mysql.connector.connect(
        # host="database-1.cpmwmw02uxdq.ap-south-1.rds.amazonaws.com",
        # user="admin",
        # password="87654321",
        # database="database-1"
#     )




# DB_HOST = os.getenv("database-1.cpmwmw02uxdq.ap-south-1.rds.amazonaws.com")
# DB_USER = os.getenv("admin")
# DB_PASSWORD = os.getenv("87654321")
# DB_NAME = os.getenv("database-1")
# DB_PORT = os.getenv("DB_PORT", 3306)


# import mysql.connector
# from mysql.connector import Error

# # MySQL connection configuration
# DB_CONFIG = {
#     "host": "database-1.cpmwmw02uxdq.ap-south-1.rds.amazonaws.com",
#     "user": "admin",
#     "password": "87654321",
#     "database": "database-1"
# }

# # Helper: Get connection
# def get_connection():
#     try:
#         conn = mysql.connector.connect(**DB_CONFIG)
#         return conn
#     except Error as e:
#         print("Error connecting to MySQL:", e)
#         return None

# # Initialize DB (tables) if not exists
# def init_db():
#     conn = get_connection()
#     if not conn:
#         return
#     cursor = conn.cursor()
    
#     # Users table
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             username VARCHAR(50) UNIQUE NOT NULL,
#             password VARCHAR(255) NOT NULL,
#             role ENUM('student','teacher','admin') NOT NULL,
#             name VARCHAR(100) NOT NULL,
#             status ENUM('Pending','Active','Suspended','Rejected') DEFAULT 'Pending'
#         )
#     """)
    
#     # You can add other tables here: students, teacher_classes, logs, etc.
    
#     conn.commit()
#     cursor.close()
#     conn.close()

# # Fetch user by username
# def get_user_by_username(username):
#     conn = get_connection()
#     if not conn:
#         return None
#     cursor = conn.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
#     user = cursor.fetchone()
#     cursor.close()
#     conn.close()
#     return user

# # Create a new user
# def create_user(username, password, role, name):
#     conn = get_connection()
#     if not conn:
#         return
#     cursor = conn.cursor()
#     cursor.execute(
#         "INSERT INTO users (username, password, role, name) VALUES (%s,%s,%s,%s)",
#         (username, password, role, name)
#     )
#     conn.commit()
#     cursor.close()
#     conn.close()


# import mysql.connector

# # 🔧 DATABASE CONFIG (CHANGE THESE)
# DB_CONFIG = {
#          "host": "database-1.cpmwmw02uxdq.ap-south-1.rds.amazonaws.com",
#          "user": "admin",
#          "password": "87654321",
#          "database": "database-1"
# }


# # ✅ Get DB connection
# def get_db():
#     return mysql.connector.connect(**DB_CONFIG)


# # ✅ Get user by username (used in auth.py)
# def get_user_by_username(username):
#     db = get_db()
#     cursor = db.cursor(dictionary=True)

#     cursor.execute(
#         "SELECT id, username, password, role FROM users WHERE username=%s",
#         (username,)
#     )

#     user = cursor.fetchone()
#     cursor.close()
#     db.close()
#     return user


# # ✅ Create new user (used in register)
# def create_user(username, password, role, name):
#     db = get_db()
#     cursor = db.cursor()

#     cursor.execute(
#         """
#         INSERT INTO users (username, password, role, name, status)
#         VALUES (%s, %s, %s, %s, 'Pending')
#         """,
#         (username, password, role, name)
#     )

#     db.commit()
#     cursor.close()
#     db.close()


# import mysql.connector

# DB_CONFIG = {
#     "host": "localhost",
#     "user": "root",
#     "password": "Amit@123400",
#     "database": "student_analytics",
#     "port": 3306
# }

# def get_db():
#     return mysql.connector.connect(**DB_CONFIG)


import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Amit@123400",
    "database": "student_analytics",
    "port": 3306
}

def get_db():
    return mysql.connector.connect(**DB_CONFIG)


def get_user_by_email(email):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM users WHERE email = %s AND is_active = 1",
        (email,)
    )

    user = cursor.fetchone()
    cursor.close()
    db.close()
    return user


def get_user_by_username(username):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM users WHERE username = %s AND is_active = 1",
        (username,)
    )

    user = cursor.fetchone()
    cursor.close()
    db.close()
    return user


def create_user(username, email, password_hash, role, linked_id=None):
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        """
        INSERT INTO users (username, email, password_hash, role, linked_id, is_active)
        VALUES (%s, %s, %s, %s, %s, 1)
        """,
        (username, email, password_hash, role, linked_id)
    )

    db.commit()
    cursor.close()
    db.close()
