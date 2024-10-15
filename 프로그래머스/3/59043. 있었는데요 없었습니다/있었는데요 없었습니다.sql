-- 코드를 입력하세요
SELECT ao.animal_id , ai.name from animal_outs ao join animal_ins ai on ao.animal_id = ai.animal_id
where ao.datetime < ai.datetime
order by ai.datetime