class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # self es el contexto de cada instancia
        self.edad = edad  # y estas son las propiedades o atributos de cada clase

    def habla(self):
        print(f"{self.nombre} dice: Hola!")


juan = Persona("juan", 25)
juan.habla()
