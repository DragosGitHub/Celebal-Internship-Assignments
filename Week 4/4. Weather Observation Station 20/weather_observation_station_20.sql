
/*
    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/
SELECT CAST(AVG(LAT_N) AS DECIMAL(10,4)) AS MEDIAN_LAT
FROM (
  SELECT LAT_N
  FROM (
    SELECT LAT_N, ROW_NUMBER() OVER (ORDER BY LAT_N) AS row_num,
           COUNT(*) OVER() AS total_rows
    FROM STATION
  ) AS numbered
  WHERE row_num = (total_rows + 1) / 2
     OR (MOD(total_rows, 2) = 0 AND row_num = (total_rows / 2) + 1)
     OR (MOD(total_rows, 2) = 0 AND row_num = total_rows / 2)
) AS median_rows;