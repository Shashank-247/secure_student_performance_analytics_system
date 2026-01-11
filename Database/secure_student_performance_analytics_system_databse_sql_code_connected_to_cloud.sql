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
    weekly_study_hours DECIMAL(4,2),
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
            WHEN total >= 450 THEN 'A'
            WHEN total >= 400 THEN 'B'
            WHEN total >= 350 THEN 'C'
            WHEN total >= 300 THEN 'D'
            WHEN total >= 250 THEN 'E'
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

-- INSERT USERS - STUDENTS
INSERT INTO users (username, password_hash, role)
SELECT CONCAT(student_name,'_',student_id),
       CONCAT(student_id, student_name, '@12345'),
       'student'
FROM students;

-- INSERT USERS - TEACHERS
INSERT INTO users (username, password_hash, role)
SELECT CONCAT(teacher_name,'_',teacher_id),
       CONCAT(teacher_id, teacher_name, '@123'),
       'teacher'
FROM teachers;

-- INSERT USER - ADMIN
INSERT INTO users (username, password_hash, role)
VALUES ('admin','Admin@12345','admin');

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
SELECT s.student_id, s.student_name, s.class, s.gender, s.district, s.weekly_study_hours,
       a.english, a.hindi, a.maths, a.science, a.sst, a.total, a.grade, a.attendance,
       f.status AS fees_status
FROM students s
JOIN academic_records a ON s.student_id = a.student_id
JOIN fees f ON s.student_id = f.student_id;

CREATE OR REPLACE VIEW student_rls_view AS
SELECT s.student_id,
       s.student_name,
       s.class,
       s.gender,
       s.district,
       s.weekly_study_hours,
       a.english,
       a.hindi,
       a.maths,
       a.science,
       a.sst,
       a.total,
       a.grade,
       a.attendance,
       f.status AS fees_status,
       CONCAT(s.student_name, '_', s.student_id) AS username
FROM students s
JOIN academic_records a ON s.student_id = a.student_id
JOIN fees f ON s.student_id = f.student_id;


-- TEACHER VIEW
CREATE OR REPLACE VIEW teacher_view AS
SELECT s.student_id, s.student_name, s.class,
       a.english, a.hindi, a.maths, a.science, a.sst, a.total, a.grade, a.attendance,
       CASE
           WHEN a.attendance >= 170 THEN 'Excellent'
           WHEN a.attendance >= 150 THEN 'Good'
           ELSE 'Warning'
       END AS attendance_status,
       CASE
           WHEN a.total >= 400 THEN 'Top Performer'
           WHEN a.total >= 300 THEN 'Average Performer'
           ELSE 'Needs Attention'
       END AS performance_category,
       (SELECT COUNT(*) FROM students s2 WHERE s2.class = s.class) AS total_students_in_class,
       (SELECT ROUND(AVG(a2.total),2) FROM academic_records a2 JOIN students s2 ON a2.student_id = s2.student_id WHERE s2.class = s.class) AS class_avg_marks,
       (SELECT ROUND(AVG(a2.attendance),2) FROM academic_records a2 JOIN students s2 ON a2.student_id = s2.student_id WHERE s2.class = s.class) AS class_avg_attendance
FROM students s
JOIN academic_records a ON s.student_id = a.student_id;

-- TEACHER UPDATE VIEW
CREATE OR REPLACE VIEW teacher_update_view AS
SELECT * FROM academic_records;

-- ADMIN VIEW
CREATE OR REPLACE VIEW admin_view AS
SELECT s.student_id, s.student_name, s.class, s.weekly_study_hours, s.gender, s.district, s.parent_education,
       a.total, a.grade, a.attendance, f.status AS fees_status
FROM students s
JOIN academic_records a ON s.student_id = a.student_id
JOIN fees f ON s.student_id = f.student_id;

-- ADMIN UPDATE VIEWS
CREATE OR REPLACE VIEW admin_students_update AS SELECT * FROM students;
CREATE OR REPLACE VIEW admin_academic_update AS SELECT * FROM academic_records;
CREATE OR REPLACE VIEW admin_fees_update AS SELECT * FROM fees;


-- SHOW TABLES AND VIEWS
SHOW FULL TABLES WHERE Table_type = 'VIEW';


-- Tables
SELECT * FROM students;
SELECT * FROM teachers;
SELECT * FROM academic_records;
SELECT * FROM fees;
SELECT * FROM users;

-- Views
SELECT * FROM student_self_view;
SELECT * FROM teacher_view;
SELECT * FROM admin_view;
SELECT * FROM teacher_update_view;
SELECT * FROM admin_students_update;
SELECT * FROM admin_academic_update;
SELECT * FROM admin_fees_update;
SELECT * FROM overall_school_analytics;
SELECT * FROM low_attendance_students;
SELECT * FROM class_avg_attendance;
SELECT * FROM class_performance;
SELECT * FROM gender_performance;
SELECT * FROM district_performance;
SELECT * FROM fee_defaulters;
SELECT * FROM performance_distribution;
SELECT * FROM top_10_students;
SELECT * FROM bottom_10_students;

SELECT CURRENT_USER();
SELECT * FROM student_rls_view;
