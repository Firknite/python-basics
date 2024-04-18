from abc import ABC, abstractmethod
# esto es para crear una clase abstracta
# una clase abstracta no puede tener instancias sino que debe ser heredada
# y sus metodos y propiedades deben ser obligatoriamente implementadas


class Model(ABC):
    # con estos decoradores hacemos que nuestra clase sea abstracto
    @property
    @abstractmethod
    def tabla(self):
        pass

    @abstractmethod
    def guardar(self):
        pass

    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscando por id {_id}")


class Usuario(Model):
    tabla = "Usuario"

    def guardar(self):
        print("guardando usuario")


usuario = Usuario()

usuario.guardar()
Usuario.buscar_por_id(123)
