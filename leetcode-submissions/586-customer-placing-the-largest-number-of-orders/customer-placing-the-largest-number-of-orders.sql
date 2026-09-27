# Write your MySQL query statement below
select customer_number
from (select customer_number, count(*) as orders
from Orders
group by customer_number
order by orders desc limit 1) as simplified_data