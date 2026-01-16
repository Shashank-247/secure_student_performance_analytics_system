from db import get_db

try:
    db = get_db()
    print("✅ Database connected successfully")
    db.close()
except Exception as e:
    print("❌ Database connection failed")
    print(e)
