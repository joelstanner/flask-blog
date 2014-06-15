#sql.py - create a sqlite3 db and populate it

import sqlite3

#create a new db if it doesn't already exist
with sqlite3.connect("blog.db") as connection:
    c = connection.cursor()
    
    #create the table
    c.execute("""CREATE TABLE posts
              (title TEXT, post TEXT)
              """)
    
    #insert dummy data into table
    c.execute('INSERT INTO posts VALUES("Good","I\'m good.")')
    c.execute('INSERT INTO posts VALUES("Well","I\'m well.")')
    c.execute('INSERT INTO posts VALUES("Excellent","I\'m excellent.")')
    c.execute('INSERT INTO posts VALUES("Okay","I\'m okay.")')
