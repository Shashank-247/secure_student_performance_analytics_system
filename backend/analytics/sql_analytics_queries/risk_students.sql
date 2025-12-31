-- Students at risk (low attendance OR low total marks)
SELECT 
    s.student_id,
    s.student_name,
    s.class,
    a.total,
    a.attendance
FROM students s
JOIN academic_records a ON s.student_id = a.student_id
WHERE a.total < 150 OR a.attendance < 60;
