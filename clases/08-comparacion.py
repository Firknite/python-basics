class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, otro) -> bool:
        return self.lat == otro.lat and self.lon == otro.lon

    def __lt__(self, otro):
        return self.lat + self.lon < otro.lat + otro.lon

    def __le__(self, otro):
        return self.lat + self.lon <= otro.lat + otro.lon


coords = Coordenadas(45, 27)
coords2 = Coordenadas(45, 29)

# esto consulta si ambas variables son exactamente iguales
# a nivel de si estan ocupando el mismo espacio fisico en RAM
# para comparar si instancias distintas del mismo objeto comparten
# los mismos valores en sus propiedades se debe implementar
# el metodo magico __eq__ que con su declaracion viene por defecto
# la implementacion de su metodo contrario __ne__ y asi con todos los metodos magicos

print(coords == coords2)
print(coords > coords2)
print(coords <= coords2)
