import sqlite3


con = sqlite3.connect('passkey.db')
cursor = con.cursor()
cursor.execute("""
CREATE TABLE passwords 
    (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL
);
 """)
con.close()

