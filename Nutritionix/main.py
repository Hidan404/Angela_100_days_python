import requests
from datetime import datetime


ID = "42f42b8f"
TOKEN = "739e728872888a6f982331c62d9f9ae8"

url = 'https://api.sheety.co/4a83785dd76a6d981cfc0442a524519d/planilhaDeCaminhada/workouts'


novo_workout = {
    "workout": {
        "date": datetime.now().strftime("%d/%m/%Y"),
        "time": datetime.now().strftime("%H:%M"),
        "exercise": "Caminhada",
        "duration": "30",
        "calories": "150"
    }
}


resposta = requests.post(url=url, json=novo_workout)
print(resposta.text)


exercicio_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
usuario_entrada = "I walked for 60 minutes"

headers = {
    "x-app-id": ID,
    "x-app-key": TOKEN,
    "Content-Type": "application/json"
}

body = {
    "query": usuario_entrada,
    "gender": "female",
    "weight_kg": 92,
    "height_cm": 161,
    "age": 21,
}

resposta = requests.post(url=exercicio_endpoint, json=body, headers=headers)

if resposta.status_code == 200:
    dados = resposta.json()
    for dado in dados["exercises"]:
        print(f"Exercise: {dado['name']}, Duration: {dado['duration_min']} min, Calories burned: {dado['nf_calories']} kcal")
else:
    print(f"Error: {resposta.status_code}, {resposta.text}")