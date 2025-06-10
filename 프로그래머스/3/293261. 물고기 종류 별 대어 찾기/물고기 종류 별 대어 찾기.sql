-- 코드를 작성해주세요
SELECT A.ID,B.FISH_NAME,A.LENGTH
FROM FISH_INFO AS A 
JOIN FISH_NAME_INFO AS B 
ON A.FISH_TYPE = B.FISH_TYPE
WHERE (B.FISH_TYPE , A.LENGTH) in
(select fish_type,max(length)
from fish_info 
group by fish_type);