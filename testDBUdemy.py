# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 11:19:40 2018

@author: mohan.choushali
"""

import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

#crete a tuple for inserting records into users table
user = (1,"jose","asdf")
insert_query = "insert into users values(?,?,?)"
cursor.execute(insert_query, user)

users = [(2,"jos","asf"),(3,"ram","any")]
cursor.executemany(insert_query,users)

select_query = "select * from users"

for row in cursor.execute(select_query):
    print (row)

connection.commit()
connection.close()
