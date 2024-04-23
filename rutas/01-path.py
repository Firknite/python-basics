from pathlib import Path

# rutas para windows
Path(r"C:\Archivos de programa\Minecraft")
Path("/usr/bin")  # rutas para linux, ruta absoluta
Path()
Path.home()
Path("one/__init__.py")  # esto es una ruta relativa

path = Path("hola-mundo/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,  # nombre del archivo
    path.stem,  # nombre del archivo sin extension
    path.suffix,  # extension del archivo
    path.parent,  # directorio padre del archivo
    path.absolute()  # entrega la ruta completa (pwd)
)

p = path.with_name("gatito.py")  # cambia el nombre del archivo
p = path.with_suffix(".bat")  # reemplaza la extension del archivo
# reemplaza el nombre del archivo sin la extension
p = path.with_stem("perrito")
