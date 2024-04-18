class Persona:
    ojos = 2  # variables de clase vinculadas a la clase

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("Hola!")

    # factory method
    @classmethod
    def factory(cls):
        return cls("Claudio", 25)


Persona.habla()
persona1 = Persona("Matias", 28)
persona2 = Persona("Jorge", 27)
persona3 = Persona.factory()

print(persona3.nombre)
