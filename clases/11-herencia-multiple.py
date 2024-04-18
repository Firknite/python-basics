class Animal:
    def pasear(self):
        print("paseando animales")


class Perro:
    def pasear(self):
        print("paseando perro")

# esto es conocido como herencia multiple


class Chanchito(Perro, Animal):
    def programar(self):
        print("programando")


chanchito = Chanchito()
