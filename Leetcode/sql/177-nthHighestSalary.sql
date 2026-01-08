CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT BEGIN RETURN (
  # Write your MySQL query statement below.
  SELECT DISTINCT salary AS getNthHighestSalary
  FROM (
      SELECT salary,
        DENSE_RANK() OVER(
          ORDER BY salary DESC
        ) AS rnk_search
      FROM Employee
    ) subquery
  WHERE N = subquery.rnk_search
);
END