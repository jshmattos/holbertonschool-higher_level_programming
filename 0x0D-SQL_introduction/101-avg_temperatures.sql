-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
-- imports data from temperatures.sql
-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
source temperatures.sql;
select city, AVG(value) as avg_temp from temperatures GROUP BY city ORDER BY avg_temp DESC;
