import random

random.seed()

numeros = [1,2,3,4,5]
numeros_pares = [n  for n in numeros if n % 2 == 0 ]
novos_numeros = [n + 1 for n in numeros]
print(numeros_pares,"\n", novos_numeros)


dicionario = {"nome": "ronald","idade": 89}


range_list = [i + 1 for i in range(1, 5)]
print(range_list)

lista_nomes = ["hidan", "kakuzu", "itachi", "pain", "konan","deidara", "sasori"]
nomes_curtos = [n for n in lista_nomes if len(n) <= 4]
nomes_longos_maiusculo = [n.upper() for n in lista_nomes if len(n) > 5]
print(nomes_longos_maiusculo)


notas_estudantes = {
    "Ana": 8.5,
    "Bruno": 7.2,
    "Carlos": 9.0,
    "Daniela": 6.8,
    "Eduardo": 7.9
}

score = {estudante: "Aprovado" if nota > 7 else "Reprovado" for estudante,nota in notas_estudantes.items()}

nota_aleatoria = {stud: random.randint(1, 10) for stud in notas_estudantes}
alunos_aprovados = {stud: "Aprov" if nota > 7 else "Reprov" for stud,nota in nota_aleatoria.items()}
print(alunos_aprovados)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"


result = {palavra: len(palavra) for palavra in sentence.split()}
print(result)


weather_c = {"Monday": [12], "Tuesday": [14], "Wednesday": [15], "Thursday": [14], "Friday": [21], "Saturday": [22], "Sunday": [24]}

weather_f = {dia: round((c[0] * (9/5)) + 32, 2) for dia,c in weather_c.items()}
print(weather_f)

import pandas as pd
dados_frame = pd.DataFrame(weather_c)

for index, row in dados_frame.iterrows():
    print(row )