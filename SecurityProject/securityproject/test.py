import sqlite3
con = sqlite3.connect("database.sqlite")
c = con.cursor()
for row in c.execute("SELECT * FROM users"):
    print row

