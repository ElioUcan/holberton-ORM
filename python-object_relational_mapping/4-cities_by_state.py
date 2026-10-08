#!/usr/bin/python3

"""
Module that takes an argument and displays all the
cities on the DB
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )
    cur = db.cursor()
    cur.execute("""SELECT c.id, c.name, s.name  FROM states s
        INNER JOIN cities c ON s.id=c.state_id ORDER BY c.id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
