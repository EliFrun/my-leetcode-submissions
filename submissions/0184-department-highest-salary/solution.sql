-- Write your PostgreSQL query statement below
select d.name as Department, e.name as Employee, e.salary as Salary 
from employee as e
join department as d on e.departmentId = d.id 
join (select departmentId, max(salary) as msal from Employee group by departmentId) as m on m.departmentId = e.departmentid where e.Salary = m.msal;
