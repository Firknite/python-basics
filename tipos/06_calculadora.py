"""
    Archivo con funciones para calculadora
"""

n1 = int(input("Ingresa primer número: "))
n2 = int(input("Ingresa segundo número: "))

suma = n1+n2
resta = n1-n2
mult = n1*n2
div = n1//n2

MENSAJE = f"""
Para los números {n1} y {n2},
el resultado de la suma es {suma}
el resultado de la resta es {resta}
el resultado de la multiplicación es {mult}
el resultado de la división es {div}
"""

print(MENSAJE)
