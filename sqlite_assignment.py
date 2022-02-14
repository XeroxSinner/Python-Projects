import sqlite3

connection = sqlite3.connect("C:/Users/nylan\Documents\GitHub\Python-Projects\Python-Projects\sqlite_test.db")
c = connection.cursor()



c.execute("DROP TABLE IF EXISTS People")
connection.commit

connection.close()


