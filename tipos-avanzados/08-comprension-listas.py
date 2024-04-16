usuarios = [["sammy", 4],  ["morita", 2],  ["arriety", 6]]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])

# ELEMENTO A RETORNAR DE CADA VUELTA DEL FOR -> ITEM DENTRO DEL FOR -> LISTA A RECORRER CON EL FOR
# ESTA OPERACION ES CONOCIDA COMO MAP
# nombres = [usuario[0] for usuario in usuarios]

# lo mismo pero con un filtro agregando un if retornando el item completo
# esto es conocido como un filter
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]

# filtra el item y retorna el campo dentro del item que especificamos en el []
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]

# LA PRIMERA FORMA DE RECORRER Y RETORNAR PERO UTILIZANDO EL METODO MAP Y LAMBDA
# nombres = list(map(lambda usuario: usuario[0], usuarios))

# Esta es la forma de hacer un filter utilizando la funcion FILTER y LAMBDA
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))

print(menosUsuarios)
