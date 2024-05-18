-- Write query to find the number of grade A's given by the teacher who has graded the most assignments

SELECT COUNT(*) AS grade_a_count
FROM assignments a
JOIN (
    SELECT teacher_id
    FROM (
        SELECT teacher_id, COUNT(*) AS graded_count
        FROM assignments
        WHERE state = 'GRADED'
        GROUP BY teacher_id
        ORDER BY graded_count DESC
        LIMIT 1
    ) AS max_grader
) AS max_teacher ON a.teacher_id = max_teacher.teacher_id AND a.grade = 'A';


