import sqlite3 as sgl3
with sgl3.connect('users2.db') as userss:
    a = userss.cursor()

    a.execute('''CREATE TABLE IF NOT EXISTS runners(
    name TEXT NO NULL,
    sername TEXT NO NULL,
    meter INT,
    mmeter INT)''')

    #CREATE
    a.execute('''INSERT INTO runners(name, sername, meter, mmeter)
    VALUES ('Erzhan', 'Akmataliev', 12, 210),('Busurman', 'Junusov', 12, 210)''')

    a.execute("SELECT * FROM runners")
    row = a.fetchall()
    for i in row:
        print(i)

