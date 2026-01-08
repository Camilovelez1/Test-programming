-- first solution
SELECT (
    SELECT DISTINCT salary
    FROM (
        SELECT salary,
          DENSE_RANK() OVER(
            ORDER BY salary DESC
          ) AS emp_rank
        FROM Employee
      ) AS subquery
    WHERE emp_rank = 2
  ) AS SecondHighestSalary;
-- improved solution
SELECT max(salary) as SecondHighestSalary
FROM Employee
WHERE salary <> (
    SELECT max(salary)
    FROM Employee
  );