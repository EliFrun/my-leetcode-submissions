# Write your MySQL query statement below
SELECT MAX(Salary) as SecondHighestSalary FROM Employee WHERE Salary not in (SELECT MAX(salary) from EMPLOYEE);
