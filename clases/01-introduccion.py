class Persona:
    def habla(self):  # cuando esta dentro de una clase se llama metodo no funcion
        print("Hola")


juan = Persona()
print(type(juan))
juan.habla()
print(isinstance(juan, Persona))  # valida si es una instancia de la clase
