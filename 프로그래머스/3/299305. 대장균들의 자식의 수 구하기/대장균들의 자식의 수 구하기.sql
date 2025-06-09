-- 코드를 작성해주세요
WITH cte as (SELECT e.id , count(*) CHILD_COUNT 
FROM ecoli_data e
join ecoli_data i on e.id = i.parent_id
group by e.id
union all
select ee.id , 0 as CHILD_COUNT
FROM ecoli_data ee
left join ecoli_data ii on ee.id = ii.parent_id
group by ee.id)
SELECT ID, sum(CHILD_COUNT) CHILD_COUNT FROM cte group by ID order by 1;


