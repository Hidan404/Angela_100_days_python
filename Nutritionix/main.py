import requests
from dados_api_nutri import NutriApi
from dados_api_sheet import SheetApi











print(resposta.text)

def main():
    nutri_api = NutriApi()
    sheet_api = SheetApi()

    resposta = requests.post(url=, json=novo_workout)

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