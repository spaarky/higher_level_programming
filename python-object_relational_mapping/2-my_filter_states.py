#!/usr/bin/python3
"""
return states starting with 'N'
parameters given to script: username, password, database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to database
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # create cursor to exec queries ; match arg[4]
    cursor = db.cursor()
    sqlCmd = """SELECT *
                FROM states
                WHERE name LIKE '{:s}' ORDER BY id ASC""".format(argv[4])
    cursor.execute(sqlCmd)
    for row in cursor.fetchall():
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    db.close()
