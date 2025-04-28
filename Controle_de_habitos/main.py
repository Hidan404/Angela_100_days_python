import requests
import datetime

# Configurações do usuário
pixela_endpoint = "https://pixe.la/v1/users"
token = "kdkajdhsiisi254s"
username = "ronald777"
graph_id = "leitura1"
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

headers = {
    "X-USER-TOKEN": token
}

def gerar_grafico():
    graph_config = {
        "id": graph_id,
        "name": "Controle de Leitura",
        "unit": "pages",
        "type": "int",
        "color": "ajisai"
    }
    resposta = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(resposta.text)  # Mostra a resposta certinha
    return resposta.ok
# Função para pegar a data no formato correto
def pegar_data():
    return datetime.datetime.now().strftime("%Y%m%d")

# Função para adicionar páginas lidas
def adicionar_paginas():
    data = pegar_data()
    paginas = input("Quantas páginas você leu hoje? ")
    
    pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"
    pixel_dados = {
        "date": data,
        "quantity": paginas
    }
    
    resposta = requests.post(url=pixel_endpoint, json=pixel_dados, headers=headers)
    print(resposta.text)

# Função para corrigir páginas de um dia específico
def corrigir_paginas():
    data = input("Digite a data que deseja corrigir (formato AAAAMMDD): ")
    novas_paginas = input("Digite o novo número de páginas: ")
    
    pixel_update_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{data}"
    pixel_update_dados = {
        "quantity": novas_paginas
    }
    
    resposta = requests.put(url=pixel_update_endpoint, json=pixel_update_dados, headers=headers)
    print(resposta.text)

# Função para deletar registro de um dia específico
def deletar_paginas():
    data = input("Digite a data que deseja deletar (formato AAAAMMDD): ")
    
    pixel_delete_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{data}"
    
    resposta = requests.delete(url=pixel_delete_endpoint, headers=headers)
    print(resposta.text)

# Função para mostrar o link do gráfico
def ver_grafico():
    print(f"Abra este link para ver seu gráfico de leitura:\nhttps://pixe.la/v1/users/{username}/graphs/{graph_id}.html")


print(gerar_grafico())

# MENU
def menu():

    while True:

        print("\n=== Controle de Leitura ===")
        print("1 - Adicionar páginas lidas hoje")
        print("2 - Corrigir páginas de um dia")
        print("3 - Deletar registro de um dia")
        print("4 - Ver gráfico")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_paginas()
        elif escolha == "2":
            corrigir_paginas()
        elif escolha == "3":
            deletar_paginas()
        elif escolha == "4":
            ver_grafico()
        elif escolha == "0":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()            