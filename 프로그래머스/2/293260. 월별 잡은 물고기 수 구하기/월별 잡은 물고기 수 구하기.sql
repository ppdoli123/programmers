-- 코드를 작성해주세요

select count(coalesce(length,10 )) fish_count , month(time) as month from fish_info

group by month(time)
order by month 