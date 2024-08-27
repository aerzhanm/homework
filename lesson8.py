import  sqlite3
with sqlite3.connect('game.db') as conn:
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(55) NOT NULL,
    nickname NEXT NOT NULL
    )''')
