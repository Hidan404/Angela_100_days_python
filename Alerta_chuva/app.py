from salvar_dados_json import salvar_json
import datetime
from icones_descricao import Icone
from enviar_msg_telegram import msg_telegram
import os


def main():
    dados = salvar_json()
    dados.salvar_arquivo_json()
    dados_json = dados.abrir_arquivo_json()

    cidade_nome = dados_json["city"]["name"]
    

    hoje = datetime.datetime.now()
    data_amanha = (hoje + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    horarios_desejados = ["09:00:00", "15:00:00", "21:00:00"]

    resumo_notificacao = f"🌦️ Clima de Amanhã em {cidade_nome}:\n"

    print("\n📍 Cidade:", cidade_nome)
    print("🗓️ Previsão para:", data_amanha)
    print("-" * 40)


    for item in dados_json["list"]:
        data_hora = item["dt_txt"]
        data, hora = data_hora.split()

        if data == data_amanha and hora in horarios_desejados:
            descricao = item["weather"][0]["description"].capitalize()
            icone = Icone(descricao)
            chuva = item.get("pop", 0) * 100

            print(f"🕒 {data_hora}")
            print(f"  {icone.emoji_clima()} {descricao}")
            print(f"  🌡️ Temp: {item['main']['temp']}°C")
            print(f"  🤔 Sensação: {item['main']['feels_like']}°C")
            print(f"  💧 Umidade: {item['main']['humidity']}%")
            print(f"  🌬️ Vento: {item['wind']['speed']} m/s")
            if chuva > 0:
                print(f"  ☔ Chance de chuva: {chuva:.0f}%")
                print("-" * 40)

                resumo_notificacao += f"{hora[:2]}h: {icone.emoji_clima()} {descricao}, {item['main']['temp']}°C\n"
    os.system(f'notify-send "Clima Amanhã - {cidade_nome}" "{resumo_notificacao}"')
    
    msg_env_telegram = msg_telegram()
    print(msg_env_telegram.enviar_mensagem_telegram(resumo_notificacao))

if __name__ == "__main__":
    main()  