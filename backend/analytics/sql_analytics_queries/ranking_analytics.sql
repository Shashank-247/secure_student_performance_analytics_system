-- Top 10 students
SELECT 
    s.student_name,
    s.class,
    a.total
FROM students s
JOIN academic_records a ON s.student_id = a.student_id
ORDER BY a.total DESC
LIMIT 10;

-- Bottom 10 students
SELECT 
    s.student_name,
    s.class,
    a.total
FROM students s
JOIN academic_records a ON s.student_id = a.student_id
ORDER BY a.total ASC
LIMIT 10;
