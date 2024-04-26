# import time
# print(time.time()) # 2024-01-01 00:00:00

from datetime import datetime

fecha = datetime(2024, 1, 1)
fecha2 = datetime(2024, 2, 1)
ahora = datetime.now()
print(fecha)  # 2024-01-01 00:00:00
print(ahora)  # 2024-04-24 17:14:58.130426

fechaStr = datetime.strptime("2023-01-03", "%Y-%m-%d")
print(fechaStr)

print(fecha.strftime("%Y/%m/%d"))
print(fecha > fecha2)

print(
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.hour,
    fecha.minute
)

# todas las directivas para formatos de fechas en el siguiente link:
# https://docs.python.org/3/library/datetime.html
