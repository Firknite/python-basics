# los metodos magicos son aquellos metodos que se ejecutan de manera indirecta
# como por ejemplo el metodo constructor de cada clase
# todos los metodos magicos comienzan con __ y terminan con __

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        print(f"Chao persona {self.nombre} D:")

    # sobreescribe el metodo para imprimir datos de la clase,
    # se ejecuta cuando se le hace print a la clase
    def __str__(self):
        return f"Clase Persona:  {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice Hola!")


persona = Persona("John", 35)
print(persona)

del persona
