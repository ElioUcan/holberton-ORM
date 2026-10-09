#!/usr/bin/python3

"""List all the cities on a state"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )
    state_name = argv[4]
    cur = db.cursor()
    cur.execute(
        """SELECT c.id, c.name FROM cities c 
        JOIN states s ON s.id = c.state_id 
        WHERE s.name = %s 
        ORDER BY c.id ASC""",
        (state_name,),
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
