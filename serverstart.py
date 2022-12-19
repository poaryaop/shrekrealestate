import sqlite3
con = sqlite3.connect("database.db")
c = con.cursor()
c.execute("""CREATE TABLE data(
    username  text,
    password  text,
    budget INTEGER,
    currentpropertyID  text
)""")
c.execute("""CREATE TABLE housesforsale(
    propertyID text,
    price INTEGER,
    area INTEGER,
    location text
)""")
c.execute("INSERT INTO data VALUES ('admin','1234',0,'0')")
con.commit()
con.close()