import subprocess

ips =["192.168.0.4","192.168.0.7","192.168.1"]

def ping():

    for ip in ips:
        try:
            result = subprocess.run(["ping", "-c", "1", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                print(f"Ping to {ip} successful.")
            else:
                print(f"Ping to {ip} failed.")
        except Exception as e:
            print(f"An error occurred while pinging {ip}: {e}")


def listar_diretorios(diretorio):
    try:
        listar = subprocess.run(["ls", "-lha", diretorio], capture_output=True, text=True)
        if listar.returncode == 0:
            print("Saída do comando 'ls':")
            print(listar.stdout)
        else:
            print(f"Erro ao listar o diretório {diretorio}:")
            print(listar.stderr)
    except Exception as e:
        print(f"Um erro ocorreu ao listar o diretório {diretorio}: {e}")

# Exemplo de uso
listar_diretorios("/home/hidan/Documentos")     