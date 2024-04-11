"""Calculadora con ciclos"""

SALIDA = False
resultado = ""

while True:
    if not resultado:
        resultado = input("Ingresa número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)

    operacion = input("Ingresa operación: ")
    if operacion.lower() == "salir":
        break

    n2 = input("Ingresa siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if operacion.lower() == "suma":
        resultado += n2
    elif operacion.lower() == "resta":
        resultado -= n2
    elif operacion.lower() == "multi":
        resultado *= n2
    elif operacion.lower() == "div":
        resultado /= n2
    else:
        print("Operación no válida")
        break
