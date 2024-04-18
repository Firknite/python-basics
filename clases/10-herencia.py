class Animal:
    def comer(self):
        print("comiendo")

# esto se conoce como herencia


class Perro(Animal):
    def pasear(self):
        print("paseando")

# esto se conoce como herencia multinivel


class Chanchito(Perro):
    def programar(self):
        print("programando")


perro = Perro()
chanchito = Chanchito()
