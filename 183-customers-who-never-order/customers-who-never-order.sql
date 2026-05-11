/* Write your T-SQL query statement below */
select name as Customers
from(select name, customerId from Customers left join Orders on Customers.id=Orders.customerId) as temp
where temp.customerId is NULL;