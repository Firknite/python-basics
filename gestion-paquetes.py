# Para realizar la documentacion de cada modulo se debe utilizar el """
# esto agrega documentacion al codigo del contexto
# documenta modulos, clases, funciones, etc

# para publicar nuestro paquete al repositorio central de pypi
# se utiliza la libreria de setuptools

# setuptools.setup(
#     name="mipaquete",
#     version="0.0.1",
#     long_description="esta es la descripcion del paquete",
#     packages=setuptools.find_packages(
#         exclude=["mocks", "tests"]
#     )
# )

# despues de tener la config de nuestro paquete usamos el siguiente comando
# para generar el build de nuestro paquete
# python3 setup.py sdist bdist_wheel

# para publicarlo usamos el comando
# twine upload dist/*
