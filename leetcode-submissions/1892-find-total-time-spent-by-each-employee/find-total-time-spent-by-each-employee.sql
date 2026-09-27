# Write your MySQL query statement below
-- select event_day as day, emp_id, min(in_time) - max(out_time) as total_time
-- from Employess

select event_day as day, emp_id, sum( out_time - in_time ) as total_time
from Employees
group by event_day, emp_id



