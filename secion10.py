import requests

respuesta = requests.get("https://web.whatsapp.com/")
print(respuesta.status_code)