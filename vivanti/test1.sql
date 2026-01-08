-- Basic version
SELECT e.name,
  e.department,
  e.salary,
  MAX(e.salary) OVER (PARTITION BY e.department) as max_department_salary,
  ROUND(
    e.salary * 100.0 / MAX(e.salary) OVER (PARTITION BY e.department),
    4
  ) as utilization_percentage
FROM employees e
WHERE e.salary = (
    SELECT MAX(salary)
    FROM employees
    WHERE department = e.department
  );
-- Optimized version with CTE
WITH max_salaries AS (
  SELECT department,
    MAX(salary) as max_salary
  FROM employees
  GROUP BY department
)
SELECT e.name,
  e.department,
  e.salary,
  ms.max_salary as max_department_salary,
  ROUND(e.salary * 100.0 / ms.max_salary, 4) as utilization_percentage
FROM employees e
  INNER JOIN max_salaries ms ON e.department = ms.department
WHERE e.salary = ms.max_salary;