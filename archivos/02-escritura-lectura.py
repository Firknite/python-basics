from pathlib import Path

archivo = Path("archivos/archivo-prueba.txt")

# para que retorne el texto separado por lineas dentro de una lista
texto = archivo.read_text("utf-8").split("\n")
print(texto)

texto.insert(0, "hola mundo")
archivo.write_text("\n".join(texto), "utf-8")
print(archivo)

# *****El metodo write_text SOBREESCRIBE TODO EL TEXTO QUE ESTE DENTRO DEL ARCHIVO
# por lo que se debe extraer y procesar el texto linea a linea si no se quiere perder
# tomamos la info, la leemos, la procesamos y la guardamos
