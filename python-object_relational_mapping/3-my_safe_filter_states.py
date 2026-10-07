#!/usr/bin/python3

"""
Module that takes an argument and displays all the
values in the states table
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        port=3306,
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
    )
    state_name = argv[4]
    cur = db.cursor()
    cur.execute(
        """SELECT * FROM states WHERE name BINARY = '{}'
    ORDER BY states.id ASC""".format(state_name)
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
