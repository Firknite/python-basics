import json
from pathlib import Path

# escribir json
# productos = [
#     {"id": 1, "name": "Surfboard"},
#     {"id": 2, "name": "Bicicleta"},
#     {"id": 3, "name": "Skate"},
# ]

# data = json.dumps(productos)
# Path("archivos/productos.json").write_text(data)

# leer json
data = Path("archivos/productos.json").read_text(encoding="utf-8")
productos = json.loads(data)

# modificar json
productos[0]['name'] = "Pelota de futbol"
Path("archivos/productos.json").write_text(json.dumps(productos), encoding="utf-8")
