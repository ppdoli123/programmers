-- 코드를 작성해주세요
select sum(hg.score) score, hg.emp_no, he.emp_name ,he.position, he.email from hr_employees he join hr_grade hg on he.emp_no = hg.emp_no 
group by emp_no 
order by 1 desc
limit 1