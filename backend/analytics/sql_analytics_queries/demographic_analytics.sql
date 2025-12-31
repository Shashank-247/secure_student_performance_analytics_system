-- Gender-wise average performance
SELECT 
    s.gender,
    AVG(a.total) AS avg_marks
FROM students s
JOIN academic_records a ON s.student_id = a.student_id
GROUP BY s.gender;

-- District-wise performance
SELECT 
    s.district,
    AVG(a.total) AS avg_marks
FROM students s
JOIN academic_records a ON s.student_id = a.student_id
GROUP BY s.district;
