from pathlib import Path
from zipfile import ZipFile

# with ZipFile("archivos/comprimidos.zip", "w") as zip:
#     for path in Path().rglob("*.*"):
#         print(path)
#         if str(path) != "archivos/comprimidos.zip":
#             zip.write(path)

with ZipFile("archivos/comprimidos.zip") as zip:
    # print(zip.namelist())  # retorna el nombre de todo lo que este dentro del zip
    info = zip.getinfo("archivos/06-comprimidos.py")
    print(info.file_size, info.compress_size)
    # descompimimos todo lo que tenga el zip dentro de la carpeta que le indiquemos
    zip.extractall("archivos/descomprimidos")
