import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions"
response = requests.get(url)
texto = response.text

soup = BeautifulSoup(texto, "html.parser")

preguntas = soup.select(".s-post-summary")

# print(preguntas[0])
for pregunta in preguntas:
    titulo = pregunta.select_one(".s-link").get_text()
    usuario = pregunta.select_one(".s-user-card--link").get_text()

    print(f"{usuario.strip()}: \n {titulo.strip()}")

# para acceder a los atributos html de cada objeto html, debemos acceder a ellos
# como si fuera una llave dentro de un objeto normal por ejemplo:
# preguntas[0]["href"]
