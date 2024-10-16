-- 코드를 입력하세요
with sta as (
select ug.board_id , case when ug.status = "SALE" then "판매중"
when ug.status = "reserved" then "예약중" 
else "거래완료" end as t from used_goods_board as ug
)
SELECT u.board_id , u.writer_id , u.title , u.price , ug.t as "status" from used_goods_board u join sta ug on u.board_id = ug.board_id
where u.created_date = "2022-10-05"
order by 1 desc