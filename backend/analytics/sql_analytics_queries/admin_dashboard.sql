-- Overall analytics
SELECT
    COUNT(DISTINCT student_id) AS total_students,
    AVG(total) AS school_avg_score
FROM academic_records;
