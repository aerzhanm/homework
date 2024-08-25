# database
# SQL -  язык
# СУБД - система управления баз данных
#


import sqlite3 as sql3
with sql3.connect('user.db') as connection:
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
    fulname TEXT NOT NULL,
    pol INT DEFAULT 0,
    bdate DATE 
    )''')

    #CREATE
    cursor.execute('''INSERT INTO students (fulname, pol, bdate)
    VALUES ('erzhan', 1, '23-06-2007'),('Elbak', 1, '24-07-2007') 
    ''')
#db = sql3.connect("test.db")
#cursor = db.cursor





