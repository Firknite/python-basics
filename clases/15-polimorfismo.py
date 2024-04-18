from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass


class Usuario(Model):
    def guardar(self):
        print("guardando en BBDD")


class Sesion(Model):
    def guardar(self):
        print("guardando en archivo")


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()
sesion = Sesion()

guardar([sesion, usuario])

# polimorfismo es la manera en la que se agrupan objetos similares con metodos similares
# y los agrupamos dentro de una misma funcion como en este caso es la funcion de guardar
