SELECT
    CASE
        WHEN total >= 75 THEN 'Excellent'
        WHEN total >= 50 THEN 'Average'
        ELSE 'Needs Improvement'
    END AS performance_level,
    COUNT(*) AS total_students
FROM academic_records
GROUP BY performance_level;
