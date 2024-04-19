if __name__ != "__main__":
    from ..gestion.crud import guardar

    def pagar_impuestos():
        print("pagando impuestos")
        guardar()

if __name__ == "__main__":
    print("tareas de mantenimiento")
