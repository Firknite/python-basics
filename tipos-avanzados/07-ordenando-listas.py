numeros = [2, 4, 6, 1, 64, 32, 9]

numeros.sort()  # retora la lista ordenada
print(numeros)

# sorted retorna una nueva lista con los elementos ordenados
numeros2 = sorted(numeros, reverse=True)
print(numeros2)


# siempre y cuando el primer elemento sea ordenable va a funcionar
usuarios = [[4, "sammy"],  [2, "morita"],  [6, "arriety"]]
usuarios.sort()
print(usuarios)

# en este caso creamos una funcion que retorne el elemento que nos
# ayudaria a ordenar que en este caso sería el segundo elmento dentro
# de cada lista (el elemento que contiene el indice 1)

usuarios2 = [["sammy", 4],  ["morita", 2],  ["arriety", 6]]


def ordena(elemento):
    return elemento[1]


usuarios2.sort(key=ordena)
print(usuarios2)

# forma utilizando lambda, lambda es una manera de generar funciones anonimas
usuarios3 = [["sammy", 4],  ["morita", 2],  ["arriety", 6]]
usuarios3.sort(key=lambda elemento: elemento[1], reverse=True)
print(usuarios3)
