mascotas = ["benito", "sammy", "arriety", "morita", "kishi", "morita"]

# agrega un elemento a la lista en un indice especifico
mascotas.insert(1, "simon")
print(mascotas)
mascotas.append("simon")
print(mascotas)
# elimina solamente la primera ocurrencia con el elemento indicado
mascotas.remove("simon")
print(mascotas)
mascotas.pop()  # elimina el ultimo elemento de la lista
print(mascotas)
mascotas.pop(1)  # elimina el elemento de la lista con ese indice
print(mascotas)
del mascotas[0]  # otra forma de eliminar elemendos con un indice especifico
print(mascotas)
mascotas.clear()  # elimina todos los elemendos dentro de la lista
