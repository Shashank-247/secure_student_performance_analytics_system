-- Total unpaid students
SELECT COUNT(*) AS unpaid_students
FROM fees
WHERE status = 'unpaid';

-- Class-wise fee defaulters
SELECT 
    s.class,
    COUNT(*) AS unpaid_count
FROM students s
JOIN fees f ON s.student_id = f.student_id
WHERE f.status = 'unpaid'
GROUP BY s.class;
