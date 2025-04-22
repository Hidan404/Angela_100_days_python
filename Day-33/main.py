import requests

url = "http://api.open-notify.org/iss-now.json"
resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    retorno = dados["message"]
    posicao_iss = dados["iss_position"]
    latitude = posicao_iss["latitude"]
    longitude = posicao_iss["longitude"]
    print(f"Retorno: {retorno}")
    print(f"A posição atual da ISS é: Latitude {dados["iss_position"]["latitude"]}, Longitude {longitude}")
else:
    print(f"Erro ao obter dados: {resposta.raise_for_status}")
