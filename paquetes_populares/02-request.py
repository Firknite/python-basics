# la pagina con los mocks para obtener data de prueba es https://jsonplaceholder.typicode.com

import requests

#### GET ####
# url = "https://jsonplaceholder.typicode.com/users"
# r = requests.get(url, timeout=10)  # timeout esta en segundos no milisegundos
# print(
#     r.status_code,
#     r.text
# )

# r = r.json()

# for user in r:
#     print(user["name"])

url = "https://jsonplaceholder.typicode.com/users/1"
r = requests.get(url, timeout=10)  # timeout esta en segundos no milisegundos
print(r.json())


#### POST ####
url = "https://jsonplaceholder.typicode.com/users"
user = {
    "name": "Gatito feliz"
}
r = requests.post(url, timeout=10, data=user)
print(r.status_code)

#### PUT ####
url = "https://jsonplaceholder.typicode.com/users/2"
user = {
    "name": "Gatito feliz"
}
r = requests.put(url, timeout=10, data=user)
print(r.status_code)

#### DELETE ####
url = "https://jsonplaceholder.typicode.com/users/2"
r = requests.delete(url, timeout=10)
print(r.status_code)

# para entregar headers, request acepta un parametro con el nombre headers
