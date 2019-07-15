-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
select city, AVG(value) as avg_temp from temperatures GROUP BY city ORDER BY avg_temp DESC;
