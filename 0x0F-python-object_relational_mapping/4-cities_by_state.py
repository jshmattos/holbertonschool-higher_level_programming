#!/usr/bin/python3
# Lists all cities from the database hbtn_0e_4_usa

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    psw = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=psw,
                         db=db_name,
                         charset="utf8")
    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities " +\
            "JOIN states ON cities.state_id = states.id ORDER BY id ASC;"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
