-- 코드를 입력하세요
SELECT USER_ID , PRODUCT_ID FROM ONLINE_SALE
GROUP BY USER_ID,PRODUCT_ID
HAVING COUNT(*) > 1
ORDER BY USER_ID , PRODUCT_ID DESC












# select user_id,product_id from online_sale
# group by user_id , product_id
# having count(*) >1
# order by 1, 2 desc;