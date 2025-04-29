import requests

class NutriApi():
    def __init__(self):
        self.exercicio_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
        self.usuario_entrada = "I walked for 60 minutes"
        self.ID = "42f42b8f"
        self.TOKEN = "739e728872888a6f982331c62d9f9ae8"

    def headers(self):
        headers = {
            "x-app-id": self.ID,
            "x-app-key": self.TOKEN,
            "Content-Type": "application/json"
        }    
        return headers
    
    def body(self):
        body = {
            "query": self.usuario_entrada,
            "gender": "female",
            "weight_kg": 92,
            "height_cm": 161,
            "age": 21,
        }
        return body

        