import requests
import json
import datetime
import os

chave_api = "5efdf341fa6100bd24e45542c7551efb"
#url = f"https://api.openweathermap.org/data/2.5/weather?q=London,UK&appid={chave_api}&lang=pt_br&units=metric"

def obter_dados():
    cidade = input("Digite uma cidade: ")
    linguagem = "pt_br"
    pais = "BR"
    return  f"{cidade},{pais}", linguagem



def emoji_clima(descricao):
    descricao = descricao.lower()
    if "chuva" in descricao:
        return "🌧️"
    elif "nuvem" in descricao:
        return "☁️"
    elif "céu limpo" in descricao or "limpo" in descricao:
        return "☀️"
    elif "neve" in descricao:
        return "❄️"
    elif "tempestade" in descricao:
        return "⛈️"
    elif "névoa" in descricao or "neblina" in descricao:
        return "🌫️"
    else:
        return "🌤️"
    
def enviar_mensagem_telegram(mensagem):
    TOKEN = "7949436359:AAGMZkjSqdQFTzXbYH--WJP1YrZVFMyvs90"
    chat_id = "1364356086"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": mensagem,
        "parse_mode": "HTML"
    }

    try:
        resposta = requests.post(url= url, data= payload)
        if resposta.status_code != 200:
            raise resposta.raise_for_status()
        else:
            print("Mensagem enviada com sucesso!")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar mensagem no Telegram: {e}")

def clima():
    cidade, linguagem = obter_dados()

    link = "https://api.openweathermap.org/data/2.5/forecast"



    parametros = {
        "q": cidade,
        "appid": chave_api,
        "lang": linguagem,
        "units": "metric"
    }
    resposta = requests.get(link, params=parametros)

    if resposta.status_code == 200:
        dados = resposta.json()
        cidade_nome = dados["city"]["name"]

        hoje = datetime.datetime.now()
        data_amanha = (hoje + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        horarios_desejados = ["09:00:00", "15:00:00", "21:00:00"]

        resumo_notificacao = f"🌦️ Clima de Amanhã em {cidade_nome}:\n"

        print("\n📍 Cidade:", cidade_nome)
        print("🗓️ Previsão para:", data_amanha)
        print("-" * 40)

        for item in dados["list"]:
            data_hora = item["dt_txt"]
            data, hora = data_hora.split()

            if data == data_amanha and hora in horarios_desejados:
                descricao = item["weather"][0]["description"].capitalize()
                icone = emoji_clima(descricao)
                chuva = item.get("pop", 0) * 100

                print(f"🕒 {data_hora}")
                print(f"  {icone} {descricao}")
                print(f"  🌡️ Temp: {item['main']['temp']}°C")
                print(f"  🤔 Sensação: {item['main']['feels_like']}°C")
                print(f"  💧 Umidade: {item['main']['humidity']}%")
                print(f"  🌬️ Vento: {item['wind']['speed']} m/s")
                if chuva > 0:
                    print(f"  ☔ Chance de chuva: {chuva:.0f}%")
                print("-" * 40)

                resumo_notificacao += f"{hora[:2]}h: {icone} {descricao}, {item['main']['temp']}°C\n"
        os.system(f'notify-send "Clima Amanhã - {cidade_nome}" "{resumo_notificacao}"')

        enviar_mensagem_telegram(resumo_notificacao)

    else:
        print(f"Erro ao acessar API: {resposta.status_code}")



if __name__ == "__main__":
    clima()

   