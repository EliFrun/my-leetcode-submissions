-- Write your PostgreSQL query statement below
select e.name as Employee from Employee as E left join Employee as EE on e.managerid = ee.id where e.salary > ee.salary;

