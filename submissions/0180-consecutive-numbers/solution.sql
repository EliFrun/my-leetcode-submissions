-- Write your PostgreSQL query statement below
SELECT distinct(a.num) as ConsecutiveNums from Logs as a left join Logs as b on a.id = b.id - 1 left join Logs as c on a.id = c.id - 2 where a.num = b.num and b.num = c.num;

