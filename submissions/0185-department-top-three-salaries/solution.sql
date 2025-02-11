-- Write your PostgreSQL query statement below
select distinct(d.name) as Department, e.name as Employee, e.salary as Salary 
from employee as e
join department as d on e.departmentId = d.id 
join (select name, departmentId, dense_rank()over(partition by departmentId order by salary desc) as r from Employee) as m on m.departmentId = e.departmentid where m.name = e.name and m.r <= 3;
