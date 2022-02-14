# use sqlite3 module - create db, add info to db
# - Requires two fields, prim ID &  data tpe field (string)
# - from variable, identify only .txt files and add only those to the DB
# Print qualifying text to console

#imports sqlite3 modlue if necessary
import sqlite3

#defines variable fileNames
fileNames =  ('information.docx','hello.txt','myImage.jpg','myMovie.mpg','world.txt','data.pdf','misc.jpg')

conn = sqlite3.connect('assignment.db')
with conn:
    cur = conn.cursor()
    #Creates required table if non-existant and defines columns to be included
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_filelist(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_fileName TEXT NOT NULL)")
    conn.commit

#Script below will add only .txt files to the database created above
with conn:
    cur= conn.cursor()
    cur.execute("INSERT INTO tbl_filelist(")
    
conn.close()

