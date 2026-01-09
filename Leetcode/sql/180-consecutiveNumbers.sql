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
-------- Other solution --------
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT num,
      LAG(num) OVER(
        ORDER BY id
      ) AS prev_num,
      LEAD(num) OVER(
        ORDER BY id
      ) AS next_num
    FROM Logs
  ) subquery
WHERE num = prev_num
  AND num = next_num