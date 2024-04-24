import csv
import os

# escribir
# with open("archivos/archivo.csv", "w") as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(["twit_id", "userd_id", "text"])
#     writer.writerow([1000, 1, "esto es un twit"])
#     writer.writerow([1001, 2, "otro twit"])

# leer
# with open("archivos/archivo.csv") as archivo:
#     reader = csv.reader(archivo)
#     # print(list(reader))
#     for linea in reader:
#         print(linea)

# actualizar csv
# para modificar una linea en especifico se debe crear un archivo temporal
# para ir guardando en un nuevo archivo el texto que queramos modificar
# se debe hacer asi ya que no se puede modificar un archivo a la vez que se esta leyendo
with open("archivos/archivo.csv") as r, open("archivos/archivo_temp.csv", "w") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader:
        if linea[0] == "1000":
            writer.writerow([1000, 1, "texto modificado"])
        else:
            writer.writerow(linea)
    os.remove("archivos/archivo.csv")
    os.rename("archivos/archivo_temp.csv", "archivos/archivo.csv")
