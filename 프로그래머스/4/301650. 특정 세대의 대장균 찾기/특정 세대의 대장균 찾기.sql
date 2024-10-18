-- 코드를 작성해주세요
WITH RECURSIVE BASE AS (
    SELECT ID ,
            1 AS GEN
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
    
    UNION ALL
                        
   SELECT D.ID , B.GEN+1 AS GEN
   FROM ECOLI_DATA D , BASE B
   WHERE D.PARENT_ID = B.ID)
                 
SELECT A.ID
FROM   ECOLI_DATA A, BASE B
WHERE  A.ID = B.ID
AND    B.GEN = 3
ORDER BY ID