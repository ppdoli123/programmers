-- 코드를 입력하세요
SELECT count(*) USERS from user_info where user_id in (select user_id from user_info where YEAR(joined) = '2021') and age >= 20 and age <= 29;