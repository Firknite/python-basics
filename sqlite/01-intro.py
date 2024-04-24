import sqlite3

# hay que acordarse de siempre cerrar la conexion ya que no es automatico
connection = sqlite3.connect("sqlite/app.db")

connection.close()
