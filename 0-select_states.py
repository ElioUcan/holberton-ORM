#!/usr/bin/python3

import MySQLdb

db = MySQLdb.connect(host="localhost", user=username, password=password, database="hbtn_0e_0_usa", port="3306")

cur = db.cursor()

states = cur.execute("SELECT id, name FROM states ORDER BY states.id ASC")
print(states)
