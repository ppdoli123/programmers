-- 코드를 입력하세요
SELECT MCDP_CD as "진료과코드" , count(*) as "5월 예약 건수"  FROM APPOINTMENT
WHERE   APNT_YMD LIKE "%05-%" 
group by mcdp_cd
ORDER BY count(*) ASC , MCDP_CD ASC
