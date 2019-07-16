-- creates the MySQL server user user_0d_1
-- creates user if it doesn't already exists, sets psw
-- grants all privilegs to user
    CREATE USER IF NOT EXISTS user_0d_1@localhost
IDENTIFIED BY 'user_0d_1_pwd';
     GRANT ALL PRIVILEGES
        ON *.*
        TO user_0d_1@localhost;
