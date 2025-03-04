import random
import string
import pyperclip


def password_generator():
    numero_letras = int(input("qualo numero de letras sua senha: "))
    if numero_letras <= 0:
        print("O número de letras deve ser maior que zero.")
        return
    

    numero_simbolos = int(input("qualo numero de simbolos sua senha: "))
    if numero_simbolos < 0:
        print("O número de símbolos deve ser maior ou igual a zero.")
        return
    
    numero_numeros = int(input("qualo numero de numeros sua senha: "))
    if numero_numeros < 0:
        print("O número de números deve ser maior ou igual a zero.")
        return

    lista_alfabetica = list(string.ascii_letters)
    lista_simbolos = list("!@#$%^&*()-_+=")
    lista_numeros = list(string.digits)

    senha = []

    for _ in range(numero_letras):
        senha.append(random.choice(lista_alfabetica))

    for _ in range(numero_simbolos):
        senha.append(random.choice(lista_simbolos))

    for _ in range(numero_numeros):
        senha.append(random.choice(lista_numeros))  

    random.shuffle(senha)  

    senha_gerada = "".join(senha) 
    
    pyperclip.copy(senha_gerada)
    print(f"Senha gerada {senha_gerada}")

if __name__ == "__main__":
    password_generator()    

