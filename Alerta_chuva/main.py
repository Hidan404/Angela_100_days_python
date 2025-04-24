import requests
import json

chave_api = "5efdf341fa6100bd24e45542c7551efb"
#url = f"https://api.openweathermap.org/data/2.5/weather?q=London,UK&appid={chave_api}&lang=pt_br&units=metric"

def obter_dados():
    latidude = float(input("digite uma latitude: "))
    longitude = float(input("digite uma longitude: "))
    linguagem = "pt_br"

    return latidude, longitude, linguagem


def clima():
    latitude, longitude, linguagem = obter_dados()

    link = "https://api.openweathermap.org/data/2.5/forecast"



    parametros = {
        "lat": latitude,
        "lon": longitude,
        "appid": chave_api,
        "lang": linguagem
    }
    resposta = requests.get(link, params=parametros)

    if resposta.status_code == 200:
        dados = resposta.json() 
        with open("Alerta_chuva/dados.json","w")as f:
            f.write(json.dumps(dados, indent=4, ensure_ascii=False))
            
        with open("Alerta_chuva/dados.json", "r") as f:
            data = f.read()

        print("\n📍 Clima em:", data['city']["name"])
        print("🌡️ Temperatura:", data["main"]["temp"], "°C")
        print("🤔 Sensação térmica:", data["main"]["feels_like"], "°C")
        print("💧 Umidade:", data["main"]["humidity"], "%")
        print("🌬️ Velocidade do vento:", data["wind"]["speed"], "m/s")
        print("🌤️ Descrição:", data["weather"][0]["description"].capitalize())
    else:
        print(f"Erro ao acessar API: {resposta.status_code}")

if __name__ == "__main__":
    clima()

   