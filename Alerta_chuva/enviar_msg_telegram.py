import requests


class msg_telegram():
    def __init__(self):
        self.TOKEN = "7949436359:AAGMZkjSqdQFTzXbYH--WJP1YrZVFMyvs90"
        self.CHAT_ID = "1364356086"
        self.URL = f"https://api.telegram.org/bot{self.TOKEN}/sendMessage"

    def enviar_mensagem_telegram(self, mensagem):
        payload = {
            "chat_id": self.CHAT_ID,
            "text": mensagem,
            "parse_mode": "HTML"
        }

        try:
            resposta = requests.post(url= self.URL, data= payload)
            if resposta.status_code != 200:
                raise resposta.raise_for_status()
            else:
                print("Mensagem enviada com sucesso!")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem no Telegram: {e}")














