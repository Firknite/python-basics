animal = "gatito feliz"

print(animal.upper())   # Mayúsculas a todos los carácteres del string
print(animal.lower())   # Minúsculas a todos los carácteres del string
print(animal.capitalize())  # Mayúsculas al primer carácter de la cadena
print(animal.title())   # Pone en mayúsculas las primeras letras de la frase
print(animal.strip())   # remueve los espacios al inicio y al final, es un trim
print(animal.rstrip())  # remueve los espacios al final
print(animal.lstrip())  # remueve los espacios al inicio
print(animal.lstrip())  # remueve los espacios al inicio
# retorna el indice del primer caracter encotrado
print(animal.find('iz'))
# retorna el indice del último caracter encotrado
print(animal.replace('fe', "j"))
# esto sirve para saber si la cadena está dentro del string, retorna un boolean
print("ito" in animal)
# esto sirve para saber si la cadena está dentro del string, retorna un boolean
print("ito" not in animal)
