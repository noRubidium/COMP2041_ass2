#!/usr/bin/python
import sqlite3
db_filename = "database/User.db"
conn = sqlite3.connect(db_filename)

c = conn.cursor()
operation="SELECT * FROM users WHERE username='AaronNinja'"

c.execute(operation)
w=c.fetchone()
print w[0]
conn.commit()
conn.close()
