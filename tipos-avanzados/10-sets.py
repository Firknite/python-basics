# set significa grupo o conjunto
# es una colección de datos que no se puede repetir y que no esta ordenada

primer = {1, 1, 2, 2, 3, 4}
print(primer)

# primer.add(5)
# primer.remove(1)

# print(primer)
segundo = set([3, 4, 5])
# utilizando el operador de union
print(primer | segundo)
# utilizando el operador de intersección que retorna los elementos comunes entre ambos sets
print(primer & segundo)
# operador de diferencia calcula la diferencia entre los sets eliminado los repetidos al primer set
print(primer - segundo)
# operador diferencia simetrica retorna los elementos que se
# encuentren en el primer y segundo set que no se repitan entre si
print(primer ^ segundo)

# no se pueden acceder a los datos dentro del set pero si podemos validar la existencia de
# un dato dentro de un set con un if
if 5 in segundo:
    print("El 5 existe en este set :D")
