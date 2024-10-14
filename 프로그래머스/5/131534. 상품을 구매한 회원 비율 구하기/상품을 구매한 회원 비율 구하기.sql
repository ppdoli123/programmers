-- 코드를 입력하세요
with total_count as (select count(*) from user_info where year(joined) = 2021 )
SELECT YEAR(os.sales_date) as year, MONTH(os.sales_date) as month , count(distinct ui.user_id) as purchased_users ,round( count(distinct ui.user_id)/(select * from total_count),1) as puchased_ration from user_info as ui 
join online_sale as os on os.user_id = ui.user_id where YEAR(ui.JOINED) = 2021
group by year,month
order by 1 , 2