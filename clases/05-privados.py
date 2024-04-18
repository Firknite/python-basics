class Persona:

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def habla(self):
        print(f"{self.__nombre} dice: Hola!")

    # factory method
    @classmethod
    def factory(cls):
        return cls("Claudio", 25)


persona1 = Persona.factory()
print(persona1.get_nombre())

# genera un diccionario con todas las propiedades de la clase
print(persona1.__dict__)
# esto es una manera de acceder a las propiedades privadas pero que no se debe hacer
print(persona1._Persona__edad)
