class MiError(Exception):
    "Esta clase es para representar mi error"

    def __init__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo = codigo

    def __str__(self) -> str:
        return f"{self.mensaje} - {self.codigo}"


def division(numero=0):
    if numero == 0:
        raise MiError("No se puede dividir por 0", 404)
    return 5/0


# con esta implementacion de una excepcion especifica podemos
# acceder a todos los parametros que le pasemos en la anterior invocacion
try:
    division()
except MiError as e:
    print(e)
