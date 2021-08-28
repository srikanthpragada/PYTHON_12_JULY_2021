# Test connection

import sqlite3   # Module to connect to SQLite DB
import dbutil

try:
    con = sqlite3.connect(dbutil.DBNAME)
    print(f"Connected Successfully with object : {con}")
    con.close()
except Exception as ex:
    print('Error :', ex)

