# Write your MySQL query statement below
WITH numbered AS (
  SELECT num,
    id,
    ROW_NUMBER() OVER(
      ORDER BY id
    ) - ROW_NUMBER() OVER(
      PARTITION BY num
      ORDER BY id
    ) AS grp
  FROM Logs
)
SELECT DISTINCT num AS ConsecutiveNums
FROM numbered
GROUP BY num,
  grp
HAVING COUNT(*) >= 3;