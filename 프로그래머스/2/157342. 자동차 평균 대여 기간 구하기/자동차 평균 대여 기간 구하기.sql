
select car_id , round(avg(datediff(end_date, start_date) + 1),1) as average_duration from car_rental_company_rental_history
 group by car_id 
 having round(avg(datediff(end_date ,start_date )+1) ,1) >= 7
 order by 2 desc , 1 desc
 
#  sELECT CAR_ID, ROUND(AVG(DATEDIFF(END_DATE,START_DATE)+1),1) AVERAGE_DURATION
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# GROUP BY CAR_ID
# HAVING AVERAGE_DURATION>=7
# ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC