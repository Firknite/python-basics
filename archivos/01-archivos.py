from pathlib import Path
from time import ctime

archivo = Path("archivos/archivo-prueba.txt")
# archivo.exists()
# archivo.rename()
# archivo.unlink() # este es para eliminar un archivo

# print(archivo.stat())
# en windows el st_ctime es cuando se creo el archivo
# y en linux y mac es cuando se modificaron los metadatos

# st_atime es la ultima fecha de acceso al archivo en formato unix
print("acceso", ctime(archivo.stat().st_atime))
print("creacion", ctime(archivo.stat().st_ctime))
print("modificacion", ctime(archivo.stat().st_mtime))
