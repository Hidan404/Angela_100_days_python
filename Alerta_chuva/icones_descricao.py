class Icone():
    def __init__(self, descricao):
        self.descricao = descricao


    def emoji_clima(self):
       
        if "chuva" in self.descricao:
            return "🌧️"
        elif "nuvem" in self.descricao:
            return "☁️"
        elif "céu limpo" in self.descricao or "limpo" in self.descricao:
            return "☀️"
        elif "neve" in self.descricao:
            return "❄️"
        elif "tempestade" in self.descricao:
            return "⛈️"
        elif "névoa" in self.descricao or "neblina" in self.descricao:
            return "🌫️"
        else:
            return "🌤️"    