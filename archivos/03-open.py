from io import open

# escritura

# texto = "Hola mundo"
# al metodo open se le debe entrgar la accion que se va a realizar con el archivo
# los metodos son w (escritura), r (lectura) o wr
# si no existe el archivo que vamos a utilizar, python se encarga de crearlo
# algo a tener en consideracion es que despues de abrir un archivo para su edicion
# debemos cerrarlo, de lo contrario quedara abierto ocupando memoria de la maquina
# archivo = open("archivos/hola-mundo.txt", "w")
# archivo.write(texto)
# archivo.close()

# lectura
# archivo = open("archivos/hola-mundo.txt", "r")
# texto = archivo.read()
# archivo.close()
# print(texto)

# lectura como lista (retorna cada linea dentro del archivo como un item dentro de una lista)
# archivo = open("archivos/hola-mundo.txt", "r")
# texto = archivo.readlines()
# archivo.close()
# print(texto)

# metodos magicos
# el metodo with es el encargado de abrir y cerrar automaticamente nuestro archivo
# y llama de manera automatica a los metodos __enter__ y __exit__
# with open("archivos/hola-mundo.txt", "r") as archivo:
#     print(archivo.readlines())  # carga todas las lineas del archivo en memoria
#     # volvemos al primer caracter del archivo obligando a resetear el indice
#     # carga solamente una linea del archivo a la vez en memoria
#     archivo.seek(0)
#     for linea in archivo:
#         print(linea)

# agregar
# archivo = open("archivos/hola-mundo.txt", "a+")
# archivo.write("chao mundo")
# archivo.close()

# lectura y escritura
# sobreescribe los caracteres a medida que vayan ocupando los espacios
with open("archivos/hola-mundo.txt", "r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "gatito feliz"
    archivo.writelines(texto)
