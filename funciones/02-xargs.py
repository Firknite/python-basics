def suma(*numeros):  # EL * ES PARA CONVERTIR TODOS LOS PARAMS EN UN ITERABLE
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5, 2, 3, 4)
