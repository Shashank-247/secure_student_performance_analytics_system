-- Class wise average performance
SELECT
    s.class,
    AVG(a.total) AS avg_score,
    AVG(a.attendance) AS avg_attendance
FROM students s
JOIN academic_records a ON s.student_id = a.student_id
GROUP BY s.class;
