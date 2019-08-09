#!/usr/bin/python3
# Lists all states with a name starting with N (upper N)
# from the database hbtn_0e_0_usa

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
    cur.execute("SELECT * FROM states WHERE " +
                "SUBSTRING(name, 1, 1)='N' ORDER BY id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
