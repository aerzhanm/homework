import  sqlite3
with sqlite3.connect('game.db') as conn:
 c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(55) NOT NULL,
nickname NEXT NOT NULL
)''')

c.execute('''CREATE TABLE IF NOT EXISTS games(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gamename TEXT NOT NULL,
    users_id INTEGER,
    FOREIGN KEY(users_id) REFERENCES users(id)
    )''')

c.execute('''INSERT INTO users(id, nickname)
    VALUES ('1', 'sayan')
    ''')

c.execute('''INSERT INTO games(users_id, name, nickname)
    VALUES ('2', 'HBHBU', 'HUBVVVV')
    ''')


