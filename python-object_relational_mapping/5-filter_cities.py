#!/usr/bin/python3
"""
return info from both tables (tables 'cities' 'states)
parameters given to script: username, password, database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to database
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # create cursor to exec queries ; joins 2 tables
    cursor = db.cursor()

    sqlCmd = """SELECT cities.name
                 FROM states
                 INNER JOIN cities ON states.id = cities.state_id
                 WHERE states.name LIKE %s
                 ORDER BY cities.id ASC"""
    cursor.execute(sqlCmd, (argv[4],))

    # formatting
    print(', '.join(["{:s}".format(row[0]) for row in cursor.fetchall()]))

    cursor.close()
    db.close()
