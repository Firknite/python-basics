lista = [1, 2, 3, 4]
lista2 = [5, 6]
# combinamos ambas listas con el operador de desempaquetamiento
combinada = [*lista, *lista2]
print(combinada)

punto1 = {"x": 19}
punto2 = {"y": 15}
# esta forma de desacoplar sobreescribe las llaves existentes de derecha a izquierda
nuevoPunto = {**punto1, **punto2}
print(nuevoPunto)
