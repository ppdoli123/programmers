-- 코드를 입력하세요
SELECT b.BOOK_ID, a.AUTHOR_NAME, date_format(b.PUBLISHED_DATE,'%Y-%m-%d') as "PUBLISHED_DATE" FROM BOOK b JOIN AUTHOR a ON a.AUTHOR_ID = b.AUTHOR_ID
where b.category = "경제"
ORDER BY b.PUBLISHED_DATE