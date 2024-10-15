-- 코드를 입력하세요
SELECT ai.animal_id , ai.animal_type , ai.name from animal_ins ai join animal_outs ao on ai.animal_id = ao.animal_id 
where ai.sex_upon_intake not regexp 'Spayed|Neutered' and ao.sex_upon_outcome regexp 'Spayed|Neutered'
order by 1

# SELECT A.ANIMAL_ID
#     , A.ANIMAL_TYPE
#     , A.NAME
# FROM ANIMAL_INS A
# JOIN ANIMAL_OUTS B USING (ANIMAL_ID)
# WHERE A.SEX_UPON_INTAKE NOT REGEXP 'Spayed|Neutered'
# AND B.SEX_UPON_OUTCOME REGEXP 'Spayed|Neutered'
# ORDER BY A.ANIMAL_ID
# ;