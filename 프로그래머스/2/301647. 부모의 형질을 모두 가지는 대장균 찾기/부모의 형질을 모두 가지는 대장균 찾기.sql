-- 코드를 작성해주세요
SELECT i.ID,i.genotype as "GENOTYPE",e.genotype as "PARENT_GENOTYPE"  FROM ECOLI_DATA e 
join ECOLI_DATA i on e.id = i.parent_id
where (e.genotype & i.genotype) = e.genotype
order by 1;