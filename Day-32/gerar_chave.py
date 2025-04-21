from cryptography.fernet import Fernet

def gerar_chave():
    """
    Gera uma chave de criptografia e a salva em um arquivo.
    """
    # Gerar uma chave
    chave = Fernet.generate_key()

    with open('Day-32/chave.key', 'wb') as chave_arquivo:
        chave_arquivo.write(chave)

    return chave    

      