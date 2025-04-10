import pandas as pd


dados = pd.read_csv("Day-25/Census Data Analisys/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#print(dados.head())
#print(dados.columns)
print(dados[dados["Primary Fur Color"] == "Gray"])

# Count the number of squirrels for each fur color
grey_count = len(dados[dados["Primary Fur Color"] == "Gray"])
cinnamon_count = len(dados[dados["Primary Fur Color"] == "Cinnamon"])
black_count = len(dados[dados["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_count, cinnamon_count, black_count]
    }

dados2 = pd.DataFrame(data_dict)
dados2.to_csv("Day-25/Census Data Analisys/squirrel_count.csv")