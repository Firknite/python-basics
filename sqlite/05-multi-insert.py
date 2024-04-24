import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    usuarios = [
        (2, "Gatito feliz"),
        (3, "Gatito triste")
    ]
    cursor.executemany(
        "INSERT INTO usuarios values(?, ?)",
        usuarios
    )
