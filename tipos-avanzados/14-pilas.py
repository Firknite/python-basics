# pilas son LIFO (last in first out)

pila = []
pila.append(1)
pila.append(2)
pila.append(3)

print(pila)
pila.pop()  # retorna el ultimo elemento de una lista y lo elimina de esta
print(pila)

print(pila[-1])  # retorna el ultimo elemento de la lista

if not pila:
    print("pila vacia")
