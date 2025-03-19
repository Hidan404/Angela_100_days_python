import requests

# URL da API
URL = "https://opentdb.com/api.php?amount=50&category=15&difficulty=medium&type=boolean"

# Requisição para a API
response = requests.get(URL)
data = response.json()  


if "results" in data:
    question_data = data["results"]
else:
    question_data = []  



     



