#!/usr/bin/python3
"""
akes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
That is safe from MySQL injections!
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states\
            WHERE name LIKE BINARY %(name)s
            ORDER BY states.id", {'name': argv[4]})

    rows = cursor.fetchall()
    for r in rows:
        print(r)
    db.close()
