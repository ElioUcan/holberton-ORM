#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa."""

import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        database="hbtn_0e_0_usa",
        port=3306,
    )
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY states.id ASC")
    for state in cur.fetchall():
        print(state)
    cur.close()
    db.close()
