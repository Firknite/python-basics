import random
import string

# por defecto retorna un numero entre 0 y 1
print(random.random())
# generar unmeros entre un rango de numeros
print(random.randint(1, 10))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# desordena de manera aleatoria los elementos dentro de una lista
random.shuffle(lista)
print(lista)

lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# elige un numero aleatorio de la lista que entre por parametro
print(random.choice(lista2))
# obtener multiples elementos de una lista de forma aleatoria
print(random.choices(lista2, k=3))
# tambien funciona con strings
print(random.choices("asdfghqerqewr934123-", k=3))


# con este metodo podemos generar por ejemplo contraseñas
chars = string.ascii_letters
digitos = string.digits
seleccion = random.choices(chars + digitos, k=16)
# utilizamos el "".join para concadenarlos en un solo string
password = "".join(seleccion)
print(password)
