# 1
cadena = "Aaaabbbbcac"
cadena = list(cadena.replace(" ", ""))
# print("#1 ", cadena)

# 2
diccionario = {}
for char in cadena:
    diccionario[char] = cadena.count(char)
# print("#2 ", diccionario)

# 3
dic_ordenado = []
while True:
    contador = 0
    mayor = []
    for key, value in diccionario.items():
        if value > contador:
            contador = value
            mayor = tuple([key, value])

    dic_ordenado.append(mayor)
    del diccionario[mayor[0]]

    if not diccionario:
        break
# print("#3 ", dic_ordenado)

# 4
tuplas_mayor = []
mayor = dic_ordenado[0]

for ele in dic_ordenado:
    if ele[1] == dic_ordenado[0][1]:
        tuplas_mayor.append(ele)
# print("# 4", tuplas_mayor)

# 5
mensaje = ""
for ele in tuplas_mayor:
    mensaje += f"{ele[0].upper()} \n"
print(
    f"Los caracteres que más se repiten con {tuplas_mayor[0][1]} repeticiones son:")
print(mensaje)


# SOLUCIONES CURSO

# string = "hola mundo estos son los caracteres del ejercicio"


# def quita_espacios(texto):
#     return [char for char in texto if char != " "]


# def cuenta_caracteres(lista):
#     chars_dict = {}
#     for char in lista:
#         if char in chars_dict:
#             chars_dict[char] += 1
#         else:
#             chars_dict[char] = 1
#     return chars_dict


# def ordena(dict):
#     return sorted(dict.items(), key=lambda key: key[1], reverse=True)


# def mayores_tuplas(lista):
#     maximo = lista[0][1]
#     respuesta = {}
#     for orden in lista:
#         if maximo > orden[1]:
#             break
#         respuesta[orden[0]] = orden[1]
#     return respuesta


# def crea_mensaje(diccionario):
#     mensaje = "Los que más se repiten son: \n"
#     for key, valor in diccionario.items():
#         mensaje += f"- {key.upper()} con {valor} repeticiones \n"
#     return mensaje


# sin_espacios = quita_espacios(string)
# contados = cuenta_caracteres(sin_espacios)
# ordenados = ordena(contados)
# mayores = mayores_tuplas(ordenados)
# print(crea_mensaje(mayores))


# print(mayores)
