-- Import in hbtn_0c_0 database this table dump
-- displays the top 3 of cities temperature during July
-- and August ordered by temperature (descending)
SELECT city, AVG(value) AS avg_t
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BT avg_t DESC
LIMIT 3;
