-- 코드를 입력하세요
SELECT YEAR(a.sales_date) as "YEAR" , MONTH(a.sales_date) as "MONTH" , b.gender as "GENDER" , count(DISTINCT a.user_id) as "USERS" FROM ONLINE_SALE a JOIN USER_INFO b on a.user_id = b.user_id
where b.gender is not NULL
GROUP BY YEAR(a.sales_date) ,  MONTH(a.sales_date) , b.gender
ORDER BY YEAR(a.sales_date) ,  MONTH(a.sales_date) , b.gender