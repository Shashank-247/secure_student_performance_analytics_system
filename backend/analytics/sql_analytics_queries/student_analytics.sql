-- Individual student performance
SELECT
    s.student_id,
    s.student_name,
    a.academic_year,
    a.term,
    a.total,
    a.grade,
    a.attendance
FROM students s
JOIN academic_records a ON s.student_id = a.student_id
WHERE s.student_id = 101;
