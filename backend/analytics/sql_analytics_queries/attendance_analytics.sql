-- Low attendance students (<75%)
SELECT 
    s.student_id,
    s.student_name,
    s.class,
    a.attendance
FROM students s
JOIN academic_records a ON s.student_id = a.student_id
WHERE a.attendance < 75
ORDER BY a.attendance ASC;

-- Class-wise average attendance
SELECT 
    s.class,
    AVG(a.attendance) AS avg_attendance
FROM students s
JOIN academic_records a ON s.student_id = a.student_id
GROUP BY s.class;
