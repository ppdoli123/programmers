-- 코드를 작성해주세요
with cte as(
select YEAR(differentiation_date) as e , max(size_of_colony) as m from ecoli_data group by YEAR(differentiation_date))
select YEAR(differentiation_date) as YEAR , (cte.m-size_of_colony) as YEAR_DEV, id from ecoli_data join cte on YEAR(ecoli_data.differentiation_date) = cte.e
order by 1,2;
