import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    # no se deben realizar consultas con los parametros formateados
    # ya que es suceptible a ataques de sql injection
    # por lo que debemos darle los valores dentro de un segundo argumento en forma de tuplas
    cursor.execute(
        "INSERT INTO usuarios values(?, ?)",
        (1, "hola mundo")
    )
