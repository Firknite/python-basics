import requests

# para importar librerias en python utilizamos pip en windows y pip3 en linux
# el principal repositorio de librerias pyton es https://pypi.org/project/pyti/

r = requests.get("https://www.google.com")
print(r)

# para crear ambientes virtuales debemos utilizar el comando python3 -m venv env
# para activar el uso de estos venv en windows es env\bin\activate.bat
# para linux es source env/bin/activate
# posiblemente haya que reinstalar autopep8
# para finalizar el ambiente virtual debemos usar el comando deactivate

# para inicializar el env de pipenv se utiliza el comando de pipenv shell

# para inicializar un proyecto e instalar sus dependencias usamos pipenv install
# esto instala nuestras dependencias haciendo referencia al Pipfile
# para proyectos antiguos es aconsejable utilizar el archivo lock para especificar versiones
# podemos saltarnos el Pipfile utilizamos el comando pipenv install --ignore-pipfile

# para visualizar el diagrama de dependencias el comando es pipenv graph
# pipenv update --outdated lista las dependencias que pueden ser actualizadas
# pipenv update actualiza las dependencias
