CREATE DATABASE student_analytics;
USE student_analytics;


-- Define Roles
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password_hash VARCHAR(255),
    role ENUM('admin','teacher','student') NOT NULL
);

-- Studnet Basic Information
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    parents_name VARCHAR(100),
    class VARCHAR(20),
    gender VARCHAR(10),
    district VARCHAR(50),
    parent_education VARCHAR(50)
);


-- Student's Academic Information ( Marks + Attandance )
CREATE TABLE academic_records (
    record_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    english INT,
    hindi INT,
    maths INT,
    science INT,
    sst INT,
    total INT,
    grade VARCHAR(5),
    attendance INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- Fees Information Table 
CREATE TABLE fees (
    fee_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    status ENUM('paid','unpaid'),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- Student Performance ( Admin / Teacher )
SELECT s.student_name, a.total, a.grade
FROM students s
JOIN academic_records a ON s.student_id = a.student_id;

-- IF Fees is Pending
SELECT s.student_name, f.status
FROM students s
JOIN fees f ON s.student_id = f.student_id
WHERE f.status = 'unpaid';

-- Student View
CREATE VIEW student_view AS
SELECT 
    s.student_id,
    s.student_name,
    s.class,
    a.english,
    a.hindi,
    a.maths,
    a.science,
    a.sst,
    a.total,
    a.grade,
    a.attendance,
    f.status AS fees_status
FROM student_analytics.students s
JOIN student_analytics.academic_records a 
    ON s.student_id = a.student_id
JOIN student_analytics.fees f 
    ON s.student_id = f.student_id;

-- Teacher View
CREATE VIEW teacher_view AS
SELECT
    s.student_id,
    s.student_name,
    s.class,
    s.gender,
    s.district,
    a.english,
    a.hindi,
    a.maths,
    a.science,
    a.sst,
    a.total,
    a.grade,
    a.attendance
FROM student_analytics.students s
JOIN student_analytics.academic_records a
    ON s.student_id = a.student_id;

-- Teacher Update View
CREATE VIEW teacher_update_view AS
SELECT
    record_id,
    english,
    hindi,
    maths,
    science,
    sst,
    total,
    grade,
    attendance
FROM student_analytics.academic_records;

-- Admin View
CREATE VIEW admin_view AS
SELECT
    s.student_id,
    s.student_name,
    s.class,
    s.gender,
    s.district,
    s.parent_education,
    a.english,
    a.hindi,
    a.maths,
    a.science,
    a.sst,
    a.total,
    a.grade,
    a.attendance,
    f.status AS fees_status
FROM student_analytics.students s
JOIN student_analytics.academic_records a
    ON s.student_id = a.student_id
JOIN student_analytics.fees f
    ON s.student_id = f.student_id;

-- Admin update view(Full update control)
CREATE VIEW admin_update_view AS
SELECT
    s.student_id,
    s.student_name,
    s.class,
    s.gender,
    s.district,
    s.parent_education,
    a.record_id,
    a.english,
    a.hindi,
    a.maths,
    a.science,
    a.sst,
    a.total,
    a.grade,
    a.attendance,
    f.status AS fees_status
FROM student_analytics.students s
JOIN student_analytics.academic_records a
    ON s.student_id = a.student_id
JOIN student_analytics.fees f
    ON s.student_id = f.student_id;

