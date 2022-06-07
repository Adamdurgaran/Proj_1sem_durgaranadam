import sqlite3 as sq

with sq.connect('products.db') as con:
    cur = con.cursor()
    #cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        cod INTEGER PRIMARY KEY AUTOINCREMENT,
        mark TEXT NOT NULL,
        type INTEGER,
        price INTEGER,
        kolvo INTEGER,
        min INTEGER,
    )""")