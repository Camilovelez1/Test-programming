SELECT Department,
  Employee,
  Salary
FROM (
    SELECT d.name AS Department,
      e.name AS Employee,
      e.salary AS Salary,
      RANK() OVER(
        PARTITION BY e.departmentId
        ORDER BY e.salary DESC
      ) AS rnk
    FROM Employee AS e
      INNER JOIN Department AS d ON e.departmentId = d.id
  ) subquery
WHERE rnk = 1;