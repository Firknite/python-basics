mascotas = ["benito", "sammy", "arriety", "morita", "kishi", "morita"]

# index retorna el indice del elemento a buscar
print(mascotas.index("arriety"))

# si buscamos un objeto dentro de una lista y este no existe, lanzará un error
# para recuperar el indice de lo que queremos buscar sin que explote
# debemos agregar un if
if "sammy" in mascotas:
    print(mascotas.index("sammy"))

# cuenta cuantas veces se encuentra el dato a lo largo de la lista
print("veces que se repite: ", mascotas.count("morita"))
