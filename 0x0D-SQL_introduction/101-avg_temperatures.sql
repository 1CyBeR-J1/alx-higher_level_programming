-- Import in hbtn_0c_0 database this table dump
-- displays the average temperature (Fahrenheit) by
-- city ordered by temperature (descending).
SELECT city, AVG(value) as avg_t
FROM temperatures
GROUP BY city
ORDER BY AVG(value) DESC;
