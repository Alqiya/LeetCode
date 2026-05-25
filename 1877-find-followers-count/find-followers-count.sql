# Write your MySQL query statement below
select user_id, count(*) as followers_count
from followers
where user_id is not null
group by user_id
order by user_id asc;