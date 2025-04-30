import requests
from dados_api_nutri import NutriApi
from dados_api_sheet import SheetApi
import webbrowser



def main():
    atividade = input("Qual atividade você fez? (ex: walked): ").strip()
    duracao = int(input("Quantos minutos durou? (ex: 45): ").strip())

    frase = f"I {atividade} for {duracao} minutes"

    nutri_api = NutriApi(frase)
    
    resposta = requests.post(url=nutri_api.exercicio_endpoint, json=nutri_api.body(), headers=nutri_api.headers())
    print(resposta.status_code)

    if resposta.status_code == 200:
        dados = resposta.json()
        for dado in dados["exercises"]:
            print(f"Exercise: {dado['name']}, Duration: {dado['duration_min']} min, Calories burned: {dado['nf_calories']} kcal")


        exerc = dados["exercises"][0]
        sheet_api = SheetApi(exerc["duration_min"], exerc['nf_calories']) 
        resposta_sheet = requests.post(url=sheet_api.url, json=sheet_api.novo_workout)
        print(resposta_sheet.text)   
        webbrowser.open("https://docs.google.com/spreadsheets/d/1igaUB4GC5kFpc_zEqoeBWkuFdCGRjl08lE8oFQem8nY/edit?gid=0#gid=0")
    else:
        print(f"Error: {resposta.status_code}, {resposta.text}")

if __name__ == "__main__":
    main()