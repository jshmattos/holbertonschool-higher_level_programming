#!/usr/bin/python3
# Takes in the name of a state as an argument and lists all cities of
# that state, using the database hbtn_0e_4_usa

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    psw = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=psw,
                         db=db_name,
                         charset="utf8")
    cur = db.cursor()
    query = "SELECT cities.name FROM cities " +\
            "JOIN states ON cities.state_id = states.id " +\
            "WHERE states.name = %s ORDER BY cities.id ASC"
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    db.close()
