-- 코드를 입력하세요
with f as ( select flavor, sum(total_order) as total_order from first_half group by flavor ) ,  ju as ( select flavor, sum(total_order) as total_order from july group by flavor) 

select f.flavor from f join ju on f.flavor = ju.flavor
order by f.total_order + ju.total_order desc
limit 3

# SELECT f.flavor , f.total_order + july.total_order from first_half f join july on f.flavor = july.flavor
# order by (f.total_order + july.total_order) desc
# limit 3