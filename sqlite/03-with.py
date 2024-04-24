import sqlite3

# con el operador with se ejecutan los metodos magicos de __exit__ y __enter__
# igualmente cuando el proceso finaliza sin errores de ejecucion llama al metodo commit

with sqlite3.connect("sqlite/app.db") as con:
    # declaramos el intermediario para hacer las consultas a la db
    cursor = con.cursor()
    cursor.execute(
        """
        CREATE TABLE if not exists usuarios
        (id INTEGER primery key, nombre VARCHAR(50));
        """
    )
