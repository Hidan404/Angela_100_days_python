import os
import subprocess
import json


def usuarios_linux(nome):
    # Comando para listar usuarios
    comando = f'sudo useradd {nome} -c "temporario" -m -s /bin/bash'
    # Ejecutar comando
    resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) 
    # Mostrar resultado
    if resultado.returncode == 0:
        print("Usuario creado con exito")
    else:
        print("Error al crear usuario {}".format(resultado.stderr.decode('utf-8')))
    # Comando para eliminar usuario

#usuarios_linux(nome="usuario1")    


def remover_usuario(nome):
    # Comando para eliminar usuario
    comando = f'sudo userdel -r -f {nome}'
    # Ejecutar comando
    resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) 
    # Mostrar resultado
    if resultado.returncode == 0:
        print("Usuario eliminado con exito")
    else:
        print("Error al eliminar usuario {}".format(resultado.stderr.decode('utf-8')))

#remover_usuario(nome="convidado1")


def salvar_json(nome, senha):
    dados = {
        "nome": nome,
        "senha": senha
    }
    with open("usuarios.json", "w") as f:
        json.dump(dados, f, indent=4)
        os.path.exists("usuarios.json")
    print("Usuario salvo com sucesso")

salvar_json(nome="usuario1", senha="senha123")

def ler_json():
    with open("usuarios.json", "r") as f:
        dados = json.load(f)
        dados.update({"senha": "senha123"})
    print(dados)   

ler_json()
