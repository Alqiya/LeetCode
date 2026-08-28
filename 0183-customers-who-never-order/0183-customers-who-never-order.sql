-- # Write your MySQL query statement below
-- select name
-- from(select * from Customer as a left join Orders as b on a.id=b.customerId)
-- where customerId is NULL;




select name as Customers 
from (select c.name,o.id, o.customerId from 
    Customers as c
    left join Orders as o
    on c.id=o.customerId) as temp
where temp.customerId is NULL;















-- select name as Customers from Customers as c left join Orders as o on c.id=o.customerId 
-- where o.id is null;