import os
import socket
import platform
import shutil
import psutil

def verificar_conexao():
    hostname = "8.8.8.8"  # Google DNS
    comando = "ping -n 4" if platform.system() == "Windows" else "ping -c 4"
    resposta = os.system(f"{comando} {hostname} > nul 2>&1" if platform.system() == "Windows" else f"{comando} {hostname} > /dev/null 2>&1")
    
    if resposta == 0:
        print("[✅] Conectado à Internet!")
    else:
        print("[❌] Sem conexão com a Internet!")

def obter_ip_local():
    ip_local = socket.gethostbyname(socket.gethostname())
    print(f"[ℹ️] IP Local: {ip_local}")







def verificar_temperatura():
    sistema = platform.system()

    if sistema == "Windows":
        print("[⚠️] Monitoramento de temperatura não disponível no Windows com psutil.")
    elif sistema == "Linux":
        try:
            temperaturas = psutil.sensors_temperatures()
            if "coretemp" in temperaturas:
                for sensor in temperaturas["coretemp"]:
                    print(f"[🌡] Núcleo {sensor.label}: {sensor.current}°C")
            else:
                print("[⚠️] Sensores de temperatura não detectados.")
        except AttributeError:
            print("[❌] Sensores de temperatura não disponíveis neste sistema.")
    else:
        print("[❌] Sistema operacional não suportado.")




def limpar_windows():
    caminhos = [
        os.path.expandvars(r"%TEMP%"),
        os.path.expandvars(r"C:\Windows\Temp")
    ]
    for caminho in caminhos:
        os.system(f"del /F /Q /S {caminho}\\*.*")

def limpar_linux():
    caminhos = ["/tmp", "/var/tmp"]
    for caminho in caminhos:
        shutil.rmtree(caminho, ignore_errors=True)

def limpar_sistema():
    sistema = platform.system()
    if sistema == "Windows":
        limpar_windows()
        print("[✅] Limpeza concluída no Windows!")
    elif sistema == "Linux":
        limpar_linux()
        print("[✅] Limpeza concluída no Linux!")
    else:
        print("[❌] Sistema não suportado.")

if __name__ == "__main__":
    limpar_sistema()





# Configuração de pastas
if platform.system() == "Windows":
    origem = os.path.expanduser("C:\\Users\\SeuUsuario\\Documents")  # Ajuste seu usuário
    destino = "D:\\Backup"  # Ajuste o caminho do destino
else:
    origem = os.path.expanduser("~/Documents")
    destino = "/media/user/Backup"

def realizar_backup():
    if not os.path.exists(destino):
        os.makedirs(destino)
    try:
        shutil.copytree(origem, destino, dirs_exist_ok=True)
        print(f"[✅] Backup concluído para {destino}")
    except Exception as e:
        print(f"[❌] Erro ao fazer backup: {e}")

if __name__ == "__main__":
    realizar_backup()
