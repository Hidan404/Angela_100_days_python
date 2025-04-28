import requests

pixela_endpoint = "https://pixe.la/v1/users"

parametros_usuario = {
    "token": "kdkajdhsiisi254s",
    "username": "ronald777",
    "agreeTermsofService": "yes",
    "notMinor": "yes",
}

resposta = requests.post(url= pixela_endpoint, json=parametros_usuario)
print(resposta.text)