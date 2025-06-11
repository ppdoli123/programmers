-- 코드를 입력하세요
select concat(concat(concat(concat(concat('/home/grep/src/',board_id),'/'),file_id),file_name),file_ext) as file_path from USED_GOODS_FILE where board_id = (select board_id from used_goods_board order by views desc limit 1) order by 1 desc;
