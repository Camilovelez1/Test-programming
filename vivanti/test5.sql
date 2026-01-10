-- CTE para calcular estadísticas por departamento
WITH DepartmentStats AS (
  SELECT DivisionID,
    SUM(Salary) AS totalDivisionSalary
  FROM maintable_9ZJWI
  GROUP BY DivisionID
),
-- CTE para identificar el empleado con mayor salario por departamento
TopEarnerPercent AS (
  SELECT m1.DivisionID,
    m1.Name,
    m1.Salary
  FROM maintable_9ZJWI m1
    INNER JOIN (
      SELECT DivisionID,
        MAX(Salary) AS MaxSalary
      FROM maintable_9ZJWI
      GROUP BY DivisionID
    ) m2 ON m1.DivisionID = m2.DivisionID
    AND m1.Salary = m2.MaxSalary
) -- Query principal
SELECT ds.DivisionID,
  ds.totalDivisionSalary,
  te.Name,
  te.Salary AS TopSalary,
  ROUND((te.Salary / ds.totalDivisionSalary) * 100, 4) AS SalaryUtilization,
  CASE
    WHEN te.Salary < (ds.totalDivisionSalary * 0.5) THEN 'Yes'
    ELSE 'No'
  END AS BudgetOptimizationPotential
FROM DepartmentStats ds
  INNER JOIN TopEarnerPercent te ON ds.DivisionID = te.DivisionID
ORDER BY ds.DivisionID;