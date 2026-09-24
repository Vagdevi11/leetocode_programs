/* Write your PL/SQL query statement below */

SELECT C.NAME AS Customers
FROM
Customers C LEFT JOIN Orders O
ON C.id=O.customerId
WHERE O.id IS NULL;
