import requests


latitude = -6.071400
longitude = -49.904732

parametros = {
    "lat": latitude,
    "lng": longitude,
    "formated": 0
}

url = f"https://api.sunrise-sunset.org/json"
resposta = requests.get(url, params=parametros)

if resposta.status_code == 200:
    dados = resposta.json()
    resposta = dados["results"]
    for c, v in resposta.items():
        print(c, v)

    sunrise = dados["results"]["sunrise"]
    print(sunrise.split("T")[0].split(":"))    
    
