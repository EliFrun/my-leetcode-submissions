CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    select distinct(e.salary) as salary from Employee as e order by e.salary desc limit 1 offset case when n > 0 then n - 1 else 1000 end
      
  );
END;
$$ LANGUAGE plpgsql;
