-- 코드를 입력하세요
# SELECT b.category as CATEGORY,count(b.price) as TOTAL_SALES  FROM BOOK b
# where b.published_date like '2022-01-%'
# JOIN BOOK_SALES s ON b.book_id = s.book_id
# GROUP BY b.category
# ORDER BY b.category;

SELECT B.CATEGORY
        ,SUM(S.SALES) AS TOTAL_SALES
FROM BOOK AS B
    JOIN BOOK_SALES AS S
        ON B.BOOK_ID = S.BOOK_ID
# WHERE DATE_FORMAT(S.SALES_DATE, '%Y-%m') = '2022-01'
WHERE S.SALES_DATE >= '2022-01-01' AND S.SALES_DATE < '2022-02-01'
GROUP BY B.CATEGORY
ORDER BY B.CATEGORY
;