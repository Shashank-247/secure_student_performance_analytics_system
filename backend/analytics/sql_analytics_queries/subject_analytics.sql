-- Subject wise performance
SELECT
    subject,
    AVG(marks) AS avg_marks
FROM subject_performance
GROUP BY subject;
