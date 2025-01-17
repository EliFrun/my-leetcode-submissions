# Write your MySQL query statement below

SELECT person_name from (SELECT *, (SUM(weight) over (order by turn)) as w FROM Queue order by w desc) as foo where foo.w <= 1000 limit 1;
