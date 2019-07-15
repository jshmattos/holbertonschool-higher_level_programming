-- lists all records of the table second_table with names in descending order of the database hbtn_0c_0
-- lists all records of the table second_table with names in descending order of the database hbtn_0c_0
SELECT score, name FROM second_table WHERE CHAR_LENGTH(name) > 0 ORDER BY score DESC;
