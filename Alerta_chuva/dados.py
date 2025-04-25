import requests



class dados_api():
    def __init__(self):
        self.cidade = ""
        self.linguagem = "pt_br"
        self.pais = "BR"
        self.link = "https://api.openweathermap.org/data/2.5/forecast"
        self.chave_api = "5efdf341fa6100bd24e45542c7551efb"

    def obter_dados(self):
        usuario_cidade = input("Digite o nome da cidade: ")
        self.cidade = usuario_cidade
        
        parametros = {
            "q": self.cidade,
            "appid": self.chave_api,
            "lang": f"{self.linguagem},{self.pais}",
            "units": "metric"
        }    

        resposta = requests.get(self.link, params=parametros)
        try:
            if resposta.status_code == 200:
                dados = resposta.json()
                return dados
            else:
                print(f"Erro ao obter dados: {resposta.status_code} - {resposta.reason}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return None
                  
