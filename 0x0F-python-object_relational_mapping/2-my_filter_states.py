#!/usr/bin/python3
# Takes in an argument and displays all values in the states table
# of hbtn_0e_0_usa where name matches the argument

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
    cur.execute("SELECT * FROM states WHERE BINARY " +
                "name='{}' ".format(state_name) +
                "ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
