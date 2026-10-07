#!/usr/bin/python3

"""Module for listing all states with name startign with N"""

import MySQLdb
from sys import argv




if __name__ == "__main__":
    db = MySQLdb.connect(
        port="3306",
        host="localhost",
        username=argv[0],
        password=argv[1],
        db=argv[2]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
