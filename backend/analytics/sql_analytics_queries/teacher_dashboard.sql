-- Teacher dashboard data
SELECT
    s.class,
    COUNT(s.student_id) AS total_students,
    AVG(a.total) AS class_avg
FROM students s
JOIN academic_records a ON s.student_id = a.student_id
GROUP BY s.class;
