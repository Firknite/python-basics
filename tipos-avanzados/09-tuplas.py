# Se pueden crear tuplas a partir de otras pero nunca modificar una existente
# las tuplas son basicamente listas a las cuales se les puede implementar
# cualquier funcion de las listas excepto las que modifican, solo las que acceden o filtran
numeros = (1, 2, 3) + (4, 5, 6)

print(numeros)

# la funcion tuple recibe cualquier iterable (listas, strings, etc)
punto = tuple([1, 2])
