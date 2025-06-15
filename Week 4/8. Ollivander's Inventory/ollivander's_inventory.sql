/*
Enter your query here.
*/
SELECT 
    wand.id, 
    prop.age, 
    wand.coins_needed, 
    wand.power
FROM 
    Wands AS wand
INNER JOIN 
    Wands_Property AS prop 
    ON wand.code = prop.code
WHERE 
    prop.is_evil = 0
    AND wand.coins_needed = (
        SELECT 
            MIN(w2.coins_needed)
        FROM 
            Wands AS w2
        INNER JOIN 
            Wands_Property AS p2 
            ON w2.code = p2.code
        WHERE 
            p2.is_evil = 0
            AND p2.age = prop.age
            AND w2.power = wand.power
    )
ORDER BY 
    wand.power DESC, 
    prop.age DESC;
