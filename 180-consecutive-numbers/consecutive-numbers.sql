# Write your MySQL query statement below
select distinct num as ConsecutiveNums
from(
    select num, lead(num) over(order by id) as lead_val,
    lag(num) over(order by id) as lag_val
    from logs
) as temp
where num=lead_val and num=lag_val;
