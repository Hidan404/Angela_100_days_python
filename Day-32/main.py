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

def dados_meu_email():
    meu_email = "ronaldkurouzo@gmail.com"
    data_atual = dt.datetime.now()
    data_formatada = data_atual.strftime("%d/%m/%Y")
    assunto = "Dias dos namorados"
    return meu_email, data_formatada, assunto, data_atual

meu_email, data_formatada, assunto, data_atual = dados_meu_email()

def corpo_email():
    with open("Day-32/msg_email.txt", "r") as arquivo:
        conteudo = arquivo.read()
    return conteudo.format(data_formatada)

corpo_email_enviar = corpo_email()
corpo_email_enviar = corpo_email_enviar.encode("utf-8")


def enviar_email():
    with smtplib.SMTP("smtp.gmail.com", 587) as conectar:
        conectar.starttls()
        conectar.login(user=meu_email, password=senha)
        conectar.sendmail(from_addr=meu_email, to_addrs="fecil72927@bauscn.com",msg= corpo_email_enviar)
        print("Email enviado com sucesso!")
        conectar.quit()

def main():
    
    dia_da_semana = data_atual.weekday()
    if dia_da_semana == 0:  # Segunda-feira
        enviar_email()
    elif dia_da_semana == 1:  # Terça-feira
        print("Hoje é terça-feira. O email não será enviado.")
    elif dia_da_semana == 2:  # Quarta-feira
        print("Hoje é quarta-feira. O email não será enviado.")
    elif dia_da_semana == 3:  # Quinta-feira
        print("Hoje é quinta-feira. O email não será enviado.")
    elif dia_da_semana == 4:  # Sexta-feira
        print("Hoje é sexta-feira. O email não será enviado.")
    elif dia_da_semana == 5:  # Sábado
        print("Hoje é sábado. O email não será enviado.")
    elif dia_da_semana == 6:  # Domingo
        print("Hoje é domingo. O email não será enviado.")    
    else:
        print("Hoje não é segunda-feira. O email não será enviado.")

if __name__ == "__main__":
    main()
