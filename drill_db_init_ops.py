# Python 3.7.2
# Database Sqlite3 (sqlite3 module)
# Scenario: a script to create a database and add new data into that database
# 
# Requirements
# 2 fields, an auto-increment primary integer field and a field with the data type of string
# read from the supplied list of file names 
# and determine only the files from the list which ends with a “.txt” file extension
# add those file names from the list ending with “.txt” file extension within database
# legibly print the qualifying text files to the console


import sqlite3

conn = sqlite3.connect('test.db')

# Create a new database and a new table
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtfiles( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_txtfile TEXT \
        )")
    conn.commit()
#conn.close()

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

# Add those files from the fileList with ".txt" file extension within database

with conn:
    cur = conn.cursor()
    for fName in fileList:
        if fName.endswith(".txt"):
            # ensure to put ,(comma) after fName to make the parameter a tuple
            cur.execute('INSERT INTO tbl_txtfiles(col_txtfile) VALUES (?)', (fName,))
            conn.commit()
#conn.close()

# Read the list of files with ".txt" extension
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_txtfile FROM tbl_txtfiles")
    txtFile = cur.fetchall()
    for file in txtFile:
        txtFile = "The found text file: {}".format(file[0])
        print(txtFile)