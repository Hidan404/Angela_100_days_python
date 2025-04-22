import requests  # Para fazer requisições HTTP às APIs
from datetime import datetime  # Para lidar com datas e horas
import smtplib  # Para enviar e-mails
import time  # Para controlar o tempo de execução com pausas

# ---------------------------------------------
# CONFIGURAÇÕES DO USUÁRIO
# ---------------------------------------------

EMAIL = ""
SENHA = ""
LATITUDE = -6.071400  # Sua latitude (exemplo: Londres)
LONGITUDE = -49.904732  # Sua longitude

# ---------------------------------------------
# FUNÇÃO: Verifica se a ISS está sobre sua localização
# ---------------------------------------------
def iss_sobrevoando():
    resposta = requests.get("http://api.open-notify.org/iss-now.json")
    resposta.raise_for_status()  # Lança erro se a requisição falhar
    dados = resposta.json()

    iss_lat = float(dados["iss_position"]["latitude"])
    iss_long = float(dados["iss_position"]["longitude"])

    # Verifica se a ISS está num raio de 5 graus da sua localização
    if LATITUDE - 5 <= iss_lat <= LATITUDE + 5 and LONGITUDE - 5 <= iss_long <= LONGITUDE + 5:
        return True
    return False

# ---------------------------------------------
# FUNÇÃO: Verifica se está de noite na sua localização
# ---------------------------------------------
def esta_de_noite():
    parametros = {
        "lat": LATITUDE,
        "lng": LONGITUDE,
        "formatted": 0,  # Retorna o horário no formato UTC ISO
    }
    resposta = requests.get("https://api.sunrise-sunset.org/json", params=parametros)
    resposta.raise_for_status()
    dados = resposta.json()

    # Converte os horários de nascer e pôr do sol para hora inteira
    nascer_do_sol = int(dados["results"]["sunrise"].split("T")[1].split(":")[0])
    por_do_sol = int(dados["results"]["sunset"].split("T")[1].split(":")[0])

    # Hora atual no sistema local
    hora_atual = datetime.now().hour

    # Está de noite se a hora atual for depois do pôr do sol ou antes do nascer do sol
    if hora_atual >= por_do_sol or hora_atual <= nascer_do_sol:
        return True
    return False

# ---------------------------------------------
# LOOP INFINITO: Verifica a cada 60 segundos
# ---------------------------------------------
def main():
    while True:
        time.sleep(60)  # Espera 60 segundos antes de repetir

        # Se a ISS estiver sobrevoando e for de noite
        if iss_sobrevoando() and esta_de_noite():
            # Estabelece conexão segura com servidor SMTP
            conexao = smtplib.SMTP("__ENDERECO_DO_SERVIDOR_SMTP_AQUI__")
            conexao.starttls()  # Inicia comunicação segura (TLS)
            conexao.login(EMAIL, SENHA)  # Faz login no e-mail
            conexao.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,  # Pode enviar para outro e-mail aqui se quiser
                msg="Subject:Olhe para cima! 👆\n\nA ISS está sobre você no céu!"
            )

if __name__ == "__main__":
    main()