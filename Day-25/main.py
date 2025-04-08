import pandas as pd


dados = pd.read_csv("Day-25/weather_data.csv", sep=",", encoding="utf-8")
print(dados.info())
print(dados.head())
print(dados.describe())
print(dados.columns)

for d in dados["temp"]:
    temperatura = []
    if isinstance(d, (int, float)):
        temperatura.append(d)
    else:
        temperatura.append(0)
    print(temperatura)