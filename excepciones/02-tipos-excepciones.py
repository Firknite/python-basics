try:
    n1 = int(input("Ingresa primer numero: "))
except ValueError as ex:
    print("Ingrese un valor que corresponda")
except NameError as ex:
    print("Ocurrio un error!")

# podemos saber que tipo de excepcion esta occuriendo con el metodo type
