-- 코드를 입력하세요
SELECT O.animal_id , O.name FROM ANIMAL_INS I RIGHT JOIN ANIMAL_OUTS O ON I.animal_id = O.animal_id WHERE I.animal_id is null and O.animal_id is not null ORDER BY O.ANIMAL_ID