
/*
    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/
--Selecting City with Shortest Name
SELECT CITY, LENGTH(CITY) AS LEN FROM STATION
ORDER BY LENGTH(CITY) ASC, CITY ASC
FETCH FIRST 1 ROW ONLY;

--Selecting City with Longest Name
SELECT CITY, LENGTH(CITY) AS LEN FROM STATION
ORDER BY LENGTH(CITY) DESC, CITY ASC
FETCH FIRST 1 ROW ONLY;
