-- 코드를 입력하세요
SELECT animal_id , name, sex_upon_intake from animal_ins
where name regexp ("^Lucy$|^Ella$|^pickle$|^rogan$|^sabrina$|^mitty$")
order by 1