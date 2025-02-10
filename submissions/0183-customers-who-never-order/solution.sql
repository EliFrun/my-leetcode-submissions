-- Write your PostgreSQL query statement below
select Name as Customers from Customers as c left join Orders as o on c.id = o.customerId where o.id is Null; 
