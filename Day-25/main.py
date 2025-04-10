import pandas as pd
import openpyxl
import matplotlib.pyplot as plt


dados = pd.read_csv("Day-25/weather_data.csv", sep=",", encoding="utf-8")
#print(dados.info())
#print(dados.head())
#print(dados.describe())
#print(dados.columns)


for d in dados["temp"]:
    temperatura = []
    if isinstance(d, (int, float)):
        temperatura.append(d)
    else:
        temperatura.append(0)
    print(temperatura)


print(dados["temp"].mean().__round__(2),"\n", dados["temp"].max())
print(dados[dados["temp"] == dados["temp"].max()]["day"].values[0])

monday = dados[dados["day"] == "Monday"]
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32
print(celsius_to_fahrenheit(monday["temp"].values[0]))


dicionario = {
    "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "temp": [32, 35, 28, 30, 29, 31, 33],
    "precipitation": [0.1, 0.2, 0.0, 0.3, 0.4, 0.5, 0.6]
}

dados2 = pd.DataFrame(dicionario)
dados2.to_csv(r"C:\Users\ronal\Documents\GitHub\Angela_100_days_python\Day-25/novos_dados.csv", index=False, sep=",", encoding="utf-8")
# dados2.to_excel("Day-25/novos_dados.xlsx", index=False)

def barra_grafico(dados):
    plt.bar(dados["day"], dados["temp"])
    plt.title("Temperatura por dia")
    plt.xlabel("Dia")
    plt.ylabel("Temperatura (°C)")
    plt.show()

barra_grafico(dados2)    