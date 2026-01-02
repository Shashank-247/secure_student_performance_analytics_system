-- CREATE DATABASE
CREATE DATABASE student_analytics;
USE student_analytics;

-- USERS TABLE
CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(150) UNIQUE,
    password_hash VARCHAR(255),
    role ENUM('admin','teacher','student') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- STUDENTS TABLE
CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    age INT,
    class VARCHAR(20),
    weekly_self_study_hours DECIMAL(4,2),
    gender VARCHAR(10),
    district VARCHAR(50),
    parent_name VARCHAR(100),
    parent_education VARCHAR(50)
);

-- TEACHERS TABLE
CREATE TABLE IF NOT EXISTS teachers (
    teacher_id INT PRIMARY KEY AUTO_INCREMENT,
    teacher_name VARCHAR(100),
    subject VARCHAR(50)
);

-- ACADEMIC RECORDS TABLE
CREATE TABLE IF NOT EXISTS academic_records (
    record_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    english INT CHECK (english BETWEEN 0 AND 100),
    hindi INT CHECK (hindi BETWEEN 0 AND 100),
    maths INT CHECK (maths BETWEEN 0 AND 100),
    science INT CHECK (science BETWEEN 0 AND 100),
    sst INT CHECK (sst BETWEEN 0 AND 100),
    total INT GENERATED ALWAYS AS (english + hindi + maths + science + sst) STORED,
    grade VARCHAR(2) GENERATED ALWAYS AS (
        CASE
            WHEN (english + hindi + maths + science + sst) >= 450 THEN 'A'
            WHEN (english + hindi + maths + science + sst) >= 400 THEN 'B'
            WHEN (english + hindi + maths + science + sst) >= 350 THEN 'C'
            WHEN (english + hindi + maths + science + sst) >= 300 THEN 'D'
            WHEN (english + hindi + maths + science + sst) >= 250 THEN 'E'
            ELSE 'F'
        END
    ) STORED,
    attendance INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- FEES TABLE
CREATE TABLE IF NOT EXISTS fees (
    fee_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    status ENUM('paid','unpaid'),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);


-- INSERT TEACHERS
INSERT INTO teachers (teacher_name, subject) VALUES
('Ayush Singh', 'Maths'),
('Sarita Mishra', 'Science'),
('Rohit Sharma', 'English'),
('Neha Singh', 'Hindi'),
('Amit Kumar', 'SST');

-- INSERT USERS STUDENTS
INSERT INTO users (username, password_hash, role)
SELECT CONCAT(student_name,'_',student_id),
       SHA2(CONCAT(student_id, student_name, '@12345'),256),
       'student'
FROM students;

-- INSERT USERS TEACHERS
INSERT INTO users (username, password_hash, role)
SELECT CONCAT(teacher_name,'_',teacher_id),
       SHA2(CONCAT(teacher_id, teacher_name, '@123'),256),
       'teacher'
FROM teachers;

-- INSERT ADMIN USER
INSERT INTO users (username, password_hash, role)
VALUES ('admin', SHA2('Admin@12345',256),'admin');

-- OVERALL SCHOOL ANALYTICS VIEW
CREATE OR REPLACE VIEW overall_school_analytics AS
SELECT COUNT(DISTINCT student_id) AS total_students,
       ROUND(AVG(total),2) AS school_avg_score
FROM academic_records;

-- LOW ATTENDANCE STUDENTS VIEW
CREATE OR REPLACE VIEW low_attendance_students AS
SELECT s.student_id, s.student_name, s.class, a.attendance
FROM students s
JOIN academic_records a ON s.student_id = a.student_id
WHERE a.attendance < 150;

-- CLASS AVG ATTENDANCE VIEW
CREATE OR REPLACE VIEW class_avg_attendance AS
SELECT s.class, ROUND(AVG(a.attendance),2) AS avg_attendance
FROM students s
JOIN academic_records a ON s.student_id = a.student_id
GROUP BY s.class;

-- CLASS PERFORMANCE VIEW
CREATE OR REPLACE VIEW class_performance AS
SELECT s.class, ROUND(AVG(a.total),2) AS avg_marks, ROUND(AVG(a.attendance),2) AS avg_attendance
FROM students s
JOIN academic_records a ON s.student_id = a.student_id
GROUP BY s.class;

-- GENDER PERFORMANCE VIEW
CREATE OR REPLACE VIEW gender_performance AS
SELECT s.gender, ROUND(AVG(a.total),2) AS avg_marks
FROM students s
JOIN academic_records a ON s.student_id = a.student_id
GROUP BY s.gender;

-- DISTRICT PERFORMANCE VIEW
CREATE OR REPLACE VIEW district_performance AS
SELECT s.district, ROUND(AVG(a.total),2) AS avg_marks
FROM students s
JOIN academic_records a ON s.student_id = a.student_id
GROUP BY s.district;

-- FEE DEFAULTERS VIEW
CREATE OR REPLACE VIEW fee_defaulters AS
SELECT s.class, COUNT(*) AS unpaid_students
FROM students s
JOIN fees f ON s.student_id = f.student_id
WHERE f.status = 'unpaid'
GROUP BY s.class;

-- PERFORMANCE DISTRIBUTION VIEW
CREATE OR REPLACE VIEW performance_distribution AS
SELECT CASE
           WHEN total >= 400 THEN 'Excellent'
           WHEN total >= 350 THEN 'Great'
           WHEN total >= 300 THEN 'Average'
           ELSE 'Needs Improvement'
       END AS performance_level,
       COUNT(*) AS total_students
FROM academic_records
GROUP BY performance_level;

-- TOP 10 STUDENTS VIEW
CREATE OR REPLACE VIEW top_10_students AS
SELECT s.student_id, s.student_name, s.class, a.total, a.grade
FROM students s
JOIN academic_records a ON s.student_id = a.student_id
ORDER BY a.total DESC
LIMIT 10;

-- BOTTOM 10 STUDENTS VIEW
CREATE OR REPLACE VIEW bottom_10_students AS
SELECT s.student_id, s.student_name, s.class, a.total, a.grade
FROM students s
JOIN academic_records a ON s.student_id = a.student_id
ORDER BY a.total ASC
LIMIT 10;

-- STUDENT SELF VIEW
CREATE OR REPLACE VIEW student_self_view AS
SELECT s.student_id, s.student_name, s.class, s.gender, s.district, s.weekly_self_study_hours,
       a.english, a.hindi, a.maths, a.science, a.sst, a.total, a.grade, a.attendance,
       f.status AS fees_status
FROM students s
JOIN academic_records a ON s.student_id = a.student_id
JOIN fees f ON s.student_id = f.student_id;

-- TEACHER VIEW
CREATE OR REPLACE VIEW teacher_view AS
SELECT s.student_id, s.student_name, s.class,
       a.english, a.hindi, a.maths, a.science, a.sst, a.total, a.grade, a.attendance
FROM students s
JOIN academic_records a ON s.student_id = a.student_id;

-- ADMIN VIEW
CREATE OR REPLACE VIEW admin_view AS
SELECT s.student_id, s.student_name, s.class, s.weekly_self_study_hours, s.gender, s.district, s.parent_education,
       a.total, a.grade, a.attendance, f.status AS fees_status
FROM students s
JOIN academic_records a ON s.student_id = a.student_id
JOIN fees f ON s.student_id = f.student_id;

-- GRANT USERS
CREATE USER IF NOT EXISTS 'admin_user'@'%' IDENTIFIED BY 'Admin@12345';
GRANT ALL PRIVILEGES ON student_analytics.* TO 'admin_user'@'%';

CREATE USER IF NOT EXISTS 'teacher_user'@'%' IDENTIFIED BY 'Teacher@123';
GRANT SELECT, UPDATE ON student_analytics.teacher_view TO 'teacher_user'@'%';

CREATE USER IF NOT EXISTS 'student_user'@'%' IDENTIFIED BY 'Student@123';
GRANT SELECT ON student_analytics.student_self_view TO 'student_user'@'%';

FLUSH PRIVILEGES;

SHOW TABLES;




