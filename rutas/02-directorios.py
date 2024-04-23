from pathlib import Path

path = Path("rutas")
# path.exists()
# path.mkdir()
# path.rmdir()  # remover directorio que debe estar vacio
# path.rename("gatito-feliz")

print(path.iterdir())  # iterdir crea un objeto generador iterable

# for p in path.iterdir():
#     print(p)

# archivos = [p for p in path.iterdir() if not p.is_dir()]

# para buscar archivos con extensiones o nombres con un patron especifico
archivos = [p for p in path.glob("01-*.py")]
# que busque de manera recursiva todos los archivos con el nombre que cumple el patron
archivos = [p for p in path.glob("**/*.py")]
# es lo mismo pero utilizando el metodo
# especifico para recursividad por lo que no ncesita un patron con **
archivos = [p for p in path.rglob("*.py")]

print(archivos)
