class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    @property  # solo se utiliza en metodos que retornen un valor
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if nombre.strip():
            self.__nombre = nombre


persona = Persona("Marcelo")
print(persona.nombre)
