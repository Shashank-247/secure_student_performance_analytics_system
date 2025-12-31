CREATE DATABASE student_analytics;
USE student_analytics;


CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100),
    password_hash VARCHAR(255),
    role ENUM('admin','teacher','student') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


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

CREATE TABLE teachers (
    teacher_id INT PRIMARY KEY AUTO_INCREMENT,
    teacher_name VARCHAR(100),
    subject VARCHAR(50)
);

INSERT INTO teachers (teacher_id, teacher_name, subject) VALUES
('1','Ayush Singh', 'Maths'),
('2','Sarita Mishra', 'Science'),
('3','Rohit Sharma', 'English'),
('4','Neha Singh', 'Hindi'),
('5','Amit Kumar', 'SST');


CREATE TABLE academic_records (
    record_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,

    english INT CHECK (english BETWEEN 0 AND 100),
    hindi INT CHECK (hindi BETWEEN 0 AND 100),
    maths INT CHECK (maths BETWEEN 0 AND 100),
    science INT CHECK (science BETWEEN 0 AND 100),
    sst INT CHECK (sst BETWEEN 0 AND 100),

    -- Automatic total
    total INT GENERATED ALWAYS AS
    (english + hindi + maths + science + sst) STORED,

    -- Automatic grade
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

CREATE TABLE fees (
    fee_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    status ENUM('paid','unpaid') NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);


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
FROM students s
JOIN academic_records a ON s.student_id = a.student_id
JOIN fees f ON s.student_id = f.student_id;


-- Teacher view

CREATE VIEW teacher_view AS
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
    a.attendance
FROM students s
JOIN academic_records a ON s.student_id = a.student_id;

-- Teacher Update View

CREATE VIEW teacher_update_view AS
SELECT record_id, student_id, english, hindi, maths, science, sst, attendance
FROM academic_records;

-- Admin View

CREATE VIEW admin_view AS
SELECT
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


-- Admin update view 
CREATE VIEW admin_students_update AS
SELECT * FROM students;

CREATE VIEW admin_academic_update AS
SELECT * FROM academic_records;

CREATE VIEW admin_fees_update AS
SELECT * FROM fees;


-- students csv file
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/students.csv'
INTO TABLE students
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(student_id, student_name, age, class, parent_name, parent_education, gender, district, weekly_self_study_hours);

-- academic_records csv file
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/academic_records.csv'
INTO TABLE academic_records
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(record_id, student_id, english, hindi, maths, science, sst, attendance);

-- Fees csv File 

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/fees.csv'
INTO TABLE fees
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(student_id, status);


-- Password Generation
	-- Student Password Generation
-- Inserting students into users table
INSERT INTO users (username, password_hash, role)
SELECT 
    student_name,
    CONCAT(student_id, student_name, '@12345'),
    'student'
FROM students;

-- Teacher Password Generation 
INSERT INTO users (username, password_hash, role)
SELECT
    teacher_name,
    CONCAT(teacher_id, teacher_name, '@123'),
    'teacher'
FROM teachers;

-- Admin Password
INSERT INTO users (username, password_hash, role)
VALUES ('admin', 'Admin@123', 'admin');


