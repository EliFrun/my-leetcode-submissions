-- Write your PostgreSQL query statement below
select t.id as id from Weather as t join weather as y on y.recordDate + interval '1'  day = t.recordDate where y.temperature < t.temperature;
