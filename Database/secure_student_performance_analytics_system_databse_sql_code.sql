-- create database
CREATE DATABASE student_analytics;
USE student_analytics;

-- Users Table
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(150) UNIQUE,
    password_hash VARCHAR(255),
    role ENUM('admin','teacher','student') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Students Table
CREATE TABLE students (
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

-- Teachers Table
CREATE TABLE teachers (
    teacher_id INT PRIMARY KEY AUTO_INCREMENT,
    teacher_name VARCHAR(100),
    subject VARCHAR(50)
);
INSERT INTO teachers (teacher_name, subject) VALUES
('Ayush Singh', 'Maths'),
('Sarita Mishra', 'Science'),
('Rohit Sharma', 'English'),
('Neha Singh', 'Hindi'),
('Amit Kumar', 'SST');

-- Academic Records
CREATE TABLE academic_records (
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

-- Fees Table
CREATE TABLE fees (
    fee_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    status ENUM('paid','unpaid') NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- Load CSV Data
-- Make sure file paths are correct
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/students.csv'
IGNORE
INTO TABLE students
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(student_id, student_name, age, class, parent_name, parent_education, gender, district, weekly_self_study_hours);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/academic_records.csv'
INTO TABLE academic_records
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(student_id, english, hindi, maths, science, sst, attendance);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/fees.csv'
INTO TABLE fees
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(student_id, @status)
SET status = LCASE(TRIM(@status));

-- Insert Users (Unique username)
-- Students
INSERT INTO users (username, password_hash, role)
SELECT 
    CONCAT(student_name,'_',student_id) AS username,
    SHA2(CONCAT(student_id, student_name, '@12345'), 256),
    'student'
FROM students;

-- Teachers

INSERT INTO users (username, password_hash, role)
SELECT 
    CONCAT(teacher_name, '_', teacher_id) AS username,
    SHA2(CONCAT(teacher_id, teacher_name, '@123'), 256) AS password_hash,
    'teacher'
FROM teachers;

-- Admin
INSERT INTO users (username, password_hash, role)
VALUES ('admin', SHA2('Admin_got_all_access@12345', 256), 'admin');

-- Student Dashboard View
CREATE OR REPLACE VIEW student_dashboard AS
SELECT 
    s.student_id,
    s.student_name,
    s.class,
    s.gender,
    s.district,
    s.parent_name,
    s.parent_education,
    s.weekly_self_study_hours,
    a.english,
    a.hindi,
    a.maths,
    a.science,
    a.sst,
    a.total,
    a.grade,
    a.attendance,
    f.status AS fees_status
FROM students s
JOIN academic_records a ON s.student_id = a.student_id
JOIN fees f ON s.student_id = f.student_id
ORDER BY s.student_id;

-- Teacher & Admin Views
CREATE OR REPLACE VIEW teacher_view AS
SELECT DISTINCT
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
    a.attendance
FROM students s
JOIN academic_records a ON s.student_id = a.student_id;

CREATE OR REPLACE VIEW admin_view AS
SELECT DISTINCT
    s.student_id,
    s.student_name,
    s.class,
    s.gender,
    s.district,
    s.parent_education,
    a.total,
    a.grade,
    a.attendance,
    f.status AS fees_status
FROM students s
JOIN academic_records a ON s.student_id = a.student_id
JOIN fees f ON s.student_id = f.student_id;

SELECT * FROM users;
SELECT * FROM students;
SELECT * FROM teachers;
SELECT * FROM academic_records;
SELECT * FROM fees;
SELECT * FROM student_dashboard;
SELECT * FROM teacher_view;
SELECT * FROM admin_view;

