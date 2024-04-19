def division(numero=0):
    if numero == 0:
        raise ZeroDivisionError("No se puede dividir por 0", f"{numero}")
    return 5/0


# con esta implementacion de una excepcion especifica podemos
# acceder a todos los parametros que le pasemos en la anterior invocacion
try:
    division()
except ZeroDivisionError as e:
    print(e)
