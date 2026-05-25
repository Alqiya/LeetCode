-- # Write your MySQL query statement below
-- select temp.department, temp.employee, temp.salary
-- from (
--     select d.name as department,
--     e.name as employee, e.salary,
--     dense_rank() over(partition by d.name order by e.salary desc) as rnk
--     from department as d 
--     join employee as e on d.id=e.departmentId
-- ) as temp
-- where rnk = 1 | rnk = 2 | rnk = 3

with ranked as(
    select d.name as department,
    e.name as employee, e.salary,
    dense_rank() over(partition by d.name order by e.salary desc) as rnk
    from department as d 
    join employee as e on d.id=e.departmentId
)

select ranked.department, ranked.employee, ranked.salary from ranked where rnk<=3;