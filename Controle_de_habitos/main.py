import requests

pixela_endpoint = "https://pixe.la/v1/users"

parametros_usuario = {
    "token": "kdkajdhsiisi254s",
    "username": "ronald777",
    "agreeTermsofService": "yes",
    "notMinor": "yes",
}

resposta = requests.post(url= pixela_endpoint, json=parametros_usuario)

grafico_endpoint = f"{pixela_endpoint}/{parametros_usuario['username']}/graphs"

grafico_config = {
    "id": "grafico1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

resposta_grafico = requests.post(url=grafico_endpoint,json= grafico_config)
print(resposta_grafico.text)