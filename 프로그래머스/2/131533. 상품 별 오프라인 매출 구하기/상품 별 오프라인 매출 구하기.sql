-- 코드를 입력하세요
SELECT P.product_code, (sum(o.sales_amount)*p.price) as sales
FROM PRODUCT AS P
JOIN OFFLINE_SALE AS O
ON P.PRODUCT_ID = O.PRODUCT_ID
group by 1
order by 2 desc , 1 