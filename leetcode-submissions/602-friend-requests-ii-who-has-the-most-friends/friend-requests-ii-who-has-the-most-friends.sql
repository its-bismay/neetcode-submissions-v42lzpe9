select temp.id, count(temp.id) as num
from (select requester_id as id from RequestAccepted
union all
select accepter_id as id from RequestAccepted) as temp
group by temp.id
order by num desc limit 1