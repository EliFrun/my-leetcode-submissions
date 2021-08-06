# Write your MySQL query statement below
SELECT person.FirstName, person.LastName, address.City, address.State FROM (Person LEFT JOIN Address ON Person.personId = Address.personId);
