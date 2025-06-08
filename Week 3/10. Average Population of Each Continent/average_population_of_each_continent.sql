-- Selecting the continent name and the average city population
SELECT COUNTRY.Continent, FLOOR(AVG(CITY.Population)) AS AvgPopulation 
FROM CITY

-- Joining the COUNTRY and CITY tables using the matching country codes
JOIN COUNTRY ON CITY.CountryCode = COUNTRY.Code

-- Group the result by continent so we get one average per continent
GROUP BY COUNTRY.Continent;
