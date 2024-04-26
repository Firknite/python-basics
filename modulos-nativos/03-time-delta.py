from datetime import datetime, timedelta

# timedelta es un modulo que agrega tiempo proporcionalmente al parametro que se le entregue
fecha1 = datetime(2024, 1, 1) + timedelta(weeks=1)
fecha2 = datetime(2024, 2, 1)

delta = fecha2 - fecha1

print(delta)
print("dias", delta.days)
print("segundos", delta.seconds)
print("microsegundos", delta.microseconds)
print("total_seconds()", delta.total_seconds())
