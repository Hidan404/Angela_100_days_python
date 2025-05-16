from internet_velocidade  import teste_interenet, formatar_resultados
from dados_email import Email_enviar


def main():
    print("Iniciando teste de velocidade da internet...")

    teste_da_interneet = teste_interenet()
    resultados_formatados = formatar_resultados(*teste_da_interneet)
    print(resultados_formatados)

    email = Email_enviar()
    email.enviar_email("Teste de Velocidade da Internet", resultados_formatados)
    print("Teste de velocidade da internet concluído e e-mail enviado com sucesso!")

    
if __name__ == "__main__":
    main()    