-- 코드를 입력하세요
SELECT f.flavor 
FROM first_half f
JOIN icecream_info i ON f.flavor = i.flavor
WHERE f.TOTAL_ORDER > 3000 and i.ingredient_type = 'fruit_based';