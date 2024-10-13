-- 코드를 입력하세요
WITH RECURSIVE TIME_CTE AS(
    SELECT 0 AS HOUR
    UNION ALL
    SELECT HOUR+1 FROM TIME_CTE
    WHERE HOUR<23
)
SELECT b.HOUR as "HOUR" , COUNT(ANIMAL_ID) as "COUNT" FROM ANIMAL_OUTS a RIGHT JOIN TIME_CTE b ON HOUR(a.DATETIME) = b.HOUR 
GROUP BY b.HOUR
ORDER BY b.HOUR