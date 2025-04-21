import smtplib
import datetime as dt
from cryptography.fernet import Fernet
import gerar_chave
import criptografar_a_senha



chave = gerar_chave.gerar_chave()
senha_criptografada = criptografar_a_senha.ler_chave()

# Ler chave
with open("Day-32/chave.key", "rb") as chave_arquivo:
    chave = chave_arquivo.read()

# Ler senha criptografada
with open("Day-32/senha.bin", "rb") as senha_arquivo:
    senha_criptografada = senha_arquivo.read()

Fernet = Fernet(chave)
senha = Fernet.decrypt(senha_criptografada).decode()

meu_email = "ronaldkurouzo@gmail.com"
data_atual = dt.datetime.now()
data_formatada = data_atual.strftime("%d/%m/%Y")
assunto = "Dias dos namorados"
corpo_email = f"Feliz dia dos namorados {data_formatada}"


with smtplib.SMTP("smtp.gmail.com", 587) as conectar:
    conectar.starttls()
    conectar.login(user=meu_email, password=senha)
    conectar.sendmail(from_addr=meu_email, to_addrs="fecil72927@bauscn.com",msg= corpo_email)
    print("Email enviado com sucesso!")
    conectar.quit()
