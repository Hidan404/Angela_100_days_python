import smtplib

class Email_enviar():
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def enviar_email(self, assunto, mensagem):
        try:
            # Configurações do servidor SMTP
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587

            # Conexão com o servidor SMTP
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(self.email, self.senha)

            # Montando o e-mail
            msg = f'Subject: {assunto}\n\n{mensagem}'

            # Enviando o e-mail
            server.sendmail(self.email, self.email, msg)
            print('E-mail enviado com sucesso!')

        except Exception as e:
            print(f'Erro ao enviar e-mail: {e}')

        finally:
            server.quit()