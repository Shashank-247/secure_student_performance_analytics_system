# backend/api/models.py

class User:
    def __init__(self, user_id, email, role):
        self.user_id = user_id
        self.email = email
        self.role = role


class Student:
    def __init__(self, student_id, name, student_class):
        self.student_id = student_id
        self.name = name
        self.student_class = student_class
