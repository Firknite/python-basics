class Persona:
    ojos = 2  # variables de clase vinculadas a la clase

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice: Hola!")


juan = Persona("juan", 25)
juan.habla()
print(juan.ojos)
