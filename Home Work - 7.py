import sqlite3 as sql3
with sql3.connect('users.db') as connection:
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS  employees (
    name TEXT NOT NULL,
    id TEXT NOT NULL,
    salary INT 
    )''')

    #CREATE
    cursor.execute('''INSERT INTO employees (name, id , salary)
    VALUES ('erzhan', 'sayan', 200000),('Elbak', 'sinister', 180000),
    ('Aziz', 'aziz1', 180000), ('musurman', 'musi1', 160000),
    ('baiemir', 'baia1', 200000),('kanatbek', 'sky1', 200000),
     ('aishat', 'moon', 200000), ('Aizhana', 'rain1', 200000),
     ('Madina', 'madness', 210000),('Aiana','yana1', 220000)
    ''')

    # SELECT
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    for row in rows:
        print(row)




