-- using join and subquery

-- select d.name as department, e.name as employee, e.salary
-- from employee as e
-- join department as d on e.departmentId=d.id
-- where e.salary = (
--     select max(salary)
--     from employee where departmentId=e.departmentId
-- );

-- using window function

select department, employee, salary 
from (
    select d.name as department,
    e.name as employee,
    e.salary,
    dense_rank() over(partition by d.name order by salary desc) as rnk
    from employee as e
    join department as d on e.departmentId = d.id
) as temp
where rnk=1;