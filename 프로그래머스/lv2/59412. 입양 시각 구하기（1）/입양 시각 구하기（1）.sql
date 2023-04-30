-- 코드를 입력하세요
SELECT DATE_FORMAT(DATETIME, '%H') AS HOUR,
        COUNT(*) AS COUNT
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) BETWEEN 9 AND 20
GROUP BY HOUR
ORDER BY HOUR