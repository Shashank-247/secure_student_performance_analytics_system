-- Top 10 students by total marks
SELECT 
    s.student_id,
    s.student_name,
    s.class,
    a.total,
    a.grade
FROM students s
JOIN academic_records a ON s.student_id = a.student_id
ORDER BY a.total DESC
LIMIT 10;
