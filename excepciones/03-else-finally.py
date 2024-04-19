try:
    n1 = int(input("Ingresa primer numero: "))
except Exception as e:
    print("Ocurrio un error!")
# este bloque solamente finaliza cuando no hay errores en el try
else:
    print("No ocurrio ningun error")
# este se ejecuta siempre hallan o no errores
finally:
    print("se ejecuta siempre")
