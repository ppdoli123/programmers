-- 코드를 입력하세요
with base as (SELECT distinct(c.car_id), c.car_type,c.daily_fee  from car_rental_company_car c join car_rental_company_rental_history h  on c.car_id = h.car_id 
             where c.car_id not in ( select distinct(h.car_id) from car_rental_company_rental_history h where datediff(h.end_date,'2022-11-01') >= 0))

# with base as ( select distinct(h.car_id) from car_rental_company_rental_history h where datediff(h.end_date,'2022-11-01') >= 0)

select base.car_id, base.car_type ,round((100-p.discount_rate) * base.daily_fee * 0.01 * 30 ) as fee from car_rental_company_discount_plan p join base on base.car_type = p.car_type
where p.duration_type regexp "(^30)" and p.car_type regexp ("^세단|^suv") 
and ((100-p.discount_rate) * base.daily_fee * 0.01 * 30 ) >= 500000 and ((100-p.discount_rate) * base.daily_fee * 0.01 * 30 ) < 2000000
order by 3 desc, 2 , 1 desc



# SELECT 
#     C.CAR_ID, 
#     C.CAR_TYPE, 
#     FLOOR(C.DAILY_FEE * 30 * (1 - DP.DISCOUNT_RATE / 100)) AS FEE
# FROM 
#     CAR_RENTAL_COMPANY_CAR C
# LEFT JOIN 
#     CAR_RENTAL_COMPANY_RENTAL_HISTORY RH 
#     ON C.CAR_ID = RH.CAR_ID 
#     AND RH.START_DATE <= '2022-11-30' 
#     AND RH.END_DATE >= '2022-11-01'
# JOIN 
#     CAR_RENTAL_COMPANY_DISCOUNT_PLAN DP 
#     ON C.CAR_TYPE = DP.CAR_TYPE 
#     AND DP.DURATION_TYPE = '30일 이상'
# WHERE 
#     C.CAR_TYPE IN ('세단', 'SUV')
#     AND RH.HISTORY_ID IS NULL  -- 2022년 11월 1일~30일 사이에 대여 이력이 없는 자동차만 선택
# HAVING 
#     FEE >= 500000 AND FEE < 2000000
# ORDER BY 
#     FEE DESC, 
#     C.CAR_TYPE ASC, 
#     C.CAR_ID DESC;