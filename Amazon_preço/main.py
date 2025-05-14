import requests
from bs4 import BeautifulSoup
import smtplib
import datetime as dt
import os


url = "https://www.amazon.com.br/Mouse-Nanoreceptor-Inclusa-Logitech-Mouses/dp/B00UC1R80C/ref=pd_bxgy_thbs_d_sccl_2/137-0836641-4032029"
resposta = requests.get(url= url).text

soup = BeautifulSoup(resposta, "html.parser")

precos_div = soup.find_all("span", class_="a-price")
precos = []

for preco in precos_div:
    try:
        inteiro = preco.find("span", class_="a-price-whole").get_text(strip=True)
        fracao = preco.find("span", class_="a-price-fraction").get_text(strip=True)
        valor = f"{inteiro}.{fracao}"
        precos.append(valor)
    except AttributeError:
        continue  # Se não encontrar uma parte, ignora esse bloco
print(precos)


precos_convertidos = []
for preco in precos:
    preco_float = float(preco.replace(".", "").replace(",", "."))
    precos_convertidos.append(preco_float)
    print(preco_float)


preco_selecionado = None  
for preco in precos_convertidos:
    if preco == 69.9:
        preco_selecionado = preco
        print(f"Preço selecionado encontrado: {preco_selecionado}")
        break


if preco_selecionado and preco_selecionado < 100:
    meu_email = "ronaldkurouzo@gmail.com"
    senha = os.getenv("SENHA_EMAIL")

    with smtplib.SMTP("smtp.gmail.com", 587) as conexao:
        conexao.starttls()
        conexao.login(user=meu_email, password=senha)
        mensagem = f"Subject:Alerta de Preço\n\nO preço caiu para R$ {preco_selecionado}!".encode("utf-8")
        conexao.sendmail(from_addr=meu_email, to_addrs="ronald.dev404@gmail.com", msg=mensagem)



        