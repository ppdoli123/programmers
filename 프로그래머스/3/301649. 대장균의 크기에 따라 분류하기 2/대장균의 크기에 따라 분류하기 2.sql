-- 코드를 작성해주세요
with base as(
select e.id, row_number() over(order by e.size_of_colony desc)/(select count(*) from ecoli_data)  as a from ecoli_data e )

select id ,
case
when a <= 0.25 then "CRITICAL"
when a <= 0.5 then "HIGH"
when a <= 0.75 then "MEDIUM"
else "LOW" end as colony_name  
from base
order by 1 