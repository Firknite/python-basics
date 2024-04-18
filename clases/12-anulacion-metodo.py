# method override
class Ave:
    def __init__(self) -> None:
        self.volador = "volador"

    def vuela(self):
        print("vuela ave")


class Pato(Ave):
    def __init__(self) -> None:
        super().__init__()
        self.nadador = "nadador"

    def vuela(self):
        # super da acceso a todos los metodos y propiedades de la clase padre
        super()
        print("vuela alto")


pato = Pato()
pato.vuela()
print(pato.volador, pato.nadador)
