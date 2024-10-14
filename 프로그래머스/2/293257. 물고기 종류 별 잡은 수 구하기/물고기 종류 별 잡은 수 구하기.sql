-- 코드를 작성해주세요
select count(*) as fish_count , fni.fish_name from fish_name_info fni join fish_info fi on fni.fish_type = fi.fish_type group by fni.fish_name
order by 1 desc