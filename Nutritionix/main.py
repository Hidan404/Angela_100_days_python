import requests
from datetime import datetime
from dados_api_nutri import NutriApi




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

def main():
    nutri_api = NutriApi()

    resposta = requests.post(url=nutri_api.exercicio_endpoint, json=nutri_api.body(), headers=nutri_api.headers())
    print(resposta.status_code)

    if resposta.status_code == 200:
        dados = resposta.json()
        for dado in dados["exercises"]:
            print(f"Exercise: {dado['name']}, Duration: {dado['duration_min']} min, Calories burned: {dado['nf_calories']} kcal")
    else:
        print(f"Error: {resposta.status_code}, {resposta.text}")

if __name__ == "__main__":
    main()