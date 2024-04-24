import sqlite3

con = sqlite3.connect("sqlite/app.db")

# declaramos el intermediario para hacer las consultas a la db
cursor = con.cursor()
cursor.execute(
    """
    CREATE TABLE if not exists usuarios
    (id INTEGER primery key, nombre VARCHAR(50));
    """
)
# para que el execute sea ejecutado debemos comprometer los cambios
# por medio del metodo commit dentro de la conexion
con.commit()

con.close()
