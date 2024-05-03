# Variables de entorno
# se agregan en un archivo .env a nivel del proyecto y se importan con os
import os

apikey = os.environ.get("SENDGRID_API_KEY")
print(apikey)
