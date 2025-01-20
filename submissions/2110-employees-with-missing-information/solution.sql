-- Write your PostgreSQL query statement below
SELECT 
    CAST(concat(e.employee_id, s.employee_id) AS INT) as employee_id
from (employees as e full outer join salaries as s on e.employee_id = s.employee_id)
where 
    (e.employee_id is NOT NULL or s.employee_id is NOT NULL) and (name is NULL or salary is NULL);
