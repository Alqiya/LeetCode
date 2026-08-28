# Write your MySQL query statement below
-- select t1.name as employee from employee as t1, employee as t2 where t1.managerId = t2.id and t1.salary>t2.salary;








select t1.name as employee 
from Employee as t1
join Employee as t2 
on t1.managerId=t2.id
where t1.salary>t2.salary;