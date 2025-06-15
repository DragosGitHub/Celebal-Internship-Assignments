
/*
    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/
SELECT 
    CASE 
        WHEN g.Grade >= 8 THEN s.Name
        ELSE 'NULL'
    END AS Name,
    g.Grade,
    s.Marks
FROM Students s
JOIN Grades g ON s.Marks BETWEEN g.Min_Mark AND g.Max_Mark
ORDER BY 
    g.Grade DESC,
    CASE 
        WHEN g.Grade >= 8 THEN s.Name
        ELSE NULL
    END,
    CASE 
        WHEN g.Grade < 8 THEN s.Marks
        ELSE NULL
    END;


