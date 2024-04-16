punto = {"x": 1, "y": 2}

print(punto["x"])
punto["z"] = 45
print(punto)

if "abc" in punto:
    print("encontre abc: ", punto["abc"])

# una forma de obtener un valor sin que lance error es con un get
# cuando no encuentre un valor podemos darle un argumento como valor por defecto
print(punto.get("abc",  85))

# se pueden eliminar elementos dentro de un diccionario con del y la funcion del()
# del punto["x"]
# del (punto["x"])

# para recorrer un diccionario podemos utilizar un for, el cual recupera los valores
# de cada llave dentro del diccionario permitiendonos acceder a sus valores
# for valor in punto:
#     print(valor, punto[valor])

# en este caso punto.items retorna una tupla, a la cual podemos hacer un desempaquetado
for llave, valor in punto.items():
    print(llave, valor)

usuarios = [
    {"id": 1, "nombre": "benito"},
    {"id": 2, "nombre": "sammy"},
    {"id": 3, "nombre": "morita"},
    {"id": 4, "nombre": "arriety"},
    {"id": 5, "nombre": "kishi"},
]

for usuario in usuarios:
    print(usuario["nombre"])
